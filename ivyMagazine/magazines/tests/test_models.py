from django.test import TestCase
from magazines.models import Customer, Magazine

class TestModels(TestCase):
    def setUp(self):
        Customer.objects.create(
            name = "unittestUser",
            email = "unittestUser@gmail.com",
            data_created = "2020-10-25 14:30:59"
        )
        Magazine.objects.create(
            name = "unittestMagazine",
            description = "unittestDescription",
            feature = "unittestFeature",
            magazineGroup = "FW2017",
            pdf = "asdf.pdf",
            thumbNail = "asdf.png",
            date_created = "2020-12-01 14:30:59",
            viewcount = 0
        )
    def test_str_is_equal_to_name(self):
        customer1 = Customer.objects.get(name = "unittestUser")
        self.assertEqual(customer1.name, "unittestUser")
        magazine1 = Magazine.objects.get(
            name = "unittestMagazine"
            )
        self.assertEqual(magazine1.magazineGroup, "FW2017")
    def test_magazine_str_is_not_equal_to_name(self):
        magazine1 = Magazine.objects.get(name = "unittestMagazine")
        self.assertNotEqual(magazine1.name, "Magazine")