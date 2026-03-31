from django.shortcuts import render

def home(request):
    context = {
        "name": "bf",
        "email": "bf@gmail.com",
        "role":"AI Engineer"
    }

    return render(request, "home.html", context)