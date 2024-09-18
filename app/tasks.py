from celery import shared_task
import subprocess
from .models import Video
from django.core.files import File
import os

@shared_task
def extract_subtitles(video_id):
    video = Video.objects.get(id=video_id)
    video_path = video.video_file.path

    # Define the path for the output subtitle file (same name as video but .srt)
    subtitle_output_path = os.path.splitext(video_path)[0] + '.srt'

    try:
        # Run ffmpeg to extract subtitles
        result = subprocess.run(
            ["ffmpeg", "-i", video_path, subtitle_output_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Ensure the subtitle file exists
        if os.path.exists(subtitle_output_path):
            # Open the subtitle file as a Django File object and save it
            with open(subtitle_output_path, 'rb') as f:
                video.subtitle_file.save(os.path.basename(subtitle_output_path), File(f), save=True)

    except subprocess.CalledProcessError as e:
        print(f"Error extracting subtitles: {e.stderr.decode('utf-8')}")
