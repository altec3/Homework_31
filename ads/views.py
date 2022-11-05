from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ad, Category


@method_decorator(csrf_exempt, name="dispatch")
class Index(View):
    def get(self, request):

        return JsonResponse({"status": "ok"}, status=200)


class AdsView(View):

    def get(self, request):
        ads: type(Ad) = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            })
        return JsonResponse(response, safe=False, status=200)


class CategoriesView(View):

    def get(self, request):
        categories: type(Category) = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                'id': category.id,
                'name': category.name
            })
        return JsonResponse(response, safe=False, status=200)
