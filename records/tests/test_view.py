from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest
from django.utils.html import escape

from records.views import home_page
from records.models import Item,List
from records.forms import ItemForm

class HomePageTest(TestCase):
    maxDiff = None

    def test_home_page_renders_home_temp(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], ItemForm)

    def test_root_url_resolve(self):
        found=resolve("/")
        self.assertEqual(found.func,home_page)

    def test_home_page_return(self):
        request=HttpRequest()
        response=home_page(request)
        # self.assertTrue(response.content.startswith(b'<html'))
        # self.assertTrue(response.content.endswith(b'</html>'))
        expected_html = render_to_string('home.html',{'form':ItemForm()})    #if error,then add the Item section
        self.assertMultiLineEqual(response.content.decode(),expected_html)


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


class NewListTest(TestCase):

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        # expected_error = "You can't have an empty list item"
        expected_error = escape("You can't have an empty list item")
        # print(expected_error)
        self.assertContains(response, expected_error)

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
        new_list=List.objects.first()
        self.assertRedirects(response,'/lists/%d/' % (new_list.id))

# class NewItemTest(TestCase):
class ListViewTest(TestCase):

    def test_validation_errors_end_up_on_lists_page(self):
        list_ = List.objects.create()
        response = self.client.post(
            '/lists/%d/' % (list_.id,),
            data={'item_text': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)

    def test_can_save_a_POST_request_to_an_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )
        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))




# Create your tests here.
