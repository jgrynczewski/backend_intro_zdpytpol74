from django.test import TestCase

from test_app.views import concatenate_two_string


class TestExample(TestCase):
    def test_concatenate_two_string(self):
        result = concatenate_two_string("Hello, ", "how are you?")

        self.assertEqual(result, "Hello, how are you?")
        self.assertEqual(concatenate_two_string('', ''), '')
