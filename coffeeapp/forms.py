from django import forms
from .models import Contact,BookTable


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control bg-transparent p-4','id':'name','placeholder':'Your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control bg-transparent p-4','id':'name','placeholder':'Your Email'}),
            'subject':forms.TextInput(attrs={'class':'form-control bg-transparent p-4','id':'name','placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control bg-transparent py-3 px-4','id':'name','placeholder':'Message','rows':5})
        }


class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = '__all__'
        widgets = {  
            'name': forms.TextInput(attrs={'class':'form-control bg-transparent border-primary p-4 mb-4','placeholder':'Name'}),
            'email' : forms.TextInput(attrs={'class':'form-control bg-transparent border-primary p-4 mb-4','placeholder':'Email'}),
            'date' : forms.DateInput(format=('%d-%m-%Y'),attrs={'class':'form-control bg-transparent border-primary p-4 mb-4', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date','placeholder':'Date'}),
            'time' : forms.TimeInput(format=('%H:%M'),attrs={'class':'form-control bg-transparent border-primary p-4 mb-4','type':'time', 'lang': 'pl','placeholder':'Time'}),
            'person' : forms.Select(attrs={'class':'custom-select bg-transparent border-primary p-4 mb-4','placeholder':'No. of Persons'})

        }      