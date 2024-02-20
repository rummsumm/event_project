from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Event


def category(request, pk: int):
    """
    Zeige eine Kategorie.
    events/category/3    
    """
    # category = Category.objects.get(pk=pk)
    # falls pk nicht existiert, erhebe einen Http404
    category = get_object_or_404(Category, pk=pk)

    return render(
        request,
        "events/category.html",
        {"category": category}
    )


def categories(request):
    """ 
    Zeige alle Kategorien an
    events/categories
    """
    print(dir(request))
    print("GET:", request.GET)
    print("user: ", request.user)
    print("Methode:", request.method)
    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(
        request,
        "events/categories.html",
        context
    )



def first_view(request):
    """ 
    events/hello    
    """
    return HttpResponse("goodbye cruel world!")
