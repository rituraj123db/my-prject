from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('insertstudent',views.insertstudent,name='insertstudent'),
path('viewsall',views.viewsall,name='viewsall'),
path('viewsall1',views.viewsall1,name='viewsall1'),
path('editdata',views.editdata, name='editdata'),
path('updatedata',views.updatedata,name='updatedata'),
path('deletedata',views.deletedata,name='deletedata'),
path('checkrno',views.checkrno,name='checkrno'),
path('logout',views.logout,name='logout')
]