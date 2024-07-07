from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload'),
    path('query/', views.query_builder, name='query'),
    path('users/', views.user_list, name='users'),
    # path('accounts/', include('allauth.urls')),  # Ensure this is included
    # path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),

]
