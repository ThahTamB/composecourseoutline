from django.shortcuts import render
from django.http import  HttpResponse
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from .models import Category, Course, Outline, Major, User
from .serializers import MajorSerializer, CategorySerializer, CourseSerializer, OutlineSerializer, UserSerializer


class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView,
                  generics.UpdateAPIView):
        queryset = User.objects.filter(is_active=True)
        serializer_class = UserSerializer
        parser_classes = [MultiPartParser, ]

        def get_permissions(self):
                if self.action == 'retrieve':
                        return [permissions.IsAuthenticated()]

                return [permissions.AllowAny()]


class MajorViewSet(viewsets.ModelViewSet):
        queryset = Major.objects.all()
        serializer_class = MajorSerializer
        # permission_classes = [permissions.IsAuthenticated]

        # def get_permission(self):
        #         if self.action == 'list':
        #                 return [permissions.AllowAny()]
        #
        #         return [permissions.IsAuthenticated()]


class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        # permission_classes = [permissions.IsAuthenticated]

        # def get_permission(self):
        #         if self.action == 'list':
        #                 return [permissions.AllowAny()]
        #
        #         return [permissions.IsAuthenticated()]


class OutlineViewSet(viewsets.ModelViewSet):
        queryset = Outline.objects.filter(active=True)
        serializer_class = OutlineSerializer
        # permission_classes = [permissions.IsAuthenticated]

        # def get_permission(self):
        #         if self.action == 'list':
        #                 return [permissions.AllowAny()]
        #
        #         return [permissions.IsAuthenticated()]

        @swagger_auto_schema(
                operation_description='This API use to hidden Outline',
                responses={
                        status.HTTP_200_OK: OutlineSerializer()
                }
        )

        @action(methods=['post'], detail=True)
        def hidden_outline(self, request, pk):
                try:
                        o = Outline.objects.get(pk=pk)
                        o.active = False
                        o.save()
                except Outline.DoesNotExít:
                        return Response(status=status.HTTP_400_BAD_REQUEST)

                return Response(data=OutlineSerializer(o, context={'request': request}).data,
                                status=status.HTTP_200_OK)

class CourseViewSet(viewsets.ModelViewSet):
        queryset = Course.objects.filter(active=True)
        serializer_class = CourseSerializer
        #permission_classes = [permissions.IsAuthenticated]

        # def get_permission(self):
        #         if self.action == 'list':
        #                 return [permissions.AllowAny()]
        #
        #         return [permissions.IsAuthenticated()]

        @action(methods=['post'], detail=True)
        def hidden_course(self, request, pk):
                try:
                        c = Course.objects.get(pk=pk)
                        c.active = False
                        c.save()
                except Course.DoesNotExít:
                        return Response(status=status.HTTP_400_BAD_REQUEST)

                return Response(data=CourseSerializer(c, context={'request': request}).data,
                                status=status.HTTP_200_OK)


# Create your views here.
def index(request):
        return render(request, template_name='index.html',context={
                'name':'Stardust'
        })