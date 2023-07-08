from django.shortcuts import render

home = lambda request: render(request, "home.html")
resume = lambda request: render(request, "resume.html")
projects = lambda request: render(request, "projects.html")

under_construction = lambda request: render(request, "under_construction.html")
about = under_construction
contact = under_construction
