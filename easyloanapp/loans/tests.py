from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Loan


class LoanViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            email="tester@gmail.com",
            password="password123",
        )
        self.loan = Loan.objects.create(
            user=self.user,
            loan_type="Personal",
            amount=10000,
            remaining_balance=6000,
            interest_rate=5.5,
            term_months=12,
            status="active",
            next_payment_date=date(2026, 5, 1),
        )

    def test_public_pages_render(self):
        for name in ["login", "register", "dashboard", "apply_loan"]:
            with self.subTest(route=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    def test_my_loans_requires_login(self):
        response = self.client.get(reverse("my_loans"))
        self.assertEqual(response.status_code, 302)

    def test_my_loans_renders_for_authenticated_user(self):
        self.client.login(username="tester", password="password123")
        response = self.client.get(reverse("my_loans"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Loans")
        self.assertContains(response, "Personal")

    def test_dashboard_includes_my_loans_content_for_authenticated_user(self):
        self.client.login(username="tester", password="password123")
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data-dashboard-panel="my-loans"')
        self.assertContains(response, "Personal")

    def test_loan_detail_only_shows_current_users_loan(self):
        other_user = User.objects.create_user(
            username="other",
            email="other@example.com",
            password="password123",
        )
        other_loan = Loan.objects.create(
            user=other_user,
            loan_type="Business",
            amount=20000,
            remaining_balance=15000,
            interest_rate=7.0,
            term_months=24,
            status="pending",
            next_payment_date=date(2026, 6, 1),
        )

        self.client.login(username="tester", password="password123")
        own_response = self.client.get(reverse("loan_detail", args=[self.loan.id]))
        other_response = self.client.get(reverse("loan_detail", args=[other_loan.id]))

        self.assertEqual(own_response.status_code, 200)
        self.assertEqual(other_response.status_code, 404)
