"""offlineWallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path,include
#from accounts.views import profile,login1,transaction
#from .views import profile
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "MunchyBank V4 | MunchyTeam"

urlpatterns = [
  
   
    

   # path('test/', views.transaction, name='test1'),
    
    path('accounts/', include('allauth.urls')),
    path('', home1),
    path('admin/', admintrap)
]
if settings.DEBUG==True:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
   #urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
   #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
