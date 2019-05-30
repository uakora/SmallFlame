from django.shortcuts import render


def layui_space_index(request):
    return render(request, 'layui_space/index.html')


def layui_demo_idx(reques, demo_idx=1):
    html = 'layui_space/demo_%d.html' % (demo_idx)
    return render(reques, html, {"demo_idx": demo_idx})
