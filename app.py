import streamlit as st
import google.generativeai as genai
API_KEY = "AQ.Ab8RN6LyFaXw3CGxH1LNCBrUnHsQW0KRLKlNdWfyzWcIheP4sw"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("AI Story Generator")
name = st.text_input("Character Name")
theme = st.text_input("Theme")
genre = st.selectbox(
    "Genre",
    ["Adventure","Fantasy","Mystery",
"Romance","Horror"]
)
length = st.selectbox(
    "Story Length",
    ["Short", "Medium","Long"]
)
if st.button("Generate Story"):
    if not name or not theme:
        st.warning("Please entre Character Name and Theme")
    else:
        prompt = f"""
        Write a {length.lower()}
{genre.lower()} story.
        Main Character: {name}
        Theme: {theme}
        Give the story a title.
        Make it interesting and suitable for students.
        """
        with st.spinner("Generating Story..."):
            response = model.generate_content(prompt)
        st.subheader("Generated Story")
        st.write(response.text)