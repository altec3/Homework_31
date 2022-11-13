import json
from typing import Dict, Any

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from HW_27 import settings
from locations.models import Location
from users.models import User


@method_decorator(csrf_exempt, name="dispatch")
class UsersListView(ListView):
    model = User

    """Get all users"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.all()

        paginator = Paginator(self.object_list, settings.ITEMS_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "role": user.role,
                "age": user.age,
                "locations": [user.location.name]
            })

        response = {
            "items": users,
            "total": paginator.count,
            "page": page_number,
            "num_pages": paginator.num_pages
        }
        return JsonResponse(response, safe=False, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']

    """Create a new user"""
    def post(self, request, *args, **kwargs):
        data: Dict[str, Any] = json.loads(request.body)

        user = User.objects.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            username=data["username"],
            password=data["password"],
            role=data.get("role", "member"),
            age=data.get("age")
        )

        if "locations" in data:
            for location in data["locations"]:
                location_obj, _ = Location.objects.get_or_create(
                    name=location
                )
                user.location = location_obj

        user.save()

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": [user.location.name]
        }, status=201)


class UserDetailView(DetailView):
    model = User

    """Get user by pk"""
    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "role": user.role,
                "age": user.age,
                "locations": [user.location.name]
            }, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']

    """Update user given its identifier"""
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if data.get("first_name"):
            self.object.first_name = data["first_name"]
        if data.get("last_name"):
            self.object.last_name = data["last_name"]
        if data.get("username"):
            self.object.username = data["username"]
        if data.get("password"):
            self.object.password = data["password"]
        if data.get("age"):
            self.object.age = data["age"]
        if "locations" in data:
            for location in data["locations"]:
                location_obj, _ = Location.objects.get_or_create(name=location)
                self.object.location = location_obj

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "age": self.object.age,
            "location": self.object.location_id
        }, status=204)


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    """Delete user given its identifier"""
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=204)
