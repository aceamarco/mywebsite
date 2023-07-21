from django.shortcuts import render
from django.http import HttpResponseForbidden
import os
import json
from jsonschema import validate


home = lambda request: render(request, "home.html")
resume = lambda request: render(request, "resume.html")

under_construction = lambda request: render(request, "under_construction.html")
about = under_construction
contact = under_construction

dev = (
    lambda request: render(request, "dev.html")
    if request.META.get("HTTP_HOST") in ["localhost", "127.0.0.1:8000"]
    else HttpResponseForbidden()
)


def validate_projects_json(
    schema_file_path: str = os.path.join(
        os.path.dirname(__file__), "schemas", "projects_schema.json"
    ),
    projects_file_path: str = os.path.join("projects.json"),
):
    # Load the JSON schema
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)

    # Load the projects.json file
    with open(projects_file_path, "r") as projects_file:
        projects_data = json.load(projects_file)

    # Validate the JSON data against the schema
    try:
        validate(projects_data, schema)
        print("projects.json data is valid!")
    except Exception as e:
        print("projects.json data is invalid. Error: ", e)


def projects(request):
    try:
        # Assuming projects.json is in the same directory as views.py
        file_path = os.path.join(os.path.dirname(__file__), "projects.json")
        validate_projects_json(projects_file_path=file_path)

        with open(file_path, "r") as projects_file:
            projects_data = json.load(projects_file)

        context = {"projects": projects_data["projects"]}

        return render(request, "projects.html", context)
    except:
        return under_construction(request)
