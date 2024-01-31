from django.urls import path

from shoppingapp import views, adminviews, shopkeeperviews, userviews, face

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_register/', views.user_registery, name='user_register'),

    path('admin_home/', adminviews.admin_home, name='admin_home'),
    path('shopkeeper_register/', adminviews.shopkeeper_registery, name='shopkeeper_register'),
    path('shopkeeper_views/', adminviews.view_shopkeeper, name='shopkeeper_views'),
    path('shopkeeper_update/<int:id>/', adminviews.update_shopkeeper, name='shopkeeper_update'),
    path('shopkeeper_delete/<int:id>/', adminviews.delete_shopkeeper, name='shopkeeper_delete'),
    path('user_views/', adminviews.view_user, name='user_views'),
    path('delete_user/<int:id>/', adminviews.delete_user, name='delete_user'),
    path('appointment_admin/', adminviews.appointment_admin, name='appointment_admin'),
    path('accept_appointment/<int:id>/', adminviews.approve_appointment, name='accept_appointment'),
    path('reject_appointment/<int:id>/', adminviews.reject_appointment, name='reject_appointment'),

    path('shopkeeper_home/', shopkeeperviews.shopkeeper_home, name='shopkeeper_home'),
    path('schedule_add/', shopkeeperviews.schedule_add, name='schedule_add'),
    path('schedule_views/', shopkeeperviews.schedule_view, name='schedule_views'),
    path('schedule_update/<int:id>/', shopkeeperviews.schedule_update, name='schedule_update'),
    path('schedule_delete/<int:id>/', shopkeeperviews.schedule_delete, name='schedule_delete'),
    path('appointment_section/',shopkeeperviews.appointment_section,name='appointment_section'),

    path('user_home/', userviews.user_home, name='user_home'),
    path('schedule/', userviews.schedule_user, name='schedule'),
    path('appointment_take/<int:id>/', userviews.take_appointment, name='appointment_take'),
    path('appointment_view/', userviews.view_appointment, name='appointment_view'),
    path('shopenter/', userviews.shopenter, name='shopenter'),
    path('shopview/', userviews.shop_view, name='shopview'),

    path('mask_detect/', face.mask_detect, name='mask_detect'),

]
