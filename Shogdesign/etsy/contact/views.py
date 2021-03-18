from django.shortcuts import render,HttpResponse
from .form import Contact
from django.shortcuts import redirect


def contact(request):

    if request.method == 'POST':

        formWeb = Contact(request.POST)

        if formWeb.is_valid():
            post = formWeb.save(commit= False)
            post.save()

            return redirect ("/contact/?valid")

    else:

        formWeb = Contact()

    return render(request,'contact/Contact.html',{'form':formWeb})
