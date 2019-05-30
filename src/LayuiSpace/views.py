from django.shortcuts import render


def layui_space_index(request):
    return render(request, 'layui_space/index.html')
