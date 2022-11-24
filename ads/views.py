from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.serializers import AdSerializer


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.order_by("-price")
    serializer_class = AdSerializer

    permissions = {
        "retrieve": [IsAuthenticated()]
    }
    permissions_default = [AllowAny()]

    def get_permissions(self):
        return self.permissions.get(self.action, self.permissions_default)

    def list(self, request, *args, **kwargs):
        categories: list = request.GET.getlist("cat")
        if categories:
            self.queryset = self.queryset.filter(category__ad__in=categories)

        text = request.GET.get("text")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get("location")
        if location:
            self.queryset = self.queryset.filter(author__location_id__name__icontains=location)

        price_from = request.GET.get("price_from")
        price_to = request.GET.get("price_to")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(self, request, *args, **kwargs)


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
