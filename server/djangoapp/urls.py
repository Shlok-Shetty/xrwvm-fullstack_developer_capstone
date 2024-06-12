# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout_request'),
    path('register', views.registration, name='registration'),
    

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
