from COMPRA_VENTA.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('crear/', all_productos, name='crear'),
    path('signupAdmin/', signupAdmin, name='signupAdmin'),
    path('homeuser/', homeuser, name='homeuser'),
    path('logout/', signout, name='logout'),
    path('signinAdmin/', signinAdmin, name='signinAdmin'),
    path('signinUser/', signinUser, name='signinUser' ),
    path('signupUser/', signupUser, name='signupUser' ),
    path('homeuserU/', homeuserU, name='homeuserU'),
    path('favoritos/', favoritos, name='favoritos')
]