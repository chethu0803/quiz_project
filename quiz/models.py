from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

#BaseUserManager allows to use Django's built-in User Model which is very useful when authentication
class AccountManager(BaseUserManager):
  #This method will be called with certain params when the user enters the username in Welcome Page.
  def create_user(self, username,email=None, password=None):
    if not username:
      raise ValueError('The Username field must be set')
    user = self.model(username=username,email=email)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  #This method allows the admin to create a superuser in terminal
  #These two are built-in functions which can be used to create users
  def create_superuser(self,email,username,password):
    user=self.create_user(email=email,username=username,password=password)
    user.is_staff=True
    user.is_admin=True
    user.is_active=True
    user.is_superadmin=True
    user.save(using=self._db)
    return user

#Account model is an extension of Django's built in user model where we can customize/extend the existing user model.
class Account(AbstractBaseUser):
  username=models.CharField(max_length=100)
  email=models.EmailField(unique=True,blank=True,null=True)

  date_joined=models.DateTimeField(auto_now_add=True)
  last_login=models.DateTimeField(auto_now=True)
  is_active=models.BooleanField(default=False)
  is_staff=models.BooleanField(default=False)
  is_admin=models.BooleanField(default=False)
  is_superadmin=models.BooleanField(default=False)

  USERNAME_FIELD='email'
  REQUIRED_FIELDS=['username']

  objects=AccountManager()

  def __str__(self):
    return self.username
  
  def has_perm(self,perms,obj=None):
    return self.is_admin
  
  def has_module_perms(self,addlabel):
    return True

#This model aims to store User Performance details
class UserProfile(models.Model):
  user=models.ForeignKey(Account,on_delete=models.CASCADE)
  total_questions_attempted=models.IntegerField(blank=True,default=0)
  score=models.IntegerField(blank=True,default=0)
  percentage=models.IntegerField(blank=True,default=0)
 
  def __str__(self):
    return self.user.username


#This model aims to store the questions.
class Question(models.Model):
  question=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.question
  
#This model aims to store the Quiz.
class Quiz(models.Model):
  title=models.TextField()
  description=models.TextField()
  total_questions=models.IntegerField(default=1)
  question=models.ManyToManyField(Question) #ManyToMany While creating quiz we can slect an existing question or create a new one.
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name='Quiz'
    verbose_name_plural='Quizes'

  def __str__(self):
    return self.title

#This model aims to store the UserQuiz attempts..
class UserQuizAttempt(models.Model):
  user=models.ForeignKey(Account,on_delete=models.CASCADE)
  quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
  score=models.IntegerField()
  created_at=models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return f"{self.user} attended {self.quiz} with a score of {self.score}"
  
#This model consists of option and related question
class Choice(models.Model):
  question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')
  choice=models.TextField()
  is_correct=models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.choice
  







  
  