from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('owner_signup',views.owner_signup, name="owner_signup"),
    path('employee_signup',views.employee_signup, name="employee_signup"),
    path('customer_signup',views.customer_signup, name="customer_signup"),
    path('admin_login',views.admin_login, name="admin_login"),
    path('employee_login',views.employee_login, name="employee_login"),
    path('customer_login',views.customer_login, name="customer_login"),
    path('owner_homepage',views.owner_homepage, name="owner_homepage"),
    path('employee_homepage',views.employee_homepage, name="employee_homepage"),
    path('customer_homepage',views.customer_homepage, name="customer_homepage"),
    path('owner_employee_check',views.owner_employee_check, name="owner_employee_check"),
    path('owner_employee_add',views.owner_employee_add, name="owner_employee_add"),
    path('owner_customer_check',views.owner_customer_check, name="owner_customer_check"),
    path('owner_customer_add',views.owner_customer_add, name="owner_customer_add"),
    path('owner_stocks_check',views.owner_stocks_check, name="owner_stocks_check"),
    path('owner_stocks_add',views.owner_stocks_add, name="owner_stocks_add"),
    path('owner_orders_check',views.owner_orders_check, name="owner_orders_check"),
    path('owner_orders_add',views.owner_orders_add, name="owner_orders_add"),
    path('employee_customer_check',views.employee_customer_check, name="employee_customer_check"),
    path('employee_customer_add',views.employee_customer_add, name="employee_customer_add"),
    path('employee_stocks_check',views.employee_stocks_check, name="employee_stocks_check"),
    path('employee_stocks_add',views.employee_stocks_add, name="employee_stocks_add"),
    path('employee_orders_check',views.employee_orders_check, name="employee_orders_check"),
    path('employee_orders_add',views.employee_orders_add, name="employee_orders_add"),
    path('customer_stocks_check',views.customer_stocks_check,name="customer_stocks_check"),
    path('customer_orders_check',views.customer_orders_check,name="customer_orders_check"),
    path('customer_orders_add',views.customer_orders_add,name="customer_orders_add"),
]