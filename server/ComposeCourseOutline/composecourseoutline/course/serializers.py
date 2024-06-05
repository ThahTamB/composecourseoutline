from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Outline, Major, Point, User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "major"]

class MajorSerializer(ModelSerializer):
    class Meta:
        model = Major
        fields = ["id", "name"]

class OutlineSerializer(ModelSerializer):
    class Meta:
        model = Outline
        fields = ["id", "major", "category", "courses", "content"]

class CourseSerializer(ModelSerializer):
    outlines = OutlineSerializer(many=True)
    class Meta:
        model = Course
        fields = ["id", "schoolYear", "major", "outlines", "image", "created_date"]

class PointSerializer(ModelSerializer):
    class Meta:
        model = Point
        fields = ["type", ]