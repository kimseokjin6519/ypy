# Python youtube-transcript-api

from youtube_transcript_api import YouTubeTranscriptApi
import json

def main():

        # Prompt for video ID
        video_id = input("Enter Youtube video ID: ").strip()
        if not video_id:
                return

        # Set language code to 'en'
        language = 'en'

        # fetch video transcript by ID and languages
        try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en'])
        except Exception as e:
                print(f"Error: {e}")
                return

        # Format transcript into JSON
        json_transcript = json.dumps(transcript, indent = 4, ensure_ascii = False)

        # Set file_name to (video_id).json
        try:

                file_name = video_id + ".json"
                with open(file_name, 'w', encoding = 'utf-8') as file:
                        file.write(json_transcript)
        except Exception as e:
                print(f"Error saving file: {e}")

        print(f"Success!!")

if __name__ == "__main__":
            main()
