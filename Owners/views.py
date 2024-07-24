from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from Owners.models import Owner
from .forms import oForm

# Create your views here.

#FONCTION POUR TOUT AFFICHER
def index(request):

    o_list = Owner.objects.all()

    context = {
        'owner': o_list
    }
    
    return render(request, 'Owners/index.html', context)

#FONCTION POUR CREER
def create(request):
    if request.method == "POST":
        form = oForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("o-list")  # Redirige vers la liste des clients après ajout
        else:
            context = {
                "o_form": form
            }
            return render(request, "Owners/create.html", context)
    else:
        form = oForm()
        context = {
            "o_form": form
        }
        return render(request, "Owners/create.html", context)




#FONCTION POUR AFFICHER
def show(request,id):
    owner = Owner.objects.get(pk=id) # SELECT * FROM Customers WHERE id = id

    context = {
        'owner': owner
    }
    return render(request, "Owners/show.html", context)


#FONCTION POUR METTRE A JOUR
def update(request, id):
    owner = Owner.objects.get(pk=id)
    if request.method == "POST":
        form = oForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect("o-list")
    else:
        form = oForm(instance=owner)
    
    context = {
        "o_form": form,
        "Owner": owner
    }
    return render(request, "Owners/update.html", context)
    
    
#FONCTION POUR SUPPRIMER
def delete(request,id):
    owner = Owner.objects.get(pk=id)
    owner.delete()
    messages.info(request, "Propriétaire supprimé avec succes")
    return redirect("o-list")
