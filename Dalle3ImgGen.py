# Install OpenAI package
# This is required to interact with OpenAI's API
!pip install openai

# Import necessary libraries
from openai import OpenAI
import requests
import os
import time
import json
from google.colab import drive

# Mount Google Drive to save images
drive.mount('/content/drive')

def safe_create_directory(path):
    """Safely create a directory. If the directory already exists, do nothing."""
    os.makedirs(path, exist_ok=True)

# Enter your OpenAI API key here
openai_api_key = "YOUR API KEY"

# Function to enhance prompt using GPT-3.5 with the chat completions endpoint
def enhance_prompt(prompt, openai_api_key):
    """Enhances the given image prompt using GPT-3.5."""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{
            "role": "user",
            "content": f"Improve this image prompt: {prompt}."
        }]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_json = response.json()
        latest_response = response_json.get('choices', [])[0].get('message', {}).get('content', '')
        return latest_response.strip()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return prompt  # Return the original prompt in case of error to avoid breaking the loop

# Initialize a global counter for image filenames
image_counter = 1

def generate_and_save_images(prompt, n=1):
    """Generates and saves images based on the given prompt."""
    global image_counter  # Reference the global counter

    client = OpenAI(api_key=openai_api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1792",
        quality="standard",
        n=n,
    )

    # Path to save images in Google Drive
    drive_folder = "/content/drive/My Drive/Dalle3/"
    safe_create_directory(drive_folder)

    for idx, image in enumerate(response.data):
        image_url = image.url
        image_response = requests.get(image_url)

        # Use the global counter in the filename to ensure a unique, sequential name
        filename = os.path.join(drive_folder, f"image{image_counter}.png")
        with open(filename, 'wb') as file:
            file.write(image_response.content)
        print(f"Image saved as {filename}")

        # Increase the counter for the next image
        image_counter += 1

# Starting prompt
start_prompt = "Generate a Github Logo Wallpaper Mobile, with glowing and minimalistic design"

# Loop to continuously enhance prompt, generate and save images
while True:
    enhanced_prompt = enhance_prompt(start_prompt, openai_api_key)
    print(f"Generating images for: {enhanced_prompt}")
    generate_and_save_images(enhanced_prompt, n=1)  # Adjusted API's constraint
