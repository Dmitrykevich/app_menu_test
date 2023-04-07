from django.shortcuts import render


def index(request):
    context = {'request': request}
    return render(request, 'app_tree_menu_template_tag/index.html', context)


def child_2_1(request):
    return render(request, 'app_tree_menu_template_tag/child_2_1.html')
