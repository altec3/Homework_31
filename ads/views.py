import json
from typing import Dict, Any

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):

    """Get all ads"""
    def get(self, request):
        ads: type(Ad) = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published
            })
        return JsonResponse(response, safe=False, status=200)

    """Create a new ad"""
    def post(self, request):
        data: Dict[str, Any] = json.loads(request.body)
        ad = Ad(**data)
        ad.save()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published
        }, status=201)


class AdView(DetailView):
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
            })
