from ninja import Router
from .models import ActsOfKindness
from .schemas import ActsOfKindnessSchema

router = Router()


@router.get("/acts", response=list[ActsOfKindnessSchema])
def list_acts(request):
    acts = ActsOfKindness.objects.all()
    for act in acts:
        act.image = act.image.url
    return acts


@router.get("/five-acts", response=list[ActsOfKindnessSchema])
def five_random_acts(request):
    acts = ActsOfKindness.objects.all().order_by('?')[:5]
    for act in acts:
        act.image = act.image.url

    return acts


@router.get("/act/{act_id}", response=ActsOfKindnessSchema)
def get_act(request, act_id: int):
    act = ActsOfKindness.objects.get(id=act_id)
    act.image = act.image.url
    return act
