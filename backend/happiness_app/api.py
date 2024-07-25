from ninja import Router
from acts_of_kindness.models import ActsOfKindness
from acts_of_kindness.schemas import ActsOfKindnessSchema
from django.core.serializers import serialize
import json

router = Router()


@router.get("/five-acts", response=list[ActsOfKindnessSchema])
def five_random_acts(request):
    acts = ActsOfKindness.objects.all().order_by('?')[:5]
    acts = serialize('json', acts)
    acts = json.loads(acts)

    return acts
