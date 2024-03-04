import requests
import os
import argparse


# Setup command line argument parsing
parser = argparse.ArgumentParser(description='Send text to the Gemini API and get a response.')
parser.add_argument('-t', '--text', help='The text to send to the API, specify multiple times for multi-turn.', required=True)
args = parser.parse_args()

# Retrieve environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = os.getenv("GEMINI_URL")


if not GEMINI_API_KEY or not GEMINI_URL:
    print("Environment variables for GEMINI_API_KEY and GEMINI_URL are not set.")
else:
    # Prepare the API URL
    api_url = f"{GEMINI_URL}?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    # Define your request payload, adjust according to the API's expected format
    payload = {
    "contents": [{
        "parts": [{
            "text": args.text
        }]
    }]
}

    # Make the POST request
    response = requests.post(api_url,headers=headers, json=payload)

    if response.status_code == 200:
        # If request is successful, process the response
        data = response.json()
        print(data["candidates"][0]["content"]["parts"][0]["text"])

        
    else:
        # If there was an error, print the error
        print(f"Error: {response.status_code}")
        print(response.text)

