from typing import Literal

from .models import Profile, Note


def profile_count(with_staff: bool = False):
    """ Counts user profiles """
    if with_staff:
        return Profile.objects.count()
    else:
        return Profile.objects.exclude(is_staff=True).count()


def create_note(username: str,
                signal_type: Literal['create', 'update', 'delete']):
    """ Creates Note instance """
    Note.objects.create(username=username, signal_type=signal_type)
