from django.shortcuts import render
from shogproducts.models import post

# Create your views here.
def product_list (request):

    imagenes = post.objects.all()


    return render(request,"shogproducts/post_list.html",{'posts': imagenes})


