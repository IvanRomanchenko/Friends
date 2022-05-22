from .orm import profile_count


def user_count(request):
    return {
        'profile_count': profile_count(),
        'profile_count_with_staff': profile_count(with_staff=True),
    }
