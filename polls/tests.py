import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future = timezone.now() + datetime.timedelta(days=30)
        question = Question(pub_date=future)
        self.assertIs(question.was_published_recently(), True)

    def test_index_page_loads(self):
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
