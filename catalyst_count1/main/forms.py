from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class QueryForm(forms.Form):
   
    name = forms.CharField(max_length=255, required=False)  # Allow blank
    domain = forms.CharField(max_length=255, required=False)  # Allow blank
    year_founded = forms.IntegerField(required=False)  # Allow blank
    industry = forms.CharField(max_length=255, required=False)  # Allow blank
    country = forms.CharField(max_length=255, required=False)  # Allow blank
    

