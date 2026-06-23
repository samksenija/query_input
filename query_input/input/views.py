from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InputForm
from .utils import write_queries_to_json_file

# Create your views here.
def input(request):
    input_form(request)
    
    return render(request, "inputs.html")

def input_form(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            
            file_name = "queries.json"
            queries = {}
            
            create_query_object = {
                form.cleaned_data['identifier']: {
                    "query": form.cleaned_data['query'],
                    "layer_tags": form.cleaned_data['layer_tags'],
                    "changes_applied": form.cleaned_data['changes_applied'],
                    "notes": form.cleaned_data['notes']
                }
            }
            
            write_queries_to_json_file(queries, file_name, create_query_object)
            
            return HttpResponseRedirect("inputs.html")
    else:
        form = InputForm()

    return render(request, "inputs.html", {"form": form})
