from django.contrib import admin
from django import  forms
from django.utils.translation import gettext as _
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import Major, Course, Category, Outline, Point
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import  path


class PointInline(admin.StackedInline):
    model = Point
    pk_name = 'outline'

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["id", "name", "major"]
    search_fields = ["name", "major_name"]


class OutlineForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Outline
        fields = '__all__'

class OutlineCourseInLine(admin.TabularInline):
    model = Outline.courses.through

class OutlineAdmin(admin.ModelAdmin):
    form = OutlineForm
    list_display = ["id", "created_date", "active", "category"]
    search_fields = ["category__name", "course__schoolYear", "created_date"]
    list_filter = ["major__name"]
    readonly_fields = ["avatar"]
    inlines = (OutlineCourseInLine, PointInline, )

    def avatar(self, obj):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width=120px />".format(img_url=obj.image.name, alt=obj.category.name))


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'

class CourseOutlineInLine(admin.TabularInline):
    model = Course.outlines.through

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = ["id", "schoolYear", "major", "created_date", "active"]
    search_fields = ["schoolYear", "created_date", "major__name"]
    list_filter = ["major__name"]
    readonly_fields = ["avatar"]
    inlines = (CourseOutlineInLine, )

    def avatar(self, obj):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width=120px />".format(img_url=obj.image.name, alt=obj.category.name))

class PointInline(admin.StackedInline):
    model = Point
    pk_name = 'outline'





class OutlineAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG QUAN LY VA BIEN SOAN DE CUONG'

    def get_urls(self):
        return [
            path('outline-stats/', self.outline_stats)
        ] + super().get_urls()

    def outline_stats(self, request):
        outline_count = Outline.objects.count()
        course_count = Course.objects.count()

        return TemplateResponse(request, 'admin/outline-stats.html', {
            'outline_count': outline_count,
            'course_count': course_count
        })



admin_site = OutlineAppAdminSite('myoutline')



# Register your models here.
#admin.site.register(Major)
#admin.site.register(Course,CourseAdmin)
#admin.site.register(Outline, OutlineAdmin)
#admin.site.register(Category)
admin_site.register(Major)
admin_site.register(Course, CourseAdmin)
admin_site.register(Outline, OutlineAdmin)
admin_site.register(Category, CategoryAdmin)
