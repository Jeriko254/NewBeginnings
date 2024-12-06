from django.shortcuts import render,redirect

from Newapp.form import ImageUploadForm
from Newapp.models import Registration, ImageModel


# Create your views here.
def registration(request):
   if request.method == "POST":
      myregister = Registration(
         fullname=request.POST['fullname'],
         username=request.POST['username'],
         email=request.POST['email'],
         password=request.POST['password'],

      )
      myregister.save()
      return redirect('/login')

   else:
      return render(request, 'registration.html')
def login(request):
   return render(request,'login.html')


def home(request):
   if request.method == 'POST':
      if Registration.objects.filter(
              username=request.POST['username'],
              password=request.POST['password']
      ).exists():
         return render(request, 'home.html')
      else:
         return render(request, 'login.html')
   else:
      return render(request, 'home.html')


def about(request):
   return render(request,'about.html')
def streak(request):
   return render(request,'streak.html')
def affirmation(request):
   return render(request,'affirmation.html')
def articles(request):
   return render(request,'articles.html')
def reviews(request):
   return render(request,'reviews.html')


def addreview(request):
   if request.method == 'POST':
      form = ImageUploadForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('/extrareviews')
   else:
      form = ImageUploadForm()
   return render(request, 'addreview.html', {'form': form})


def extrareviews(request):
    images = ImageModel.objects.all()
    return render(request, 'extrareviews.html', {'images': images})


def imagedelete(request, id):
   image = ImageModel.objects.get(id=id)
   image.delete()
   return redirect('/addreview')


def emergency(request):
   return render(request,'emergency.html')

def article1(request):
   return render(request,'article1.html')

def article2(request):
   return render(request,'article2.html')

def article3(request):
   return render(request,'article3.html')

def article4(request):
   return render(request,'article4.html')

def article5(request):
   return render(request,'article5.html')

def article6(request):
   return render(request,'article6.html')

def support(request):
   return render(request,'support.html')