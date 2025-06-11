from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "jobs/post_list.html"
    context_object_name = "object_list"
    queryset = Post.objects.filter(status=1).order_by("-created_at")