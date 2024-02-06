from django.shortcuts import reverse
from django.test import TestCase

from views_app.models import Person


class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        """Metoda uruachamiana RAZ, przed WSZYSTKIMI testami jednostkowymi."""
        pass

    def setUp(self):
        """Metoda uruchamiana przed KAŻDYM testem jednostkowym."""
        self.person = Person.objects.create(
            name='John',
            age=11,
            city='NY'
        )

    def tearDown(self):
        """Metoda uruchamiana po KAŻDYM teście jednostkwym."""
        ...

    @classmethod
    def tearDownClass(cls):
        """Metoda uruchamiana RAZ, po WSZYSTKICH testach."""
        ...

    def test_hello_template_view(self):
        url = reverse('views_app:hello-template')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views_app/hello.html')
        self.assertIn(b'Hello', response.content)

    def test_person_detail_view(self):
        response = self.client.get(reverse('views_app:person-detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views_app/person_detail.html')

        ctx = response.context
        person = ctx.get('person')
        self.assertEqual(person.name, 'John')

    def test_person_detail_view3(self):
        response = self.client.get(reverse('views_app:person-detail', args=[100]))
        self.assertEqual(response.status_code, 404)
