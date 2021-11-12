from rest_framework import mixins, viewsets

from .models import Contact
from .serializers import ContactSerializer


class ContactView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
