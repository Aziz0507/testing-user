from django.contrib import admin
from django.urls import path
from test_user.views import main_page, login_views, register, logut, test_them

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name = 'main'),
    path('login/', login_views.as_view(), name = 'login'),
    path('register/', register, name = 'register'),
    path('logut/', logut, name = 'logut'),
    path('test_them/<int:pk>', test_them, name = 'test_them')
]
