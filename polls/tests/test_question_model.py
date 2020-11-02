import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from ..models import Question

class QuestionModelTests(TestCase):
    """
    Test for Question model.
    """

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_is_published_with_future_question(self):
        """
        is_published() return False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.is_published(), False)

    def test_is_publish_with_one_year_question(self):
        """
        is_published() return True for questions whose pub_date
        is older than current time no matter how old it is.
        """
        time = timezone.now() - datetime.timedelta(days=365)
        very_old_question = Question(pub_date=time)
        self.assertIs(very_old_question.is_published(), True)

    def test_can_vote_with_future_question(self):
        """
        can_vote() return False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.can_vote(), False)

    def test_can_vote_with_closed_question(self):
        """
        can_vote() return False for questions whose end_date
        is already pass.
        """
        pub_date_time = timezone.now() - datetime.timedelta(days=7)
        end_date_time = timezone.now() - datetime.timedelta(days=1)
        closed_question = Question(pub_date=pub_date_time, end_date=end_date_time)
        self.assertIs(closed_question.can_vote(), False)

    def test_can_vote_with_open_question(self):
        """
        can_vote() return True for questions whose still open.
        pub_date is in the past and end_date is in the future.
        """
        pub_date_time = timezone.now() - datetime.timedelta(days=1)
        end_date_time = timezone.now() + datetime.timedelta(days=1)
        open_question = Question(pub_date=pub_date_time, end_date=end_date_time)
        self.assertIs(open_question.can_vote(), True)