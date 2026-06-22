from django import forms

class InputForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea, required=True)
    layer_tags = forms.CharField(max_length=15, required=True)
    changes_applied = forms.CharField(max_length=250, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)