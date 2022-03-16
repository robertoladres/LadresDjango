# from django.contrib import admin
from django.urls import path
from myapp1 import views
from . import views

app_name='myapp1'
 

urlpatterns = [

    path('index',views.MyIndexView.as_view(),name="my_index_view"),
    path('display',views.MyDisplayView.as_view(),name="my_display_view"),
    path('index Customer',views.MyIndexViewCustomer.as_view(),name="my_index_view_Customer"),
    path('dashboard',views.MyDashboardView.as_view(),name="my_dashboard_view"),
    path('dashboardViewBooks',views.MyDashboardViewBooks.as_view(),name="my_dashboard_view_books"),
    path('dashboardCustomer',views.MyDashboardCustomerView.as_view(),name="my_dashboard_customer_view"),
    path('dashboardmain',views.MyDashboardMainView.as_view(),name="my_dashboard_main_view"),
    path('dashboardSales', views.MyDashboardSalesView.as_view(), name="my_dashboard_sales_view"),
    path('dashboardOrder', views.MyDashboardOrderView.as_view(), name="my_dashboard_order_view"),
    path('dashboardOrder Customer View', views.MyDashboardOrderCustomerView.as_view(), name="my_dashboard_orderCustomer_view"),
    path('dashboardAdmin', views.MyDashboardAdminView.as_view(), name="my_dashboard_admin_view"),
    path('signinBoard',views.MySigninView.as_view(),name="my_signin_main_view"),
    path('landing',views.MyLandingView.as_view(),name="my_landing_view"),
    path('registration',views.MyBookRegistrationView.as_view(),name="my_bookregistration_view"),
    path('registrationAdmin',views.MyAdminRegistrationView.as_view(),name="my_adminregistration_view"),
    path('registrationCustomer',views.MyCustomerRegistrationView.as_view(),name="my_customer_registration_view"),
    path('registrationPracticalBook',views.MyRegistrationPracticalBookView.as_view(),name="my_book_registrationPracticalBook_view"),
    path('registrationPracticalAuthor',views.MyRegistrationPracticalAuthorView.as_view(),name="my_book_registrationPracticalAuthor_view"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.login,name="login"),
    path('login Admin',views.loginAdmin,name="loginAdmin"),
    path('register',views.register,name="register"),
   
] 