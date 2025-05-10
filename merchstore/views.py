from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import ProductType, Product, Transaction, Profile
from .forms import ProductCreator


class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"
    context_object_name = "products"


"""
def merchstoreVariety(request, product_type=""):
    # This function is deprecated
    # Shows products of a certain type

    chosen_product_type = get_object_or_404(ProductType, name=product_type)
    available_items = get_list_or_404(Product, product_type=chosen_product_type)

    context = {"product_kind": chosen_product_type, "items": available_items}

    return render(request, "merchstore/merchstore_variety.html", context)
"""



class ProductDetailView(DetailView):
    template_name = "merchstore/product_detail.html"
    model = Product
    success_url = reverse_lazy("merchstore:product_list")
    context_object_name = "product"

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(
                reverse_lazy("merchstore:product_detail", kwargs={"pk": context["pk"]}),
                reverse("login"),
            )
        else:
            affected_product = get_object_or_404(Product, pk=request.POST.get('bought_product'))
            amount_to_buy = int(request.POST.get('amount'))
            if affected_product.stock >= amount_to_buy:
                transaction = Transaction()
                transaction.buyer = request.user.profile
                transaction.product = affected_product
                transaction.amount = amount_to_buy
                transaction.save()
                affected_product.reduce_stock(transaction.amount)
                
        return HttpResponseRedirect(self.request.path_info)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreator
    success_url = reverse_lazy("merchstore:product_list")
    template_name_suffix = "_create"

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(ProductCreateView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['user'] = self.request.user
        return form_kwargs
    

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy("merchstore:product_list")
    template_name_suffix = "_create"
    fields = ['name','product_type','description','price','stock','status']