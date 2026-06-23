from django.shortcuts import render
from .forms import InputForm

from django.http import HttpResponseRedirect

import json, os

# Create your views here.
def input(request):
    input_form(request)
    
    return render(request, "inputs.html")

def input_form(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            
            file_name = "queries.json"
            queries = []
            
            if os.path.isfile(file_name):
                with open(file_name) as f:
                    queries = json.load(f) 
                    print(queries)   
            
            create_object = {
                form.cleaned_data['identifier']: {
                    "query": form.cleaned_data['query'],
                    "layer_tags": form.cleaned_data['layer_tags'],
                    "changes_applied": form.cleaned_data['changes_applied'],
                    "notes": form.cleaned_data['notes']
                }
            }
            
            queries.update(create_object)
            
            with open(file_name, "w") as f:
                json.dump(queries, f, indent=4)
            
            return HttpResponseRedirect("inputs.html")
    else:
        form = InputForm()

    return render(request, "inputs.html", {"form": form})
