from django import forms
from django.forms import modelformset_factory
from django.forms.widgets import TextInput, Textarea

from .models import *


class PersonalForm(forms.ModelForm):
    name = forms.CharField(label="Name",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', }))
    email = forms.CharField(label="Email",
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', }))
    mobile = forms.CharField(label="Mobile",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile', }))
    summary = forms.CharField(label="Summary",
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Summary', }))
    city = forms.CharField(label="City",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City', }))
    country = forms.CharField(label="Country",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country', }))

    class Meta:
        model = Personal
        fields = ['name', 'email', 'mobile', 'summary', 'city', 'country']


class SkillsForm(forms.ModelForm):
    technical = forms.CharField(label="Technical Skills",
                           widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Technical', }))
    management = forms.CharField(label="Management Skills",
                            widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Management', }))

    class Meta:
        model = Skills
        fields = ['management', 'technical']


EducationFormset_extra1 = modelformset_factory(Education,
                                        exclude=('user',), extra=1, max_num=4,
                                        widgets={
                                            'college': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'College', }),
                                            'gpa': TextInput(attrs={'class': 'form-control', 'placeholder': 'GPA', }),
                                            'degree': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'Degree', }),
                                            'major': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'Major', }),
                                            'city': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'City', }),
                                            'country': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'Country', }),
                                            'from_year': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'From', }),
                                            'to_year': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'To', })

                                        })

EducationFormset = modelformset_factory(Education,
                                        exclude=('user',), extra=0, max_num=4,
                                        widgets={
                                            'college': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'College', }),
                                            'gpa': TextInput(attrs={'class': 'form-control', 'placeholder': 'GPA', }),
                                            'degree': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'Degree', }),
                                            'major': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'Major', }),
                                            'city': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'City', }),
                                            'country': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'Country', }),
                                            'from_year': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'From', }),
                                            'to_year': TextInput(
                                                attrs={'class': 'form-control', 'placeholder': 'To', })

                                        })


WorkFormset = modelformset_factory(Work,
                                   exclude=('user',), extra=1, max_num=6,
                                   widgets={
                                       'company': TextInput(
                                           attrs={'class': 'form-control', 'placeholder': 'Company', }),
                                       'designation': TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation', }),
                                       'work_summary': Textarea(attrs={'class': 'form-control', 'placeholder': 'Roles', }),
                                       'city': TextInput(
                                           attrs={'class': 'form-control', 'placeholder': 'City', }),
                                       'country': TextInput(
                                           attrs={'class': 'form-control', 'placeholder': 'Country', }),
                                       'from_year': TextInput(
                                           attrs={'class': 'form-control', 'placeholder': 'From', }),
                                       'to_year': TextInput(
                                           attrs={'class': 'form-control', 'placeholder': 'To', }),
                                   })


