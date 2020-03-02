from django.urls import include, path
from .views import classroom




urlpatterns = [
    path('', classroom.home, name='home'),
    path('post/new/', classroom.post_new, name='post_new'),
 
       
   
        

        
#<int:pk>/

    ]
