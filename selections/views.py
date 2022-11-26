from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from selections.models import Selection
from selections.permissions import SelectionEditPermission
from selections.serializers import SelectionListSerializer, SelectionCreateSerializer, SelectionRetrieveSerializer, \
    SelectionUpdateSerializer, SelectionDestroySerializer


class SelectionsListView(ListAPIView):
    """Get all selections"""
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionCreateView(CreateAPIView):
    """Create a new selection"""
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionDetailView(RetrieveAPIView):
    """Get selection by pk"""
    queryset = Selection.objects.all()
    serializer_class = SelectionRetrieveSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    """Update selection given its identifier"""
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]


class SelectionDeleteView(DestroyAPIView):
    """Delete selection given its identifier"""
    queryset = Selection.objects.all()
    serializer_class = SelectionDestroySerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]
