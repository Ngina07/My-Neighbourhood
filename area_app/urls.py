from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^authorities',views.authorities, name='authorities'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)