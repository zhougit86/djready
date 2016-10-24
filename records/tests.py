from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest

from records.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolve(self):
        found=resolve("/")
        self.assertEqual(found.func,home_page)

    def test_home_page_return(self):
        request=HttpRequest()
        response=home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.endswith(b'</html>'))
        expected_html = render_to_string('home.html')
        self.assertTrue(response.content.decode(),expected_html)

    def test_home_page_can_save_post(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)
        self.assertIn('A new list item',response.content.decode())




# Create your tests here.
