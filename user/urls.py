from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/',views.change_password, name='change_password'),
    path('comments/',views.comments, name='comments'),
    path('deletecomment/<int:id>/', views.deletecomment, name='deletecomment'),
    path('myblogs/',views.myblogs, name='myblogs'),
    path('addblog/',views.addblog, name='addblog'),
    path('editblog/<int:id>/', views.editblog, name='editblog'),
    path('deleteblog/<int:id>/', views.deleteblog, name='deleteblog'),
    #path('addcomment/<int:id>',views.addcomment,name='addcomment')

    # ex: /blog/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]