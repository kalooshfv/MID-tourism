from django.test import TestCase
from resto.models import *
import datetime

# Create your tests here.
# TODO: Every single test :D
class RestoTest(TestCase):
    def test_resto_url(self):
        resp = self.client.get('/resto/')
        self.assertEqual(resp.status_code, 200)

    def test_resto_template(self):
        resp = self.client.get('/resto/')
        self.assertTemplateUsed(resp, 'resto.html')

    def test_resto_object(self):
        Restaurant.objects.create(
            resto_name = "My House",
            resto_address = "Puri Beta 1 Jalan Tanjung 1 No.18, Banten, Tangerang",
            resto_email = "kf.verrell@gmail.com",
            resto_phone = "087881001234",
            resto_days = "Monday, Tuesday, Wednesday, Thursday, Friday",
            resto_open_hour = datetime.time(8, 0, 0),
            resto_close_hour = datetime.time(14, 0, 0),
            resto_description = "Literally just my house",
        )