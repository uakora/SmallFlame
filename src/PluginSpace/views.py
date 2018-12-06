from django.shortcuts import render

# Create your views here.
def plugin_space_index(request):
    return render(request, 'index.html')

def datatable_learn01(request):
    return render(request, 'datatables/learn01.html')

def datatable_learn02(request):
    return render(request, 'datatables/learn02.html')

def datatable_learn03(request):
    return render(request, 'datatables/learn03.html')