from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from civi_api.models import Fact

class TestApi(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user=get_user_model().objects.create_user(
            username='testuser',
            password='testuser'
        )
        test_user.save()

        test_thing=Fact.objects.create(
            date='1987-09-11',
            flags='c',
            fact='some texts here!',
            progress=True,
            contributor=test_user,
        )
        test_thing.save()

    def setUp(self):
        self.client.login(
            username='testuser',
            password='testuser'
        )

    def test_home_page_status(self):
        urls=reverse('fact_list')
        response=self.client.get(urls)
        self.assertEqual(response.status_code, 200)

    def test_models(self):
        fact=Fact.objects.get(id=1)
        test_date=str(fact.date)
        test_flag=str(fact.flags)
        test_fact=str(fact.fact)
        test_progress=fact.progress
        test_contributor=str(fact.contributor)
        self.assertEqual(test_date, '1987-09-11')
        self.assertEqual(test_flag, 'c')
        self.assertEqual(test_fact, 'some texts here!')
        self.assertEqual(test_progress, True)
        self.assertEqual(test_contributor, 'testuser')

    def test_get_fact(self):
        url=reverse('fact_list')
        response=self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        fact=response.data
        self.assertEqual(len(fact), 1)
        self.assertEqual(fact[0]['date'], '1987-09-11')