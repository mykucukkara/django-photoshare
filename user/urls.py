from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    #path('addcomment/<int:id>',views.addcomment,name='addcomment')
    # ex: /blog/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]