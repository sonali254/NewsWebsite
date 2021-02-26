from django.shortcuts import render, redirect
from .models import Subcat
from cat.models import Cat

# Create your views here.
def subcat_list(request):
    cat=Subcat.objects.all()
    return render(request, 'back/subcat_list.html', {'cat':cat})


def subcat_add(request):
    cat=Cat.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        cat_id=request.POST.get('cat')
        if name == "" :
            error = "all field requried"
            return render(request, 'back/error.html', {'error': error})
        if len(Subcat.objects.filter(name=name)) !=0 :
            error = "already name used before"
            return render(request, 'back/error.html', {'error': error})
        cat_name= Cat.objects.get(pk=cat_id).name
        b=Subcat(name=name, cat_name=cat_name, cat_id=cat_id)
        b.save()
        return redirect('subcat_list')


    return render(request,'back/subcat_add.html', {'cat':cat})