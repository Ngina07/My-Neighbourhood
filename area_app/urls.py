from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^authorities',views.authorities, name='authorities'),
    url(r'^businesses',views.businesses, name='businesses'),
    url(r'^health-services',views.health, name='health'),
    url(r'^notifications',views.notification, name='notifications'),
    url(r'^new/business$',views.new_business, name='new-business'),
    url(r'^new/notification$',views.new_notification, name='new-notification'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url(r'^search/',views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)