from rest_framework.permissions import OR
from shortener.models import Organization, PayPlan, Users
from ninja import Schema
from django.contrib.auth.models import User as U
from ninja.orm import create_schema


# OrganizationSchema = create_schema(Organization)
Users = create_schema(Users, depth=1, fields=["id", "full_name", "organization"])


# class Users(Schema):
#     id: int
#     full_name: str = None
#     organization: OrganizationSchema = None
