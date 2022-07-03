from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from .models import Drug
from .forms import DrugForm
#from django.contrib.auth.decorators import login_required

# Create your views here.
def drugs(request):
    keyword = request.GET.get("keyword")
    if keyword:
        drugs = Drug.objects.filter(title__contains=keyword)
        return render(request,"drugs.html",{"drugs": drugs})
    drugs = Drug.objects.all()
    
    return render(request,"drugs.html",{"drugs":drugs})

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

#@login_required(login_url = "user:login")
def dashboard(request):
    drugs = Drug.objects.filter()
    context = {
        "drugs":drugs
    }
    return render(request,"dashboard.html",context)


def addDrug(request):
    form = DrugForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        drug = form.save(commit=False)
        #drug.author = request.user
        drug.save()

        messages.success(request,"The drug has been successfully created.")
        return redirect("drug:dashboard")
    return render(request,"adddrug.html",{"form":form})
def detail(request,id):
    #drug = Drug.objects.filter(id = id).first()
    drug = get_object_or_404(Drug,id = id)
    return render(request,"detail.html",{"drug":drug})

#@login_required(login_url = "user:login")
def updateDrug(request,id):
    drug = get_object_or_404(Drug,id = id)
    form = DrugForm(request.POST or None,request.FILES or None,instance = drug)
    if form.is_valid():
        drug = form.save(commit=False)
        #drug.author = request.user
        drug.save()

        messages.success(request,"The drug has been successfully updated.")
        return redirect("drug:dashboard")
    return render(request,"update.html",{"form":form})

#@login_required(login_url = "user:login")
def deleteDrug(request,id):
    drug = get_object_or_404(Drug,id = id)
    drug.delete()
    messages.success(request,"The drug was deleted successfully.")
    return redirect("drug:dashboard")

