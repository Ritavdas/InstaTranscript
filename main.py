import os

import instaloader
import whisper
from moviepy.editor import VideoFileClip


def download_instagram_reel(reel_url, download_path):
    # Initialize Instaloader
    loader = instaloader.Instaloader()
    # Download the reel
    loader.download_post(
        instaloader.Post.from_shortcode(loader.context, reel_url.split("/")[-2]),
        target=download_path,
    )
    # Find the downloaded video file
    for file in os.listdir(download_path):
        if file.endswith(".mp4"):
            return os.path.join(download_path, file)
    return None


def extract_audio_from_video(video_path, audio_path):
    # Load the video file
    video = VideoFileClip(video_path)
    # Extract and save the audio
    video.audio.write_audiofile(audio_path)


def transcribe_audio(audio_path):
    # Load the Whisper model
    model = whisper.load_model("base")
    # Transcribe the audio file
    result = model.transcribe(audio_path)
    return result["text"]


def main(reel_url):
    download_path = "downloads"
    audio_path = "audio.wav"
    os.makedirs(download_path, exist_ok=True)

    try:
        print("Downloading Instagram Reel...")
        video_path = download_instagram_reel(reel_url, download_path)
        if not video_path:
            print("Failed to download the Instagram Reel.")
            return

        print("Extracting audio from video...")
        extract_audio_from_video(video_path, audio_path)

        print("Transcribing audio...")
        transcript = transcribe_audio(audio_path)
        print("Transcript:")
        print(transcript)

    finally:
        # Clean up downloaded files and folders
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(download_path):
            for file in os.listdir(download_path):
                os.remove(os.path.join(download_path, file))
            os.rmdir(download_path)


# if __name__ == "__main__":
reel_url = input("Enter the Instagram Reel URL: ")
main(reel_url)
