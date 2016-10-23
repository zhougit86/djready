from django.test import TestCase
from django.core.urlresolvers import resolve
from records.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolve(self):
        found=resolve("/")
        self.assertEqual(found.func,home_page)

# Create your tests here.
