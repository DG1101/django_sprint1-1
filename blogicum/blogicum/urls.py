from django.contrib import admin
from django.urls import include, path

app_name = 'blogicum'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='blog'),
    path('pages/', include('pages.urls'), name='pages'),
]
