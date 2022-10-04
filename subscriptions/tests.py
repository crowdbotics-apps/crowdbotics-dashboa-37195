from django.test import TestCase

from subscriptions.api.v1.viewsets import PlanViewSet
from subscriptions.models import Plan
from users.admin import User
from rest_framework.test import APIRequestFactory, force_authenticate


class PlanViewsetTest(TestCase):
    """ Test class for Plan Viewsets"""

    fixtures = ['subscriptions/fixtures/plans.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_user = User.objects.create_user('tester', 'p455w0rd')

    def test_unauthorised_plan_listing(self):
        request = self.factory.get('/api/v1/plan/')
        view = PlanViewSet.as_view({'get': 'list'})
        response = view(request)

        self.assertEqual(
            response.status_code, 403)

    def test_authorised_plan_listing(self):
        request = self.factory.get('/api/v1/plan/')
        force_authenticate(request, user=self.test_user)
        view = PlanViewSet.as_view({'get': 'list'})
        response = view(request)

        self.assertEqual(
            response.status_code, 200)

        self.assertEqual(
            len(response.data), 3)

    def test_unauthorised_plan_creation(self):
        plan_data = {
            "name": "Extra Plan",
            "price": "1000"
        }
        request = self.factory.post('/api/v1/plan/', plan_data)
        view = PlanViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(
            response.status_code, 403)

    def test_authorised_plan_creation(self):
        plan_data = {
            "name": "Extra Plan",
            "price": "1000"
        }
        request = self.factory.post('/api/v1/plan/', plan_data)
        force_authenticate(request, user=self.test_user)
        view = PlanViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(
            response.status_code, 403)

    def test_superuser_plan_creation(self):
        plan_data = {
            "name": "Extra Cheap Plan",
            "price": "5"
        }

        request = self.factory.post(f'/api/v1/plan/', plan_data)
        self.test_user.is_superuser = True
        self.test_user.is_staff = True
        self.test_user.save()
        force_authenticate(request, user=self.test_user)
        view = PlanViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(
            response.status_code, 201)

    def test_plan_update(self):
        plan = Plan.objects.create(
            name="Update plan",
            price=25,
        )
        update_data = {
            "description": "Extra Cheap Plan",
        }

        request = self.factory.patch(f'/api/v1/plan/{plan.id}/', update_data)
        force_authenticate(request, user=self.test_user)
        view = PlanViewSet.as_view({'patch': 'update'})
        response = view(request, pk=plan.id)

        self.assertEqual(
            response.status_code, 403)

    def test_superuser_plan_update(self):
        self.test_user.is_superuser = True
        self.test_user.is_staff = True
        self.test_user.save()
        plan = Plan.objects.create(
            name="Update plan",
            price=25,
        )
        update_data = {
            "description": "Update Plan",
        }

        request = self.factory.patch(f'/api/v1/plan/{plan.id}/', update_data)
        force_authenticate(request, user=self.test_user)
        view = PlanViewSet.as_view({'patch': 'update'})
        response = view(request, pk=plan.id)

        self.assertEqual(
            response.status_code, 200)

    def test_plan_delete(self):
        plan = Plan.objects.create(
            name="Delete plan",
            price=40,
        )
        request = self.factory.delete(f'/api/v1/plan/{plan.id}/')
        force_authenticate(request, user=self.test_user)
        view = PlanViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=plan.id)

        self.assertEqual(
            response.status_code, 403)

    def test_superuser_plan_delete(self):
        self.test_user.is_superuser = True
        self.test_user.is_staff = True
        self.test_user.save()
        plan = Plan.objects.create(
            name="Delete plan",
            price=40,
        )
        update_data = {
            "description": "Delete Plan",
        }

        request = self.factory.delete(f'/api/v1/plan/{plan.id}/', update_data)
        force_authenticate(request, user=self.test_user)
        view = PlanViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=plan.id)

        self.assertEqual(
            response.status_code, 204)
