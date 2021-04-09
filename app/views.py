from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  laptops = Product.objects.filter(category='L')
  return render(request,'app/home.html',
  {
      'topwears' :topwears, 'bottomwears' :bottomwears, 'mobiles' :mobiles, 'laptops' :laptops})

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render (request, 'app/productdetail.html',{'product' :product})

def add_to_cart(request):
  user=request.user
  product_id = request.GET.get('prod_id')
  product = Product.objects.get(id=product_id)
  Cart(user=user, product=product).save()
  return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

#def profile(request):
 #return render(request, 'app/profile.html')

def address(request):
  add = Customer.objects.filter(user=request.user)
  return render(request, 'app/address.html',{'add':add , 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

#def change_password(request):
 #return render(request, 'app/changepassword.html')

def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category='M')
 elif data == 'Redmi' or data == 'Samsung' or data == 'Apple' :
  mobiles = Product.objects.filter(category='M').filter(brand=data)
 return render(request, "app/mobile.html",{'mobiles':mobiles})

def laptop(request, data=None):
 if data == None:
  laptops = Product.objects.filter(category='L')
 elif data == 'lenovo' or data == 'Dell':
  laptops = Product.objects.filter(category='L').filter(brand=data)
 return render(request, "app/laptop.html",{'laptops':laptops})

def topwear(request, data=None):
 if data == None:
  topwears = Product.objects.filter(category='TW')
 elif data == 'Lee' or data == 'Spykar':
  topwears = Product.objects.filter(category='TW').filter(brand=data)
 return render(request, "app/topwear.html",{'topwears':topwears})

def bottomwear(request, data=None):
 if data == None:
  bottomwears = Product.objects.filter(category='BW')
 elif data == 'Pepe' or data == 'Spykar':
  bottomwears = Product.objects.filter(category='BW').filter(brand=data)
 return render(request, "app/bottomwear.html",{'bottomwears':bottomwears})
 
def checkout(request):
 return render(request, 'app/checkout.html')


class CustomerRegistrationView(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request,'app/Customerregistration.html',{'form':form})
  def post(self,request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      messages.success(request,'Congratulations !!!,Registration successful')
      form.save()
    return render(request,'app/Customerregistration.html',{'form':form})

class ProfileView(View):
  def get(self, request):
    form = CustomerProfileForm()
    return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

  def post(self, request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      usr = request.user
      name = form.cleaned_data['name']
      locality = form.cleaned_data['locality']
      city = form.cleaned_data['city']
      state = form.cleaned_data['state']
      zipcode = form.cleaned_data['zipcode']
      reg = Customer(user=usr, name=name, locality=locality,city=city,state=state,zipcode=zipcode)
      reg.save()
      messages.success(request, 'Congratulations!!!! Profile updated Successfully')
      return render(request, 'app/profile.html', {'form':form,'active':'btn-primary'})



