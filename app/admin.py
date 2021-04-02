from django.contrib import admin
from app.models import (
    Customer ,
    Product,
    Cart,
    OrderPlaced
)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderPlaced)

#@admin.register(Customer)
list_display = ['id','user','name','locality','city','zipcode','state']

#@admin.register(Product)
#class ProductModelAdmin(admin.ModelAdmin):
list_display = ['id','title','selling_price','discounted_price','description','brand','category','product_image']

#@admin.register(Cart)
#class OrderPlacedModelAdmin(admin.ModelAdmin):
list_display = ['id','user','customer','product','quantity','ordered_date','status']



# Register your models here.
