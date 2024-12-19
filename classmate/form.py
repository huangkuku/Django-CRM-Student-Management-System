from django import forms        
from .models import Classmate

class ClassmateForm(forms.ModelForm):
    student_number = forms.CharField(required=True, widget=forms.widgets.NumberInput(attrs={'class':'form-control', 'placeholder':'Student Number'}),label='')
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),label='')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),label='')
    field_of_study = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Field of Study'}),label='')
    grade = forms.CharField(required=True, widget=forms.widgets.NumberInput(attrs={'class':'form-control', 'placeholder':'Student Grade'}),label='')
    chinese_score = forms.CharField(required=True, widget=forms.widgets.NumberInput(attrs={'class':'form-control', 'placeholder':'Chinese Score'}),label='')
    math_score = forms.CharField(required=True, widget=forms.widgets.NumberInput(attrs={'class':'form-control', 'placeholder':'Math Score'}),label='')
    english_score = forms.CharField(required=True, widget=forms.widgets.NumberInput(attrs={'class':'form-control', 'placeholder':'Engilsh Score'}),label='')
    
    class Meta:
        model = Classmate
        fields = ['student_number','first_name','last_name','email','field_of_study','grade','chinese_score','math_score','english_score'] # __all__(使用所有) ==
        