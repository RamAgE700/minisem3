# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import os

# Set your API key
os.environ["GEMINI_API_KEY"] = "AIzaSyA_VjcdSNFywoWL5eDjJnWNbgIyOaBAIOE"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@csrf_exempt  # Disable CSRF protection for testing; use with caution
def chat_view(request):
    if request.method == 'POST':
        # Get the user's message from the request
        user_message = request.POST.get('message')

        # Create a chat session
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "I want to travel to a location in a selected car. Please provide the details.",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Sure! Please tell me your travel location, the car you selected, the number of people, and the number of days.",
                    ],
                },
            ]
        )

        # Send the user's message to the chat session and get a response
        response = chat_session.send_message(user_message)

        # Return the response as JSON
        return JsonResponse({'response': response.text})

    return JsonResponse({'error': 'Method not allowed'}, status=405)  # Handle non-POST requests