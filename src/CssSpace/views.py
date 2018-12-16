from django.shortcuts import render


def css_space_index(request):
    return render(request, 'demos/demo_01.html')

def css_demo_01(request):
    return render(request, 'demos/demo_01.html')

def css_demo_02(request):
    return render(request, 'demos/demo_02.html')
