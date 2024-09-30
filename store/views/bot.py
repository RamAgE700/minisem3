import re
import requests
from django.shortcuts import render
from django.http import JsonResponse

# Your Google Gemini API key
API_KEY = 'AIzaSyAlkMqarUExaxDatDQ0t-1udhy9H7vrzLM'
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

# Function to generate a response from the Gemini API
def generate_response(user_query):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'contents': [{
            'parts': [{
                'text': user_query
            }]
        }]
    }
    # Make a request to the Google Gemini API
    response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        # Extract and return the response text
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            raw_text = response_data['candidates'][0]['content']['parts'][0]['text']
            return clean_response(raw_text)  # Clean the response text
        else:
            return 'No candidates found in response.'
    else:
        return f"Error: {response.status_code} - {response.text}"

# Function to clean the bot's response
def clean_response(response_text):
    # Remove specific patterns like '**Section:**' and standalone '**' or '*' symbols
    cleaned_text = re.sub(r'\*\*\s*([^*]+?)\s*\*\*', r'\1', response_text)  # Remove **Section:** style
    cleaned_text = re.sub(r'\*\*|__|\*', '', cleaned_text)  # Remove any remaining **, __, or *
    cleaned_text = ' '.join(cleaned_text.split())  # Remove extra spaces
    return cleaned_text.strip()

def chatbot_view(request):
    # Initialize chat with a welcome message
    if request.method == 'GET':
        return render(request, 'chatbot.html', {'initial_message': "Which game would you like information about?"})
    
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = generate_response(user_input)
        return JsonResponse({'response': bot_response})
