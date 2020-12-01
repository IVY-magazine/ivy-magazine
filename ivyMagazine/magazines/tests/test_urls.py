from django.test import SimpleTestCase
from django.urls import reverse, resolve
from magazines.views import home, loginPage, detailView, viewMagazine

class TestUrls(SimpleTestCase):

    def test_home_url_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_loginHome_url_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, loginPage)

    def test_detail_url_resolved(self):
        url = reverse('detail', args = [1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, detailView)    

    def test_viewMagazine_url_resolved(self):
        url = reverse('viewMagazine', args = ["testMagazine"])
        print(resolve(url))
        self.assertEquals(resolve(url).func, viewMagazine)  