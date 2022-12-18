from django.urls import path
from .views import UploadBlog

urlpatterns = [
    path("blog_upload/", UploadBlog.as_view(), name="upload_blog"),
]