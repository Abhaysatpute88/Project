from django.contrib import admin
from .models import Video, Subtitle

# Register the Video model
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'video_file', 'subtitle_file')
    search_fields = ('title',)
    list_filter = ('upload_date',)

# Register the Subtitle model
@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    list_display = ('video', 'language', 'timestamp')
    search_fields = ('video__title', 'text')
    list_filter = ('language',)