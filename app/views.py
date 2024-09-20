import ffmpeg
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
import os
from django.db.models import Q

# Function to extract subtitles using ffmpeg

def extract_subtitles(video_path):    
    input_file = video_path
    output_file = os.path.splitext(input_file)[0] + '.srt'

    # Use ffmpeg to extract subtitles
    (
        ffmpeg
        .input(input_file)
        .output(output_file, format='srt', map='0:s:0')  # 'map' selects the subtitle stream, typically 0:s:0
        .run()
    )
    return output_file 



# Video Upload View
def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            # Process the video and extract subtitles
            video.subtitle = extract_subtitles(video.video_file.path)
            video.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video_upload.html', {'form': form})



# List and Search Videos
def video_list(request):
    query = request.GET.get('q')
    if query:
        # Search for phrases within subtitles
        videos = Video.objects.filter(Q(subtitle__icontains=query))
    else:
        videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})



# Play Video with Captions
def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_detail.html', {'video': video})
