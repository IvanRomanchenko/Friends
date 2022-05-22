from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .orm import create_note, Profile


@receiver(post_save, sender=Profile, dispatch_uid="update_profile")
def update_profile(sender, instance, created=False, update_fields=None, **kwargs):
    if created:
        create_note(instance.username, 'create')

    else:
        if update_fields != frozenset({'last_login'}):
            create_note(instance.username, 'update')


@receiver(post_delete, sender=Profile, dispatch_uid="delete_profile")
def delete_profile(sender, instance, **kwargs):
    create_note(instance.username, 'delete')
