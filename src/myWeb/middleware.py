from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

PATH_IGNORED = [
    reverse("users:user_profile"),
    reverse("posts:list_posts"),
    reverse("users:user_logout")
]


class ProfileNotCompleted:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        user = request.user
        print("USER: ", user)
        if user.is_authenticated:
            profile = user.profile
            if profile.birthday == None or profile.phone_number == None or profile.avatar.name == '':
                if request.path not in PATH_IGNORED:
                    messages.add_message(request, messages.INFO, 'You must complete your profile in order to use our services.')
                    return redirect("users:user_profile")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response