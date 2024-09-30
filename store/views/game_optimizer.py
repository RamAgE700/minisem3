from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests

API_KEY = 'AIzaSyAlkMqarUExaxDatDQ0t-1udhy9H7vrzLM'

class GameOptimizerView(View):
    template_name = 'game_optimizer.html'

    def get(self, request):
        # Render the empty form on GET request
        return render(request, self.template_name)

    def post(self, request):
        game_title = request.POST.get('game_title')
        cpu = request.POST.get('cpu')
        gpu = request.POST.get('gpu')
        ram = request.POST.get('ram')
        resolution = request.POST.get('resolution')

        # Prepare the data in the required format for the API request
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": f"Optimize settings for {game_title} based on specs: CPU: {cpu}, GPU: {gpu}, RAM: {ram}GB, Resolution: {resolution}"}
                    ]
                }
            ]
        }

        # Call the Google Gemini API (replace YOUR_API_KEY)
        url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'
        
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            optimized_settings = response.json()
            return render(request, self.template_name, {'settings': optimized_settings})
        else:
            return render(request, self.template_name, {'error': 'Failed to retrieve optimized settings.'})
