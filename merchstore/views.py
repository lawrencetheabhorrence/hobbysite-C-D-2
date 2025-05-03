from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import ProductType, Product, Transaction, Profile
from .forms import TransactionForm, ProductCreator


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


class ProductDetails(DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TransactionForm(item=None)
        return context


class TransactionOnProduct(SingleObjectMixin, FormView):
    template_name = "merchstore/product_detail.html"
    form_class = TransactionForm
    model = Transaction
    success_url = reverse_lazy("merchstore:product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = get_object_or_404(Product, pk=context["pk"])
        return context

    def post(self, request, *args, **kwargs):
        self.object = Transaction
        context = self.get_context_data(**kwargs)
        if not request.user.is_authenticated:
            return redirect_to_login(
                reverse_lazy("merchstore:product_detail", kwargs={"pk": context["pk"]}),
                reverse("login"),
            )
        else:
            form = TransactionForm(request.POST, item=context["product"])
            if form.is_valid():
                form.instance.buyer = request.user.profile
                form.instance.product = context["product"]
                form.instance.status = "On Cart"
                self.object = form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form, request, context)

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        amount_requested = self.object.amount
        affected_product = self.object.product
        affected_product.reduce_stock(amount_requested)
        return super().form_valid(form)

    def form_invalid(self, form, request, context):
        return render(
            request, "merchstore/product_detail.html", context | {"form": form}
        )


class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        view = ProductDetails.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = TransactionOnProduct.as_view()
        return view(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreator
    success_url = reverse_lazy("merchstore:product_list")
    template_name = "merchstore/product_create.html"

    def final_initial(self, live):
        self.initial = super().get_initial()
        self.initial["owner"] = live.user.profile

    def get(self, request, *args, **kwargs):
        self.final_initial(request)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ProductCreator(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        self.object.status_augment()
        return super().form_valid(form)


def productUpdate(request, pk=-1):
    return render(request, "merchstore/product_update.html", {})


"""
def productUpdate(request, itemID):

def cartContents(request):

def transactionList(request):

"""
