from django.db import models



class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    subtitle_file = models.FileField(upload_to='subtitles/', blank=True)  # Path to the .vtt file
    subtitle_text = models.TextField(blank=True)  # Store the subtitle text for display
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
