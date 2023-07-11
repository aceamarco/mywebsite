from django.shortcuts import render
from django.http import HttpResponseForbidden

home = lambda request: render(request, "home.html")
resume = lambda request: render(request, "resume.html")
projects = lambda request: render(request, "projects.html")

under_construction = lambda request: render(request, "under_construction.html")
about = under_construction
contact = under_construction

dev = (
    lambda request: render(request, "dev.html")
    if request.META.get("HTTP_HOST") in ["localhost", "127.0.0.1:8000"]
    else HttpResponseForbidden()
)
