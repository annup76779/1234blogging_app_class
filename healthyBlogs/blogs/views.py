from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import BlogPostForm

# Create your views here.
class UploadBlog(View):
    template = "blogs/upload.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, context={"form": BlogPostForm()})

    def post(self, request, *args, **kwargs):
        form = BlogPostForm(request.POST)
        print(request.POST.get("image"))
        print(form.errors.as_data())
        if form.is_valid():
            # form.save()
            return HttpResponse(f"Uploading blog %s" % request.POST.get("title"))
        else:
            return HttpResponse(f"Problem uploading blog %s" % request.POST.get("title"))