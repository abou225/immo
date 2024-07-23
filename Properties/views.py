from django.shortcuts import render, redirect
from django.contrib import messages
from Properties.models import Property
from .forms import pForm

# Create your views here.

#FONCTION POUR TOUT AFFICHER
def index(request):

    p_list = Property.objects.all()

    context = {
        'properties': p_list
    }
    
    return render(request, 'Properties/index.html', context)

#FONCTION POUR CREER
def create(request):
    if request.method == "POST":
        form = pForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("p-list")  # Redirige vers la liste des propriétés après ajout
        else:
            context = {
                "p_form": form
            }
            return render(request, "Properties/create.html", context)
    else:
        form = pForm()
        context = {
            "p_form": form
        }
        return render(request, "Properties/create.html", context)


#FONCTION POUR AFFICHER
def show(request,id):
    property = Property.objects.get(pk=id) # SELECT * FROM Properties WHERE id = id

    context = {
        'property': property
    }
    return render(request, "Properties/show.html", context)


#FONCTION POUR METTRE A JOUR
def update(request, id):
    property = Property.objects.get(pk=id)
    if request.method == "POST":
        form = pForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect("c-list")
    else:
        form = pForm(instance=property)
    
    context = {
        "p_form": form,
        "Property": property
    }
    return render(request, "Properties/update.html", context)
    
    
    
    
#FONCTION POUR SUPPRIMER
def delete(request,id):
    property = Property.objects.get(pk=id)
    property.delete()
    messages.info(request, "Propriété supprimée avec succes")
    return redirect("p-list")
