import json
import numpy as np
from chatbot_backend import search_law
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

# Load test queries
with open("test_queries.json", "r") as f:
    test_cases = json.load(f)

import json

# Load laws from your JSON file
with open("cyber_laws.json", "r") as f:
    laws_data = json.load(f)

labels = list({(law["law"], law["section"]) for law in laws_data})
label_to_index = {label: idx for idx, label in enumerate(labels)}
index_to_label = {idx: label for label, idx in label_to_index.items()}

y_true = []
y_pred = []

top_k = 3
correct_at_1 = 0
correct_within_k = 0
reciprocal_ranks = []
rows = []

for case in test_cases:
    query = case["query"]
    expected = (case["expected_law"], case["expected_section"])
    expected_idx = label_to_index.get(expected, -1)
    y_true.append(expected_idx)

    results = search_law(query, top_k=top_k)
    predicted_idx = -1
    predicted_label = ("None", "None")

    for rank, result in enumerate(results, start=1):
        predicted = (result["meta"]["law"], result["meta"]["section"])
        predicted_idx = label_to_index.get(predicted, -1)
        if predicted == expected:
            if rank == 1:
                correct_at_1 += 1
            correct_within_k += 1
            reciprocal_ranks.append(1 / rank)
            break
    else:
        reciprocal_ranks.append(0)

    if predicted_idx in index_to_label:
        predicted_label = index_to_label[predicted_idx]

    rows.append({
        "Query": query,
        "Expected Law": expected[0],
        "Expected Section": expected[1],
        "Predicted Law": predicted_label[0],
        "Predicted Section": predicted_label[1],
        "Correct": expected == predicted_label
    })
    y_pred.append(predicted_idx)

# Save CSV of predictions
df = pd.DataFrame(rows)
df.to_csv("evaluation_results.csv", index=False)

# Metrics
total = len(test_cases)
precision_at_1 = correct_at_1 / total
recall_at_k = correct_within_k / total
mrr = sum(reciprocal_ranks) / total

# Save summary metrics
with open("evaluation_metrics.txt", "w") as f:
    f.write(f"Evaluation Results on {total} queries:\n")
    f.write(f"Precision@1: {precision_at_1:.2f}\n")
    f.write(f"Recall@{top_k}: {recall_at_k:.2f}\n")
    f.write(f"MRR: {mrr:.2f}\n\n")
    f.write("Classification Report:\n")
    f.write(classification_report(y_true, y_pred, target_names=[
        f"{law} - S{sec}" for law, sec in label_to_index.keys()
    ], zero_division=0))
