from django.test import TestCase
from . import views
from django.urls import reverse
# Create your tests here.
class TestHoroscope(TestCase):

    def test_index(self):
        responce = self.client.get('/horoscope/')
        self.assertEqual(responce.status_code, 200)

    def test_libra(self):
        responce = self.client.get('/horoscope/libra')
        self.assertEqual(responce.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      responce.content.decode())


    def test_signs(self):
        for i in views.zodiac_dict:
            sign_url = reverse('horoscope-name', args=[i])
            responce = self.client.get(sign_url)
            self.assertEqual(responce.status_code, 200)
            self.assertIn(views.zodiac_dict[i], responce.content.decode())

    def test_sign_redirect(self):
        for i in range(1,13):
            response = self.client.get(f'/horoscope/{i}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{list(views.zodiac_dict.keys())[i-1]}')
