from ninja import Router
from .models import Post
from .schemas import PostSchema

router = Router()


@router.get("/posts", response=list[PostSchema])
def list_posts(request):
    posts = Post.objects.all()
    for post in posts:
        post.image = post.image.url
        post.user_profile.profile_image = post.user_profile.profile_image.url
    return posts
