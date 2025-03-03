from django.views import generic # type: ignore
from .models import Item

class MenuList(generic.ListView):
    model = Item
    template_name = 'index.html'
    queryset = Item.objects.order_by('-date_created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_detail.html'