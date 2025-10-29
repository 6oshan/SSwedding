from django.shortcuts import render
from .models import SliderImage,YouTubeLink, Groom, Bride, FamilyMember, GalleryImage

def index(request):
    sliders = SliderImage.objects.all()
    Y_link = YouTubeLink.objects.all()
    groom = Groom.objects.first()
    bride = Bride.objects.first()
    groom_family = FamilyMember.objects.filter(family_type='groom')
    bride_family = FamilyMember.objects.filter(family_type='bride')
    gallery = GalleryImage.objects.all()

    context = {
        'sliders': sliders,
        'Y_link' : Y_link,
        'groom': groom,
        'bride': bride,
        'groom_family': groom_family,
        'bride_family': bride_family,
        'gallery': gallery,
    }
    return render(request, 'index.html', context)
