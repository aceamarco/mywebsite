from django.shortcuts import render
from django.http import HttpResponseForbidden
import os
import json
from jsonschema import validate
from django.conf import settings


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
    # TODO: Kanji Trainer
    # TODO: Parthean SlackBot
    # TODO: ArgoCD AppSource Controller
    # TODO: GraphQL Rate Limiter
    # TODO: Boeing ESEC Tool
    # TODO: Embedded Control System Projects
    # TODO: Speech Signal Processing Library from Capstone
    if settings.DEBUG:
        # Assuming projects.json is in the same directory as views.py
        file_path = os.path.join(os.path.dirname(__file__), "projects.json")
        validate_projects_json(projects_file_path=file_path)

        with open(file_path, "r") as projects_file:
            projects_data = json.load(projects_file)

        context = {"projects": projects_data["projects"]}

        return render(request, "projects.html", context)
    else:
        try:
            # Assuming projects.json is in the same directory as views.py
            file_path = os.path.join(os.path.dirname(__file__), "projects.json")
            validate_projects_json(projects_file_path=file_path)

            with open(file_path, "r") as projects_file:
                projects_data = json.load(projects_file)

            context = {"projects": projects_data["projects"]}

            return render(request, "projects.html", context)
        except Exception as e:  # Capture the exception
            if settings.DEBUG:
                raise e  # Re-raise the exception if debug is true
            return under_construction(request)
