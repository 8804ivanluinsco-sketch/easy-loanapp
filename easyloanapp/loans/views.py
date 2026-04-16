from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from .models import Loan
from django.contrib.auth.decorators import login_required


def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


def _build_loans_context(user):
    if not user.is_authenticated:
        return {
            'loans': Loan.objects.none(),
            'total_balance': 0,
            'total_loans': 0,
            'active_loans': 0,
        }

    loans = Loan.objects.filter(user=user)

    total_balance = loans.aggregate(
        total=Sum('remaining_balance')
    )['total'] or 0

    return {
        'loans': loans,
        'total_balance': total_balance,
        'total_loans': loans.count(),
        'active_loans': loans.filter(status='active').count(),
    }


def dashboard_view(request):
    return render(request, "dashboard.html", _build_loans_context(request.user))


def apply_loan_view(request):
    return render(request, "apply_loan.html")


@login_required
def my_loans(request):
    return render(request, 'my-loans.html', _build_loans_context(request.user))


@login_required
def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, user=request.user)
    return render(request, 'loan_details.html', {'loan': loan})
