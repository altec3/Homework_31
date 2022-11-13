import json
from typing import Dict, Any

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from categories.models import Category


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesListView(ListView):
    model = Category

    """Get all categories"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")

        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    """Create a new category"""
    def post(self, request, *args, **kwargs):
        data: Dict[str, Any] = json.loads(request.body)

        category = Category.objects.create(**data)
        category.save()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, status=201)


class CategoryDetailView(DetailView):
    model = Category

    """Get category by pk"""
    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    """Update a category given its identifier"""
    def patch(self, request, *args, **kwargs):

        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        self.object.name = data["name"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        }, status=204)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    """Delete a category given its identifier"""
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=204)
