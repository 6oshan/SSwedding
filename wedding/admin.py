from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SliderImage, YouTubeLink, Groom, Bride, FamilyMember, GalleryImage


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'uploaded_at')

@admin.register(YouTubeLink)
class YouTubeLinkAdmin(admin.ModelAdmin):
    list_display = ('youtube_link', 'uploaded_at')

@admin.register(Groom)
class GroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at')


@admin.register(Bride)
class BrideAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at')


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'relation', 'family_type', 'uploaded_at')
    list_filter = ('family_type',) 
    search_fields = ('name', 'relation') 


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')


