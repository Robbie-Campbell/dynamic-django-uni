from django.test import TestCase
from store.models import Category, Product

class DatabaseTestCase(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name="firstname", slug="firstname")
        self.product = Product.objects.create(category=Category.objects.first(), title="Rice")

    def test_validate_data_in_category(self):
        d = self.cat
        prod = self.product
        self.assertTrue(isinstance(d, Category))
        self.assertTrue(str(d), "firstname")
        self.assertNotEqual(str(d), "hello")
        self.assertTrue(isinstance(prod, Product))
        self.assertTrue(str(prod), "Rice")
