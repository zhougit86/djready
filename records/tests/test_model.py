from django.test import TestCase
from django.core.exceptions import ValidationError
from records.models import Item,List


class ListViewTest(TestCase):

    def test_cannot_save_empty_list_items(self):
        list_=List.objects.create()
        item=Item(list=list_,text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_uses_list_template(self):
        list_=List.objects.create()
        response = self.client.get('/lists/%d/' % list_.id)
        self.assertTemplateUsed(response,'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_passes_correct_list_to_temp(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)

    # def test_display_all_items(self):
    #     list_=List.objects.create()
    #     Item.objects.create(text='item1',list=list_)
    #     Item.objects.create(text='item2',list=list_)
    #
    #     response = self.client.get('/lists/the-only-list/')
    #     self.assertContains(response, 'item1')
    #     self.assertContains(response, 'item2')
    #
    # def test_use_list_template(self):
    #     response=self.client.get('/lists/the-only-list/')
    #     self.assertTemplateUsed(response,'list.html')





# Create your tests here.
