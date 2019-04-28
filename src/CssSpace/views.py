from django.shortcuts import render


def css_space_index(request):
    return render(request, 'demos/demo_1.html')

def css_demo_01(request):
    return render(request, 'demos/demo_1.html')

def css_demo_02(request):
    return render(request, 'demos/demo_02.html')

def css_demo_03(request):
    return render(request, 'demos/demo_03.html')

def css_demo_04(request):
    return render(request, 'demos/demo_04.html')
