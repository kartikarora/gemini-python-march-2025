# Gemini API Python Examples

This repository contains a collection of Python examples demonstrating how to use Google's Gemini API for various generative AI tasks. These examples showcase the capabilities of the Gemini models for text generation, image analysis, video understanding, function calling, and more.

This repository is related to the codelab on the same topic available at https://codelabs.kartikarora.me/

## Features

- **Text Generation**: Simple text prompts and responses
- **Streaming Text**: Real-time streaming of generated text
- **Image Analysis**: Processing and understanding images
- **Video Understanding**: Analyzing and extracting information from videos
- **Function Calling**: Using Gemini to call external functions
- **System Instructions**: Customizing model behavior with system prompts
- **Multi-modal Inputs**: Combining text with images for complex queries

## Prerequisites

- Python 3.9+
- Google API key for Gemini

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/GeminiPython2025.git
   cd GeminiPython2025
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv gemini-venv
   source gemini-venv/bin/activate  # On Windows: gemini-venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `credentials.py` file with your Google API key:
   ```python
   GOOGLE_API_KEY = "your-api-key-here"
   ```


## Available Examples

- `simple_text.py`: Basic text generation
- `streaming_text.py`: Real-time text streaming
- `describe_image.py`: Image analysis
- `remote_image.py`: Processing remote images
- `mutliple_images.py`: Working with multiple images
- `prompt_video.py`: Video understanding
- `function_calling.py`: Function calling capabilities
- `system_instructions.py`: Using system instructions

## Models Used

- `gemini-2.0-flash`: Fast text and image processing
- `gemini-1.5-pro`: Advanced multimodal capabilities including video

## Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Python SDK Reference](https://ai.google.dev/api/python/google/generativeai)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
