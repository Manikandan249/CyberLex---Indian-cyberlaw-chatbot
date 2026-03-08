import streamlit as st
from chatbot_backend import search_law

st.set_page_config(page_title="Cyber Law Chatbot 🇮🇳", layout="centered")
st.title("🧑‍⚖️ Indian Cyber Law Chatbot")
st.caption("Ask anything about Indian Cyber Laws. I'll find the most relevant section.")

query = st.text_input("🔎 Type your question here:", placeholder="e.g., Can someone be punished for deleting software code?")

if query:
    results = search_law(query)
    if results:
        for match in results:
            st.subheader(f"📘 Match: {match['meta']['law']} – Section {match['meta']['section']}")
            st.write(f"**Offence:** {match['meta']['offence']}")
            st.write(f"**Punishment:** {match['meta']['punishment']}")
            
            text = match['match']
            layman = text.split('Layman Explanation:')[1].split('Example:')[0].strip()
            example = text.split('Example:')[1].strip()
            
            st.markdown(f"**Explanation:** {layman}")
            st.markdown(f"**Example:** {example}")
            st.markdown("---")
    else:
        st.warning("No matching law found.")
