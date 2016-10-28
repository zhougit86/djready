from django.test import TestCase

from records.forms import ItemForm

class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form=ItemForm()

        self.assertFalse(form.is_valid())
        # self.assertEqual(form.errors['text'],["You can't have an empty list item"])
        # self.fail(form.as_p())
        # form = ItemForm(data={'text': ''})