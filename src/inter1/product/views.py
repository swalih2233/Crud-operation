from django.shortcuts import render,reverse
from django.shortcuts import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from product.models import Product,Author

from django.contrib.auth.models import User

from product.form import ProductForm

@login_required(login_url='/login')
def index(request):
        products = Product.objects.all()

        context ={
            "title":"ECOMMERCE",
            "products":products
        }


        return render(request, "index.html", context=context)



def login(request):
     if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")


        if username and password:
                        user = authenticate(request, username=username, password=password)
                        if user is not None:
                            auth_login(request, user)

                            return HttpResponseRedirect(reverse("product:index"))
                        
                        else:
                            context ={
                                "title":"Login",
                                "error":True,
                                "message":"invalid credentials"
                            }

                        return render(request, "login.html", context=context)
            
        else:
            context ={
                "title":"Login",
            }
            return render(request, "login.html", context=context)
        
     else:
         context ={
                        "title":"Login",
                    }
         return render(request, "login.html", context=context)
         
        
  

def logout(request):
  
    auth_logout(request)

    return HttpResponseRedirect(reverse("product:login"))

def register(request):
    if request.method == 'POST':
       username = request.POST.get("username")
       first_name = request.POST.get("first_name")
       last_name = request.POST.get("last_name")
       password = request.POST.get("password")

       user = User.objects.create_user(
           username = username,
           first_name = first_name,
           last_name = last_name,
           password = password

       )

       user.save()

       author = Author.objects.create(
           user=user
       )

       author.save()

       return HttpResponseRedirect(reverse("product:login"))
    
    else:
       context={
           "title":"Create account",
       }
    
       return render(request, "register.html", context=context)
    
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,)
        if form.is_valid():
            instance =form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("product:index"))
        
        else:
            pass


    else:
        form = ProductForm()
        context =  {
            "title": "product | index",
            "form":form
        }
        return render(request,"add_product.html", context=context)
    
def product_edit(request, id):
    instance = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse("product:index"))
        
        else:
            pass

    else:
        form = ProductForm(instance=instance)
        context={
            "title":" product | index",
            "form":form
        }

        return render(request, "add_product.html", context=context)
    
def product_del(request, id):
   products =Product.objects.get(id=id)
   products.delete()

   return HttpResponseRedirect(reverse("product:index"))
