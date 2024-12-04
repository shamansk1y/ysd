from main_page.models import ContactUs, Subscription
from django import forms

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "name",
                'placeholder': "Enter Your Name",
                'required': "required",
                'data-validation-required-message': "Please enter your name",
            }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': "form-control",
                'id': "email",
                'placeholder': "Enter Your Email",
                'required': "required",
                'data-validation-required-message': "Please enter your email",
            }))

    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "subject",
                'placeholder': "Enter Your Subject",
                'required': "required",
                'data-validation-required-message': "Please enter a subject",
            }))


    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'rows': "8",
                'id': "message",
                'placeholder': "Write Your Message",
                'required': "required",
                'data-validation-required-message': "Please enter your message",
            }))

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'placeholder': "Your Email",
            }))
    class Meta:
        model = Subscription
        fields = ['email']
