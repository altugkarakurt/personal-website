from django.contrib import admin
from django.urls import path, include

from .views import about


urlpatterns = [
    path('', about, name="about_me"),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
