from django import forms
from .models import Student

gen = [('male', 'Male'), ('female', 'Female')]
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'roll': 'Student Roll No.',
            'name': 'Student Name',
            'dob': 'Birth Date',
            'gender': 'Gender',
            'marks': 'Marks',
            'profile_pic': 'Profile Picture'
        }

        widgets = {
            'roll': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'gender': forms.RadioSelect(choices=gen),
            'marks': forms.NumberInput(attrs={'class':'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class':'form-control'})
        }