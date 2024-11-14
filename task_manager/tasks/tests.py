from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.task = Task.objects.create(user=self.user, title='Test Task', description='Test Description')

    def test_unauthorized_access(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_forbidden_access(self):
        # Log in with another user
        another_user = User.objects.create_user(username='anotheruser', password='password')
        self.client.force_authenticate(user=another_user)
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
