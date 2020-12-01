from django.test import SimpleTestCase
from magazines.forms import UserForm, CreateUserForm


class TestForms(SimpleTestCase):

    def test_UserForm_valid(self):
        form = UserForm(data = {
            'username' : 'test1',
            'email' : 'test@naver.com',
            'password1' : 'passWord1!',
            'password2' : 'passWord1!'

        })

        self.assertTrue(form.is_valid())

    def test_UserForm_empty(self):
        form = UserForm(data = {}
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)