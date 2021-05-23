

from django.contrib import admin
from django.urls import path , include
from stud.views import  CustomAuthToken


urlpatterns = [
    
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path('', include ('stud.urls')),
]
