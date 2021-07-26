from django.urls import path
from simple import views
from django.conf.urls import url, include






app_name = "simple"   


urlpatterns = [

    
   
        path('accounts/register/',views.register, name="register"),
        path('accounts/login/', views.authlogin,name="login"),
        path('accounts/logout/', views.authlogout,name="logout"),
        path('account/', include('django.contrib.auth.urls')),

    path('',views.index, name="index"),
    path('Aboutus/',views.Aboutus, name="Aboutus"),
    path('access/',views.access, name="access"),
    path('CCTV/',views.CCTV, name="CCTV"),
    path('contacts/',views.contacts, name="contacts"),
    path('Hardware/',views.Hardware, name="Hardware"),
    path('networking/',views.networking, name="networking"),
    path('outsourcing/',views.outsourcing, name="outsourcing"),
    path('support/',views.support, name="support"),
    path('telecom/',views.telecom, name="telecom"),
    path('post_detail/',views.post_detail, name="post_detail"),


    # path('accounts/password_change/', views.password_change, name='password_change'),
    # path('accounts/password_change/done/' , views.password_change_done,name='password_change_done'),
    # path('accounts/password_reset/', views.password_reset, name='password_reset'),
    # path('accounts/password_reset/done/',views.password_reset_done,name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    # 'django.contrib.auth.views.password_reset_confirm',
    # name='password_reset_confirm'),
    # path('accounts/password_reset_complete/done/', views.password_reset_complete, name='password_reset_complete'),
    ]
