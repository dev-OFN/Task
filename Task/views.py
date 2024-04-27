
from rest_framework import generics
from .models import Books,Category
from .serializers import CategorySerializer, BookSerializer
from rest_framework.response import Response

from django.views.generic import ListView

# Create your views here.


class CategoryListView(ListView):
# class CategoryListCreateView(generics.ListCreateAPIView):
    model = Category
    template_name = 'category_list.html'
    queryset = Category.objects.all()
    context_object_name = 'data'
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer