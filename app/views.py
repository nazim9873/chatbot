from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Intent
from .forms import CreateUserForm,IntentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.http import JsonResponse
from .models import User
# Create your views here.
@login_required(login_url='login')
def home(request):
  form=IntentForm(initial={'user':request.user})
  user=request.user
  if request.method=='POST':
    data=request.POST.copy()
    userobj=User.objects.get(username=user)
    data['user']=userobj
    form=IntentForm(data)
    if form.is_valid():
      form.save()
      return redirect('home')
  intent=user.intent_set.all()
  context={'form':form,'intent':intent,'user':user}
  return render(request,'accounts/home.html',context)

def edit_intent(request,pk):
  if request.method=='POST':
    intent=Intent.objects.get(id=pk)
    data=request.POST.copy()
    userobj=intent.user
    data['user']=userobj
    form=IntentForm(data,instance=intent)
    print(form)
    if form.is_valid():
      form.save()
      return redirect('/home')
    else:
      print('Not valid')  
  else:
    intent=Intent.objects.get(id=pk)
    form=IntentForm(instance=intent)
  return render(request,'accounts/edit_home.html',{'form':form})  

def delete_intent(request,pk):
  if request.method=='POST':
    intent=Intent.objects.get(id=pk)
    intent.delete()
    return HttpResponseRedirect('/home')

def chatbotPage(request):
  # Creating ChatBot Instance
  chatbot = ChatBot(
    request.user.username,
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

    response=chatbot.get_response(request.POST.get('a',"False"))
    
    data={'response':str(response)}
    print(data)

    return JsonResponse({'status':'OK','response':str(response)})
  else:
 
    print(request.user)

  # Training with Personal Ques & Ans 
    conversation = []
    intent=request.user.intent_set.all()
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

