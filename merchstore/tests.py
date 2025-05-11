from django.test import TestCase
from user_management.models import Profile
from django.contrib.auth.models import User
from .models import Product, ProductType


class ProductModelTest(TestCase):
    def setUp(self):
        u = User.objects.create_user("test", "test@email.com", "testpass")
        user = Profile.objects.create(user=u, name="Test User", email_address=u.email)
        ptype = ProductType.objects.create(name="Test Type", description="Test")

        product = Product(
            name="TestCase Product",
            product_type=ptype,
            owner=user,
            price=99.99,
            stock=0,
        )

        product.save()

    def test_product_should_be_out_of_stock(self):
        product = Product.objects.get(name="TestCase Product")
        self.assertEqual(product.status, Product.ProductStatusChoices.OUT_OF_STOCK)

    def test_product_reduce_stock_errror(self):
        product = Product.objects.get(name="TestCase Product")
        self.assertRaises(ValueError, product.reduce_stock, 5)

    def test_product_add_stock(self):
        product = Product.objects.get(name="TestCase Product")
        product.stock = 10
        product.update_status()
        self.assertEqual(product.status, Product.ProductStatusChoices.AVAILABLE)

    def test_product_reduce_stock_success(self):
        product = Product.objects.get(name="TestCase Product")
        product.stock = 10
        product.update_status()
        product.reduce_stock(5)
        self.assertEqual(product.status, Product.ProductStatusChoices.AVAILABLE)
        self.assertEqual(product.stock, 5)
        product.reduce_stock(5)
        self.assertEqual(product.status, Product.ProductStatusChoices.OUT_OF_STOCK)
        self.assertEqual(product.stock, 0)
