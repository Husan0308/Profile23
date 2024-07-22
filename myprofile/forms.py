from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class UserCreationForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PersonForm(ModelForm):
    #image = forms.ImageField(required=True)
    #name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #skill = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #website = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #location = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    
    
    class Meta:    
        model = Person 
        fields = "__all__"
    
class EducationForm(ModelForm):
    #year = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #qualification = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"class":"form-control"}), label="")
    #universityname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    

    class Meta:
        model = Education 
        fields = "__all__"

class LanguageForm(ModelForm):
    #language = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #value = forms.DecimalField(required=True)

   
    class Meta:
        model = Language 
        fields = "__all__"

class ProfileForm(ModelForm):
    #about = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"class":"form-control"}), label="")
   

    class Meta:
        model = Profile 
        fields = "__all__"

class ExperienceForm(ModelForm):
    #year_company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #company_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #job = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #about_job = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"class":"form-control"}), label="")
 

    class Meta:
        model = Experience 
        fields = "__all__"

class SkillsForm(ModelForm):
    #skill = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")
    #value = forms.DecimalField(required=True)
   

    class Meta:
        model = Skills 
        fields = "__all__"

class InterestForm(ModelForm):
    #interests = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="")

    class Meta:
        model = Interest 
        fields = "__all__"
