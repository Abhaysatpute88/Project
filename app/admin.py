from django.contrib import admin
from .models import Video

# Register the Video model
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'video_file', 'subtitle_text')
    search_fields = ('title',)
    list_filter = ('upload_date',)