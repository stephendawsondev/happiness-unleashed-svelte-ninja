from ninja import Router
from .models import UserProfile
from .schemas import UserProfileSchema


router = Router()


@router.get("/profiles", response=list[UserProfileSchema])
def list_profiles(request):
    profiles = UserProfile.objects.all()
    for profile in profiles:
        profile.profile_image = profile.profile_image.url

    return profiles
