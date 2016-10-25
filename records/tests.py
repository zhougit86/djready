from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest

from records.views import home_page
from records.models import Item,List

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


    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list=list_
        first_item.save()
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list=list_
        second_item.save()

        saved_list=List.objects.first()
        self.assertEqual(saved_list,list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list,list_)
        self.assertEqual(second_saved_item.text, 'Item the second')

    # def test_home_page_displays_all(self):
    #     Item.objects.create(text='item1')
    #     Item.objects.create(text='item2')
    #
    #     request=HttpRequest()
    #     response=home_page(request)
    #
    #     self.assertIn('item1',response.content.decode())
    #     self.assertIn('item2', response.content.decode())

class ListViewTest(TestCase):
    def test_display_all_items(self):
        Item.objects.create(text='item1')
        Item.objects.create(text='item2')

        response = self.client.get('/lists/the-only-list/')
        self.assertContains(response, 'item1')
        self.assertContains(response, 'item2')

    def test_use_list_template(self):
        response=self.client.get('/lists/the-only-list/')
        self.assertTemplateUsed(response,'list.html')

class NewListTest(TestCase):

    def test_home_page_can_save_post(self):
        # request=HttpRequest()
        # request.method='POST'
        # request.POST['item_text']='A new list item'

        response=self.client.post(
            '/lists/new',
            data={'item_text':'A new list item'}
        )

        # response=home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        response=self.client.post(
            '/lists/new',
            data={'item_text':'A new list item'}
        )

        # self.assertEqual(response.status_code,302)
        # self.assertEqual(response['location'],'/lists/the-only-list/')
        self.assertRedirects(response,'/lists/the-only-list/')


# Create your tests here.
