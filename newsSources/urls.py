from django.urls import re_path
from .views import News
urlpatterns = [
    re_path('sources/', News.as_view(), name='get_sources' )
]