from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class UploadBlog(View):
    template = "blogs/upload.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template)


    def post(self, request, *args, **kwargs):
        return HttpResponse(f"Uploading blog %s" % request.POST.get("title"))