from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'treatment_type', 'preferred_location', 'message']

    def __init__(self, *args, **kwargs):
        super(InquiryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Full Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address', 'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone Number (Optional)', 'class': 'form-control'})
        self.fields['treatment_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['preferred_location'].widget.attrs.update({'placeholder': 'Preferred Treatment Location', 'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Additional Information', 'class': 'form-control'})
