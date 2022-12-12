from django.shortcuts import render
from .models import *
# from forms import *


# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name') 

    context = {'all_pizzas': pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    context = {'pizza':p, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html',context)

# def comments(request, pizza_id):
#     pizza = Pizza.objects.get(id=pizza_id)
#     if request.method != 'POST':
#         form=CommentForm()
#     else:
#         form = CommentForm(data=request.POST)
#         if form.is_valid():
#             new_comment = form.save(commit=FALSE)
#             new_comment.form = form

#     context = {'form': form, 'pizza': pizza}
#     return render(request, 'Pizzeria/comments.html', context)

