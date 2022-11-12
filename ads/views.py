import json
from typing import Dict, Any

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ad
from categories.models import Category
from users.models import User


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdsListView(ListView):
    model = Ad

    """Get all ads"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.all()

        response = []
        for ad in self.object_list:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'image': ad.image.url if ad.image else None,
                'author': ad.author_id,
                'category': ad.category_id
            })
        return JsonResponse(response, safe=False, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'image', 'author', 'category']

    """Create a new ad"""
    def post(self, request, *args, **kwargs):
        data: Dict[str, Any] = json.loads(request.body)

        ad = Ad.objects.create(
            name=data["name"],
            price=data["price"],
            description=data["description"],
            is_published=data["is_published"],
            image=data.get("image")
        )
        ad.author = get_object_or_404(User, pk=data["author_id"])
        ad.category = get_object_or_404(Category, pk=data["category_id"])
        ad.save()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "author": ad.author_id,
            "category": ad.category_id
        }, status=201)


class AdDetailView(DetailView):
    model = Ad

    """Get ad by pk"""
    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
                'id': ad.id,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published
            }, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'image', 'author', 'category']

    """Update ad given its identifier"""
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if data.get("name"):
            self.object.name = data["name"]
        if data.get("price"):
            self.object.price = data["price"]
        if data.get("description"):
            self.object.description = data["description"]
        self.object.author = get_object_or_404(User, pk=data["author_id"])
        self.object.category = get_object_or_404(Category, pk=data["category_id"])
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "author": self.object.author_id,
            "category": self.object.category_id
        }, status=204)


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    """Delete ad given its identifier"""
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=204)


@method_decorator(csrf_exempt, name="dispatch")
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'image', 'author', 'category']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "author": self.object.author_id,
            "category": self.object.category_id
        }, status=204)
