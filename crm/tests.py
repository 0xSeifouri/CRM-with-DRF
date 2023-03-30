from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from .models import CustomerData


class TestUrlResponse(TestCase):
    # Url Test Response use name
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.user = User.objects.create(username='user1')
        cls.token = Token.objects.create(user=cls.user)
        cls.token.save()
        cls.crm = CustomerData.objects.create(
            first_name='test',
            last_name='test',
            email='test@email.com',
            phone='09123456789',
            address='test st',
            city='test city',
            state='test state',
            zipcode='0123456789',
        )

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_url(self):
        response = self.client.post(reverse('create'), {'first_name': 'test', 'last_name': 'test',
                                                        'email': 'test@email.com', 'phone': '09123456789',
                                                        'address': 'test st', 'city': 'test city',
                                                        'state': 'test state', 'zipcode': '0123456789'})
        self.assertEqual(response.status_code, 302)

    def test_retrieve_url(self):
        response = self.client.get(reverse('retrieve', args=[self.crm.id]))
        self.assertEqual(response.status_code, 200)

    def test_update_url(self):
        response = self.client.get(reverse('update', args=[self.crm.id]), {'first_name': 'test', 'last_name': 'test',
                                                                           'email': 'test@email.com',
                                                                           'phone': '09123456789',
                                                                           'address': 'test st', 'city': 'test city',
                                                                           'state': 'test state',
                                                                           'zipcode': '0123456789'})
        self.assertEqual(response.status_code, 302)

    def test_destroy_url(self):
        response = self.client.get(reverse('destroy', args=[self.crm.id]))
        self.assertEqual(response.status_code, 302)

    def test_api_list_url(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)

    def test_api_retrieve_url(self):
        response = self.client.get(reverse('api-retrieve', args=[self.crm.id]))
        self.assertEqual(response.status_code, 200)

