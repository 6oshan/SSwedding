from django.db import models

class SliderImage(models.Model):
    title = models.CharField(max_length=100 , blank=True)
    description = models.TextField(blank=True)
    desktop_image = models.ImageField(upload_to='slider/desktop')
    mobile_image = models.ImageField(upload_to='slider/mobile')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Slider {self.id}"
    
class YouTubeLink(models.Model):
    youtube_link = models.URLField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.youtube_link or "YouTube Link"

class Groom(models.Model):
    name = models.CharField(max_length=40 , blank=True )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'groom/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Bride(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='bride/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class FamilyMember(models.Model):
    FAMILY_CHOICES = [
        ('groom', "Groom's Family"),
        ('bride', "Bride's Family"),
    ]

    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100, blank=True)
    family_type = models.CharField(
    max_length=10,
    choices=FAMILY_CHOICES,
    default='groom' 
)
    image = models.ImageField(upload_to='family/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.relation} ({self.family_type})"

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}" 