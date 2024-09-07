from django.urls import path
from .views import homepage,registration,product_detail,signin,log_out

urlpatterns = [
    path('',homepage,name='home'),
    path('product/<int:id>',product_detail,name='detail'),
    path('reg/',registration,name='reg'),
    path('login/',signin,name='login'),
    path('logout/',log_out,name='logout'),
    
]
