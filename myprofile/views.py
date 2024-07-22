from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
import json



from django.contrib.auth import authenticate

def index(request):

    return render(request, 'profile/index.html')

def home(request):

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     person, created = Person.objects.get_or_create(customer=customer)
    #     person.save()
    # if request.user.is_authenticated:
    #     education = request.user.education

    persons = Person.objects.all()
    educations = Education.objects.all()
    languages = Language.objects.all()
    profiles = Profile.objects.all()
    experiences = Experience.objects.all()
    skills = Skills.objects.all()
    interests = Interest.objects.all()



        
    context = {
        'persons':persons,
        'educations':educations,
        'languages':languages, 
        'profiles':profiles,
        'experiences':experiences,
        'skills':skills,
        'interests':interests,
        # 'education':education
        }
    return render(request, 'profile/home.html', context)


def login_user(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('add')
        else:
            return redirect('login')
    else:
        return render(request, 'profile/login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('home')

def signup_user(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
 
        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        print(uname,email,pass1,pass2)
        return redirect('login')

    return render(request, 'profile/signup.html', {} )


def save_personal(request):

   
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        image_path = None
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            image_path = default_storage.save(f'media/{image.name}', ContentFile(image.read()))
        person = Person.objects.create(
            name=request.POST.get('name'),
            level=request.POST.get('level'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            website=request.POST.get('website'),
            location=request.POST.get('location'),
            image=image_path
        )

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     education = Education.objects.get_or_create(customer=customer)
    # else:
    #     return redirect('login')

    return JsonResponse(data={'msg':'OK'}, status=200)

    
      
def save_skill_box(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])

        for item in data:
            skills = Skills.objects.create(
                skill=item.get('skill'),
                value=item.get('skill_level'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_education_box(request):
    

    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])
        
        for item in data:
            education = Education.objects.create(
                year=item.get('year'),
                qualification=item.get('qualification'),
                universityname=item.get('universityname')
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_language_box(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])
        
        for item in data:
            language = Language.objects.create(
                language=item.get('language'),
                value=item.get('level'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_profile_box(request):
    if request.method == 'POST':
        print(request.POST)
        
        profile = Profile.objects.create(
            about=request.POST.get('about'),
        )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_experience_box(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])

        for item in data:
            experience = Experience.objects.create(
                year_company=item.get('year_company'),
                company_name=item.get('company_name'),
                job=item.get('job'),
                about_job=item.get('about_job'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)


def save_interest_box(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])
         
        for item in data:
            interest = Interest.objects.create(
                interests=item.get('interests'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def add(request):

    if request.method == "POST":
        personform = PersonForm(request.POST)
        print(' --- ', request.FILES)
        educateform = EducationForm(request.POST)
        languageform = LanguageForm(request.POST)
        profileform = ProfileForm(request.POST)
        experienceform = ExperienceForm(request.POST)
        skillform = SkillsForm(request.POST)
        interestform = InterestForm(request.POST)
        
        if personform.is_valid() and educateform.is_valid() and languageform.is_valid() and profileform.is_valid() and experienceform.is_valid() and skillform.is_valid() and interestform.is_valid():
            personform.save()
            print(' -- ',personform.files)
            educateform.save()
            languageform.save()
            profileform.save()
            experienceform.save()
            skillform.save()
            interestform.save()

            return redirect('home')
    else:
        personform = PersonForm()
        educateform = EducationForm()
        languageform = LanguageForm()
        profileform = ProfileForm()
        experienceform = ExperienceForm()
        skillform = SkillsForm()
        interestform = InterestForm()

    personform = PersonForm
    educateform = EducationForm
    languageform = LanguageForm
    profileform = ProfileForm
    experienceform = ExperienceForm
    skillform = SkillsForm
    interestform = InterestForm()
        
    return render(request, 'profile/add1.html', {
                                        'personform':personform, 
                                        'educateform':educateform,
                                        'languageform':languageform, 
                                        'profileform':profileform, 
                                        'experienceform':experienceform, 
                                        'skillform':skillform, 
                                        'interestform':interestform
                                        })


# def education(request):

#     if request.method == "POST":
#         educateform = EducationForm(request.POST)
        
#         if educateform.is_valid():
#             educateform.save()
#             return redirect('home')
#     else:
#         educateform = EducationForm()

#     educateform = EducationForm
#     return render(request, 'profile/education.html', {'educateform':educateform})

# def language(request):

#     if request.method == "POST":
#         languageform = LanguageForm(request.POST)
        
#         if languageform.is_valid():
#             languageform.save()
#             return redirect('home')
#     else:
#         languageform = LanguageForm()

#     languageform = LanguageForm
#     return render(request, 'profile/language.html', {'languageform':languageform})

# def experience(request):

#     if request.method == "POST":
#         experienceform = ExperienceForm(request.POST)
        
#         if experienceform.is_valid():
#             experienceform.save()
#             return redirect('home')
#     else:
#         experienceform = ExperienceForm()

#     experienceform = ExperienceForm
#     return render(request, 'profile/experience.html', {'experienceform':experienceform})


# def skill(request):

#     if request.method == "POST":
#         skillform = SkillsForm(request.POST)
        
#         if skillform.is_valid():
#             skillform.save()
#             return redirect('home')
#     else:
#         skillform = SkillsForm()

#     skillform = SkillsForm
#     return render(request, 'profile/skill.html', {'skillform':skillform})

# def interest(request):

#     if request.method == "POST":
#         interestform = InterestForm(request.POST)
        
#         if interestform.is_valid():
#             interestform.save()
#             return redirect('home')
#     else:
#         interestform = InterestForm()

#     interestform = InterestForm

        
#     return render(request, 'profile/interest.html', {'interestform':interestform})