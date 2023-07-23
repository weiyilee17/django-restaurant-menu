from django.views import generic

from .models import Dish, CATEGORY


# Create your views here.
class DishList(generic.ListView):
    queryset = Dish.objects.order_by('date_created')
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CATEGORY

        return context


class DishDetail(generic.DetailView):
    # This line is the reason why we can access dish in dish_detail.html
    model = Dish
    template_name = 'dish_detail.html'
