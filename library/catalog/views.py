from django.db.models import F
from django.db.models.functions import Lower
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse, JsonResponse
from .models import Book, Author, BookInstance, Genre, Student
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer, BookInstanceSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from django.db import connection

import string
import random
from django.db.models import Q
from functools import reduce
from operator import or_


# Create your views here.
def index(request):
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'catalog/index.html', context=context)


def count_books(request):
    c = Book.objects.all().count()
    return HttpResponse(f'Number of available books are ------ {c}')


class BookCreate(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy('sample : index')


# def Author_Details(request):
#    au = Author.objects.get(id=2)
#    s = AuthorSerializer(au)
#    j_son = JSONRenderer().render(s.data)
#    return HttpResponse(j_son, content_type='application/json')

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    ordering_fields = '__all__'
    search_fields = (
        "first_name",
        "last_name",
        "date_of_birth",
        "date_of_death"
    )
    filterset_fields = [
        "first_name",
        "last_name",
        "date_of_birth",
        "date_of_death"
    ]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields = '__all__'
    search_fields = (
        "id",
        "title",
        "genre",
        "author",
        "isbn",
    )
    filterset_fields = [
        "id",
        "title",
        "genre",
        "author",
        "isbn"
    ]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class NewAPI(APIView):
    http_method_names = ['get', 'head']
    permission_classes = (permissions.AllowAny,)

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        books = Book.objects.all()
        auth = Author.objects.all()
        genre = Genre.objects.all()
        book_ins = BookInstance.objects.all()
        b = BookSerializer(books, many=True)
        a = AuthorSerializer(auth, many=True)
        g = GenreSerializer(genre, many=True)
        bi = BookInstanceSerializer(book_ins, many=True)

        return Response([a.data, b.data, g.data, bi.data])


# ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises

# ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises # ORM Exercises


class Scenario1(APIView):
    http_method_names = ['get', 'head']
    permission_classes = (permissions.AllowAny,)

    def get(self, request, Format=None):
        num = self.request.query_params.get('id', None)
        temp = self.request.query_params.get('name__endswith', None)
        queryset = Book.objects.filter(id=num).filter(title__endswith=temp)

        print(len(connection.queries))
        q = BookSerializer(queryset, many=True)
        return Response(q.data)


#
# class ScenarioViewSet(viewsets.ModelViewSet):
#     # http_method_names = ['get', 'head']
#     # permission_classes = (permissions.AllowAny,)
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()
#
#     def get_queryset(self):
#         num = self.request.query_params.get('id', None)
#         temp = self.request.query_params.get('name__endswith', None)
#         queryset = Book.objects.filter(id=num)
#
#         return queryset

class Scenario2(APIView):
    http_method_names = ['get', 'head']
    permission_classes = (permissions.AllowAny,)

    def get(self, request, Format=None):
        queryset = Book.objects.annotate(sum=F('id') + 100).order_by('id').values_list('sum', flat=True)
        # q = BookSerializer(queryset, many=True)
        return Response(queryset)


class Scenario3(APIView):
    http_method_names = ['get', 'head']
    permission_classes = (permissions.AllowAny,)

    def get(self, request, Format=None):
        queryset = Book.objects.values('id').annotate(author=F('author__first_name'))
        # q = BookSerializer(queryset, many=True)
        return Response(queryset)


class Scenario4(APIView):
    def post(self, request):
        n = 9
        lst = []
        for i in range(10000):
            res = ''.join(random.choices(string.ascii_letters, k=n))
            obj = Student(name=res)
            lst.append(obj)
        queryset = Student.objects.all()
        if queryset.exists() == False:
            Student.objects.bulk_create(lst)
            return Response(data="Posted data")
        return Response(data="data already exists")


class Scenario5(APIView):
    def post(self, request):
        data = self.request.data.get('lst')
        data = list(data.split(","))
        for i in data:
            print(i)
        # res = [Student.objects.filter(name__iexact=name) for name in data]
        # n = len(res)
        res = Student.objects.filter(name__in=data).count()
        return Response(res)


class Scenario9(APIView):
    def post(self, request):
        id = self.request.data.get('id',None)
        name = self.request.data.get('name')
        if id==None:
            obj = Student(id=id, name=name)
            obj.save()
            return Response(data="Created object successfully")
        else:
            obj = Student.objects.get(id=id)
            obj.name = name
            obj.save()
            return Response(data="Updated name successfully")

