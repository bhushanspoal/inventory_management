from django.contrib import admin


from owner.models import Owner,Employee,Customer,Stock,Order
# Register your models here.
admin.site.register(Owner)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Stock)
admin.site.register(Order)