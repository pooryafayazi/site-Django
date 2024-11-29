from django import forms
from wesite1.models import Contact,Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =  '__all__'


"""class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)"""


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields =  '__all__'