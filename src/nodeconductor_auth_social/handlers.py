from nodeconductor.structure import models as structure_models
from .models import AuthProfile


def create_auth_profile(sender, instance=None, created=False, **kwargs):
    if created:
        AuthProfile.objects.create(user=instance)
