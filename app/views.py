import ffmpeg
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
import os
from django.db.models import Q

# Function to extract subtitles using ffmpeg

def extract_subtitles(video_path):
    input_file = video_path
    output_file = os.path.splitext(input_file)[0] + '.vtt'  # Convert to .vtt for the video player

    # Use ffmpeg to extract subtitles as .vtt
    (
        ffmpeg
        .input(input_file)
        .output(output_file, format='webvtt', map='0:s:0')  # Extract subtitle stream
        .run()
    )

    # Read the subtitle file and return its contents for display
    with open(output_file, 'r', encoding='utf-8') as subtitle_file:
        subtitle_content = subtitle_file.read()

    return output_file, subtitle_content  # Return both file path and text content




# Video Upload View
def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            # Process the video and extract subtitles
            subtitle_file_path, subtitle_text = extract_subtitles(video.video_file.path)
            video.subtitle_file = subtitle_file_path  # Save the file path to the subtitle file
            video.subtitle_text = subtitle_text  # Save the actual subtitle text for display
            video.save()
            return redirect('video_list')  # Redirect to video list
    else:
        form = VideoForm()
    return render(request, 'video_upload.html', {'form': form})



# List and Search Videos
def video_list(request):
    query = request.GET.get('q')
    if query:
        # Search for phrases within subtitles
        videos = Video.objects.filter(Q(subtitle_text__icontains=query))
    else:
        videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})



# Play Video with Captions
def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_detail.html', {'video': video})
