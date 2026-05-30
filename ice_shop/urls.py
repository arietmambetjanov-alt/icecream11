from tempfile import template
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.product_view, name='index'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='ice_shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
