from django.test import TestCase
from django.shortcuts import reverse

from .models import CustomerData


class TestUrlResponse(TestCase):
    # Url Test Response use name
    @classmethod
    def setUpTestData(cls):
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

    # def test_create_url(self):
    #     response = self.client.get(reverse('create'))
    #     self.assertEqual(response.status_code, 200)

    # def test_retrieve_url(self):
    #     response = self.client.get(f'show/{self.crm.id}/', args=[self.crm.id])
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_update_url(self):
    #     response = self.client.get(reverse('update'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_destroy_url(self):
    #     response = self.client.get(reverse('destroy'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_api_list_url(self):
    #     response = self.client.get(reverse('list'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_api_create_url(self):
    #     response = self.client.get(reverse('api-create'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_api_retrieve_url(self):
    #     response = self.client.get(reverse('api-retrieve'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_api_update_url(self):
    #     response = self.client.get(reverse('api-update'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_api_destroy_url(self):
    #     response = self.client.get(reverse('api-destroy'))
    #     self.assertEqual(response.status_code, 200)
