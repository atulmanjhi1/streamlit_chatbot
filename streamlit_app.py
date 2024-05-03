import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key="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",
)

def generate_chat_completion(system_message, user_message):
    # Generate chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-70b-8192",
    )
    
    return chat_completion.choices[0].message.content

# Streamlit app layout
st.title("MindfulAI")

# Input fields for system and user messages
system_message = st.text_input("Define Role:")
user_message = st.text_input(" Message:")

# Submit button to generate chat completion
if st.button("Run"):
    # Check if both inputs are not empty
    if system_message and user_message:
        # Generate chat completion and display it
        response = generate_chat_completion(system_message, user_message)
        st.write(f"Response: {response}")
    else:
        st.warning("Please fill in both fields.")
