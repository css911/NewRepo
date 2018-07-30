"""library URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from lib import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/',views.ren1),
    url(r'^login/',views.ren),
    url(r'^enterregister',views.enterregister),
    url(r'^check',views.check),
    url(r'^retrivelist',views.retrivelist),
    url(r'^logout',views.logout),
    url(r'^book_details',views.books),
    url(r'^profile',views.profile),
    url(r'^search',views.search),
    url(r'^issue_a_book',views.issuebook),
    url(r'^book_a_book',views.book_a_book),  #used to book a book from the student
    url(r'^booked',views.issuedBook),        #used to see the issued book
    url(r'^issueit',views.issueit)           #used to mark a book as issued
]
