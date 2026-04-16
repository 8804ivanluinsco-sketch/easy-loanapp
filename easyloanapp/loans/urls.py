from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("apply-loan/", views.apply_loan_view, name="apply_loan"),

    path("my-loans/", views.my_loans, name="my_loans"),
    path("loan/<int:loan_id>/", views.loan_detail, name="loan_detail"),
]