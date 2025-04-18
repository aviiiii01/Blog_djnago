from django.urls import path
from . import views
from User import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('register/',user_views.register,name='register'),
    path('login/',user_views.loginn,name='login'),#so it Automatically pass a login form "form" to the template given peeche (AuthenticationForm)
    # auth_views.LoginView.as_view(template_name="users/login.html")
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/',user_views.profile,name='profile')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    