from django.contrib import admin
from django.urls import include, path
import quiz.views

urlpatterns = [
    path('quiz/', include('quiz.urls')),
    path('admin/', admin.site.urls),
    path('', quiz.views.IndexView)
]