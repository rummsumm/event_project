from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, Event
from .forms import CategoryForm, EventForm


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy("events:events")
    # generische Templatename: event_confirm_delete.html


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    # success_url angeben, wenn nicht auf get_absolute_url weitergeleitet werden soll
    # success_url = reverse_lazy("events:events")
    # generische Templatename: event_form.html

    def form_valid(self, form):
        """Beim Anlegen eines Events setzen wir den Autor 
        des Events auf den aktuell eingeloggten User."""
        form.instance.author = self.request.user 
        return super().form_valid(form)


class EventDetailView(DetailView):
    """
    events/3
    generischer Templatename: event_detail.html
    """
    model = Event


class EventListView(ListView):
    """
    events/
    generischer Templatename: event_list.html
    """
    model = Event
    queryset = Event.objects.select_related("category")
    

def category_update(request, pk):
    """ 
    eine Kategorie editieren 
    events/category/343/update
    """
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        category = form.save()
        return redirect(category)  # nutzt get_absolute_url()!
    
    return render(
        request, 
        "events/category_form.html", 
        {
            "category": category,
            "form": form
        }
    )


def category_create(request):
    """ 
    Lege eine neue Kategorie an 
    events/category/create
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            # category = form.save(commit=False) wird nicht in DB gepsiechert
            # category.author = request.user
            # category.save()

            # hier erfolgt ein Redirect!
            # return redirect("events:categories")
            # return redirect("events:category", category.pk )
            
            # falls im Model get_absolute_url implmementiert ist
            return redirect(category)

    else:
        # wurde per GET abgesendet! 
        # leeres Formular anzeigen!
        form = CategoryForm()
    
    return render(
        request, 
        "events/category_form.html", 
        {"form": form}
    )


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
