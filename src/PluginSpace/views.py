from django.shortcuts import render

# Create your views here.
def plugin_space_index(request):
    return render(request, 'index.html')
