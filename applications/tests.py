from django.test import TestCase

from applications.api.v1.viewsets import AppViewSet
from applications.models import App
from subscriptions.models import Subscription
from users.admin import User
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate


class AppViewsetTest(TestCase):
    """ Test class for App Viewsets"""

    fixtures = ['subscriptions/fixtures/plans.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_user = User.objects.create_user('tester', 'p455w0rd')

    def test_unauthorised_app_creation(self):
        app_data = {
            "name": "Free App",
            "description": "Testing Freee App",
            "type": "Web",
            "framework": "Django",
        }
        request = self.factory.post('/api/v1/app/', app_data)
        view = AppViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(
            response.status_code, 403)

    def test_authorised_app_creation(self):
        app_data = {
            "name": "Free App",
            "description": "Testing Freee App",
            "type": "Web",
            "framework": "Django",
        }
        request = self.factory.post('/api/v1/app/', app_data)
        force_authenticate(request, user=self.test_user)
        view = AppViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(
            response.status_code, 201)

    def test_updating_app(self):
        app = App.objects.create(
            name="Update App",
            user=self.test_user,
            type="Web",
            framework="Django"
        )
        update_data = {
            "description": "Update app description"
        }
        request = self.factory.patch(f'/api/v1/app/{app.id}/', update_data)
        force_authenticate(request, user=self.test_user)
        view = AppViewSet.as_view({'patch': 'update'})
        response = view(request, pk=app.id)

        self.assertEqual(
            response.status_code, 200)

    def test_deleting_app(self):
        app = App.objects.create(
            name="Delete App",
            user=self.test_user,
            type="Web",
            framework="Django"
        )

        request = self.factory.delete(f'/api/v1/app/{app.id}/')
        force_authenticate(request, user=self.test_user)
        view = AppViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=app.id)

        self.assertEqual(
            response.status_code, 204)
