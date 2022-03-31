"""
import settings
Will import settings(.py) module of your Django project (if you are writing this code from the "root" package of your application, of course)

 from django.conf import settings
 Will import settings object from django.conf package (Django's provided files). This is important, because

 [..] note that your code should not import from either global_settings or your own settings file. django.conf.settings abstracts the concepts of default settings and site-specific settings; it presents a single interface. It also decouples the code that uses settings from the location of your settings."""

from django.urls import path
from testapp import views
from django.conf import settings  # settings is a object
from django.conf.urls.static import static

urlpatterns = [

    # XXX registration
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('profile/', views.profile, name="profile"),


    # XXX project urls
    path('base/', views.base, name='base'),
    path('upload/', views.upload, name='upload'),
    path('book_list/', views.book_list, name='book_list'),
    path('delete/<int:id>', views.delete, name='delete'),

]


# just for devlopement purpose when settings is in DEBUG
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                       document_root=settings.MEDIA_ROOT)
