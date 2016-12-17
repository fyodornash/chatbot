from django.shortcuts import render,redirect
from chat.models import Sentence,Conversation,Response
from chat.eliza import analyze;

def home_page_view(request):
    '''if request.method == 'POST':
        conversation = Conversation.objects.create()
        Sentence.objects.create(text = request.POST['story_text'],conversation=conversation)
        sentences = Sentence.objects.all()
        return render(request,'conversation.html',{
            'sentences' : sentences,
            'conversation': conversation,
        })'''

    return render(request,'home.html')

def new_conversation(request):
    conversation = Conversation.objects.create()
    Sentence.objects.create(text = request.POST['story_text'],conversation = conversation)   
    Response.objects.create(text = analyze(request.POST['story_text']),conversation = conversation)
    responses=Response.objects.filter(conversation=conversation)
    sentences=Sentence.objects.filter(conversation=conversation)

    exchanges = list(zip(sentences,responses))

    return render(request,'conversation.html',{
        'exchanges' : exchanges,
        'conversation':conversation,
    })

def view_conversation(request,conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    sentences=Sentence.objects.filter(conversation=conversation)
    responses=Response.objects.filter(conversation=conversation)
    
    exchanges = list(zip(sentences,responses))

    return render(request,'conversation.html', {
        'exchanges' : exchanges,
        'conversation':conversation,
    })
    

def add_exchange(request,conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    Sentence.objects.create(text = request.POST['story_text'],conversation = conversation)
    Response.objects.create(text = analyze(request.POST['story_text']),conversation = conversation)
    return redirect('/conversation/%d/' % (int(conversation_id),))

#Create your views here.
