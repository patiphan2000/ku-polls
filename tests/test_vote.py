from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from polls.models import Question

class VoteTest(TestCase):
    def test_vote_before_login(self):
        new_question = Question.objects.create(question_text='Question for test auth', pub_date=timezone.now())
        response = self.client.post(reverse('polls:vote', args=(new_question.id,)))
        self.assertEqual(response.status_code, 302)  # should redirect to login
    
    def test_vote_after_login(self):
        new_question = Question.objects.create(question_text='Question for test auth', pub_date=timezone.now())

        user = User.objects.create(username='testuser')
        user.set_password('55555')
        user.save()
        self.client.login(username='testuser', password='55555')

        response = self.client.post(reverse('polls:vote', args=(new_question.id,)))
        self.assertEqual(response.status_code, 200)