# Personal-AI-Assistant
Build your own Jarvis for free using Google Gemini from scratch using Python(Local as well as on Cloud)

Step 1: Create a virtual environment 
```
pip install virtualenv
python3.9 -m venv ai_assistant
source ai_assistant/bin/activate
pip install --upgrade pip
```
Step 2: Create a requirements.txt file
Add pakages that are needed for the project
```
pip3 install -r requirements.txt
```
Step 3: 
Download or copy Gemini api key from Google AI Studio, its free!!!

Open this Link: https://ai.google.dev/
If the link is dead by the time you open this link google: Gemini Api key and the results  will get you the page.

Step 4:
After you get the api key then run these commands on your terminal
```
vim ~/.bashrc
```

Go to the end of file and add this to the file
```
export GEMINI_API_KEY='key-you-got-from-google-gemini' 
(update google api key here!!)
```
```
export GEMINI_URL='https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
```
close the vim while  saving the file using :wq

```
source ~/.bashrc
```

