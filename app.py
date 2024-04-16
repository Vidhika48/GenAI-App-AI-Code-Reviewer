import streamlit as st
from openai import OpenAI

# Load your OpenAI API key from a file
with open('key.txt') as f:
    OPENAI_API_KEY = f.read().strip()

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to perform code review
def code_review(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a code reviewer for a software development company. 
                Your responsibility is to meticulously examine submitted code for potential bugs, errors, 
                or areas of improvement to ensure the quality and efficiency of the software. 
                You are known for your constructive feedback and keen eye for detail. 
                If the code meets all requirements and standards, you provide commendation and suggestions 
                for further enhancements. However, if there are issues, you kindly point them out 
                and offer suggestions for improvement. Let's review the submitted code together."""},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
def main():
    st.title('GenAI App - AI Code Reviewer')
    st.write("Submit your Python code for review.")

    # Input for user's Python code
    user_input = st.text_area("Enter your Python code here:", "")

    if st.button("Submit"):
        if user_input.strip() == "":
            st.warning("Please enter some Python code for review.")
        else:
            # Perform code review
            st.write("Reviewing your code...")
            ai_response = code_review(user_input)
            st.write("AI's Response:")
            st.code(ai_response)

if __name__ == "__main__":
    main()