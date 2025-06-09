from django.http import HttpResponse

def post_list(request):
    """
    View function for listing blog posts.
    """
    return HttpResponse("Blog Posts List")

def post_detail(request, post_id):
    """
    View function for displaying a single blog post.
    """
    return HttpResponse(f"Blog Post #{post_id} Detail")