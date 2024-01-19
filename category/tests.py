from django.test import TestCase
from .models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(category_name="test cat", slug="test_cat", description="test desc")
        Category.objects.create(category_name="test cat 2", slug="test_cat_2", description="test desc 2")

    def test_category_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('category_name').max_length
        self.assertEquals(max_length, 50)

    def test_slug_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('slug').max_length
        self.assertEqual(max_length, 100)

    def test_category_str_method(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'test cat')

    def test_category_url_function(self):
        for i in range(1,3):
            category = Category.objects.get(id=i)
            cat_url = category.get_url()
            print('cat_url:',cat_url)
            if i==1:
                self.assertEqual(cat_url,'/store/category/test_cat/')
            elif i==2:
                self.assertEqual(cat_url, '/store/category/test_cat_2/')