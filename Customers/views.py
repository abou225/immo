from django.shortcuts import render, redirect
from django.contrib import messages
from Customers.models import Customer
from .forms import cForm

# Create your views here.

#FONCTION POUR TOUT AFFICHER
def index(request):

    c_list = Customer.objects.all()

    context = {
        'customers': c_list
    }
    
    return render(request, 'Customers/index.html', context)

#FONCTION POUR CREER
def create(request):
    if request.method == "POST":
        form = cForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("c-list")  # Redirige vers la liste des clients après ajout
        else:
            context = {
                "c_form": form
            }
            return render(request, "Customers/create.html", context)
    else:
        form = cForm()
        context = {
            "c_form": form
        }
        return render(request, "Customers/create.html", context)




#FONCTION POUR AFFICHER
def show(request,id):
    customer = Customer.objects.get(pk=id) # SELECT * FROM Customers WHERE id = id

    context = {
        'customer': customer
    }
    return render(request, "Customers/show.html", context)


#FONCTION POUR METTRE A JOUR
def update(request, id):
    customer = Customer.objects.get(pk=id)
    if request.method == "POST":
        form = cForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("c-list")
    else:
        form = cForm(instance=customer)
    
    context = {
        "c_form": form,
        "Customer": customer
    }
    return render(request, "Customers/update.html", context)
    
    
#FONCTION POUR SUPPRIMER
def delete(request,id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    messages.info(request, "Client supprimé avec succes")
    return redirect("c-list")
