from django.contrib import admin
from django.urls import path, include

from dummy.views import DummyView

api_url_patterns = [
    path('dummies', DummyView.as_view(), name='dummies'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
]
