from Blog.models import Post , Category

def recent_post(request):
    recent = Post.objects.order_by("-created")
    return {"recent_post" : recent}
def category(request):
    cat = Category.objects.all()
    return {"categorys" : cat}