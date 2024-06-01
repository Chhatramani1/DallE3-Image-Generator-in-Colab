# DallE3-Image-Generator-in-Colab
This project demonstrates how to use OpenAI's DALL-E 3 model to generate images from text prompts. The code enhances the prompts using GPT-3.5 and saves the generated images to Google Drive.

## Key Features

- Enhances image prompts using GPT-3.5.
- Generates high-quality images using DALL-E 3.
- Saves generated images directly to Google Drive.
- Automatically names and organizes saved images.

## Setup Instructions

1. **Install Required Packages:**
    In your first cell, run the following command to install the OpenAI package:
    ```bash
    pip install openai
    ```

2. **Import Necessary Libraries and Mount Google Drive:**
    In your second cell, run the following code:
    ```python
    from openai import OpenAI
    import requests
    import os
    import time
    import json
    from google.colab import drive

    # Mount Google Drive
    drive.mount('/content/drive')
    ```

3. **Enter Your OpenAI API Key:**
    Replace `"YOUR API KEY"` with your actual OpenAI API key in the code.

## Usage

The provided code is designed to:
1. Enhance a text prompt using GPT-3.5.
2. Generate images from the enhanced prompt using DALL-E 3.
3. Save the generated images to a specified folder in Google Drive.

### Functions Overview

- `safe_create_directory(path)`: Safely creates a directory if it doesn't already exist.
- `enhance_prompt(prompt, openai_api_key)`: Enhances the given prompt using GPT-3.5.
- `generate_and_save_images(prompt, n=1)`: Generates and saves `n` images based on the given prompt.

### Example Workflow

1. **Define the Starting Prompt:**
    ```python
    start_prompt = "Generate a Github Logo Wallpaper Mobile, with glowing and minimalistic design"
    ```

2. **Run the Image Generation Loop:**
    The loop continuously enhances the prompt and generates images until stopped:
    ```python
    # Initialize a global counter for image filenames
    image_counter = 1

    # Loop to continuously enhance prompt, generate, and save images
    while True:
        enhanced_prompt = enhance_prompt(start_prompt, openai_api_key)
        print(f"Generating images for: {enhanced_prompt}")
        generate_and_save_images(enhanced_prompt, n=1)
    ```

### Code Explanation

The provided code includes detailed comments to help you understand each part of the process. Here is a brief explanation of the main steps:

1. **Mount Google Drive**: Ensures that Google Drive is mounted so images can be saved there.
2. **Enhance Prompt**: Uses GPT-3.5 to improve the image prompt.
3. **Generate Images**: Uses DALL-E 3 to generate images from the enhanced prompt.
4. **Save Images**: Saves the generated images to Google Drive with unique filenames.

## Requirements

- Python 3.x
- Google Colab (for Google Drive integration)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

