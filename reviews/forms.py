from django import forms


class ReviewForm(forms.ModelForm):
    user_name = forms.CharField()
    
    