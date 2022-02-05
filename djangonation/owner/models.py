
from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Owner(models.Model):
    owner_fname=models.CharField(max_length=30,default='bhushan')
    owner_lname=models.CharField(max_length=30,default='poal')
    owner_sex=models.CharField(max_length=10,default='male')
    owner_email=models.EmailField(max_length=30, primary_key=True)
    owner_password=models.CharField(max_length=30,default='male')
    owner_inventory_name=models.CharField(max_length=30,default='inventory')
    owner_inventory_city=models.CharField(max_length=30,default='bangalore')

class Employee(models.Model):
    Emp_id=models.IntegerField(primary_key=True)
    Emp_fname=models.CharField(max_length=30)
    Emp_lname=models.CharField(max_length=30)
    Emp_sex=models.CharField(max_length=10)
    Emp_email=models.EmailField(max_length=30)
    Emp_password=models.CharField(max_length=30)
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)

class Customer(models.Model):
    Cust_id=models.IntegerField(primary_key=True)
    Cust_fname=models.CharField(max_length=30)
    Cust_lname=models.CharField(max_length=30)
    Cust_sex=models.CharField(max_length=10)
    Cust_email=models.EmailField(max_length=30)
    Cust_password=models.CharField(max_length=30)
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)

class Order(models.Model):
    Order_id=models.IntegerField(primary_key=True)
    Order_quantity=models.IntegerField()
    Order_name=models.CharField(max_length=30)
    Order_description=models.CharField(max_length=150)
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)

class Stock(models.Model):
    Stock_id=models.IntegerField(primary_key=True)
    Stock_name=models.CharField(max_length=30)
    Stock_quantity=models.CharField(max_length=30)
    Stock_description=models.CharField(max_length=150)
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)