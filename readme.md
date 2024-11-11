# Instagram Reel Transcription with Python

Automate the process of downloading Instagram Reels, extracting audio, and transcribing the content using OpenAI's Whisper model. This tool is perfect for social media enthusiasts, content creators, and data analysts who want to generate transcripts efficiently.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Download Instagram Reels**: Fetch publicly accessible Instagram Reels using the Instaloader library.
- **Extract Audio**: Convert downloaded video files into audio files with MoviePy.
- **Transcribe Audio**: Generate accurate transcripts from audio files using OpenAI's Whisper model.

## Prerequisites

- **Python 3.8** or higher
- A machine with adequate resources to run the Whisper model

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/instagram-reel-transcription.git
   cd instagram-reel-transcription
   ```

2. **Create a Virtual Environment (Optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Libraries**

   ```bash
   pip install instaloader moviepy openai-whisper
   ```

## Usage

1. **Run the Script**

   ```bash
   python script_name.py
   ```

2. **Input the Instagram Reel URL**

   When prompted, paste the URL of the Instagram Reel you wish to transcribe.

   ```plaintext
   Enter the Instagram Reel URL:
   ```

3. **View the Transcript**

   The script will display the transcribed text in the console.

## Example

Here's a step-by-step example of how to use the script.

1. **Start the Script**

   ```bash
   python reel_transcriber.py
   ```

2. **Enter the Reel URL**

   ```plaintext
   Enter the Instagram Reel URL: https://www.instagram.com/reel/EXAMPLE_SHORTCODE/
   ```

3. **Output**

   ```plaintext
   Transcript:
   This is the transcribed text of the Instagram Reel.
   ```

## Limitations

- **Resource Intensive**: The Whisper model requires significant computational resources. Ensure your machine meets the requirements.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs, features, or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
