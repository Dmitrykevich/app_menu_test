from django.urls import path

from .views import index, child_2_1


app_name = 'tree_menu'

urlpatterns = [
    path('', index, name='index'),
    path('child_2_1/', child_2_1, name='child_2_1')
]
