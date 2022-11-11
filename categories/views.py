import json
from typing import Dict, Any

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from categories.models import Category


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):

    """Get all categories"""
    def get(self, request):
        categories: type(Category) = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                'id': category.id,
                'name': category.name
            })
        return JsonResponse(response, safe=False, status=200)

    """Create a new category"""
    def post(self, request):
        data: Dict[str, Any] = json.loads(request.body)
        category = Category(**data)
        category.save()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, status=201)


class CategoryView(DetailView):
    model = Category

    """Get category by pk"""
    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })
