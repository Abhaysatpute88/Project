from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    subtitle_file = models.CharField(max_length=255, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title + ": " + str(self.video_file)




class Subtitle(models.Model):
    video = models.ForeignKey(Video, related_name='subtitles', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.TimeField()
