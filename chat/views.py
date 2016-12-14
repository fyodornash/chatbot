from django.shortcuts import render
from chat.models import Sentence

def home_page_view(request):
    if request.method == 'POST':
        Sentence.objects.create(text = request.POST['story_text'])

    sentences = Sentence.objects.all()
    return render(request,'home.html',{
        'sentences' : sentences
    })
# Create your views here.
