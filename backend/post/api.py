from ninja import Router
from .models import Post
from .schemas import PostSchema

router = Router()


@router.get("/posts", response=list[PostSchema])
def list_posts(request):
    posts = Post.objects.all()
    return [PostSchema.from_django(post) for post in posts]
