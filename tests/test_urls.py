# Testowanie urls
# python manage.py test tests
from django.shortcuts import reverse
from django.urls import resolve
from django.test import SimpleTestCase

from views_app.views import hello_template, HelloClassView, person_detail


class TestUrls(SimpleTestCase):
    def test_functional_hello_template_url_is_resolved(self):
        url = reverse('views_app:hello-template')
        functional_view = resolve(url).func

        self.assertEqual(functional_view, hello_template)

    def test_class_hello_template_url_is_resolved(self):
        url = reverse('views_app:hello-template2')
        class_view = resolve(url).func.view_class

        self.assertEqual(class_view, HelloClassView)

    def test_parametrized_detail_view_url_is_resolved(self):
        url = reverse('views_app:person-detail', args=[1])
        view = resolve(url).func

        self.assertEqual(view, person_detail)
