"""Redirection for page and link to html files."""
from django.shortcuts import redirect


def index(request):
    """Redirect to the polls index."""
    return redirect("portfolio:index")
