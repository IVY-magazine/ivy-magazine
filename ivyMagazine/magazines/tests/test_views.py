from django.test import TestCase, Client
from django.urls import reverse
from magazines.models import Customer, Magazine, Post 
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.blog_url = reverse('blog')
        self.contactus_url = reverse('contactUs')
        self.aboutus_url = reverse('aboutUs')
        self.info_url = reverse('info')


    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazines/homepage.html')

    def test_blog_GET(self):
        response = self.client.get(self.blog_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazines/blog.html')

    def test_contactus_GET(self):
        response = self.client.get(self.contactus_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazines/contactUs.html')

    def test_aboutus_GET(self):
        response = self.client.get(self.aboutus_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazines/aboutUs.html')

