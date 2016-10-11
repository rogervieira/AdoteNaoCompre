"""AdoteNaoCompre_MAIN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include, handler404, handler403
from django.contrib import admin


urlpatterns = [
    url(r'^', include('AdoteNaoCompreSITE.urls')),
    url(r'^admin/', admin.site.urls),
]

handler403 = 'AdoteNaoCompreSITE.controllers.generic_controller.unauthorizedHandler'
handler404 = 'AdoteNaoCompreSITE.controllers.generic_controller.pageNotFoundHandler'