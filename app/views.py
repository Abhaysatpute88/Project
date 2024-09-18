from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Video, Subtitle
from .forms import VideoUploadForm
from .tasks import extract_subtitles

# Create your views here.

def video_upload(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    videos = Video.objects.all()
    return render(request, 'video_upload.html', {'form': form, 'videos': videos})



def search_subtitles(request):
    query = request.GET.get('q', '').lower()
    video_id = request.GET.get('video_id')
    subtitles = Subtitle.objects.filter(video_id=video_id, content__icontains=query)
    results = [{'timestamp': sub.timestamp, 'content': sub.content} for sub in subtitles]
    return JsonResponse({'results': results})













