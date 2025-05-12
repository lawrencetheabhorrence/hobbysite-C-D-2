from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Product, Transaction
from .forms import ProductCreator


class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "merchstore/product_detail.html"
    model = Product
    success_url = reverse_lazy("merchstore:product_list")
    context_object_name = "product"

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(
                reverse_lazy("merchstore:product_detail", kwargs={"pk": request.POST.get("bought_product")}),
                reverse("login"),
            )
        else:
            affected_product = get_object_or_404(
                Product, pk=request.POST.get("bought_product")
            )
            if len(request.POST.get("amount"))!=0 and affected_product.stock >= int(request.POST.get("amount")):
                amount_to_buy = int(request.POST.get("amount"))
                transaction = Transaction()
                transaction.buyer = request.user.profile
                transaction.product = affected_product
                transaction.amount = amount_to_buy
                transaction.save()
                affected_product.reduce_stock(transaction.amount)
            else:
                return HttpResponseRedirect(self.request.path_info)

        return HttpResponseRedirect(self.success_url)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreator
    success_url = reverse_lazy("merchstore:product_list")
    template_name_suffix = "_create"

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(ProductCreateView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs["owner"] = self.request.user.profile
        return form_kwargs

    def form_valid(self, form):
        if form.cleaned_data["price"] < 0:
            return super().form_invalid(form)
        updated_product = form.save()
        updated_product.update_status()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy("merchstore:product_list")
    template_name_suffix = "_update"
    fields = ["name", "product_type", "description", "price", "stock", "status"]

    def get(self, request, *args, **kwargs):
        self.object = Product
        context = super().get_context_data(**kwargs)
        affected_product = get_object_or_404(Product, pk=context["pk"])
        if request.user.profile != affected_product.owner:
            return HttpResponseRedirect(reverse_lazy("merchstore:product_list"))
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if form.cleaned_data["price"] < 0:
            return super().form_invalid(form)
        updated_product = form.save()
        updated_product.update_status()
        return super().form_valid(form)


class CartListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/cart_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile).order_by('product__owner','-created_on')


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(product__owner=self.request.user.profile).order_by('buyer','-created_on')
