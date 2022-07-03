from cgi import print_exception
from django.shortcuts import render,redirect ,get_object_or_404
from .models import drug
from django.contrib.auth import authenticate, login
from .forms import loginForm

# Create your views here.
def index(request):
    drugs = drug.objects.all()
    return render(request , "homepage.html",{"drugs":drugs})

def addDrug(request):

    if request.method == "GET":
        return redirect("/homepage")
    else:
       
        Name = request.POST.get("name")
        Price = request.POST.get("price")
        Stock = request.POST.get("stock")
        Quantity = request.POST.get("quantity")
        newDrug = drug(name = Name , price = Price , stock = Stock , quantity = Quantity)

        newDrug.save()
        return redirect("/homepage")

def delete(request , id):
    newDrug = get_object_or_404(drug,id = id)

    newDrug.delete()
    return redirect("/homepage")

def login_view(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username , password = password)
        login(request,user)
        return redirect('/homepage')
    return render(request, 'form.html', {'form':form})