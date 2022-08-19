from django.urls import URLPattern, path


urlpatterns = [
    '''
    path('register/', views.registration, name='register'),
    path('login/', views.log_in, name='login'),
    '''
]