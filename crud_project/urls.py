# crud_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summoners/', include('items.urls')),  # 앱의 URL 패턴 포함
    path('', include('items.urls')),  # 루트 URL을 앱의 URL 패턴으로 연결
]
