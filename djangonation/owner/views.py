
from email import message
import email
from multiprocessing import context
from tkinter.messagebox import Message
import MySQLdb
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from owner.models import Owner, Stock, Order
from owner.models import Employee
from owner.models import Customer
from operator import itemgetter
from django.contrib.auth.decorators import login_required
# import mysql.connector
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def owner_signup(request):
    return render(request,'owner_signup.html')

def employee_signup(request):
    return render(request,'employee_signup.html')

def customer_signup(request):
    return render(request,'customer_signup.html')


def admin_login(request):
    con = MySQLdb.connect(host='localhost', user='root', password='bhushan12',database='django_demo1')
    cursor=con.cursor()
    con2 = MySQLdb.connect(host='localhost', user='root', password='bhushan12',database='django_demo1')
    cursor2=con2.cursor()
    sqlcommand1="select owner_email from owner_owner"
    sqlcommand2="select owner_password from owner_owner"
    cursor.execute(sqlcommand1)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0),p))
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        i=0
        k=len(res)
        while i<k:
            if res[i]==email and res2[i]==password:
                    return render(request, 'owner_homepage.html',{'email':email})
                    break
            i+=1
        else:
            # message.info(request,"check email or password")
            return render(request, 'admin_login.html')
    return render(request, 'admin_login.html')    
        

def employee_login(request):
    con = MySQLdb.connect(host='localhost', user='root', password='bhushan12',database='django_demo1')
    cursor=con.cursor()
    con2 = MySQLdb.connect(host='localhost', user='root', password='bhushan12',database='django_demo1')
    cursor2=con2.cursor()
    sqlcommand1="select Emp_email from owner_employee"
    sqlcommand2="select Emp_password from owner_employee"
    cursor.execute(sqlcommand1)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0),p))
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        i=0
        k=len(res)
        while i<k:
            if res[i]==email and res2[i]==password:
                    return render(request, 'employee_homepage.html',{'email':email})
                    break
            i+=1
        else:
            # message.info(request,"check email or password")
            return render(request, 'employee_login.html')
    return render(request, 'employee_login.html')    

def customer_login(request):
    con = MySQLdb.connect(host='localhost', user='root', password='bhushan12',database='django_demo1')
    cursor=con.cursor()
    con2 = MySQLdb.connect(host='localhost', user='root', password='bhushan12',database='django_demo1')
    cursor2=con2.cursor()
    sqlcommand1="select Cust_email from owner_customer"
    sqlcommand2="select Cust_password from owner_customer"
    cursor.execute(sqlcommand1)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0),p))
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        i=0
        k=len(res)
        while i<k:
            if res[i]==email and res2[i]==password:
                    return render(request, 'customer_homepage.html',{'email':email})
                    break
            i+=1
        else:
            # message.info(request,"check email or password")
            return render(request, 'customer_login.html')
    return render(request, 'customer_login.html') 




def owner_homepage(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        password=request.POST.get('password')
        inventory_name=request.POST.get('inventory_name')
        city=request.POST.get('city')
        oh=Owner(owner_fname=fname,owner_lname=lname,owner_sex=gender,owner_email=email,owner_password=password,owner_inventory_name=inventory_name,owner_inventory_city=city)
        oh.save()
    return render(request,'admin_login.html')

def employee_homepage(request):
    if request.method == "POST":
        empid=request.POST.get('empid')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        password=request.POST.get('password')
        owner_email=request.POST.get('owner_email')
        eh=Employee(Emp_id=empid,Emp_fname=fname,Emp_lname=lname,Emp_sex=gender,Emp_email=email,Emp_password=password,owner_id=owner_email)
        eh.save()
    return render(request,'employee_login.html')

def customer_homepage(request):
    if request.method == "POST":
        custid=request.POST.get('custid')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        password=request.POST.get('password')
        owner_email=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        ch=Customer(Cust_id=custid,Cust_fname=fname,Cust_lname=lname,Cust_sex=gender,Cust_email=email,Cust_password=password,owner_id=owner_email,employee_id=empid)
        ch.save()
    return render(request,'customer_login.html')

# email=admin_login()
def owner_employee_check(request):
    items = Employee.objects.raw('select * from owner_employee ')
    context={
        'items':items,
    }
    return render(request, 'owner_employee_check.html',context)

def owner_employee_add(request):
    if request.method == "POST":
        id=request.POST.get('empid')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        password=request.POST.get('password')
        owner_email=request.POST.get('owner_email')
        eh=Employee(Emp_id=id,Emp_fname=fname,Emp_lname=lname,Emp_sex=gender,Emp_email=email,Emp_password=password,owner_id=owner_email)
        eh.save()
    return render(request, 'owner_employee_add.html')

def owner_customer_check(request):
    items = Customer.objects.raw('select * from owner_customer')
    context={
        'items':items,
    }
    return render(request,'owner_customer_check.html',context)

def owner_customer_add(request):
    if request.method == "POST":
        custid=request.POST.get('custid')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        password=request.POST.get('password')
        owner_email=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        ch=Customer(Cust_id=custid,Cust_fname=fname,Cust_lname=lname,Cust_sex=gender,Cust_email=email,Cust_password=password,owner_id=owner_email,employee_id=empid)
        ch.save()
    return render(request,'owner_customer_add.html')

def owner_stocks_check(request):
    items = Stock.objects.raw('select * from owner_stock')
    context={
        'items':items,
    }
    return render(request,'owner_stocks_check.html',context)

def owner_stocks_add(request):
    if request.method == "POST":
        stockid=request.POST.get('id')
        stockname=request.POST.get('stock_name')
        quantity=request.POST.get('quantity')
        description=request.POST.get('description')
        owneremail=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        custid=request.POST.get('custid')
        sh=Stock(Stock_id=stockid,Stock_name=stockname,Stock_quantity=quantity,Stock_description=description,owner_id=owneremail,employee_id=empid,customer_id=custid)
        sh.save()
    return render(request,'owner_stocks_add.html')

def owner_orders_check(request):
    items = Order.objects.raw('select * from owner_order')
    context={
        'items':items,
    }
    return render(request,'owner_orders_check.html',context)

def owner_orders_add(request):
    if request.method == "POST":
        orderid=request.POST.get('id')
        quantity=request.POST.get('quantity')
        ordername=request.POST.get('stock_name')
        description=request.POST.get('description')
        owneremail=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        custid=request.POST.get('custid')
        sh=Stock(Order_id=orderid,Order_quantity=quantity,Order_name=ordername,Order_description=description,owner_id=owneremail,employee_id=empid,customer_id=custid)
        sh.save()
    return render(request, 'owner_orders_add.html')

def employee_customer_check(request):
    items = Customer.objects.raw('select * from owner_customer')
    context={
        'items':items,
    }
    return render(request, 'employee_customer_check.html',context)

def employee_customer_add(request):
    if request.method == "POST":
        custid=request.POST.get('custid')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        password=request.POST.get('password')
        owner_email=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        ch=Customer(Cust_id=custid,Cust_fname=fname,Cust_lname=lname,Cust_sex=gender,Cust_email=email,Cust_password=password,owner_id=owner_email,employee_id=empid)
        ch.save()
    return render(request,'employee_customer_add.html')

def employee_stocks_check(request):
    items = Stock.objects.raw('select * from owner_stock')
    context={
        'items':items,
    }
    return render(request,'employee_stocks_check.html',context)

def employee_stocks_add(request):
    if request.method == "POST":
        stockid=request.POST.get('id')
        stockname=request.POST.get('stock_name')
        quantity=request.POST.get('quantity')
        description=request.POST.get('description')
        owneremail=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        custid=request.POST.get('custid')
        sh=Stock(Stock_id=stockid,Stock_name=stockname,Stock_quantity=quantity,Stock_description=description,owner_id=owneremail,employee_id=empid,customer_id=custid)
        sh.save()
    return render(request, 'employee_stocks_add.html')

def employee_orders_check(request):
    items = Order.objects.raw('select * from owner_order')
    context={
        'items':items,
    }
    return render(request,'employee_orders_check.html',context)

def employee_orders_add(request):
    if request.method == "POST":
        orderid=request.POST.get('id')
        quantity=request.POST.get('quantity')
        ordername=request.POST.get('stock_name')
        description=request.POST.get('description')
        owneremail=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        custid=request.POST.get('custid')
        sh=Order(Order_id=orderid,Order_quantity=quantity,Order_name=ordername,Order_description=description,owner_id=owneremail,employee_id=empid,customer_id=custid)
        sh.save()
    return render(request,'employee_orders_add.html')

def customer_stocks_check(request):
    items = Stock.objects.raw('select * from owner_stock')
    context={
        'items':items,
    }
    return render(request,'customer_stocks_check.html',context)

def customer_orders_check(request):
    items = Order.objects.raw('select * from owner_order')
    context={
        'items':items,
    }
    return render(request, 'customer_orders_check.html',context)

def customer_orders_add(request):
    if request.method == "POST":
        orderid=request.POST.get('id')
        quantity=request.POST.get('quantity')
        ordername=request.POST.get('stock_name')
        description=request.POST.get('description')
        owneremail=request.POST.get('owner_email')
        empid=request.POST.get('empid')
        custid=request.POST.get('custid')
        sh=Order(Order_id=orderid,Order_quantity=quantity,Order_name=ordername,Order_description=description,owner_id=owneremail,employee_id=empid,customer_id=custid)
        sh.save()
    return render(request,'customer_orders_add.html')