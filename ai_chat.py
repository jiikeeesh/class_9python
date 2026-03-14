import os
from google import genai

# Setup the client
client = genai.Client(api_key="Google-Api Key") # Or os.getenv("GOOGLE_API_KEY")

print("--- Modern Gemini Chat (Type 'exit' to stop) ---")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    # New syntax for Gemini 2.0 Flash
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input
    )
    
    print(f"Gemini: {response.text}\n")