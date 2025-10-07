from django.urls import path
from blog import views

urlpatterns = [
    path("",views.index, name='blog'),
    path("post/",views.show_post, name='post'),
    path('newpost/', views.add_post, name="addposts"),
    path('post/<int:id>/', views.find_post, name= "find_post"),
    
    path('updatepost/<int:id>', views.update_post, name= 'updatepost'),
    path('deletepost/<int:id>', views.delete_post, name= 'deletepost')
]