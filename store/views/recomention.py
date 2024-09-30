from django import forms
from django.shortcuts import render
import google.generativeai as genai
import requests

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyAlkMqarUExaxDatDQ0t-1udhy9H7vrzLM")


# Define the form inside the view
class GameRecommendationForm(forms.Form):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Simulation', 'Simulation'),
    ]
    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
        ('PS5', 'PS5'),
    ]
    
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=True)
    release_year_start = forms.IntegerField(label="Release Year Start (2000-2024)", min_value=2000, max_value=2024, required=True)
    release_year_end = forms.IntegerField(label="Release Year End (2000-2024)", min_value=2000, max_value=2024, required=True)
    price_min = forms.IntegerField(label="Minimum Price ($)", min_value=0, max_value=100, required=True)
    price_max = forms.IntegerField(label="Maximum Price ($)", min_value=0, max_value=100, required=True)
    rating_min = forms.DecimalField(label="Minimum Rating (0-10)", min_value=0, max_value=10, decimal_places=1, required=True)
    rating_max = forms.DecimalField(label="Maximum Rating (0-10)", min_value=0, max_value=10, decimal_places=1, required=True)
    platform = forms.MultipleChoiceField(choices=PLATFORM_CHOICES, widget=forms.CheckboxSelectMultiple, required=True)

def parse_recommendations(response_text):
    # Split the response by lines and extract table rows
    lines = response_text.split("\n")
    table_data = []
    for line in lines:
        if "|" in line:
            row = [item.strip() for item in line.split("|")[1:-1]]  # Splits by '|' and removes empty cells
            table_data.append(row)
    return table_data

def game_recommendation_view(request):
    form = GameRecommendationForm()
    recommendations = None

    if request.method == 'POST':
        form = GameRecommendationForm(request.POST)
        if form.is_valid():
            # Get the form data
            genre = form.cleaned_data['genre']
            release_year_start = form.cleaned_data['release_year_start']
            release_year_end = form.cleaned_data['release_year_end']
            price_min = form.cleaned_data['price_min']
            price_max = form.cleaned_data['price_max']
            rating_min = form.cleaned_data['rating_min']
            rating_max = form.cleaned_data['rating_max']
            platform = ','.join(form.cleaned_data['platform'])

            # Create the prompt based on user input
            prompt = f"""
            recommend video games in table format. 
            Genre: {genre}, 
            Release Year Range: {release_year_start}-{release_year_end}, 
            Price ($) Range: {price_min}-{price_max}, 
            Rating Range: {rating_min}-{rating_max}, 
            Platforms: {platform}
            """

            # Start a chat session with the model
            chat_session = genai.GenerativeModel(model_name="gemini-1.5-flash").start_chat(
                history=[
                    {
                        "role": "user",
                        "parts": [prompt],
                    }
                ]
            )

            # Send the request and get the response
            response = chat_session.send_message("recommend video games")
            recommendations = parse_recommendations(response.text)

    return render(request, 'game_recommendation.html', {'form': form, 'recommendations': recommendations})
