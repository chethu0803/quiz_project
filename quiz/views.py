from django.shortcuts import render,redirect
from .models import Account,UserProfile,Question,Choice

#Welcome function aims to create a User Record in DB and sessions.
def welcome(request):
  if request.method == "POST": #Checking for POST request
    name = request.POST.get("name")
    if Account.objects.filter(username=name).exists():
      print('XXX')
      return redirect('dashboard')  #Redirect to Dashboard if user already exists in DataBase
    else:
      user = Account.objects.create_user(username=name) #Creating a new user record in DB.
      userprofile = UserProfile(user=user) #New UserProfile
      userprofile.save() #Saving Userprofile to DB
      user.save() # Saving the User Record to DB
      request.session['username'] = name #Creating a session
      return redirect('dashboard')
  try:
    if request.session['username']:
      return redirect('dashboard')
  except:
    return render(request, 'quiz/welcome.html')
  return render(request, 'quiz/welcome.html')


def dashboard(request):
  username=request.session.get('username') #checking for existing session
  if username:
    try:
      user=Account.objects.get(username=username) #extracting user based on session name
      userprofile=UserProfile.objects.get(user=user)
    except:
      return redirect('welcome')
  else:
    return redirect('welcome')
  
  context={
    'userprofile':userprofile,
    }
  return render(request,'quiz/dashboard.html',context)

def quiz(request):
  questions=Question.objects.all().order_by("?") #Retrives all records and shuffles them.
  if questions:
    question=questions.first() #First QuerySet
  context={
    'question':question,
  }
  return render(request,'quiz/quiz.html',context)

def submission(request):
  if request.method=="POST":

    question_id=request.POST['question_id'] #extracting question_id which is submitted through Forms
    user_choice=request.POST.get('user_choice')  #extracting user_choice which is submitted through Forms which is a choice_id

    if user_choice is not None:
      user_choice = int(user_choice) #Converting to int
    else:
      user_choice = None 

    correct_choice=Choice.objects.filter(question__id=question_id,is_correct=True).first() #Searching for the correct choice based on the question id and boolean value
    username=request.session.get('username')

    user=Account.objects.get(username=username) #Retrieving user object
    userprofile=UserProfile.objects.get(user=user)
    userprofile.total_questions_attempted+=1 #Incrementing the attempts of a question

    if user_choice==correct_choice.id:
      userprofile.score+=1  #Incrementing the score
    calc_percent=(userprofile.score/userprofile.total_questions_attempted)*100 #Calculating the percentage
    userprofile.percentage=calc_percent

    userprofile.save() #Updating the user's performance to UserProfile
    question=Question.objects.get(id=question_id)
  context={
    'correct_choice':correct_choice,
    'question':question,
    'user_choice':user_choice,
  }
  return render(request,'quiz/quiz.html',context)