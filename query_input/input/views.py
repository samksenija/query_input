from django.shortcuts import render
from .forms import InputForm

from django.http import HttpResponseRedirect

# Create your views here.
def input(request):
    input_form(request)
    
    return render(request, "inputs.html")

def input_form(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            # Review the cleaned data; TODO to be removed
            print(form.cleaned_data['query'])
            print(form.cleaned_data['layer_tags'])
            print(form.cleaned_data['changes_applied'])
            print(form.cleaned_data['notes'])
            
            return HttpResponseRedirect("inputs.html")
    else:
        form = InputForm()

    return render(request, "inputs.html", {"form": form})
