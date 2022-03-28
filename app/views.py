from django.shortcuts import render,redirect
from .models import Intent
from .forms import CreateUserForm,IntentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create your views here.
@login_required(login_url='login')
def home(request):
  form=IntentForm()
  if request.method=='POST':
    form=IntentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  intent=Intent.objects.all()
  context={'form':form,'intent':intent}
  return render(request,'accounts/home.html',context)

def chatbotPage(request):
     # Creating ChatBot Instance
  chatbot = ChatBot(
    'AedificoBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.70
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)
  if request.method=='POST':
    print(request.POST['message'])

    response=chatbot.get_response(request.POST['message'])
    print('response:',response)
    return render(request,'bot/chatbot1.html',{'response':response})
  else:
 

  # Training with Personal Ques & Ans 
    conversation = []
    intent=Intent.objects.all()
    for i in intent:
      conversation.append(i.trigger)
      conversation.append(i.response)
    print(conversation)

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

  # Training with English Corpus Data 
  #   trainer_corpus = ChatterBotCorpusTrainer(chatbot)
  #   trainer_corpus.train(
  #     'chatterbot.corpus.english'
  # ) 
    return render(request,'bot/chatbot1.html')

def registerPage(request):
  form=CreateUserForm()
  if request.method=='POST':
    form =CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user=form.cleaned_data.get('username')
      messages.success(request,'Account Created Successfully for'+ user)
      return redirect('login')
  context={'form':form}
  return render(request,'accounts/register.html',context)

def loginPage(request):
  if request.method=='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      messages.info(request,'Username or Password is incorrect')

  return render(request,'accounts/login.html')

def logoutPage(request):
  logout(request)
  return redirect('login')

