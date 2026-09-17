from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from fakelogin import forms


@user_passes_test(lambda u: u.is_superuser)
def fakelogin(request):
    """Вход под определенным пользователем для администратора"""

    form = forms.FakeLoginForm(request.POST)
    if request.POST:
        # if not settings.DEBUG:
        #     return redirect("/")
        if form.is_valid():
            try:
                field_user = form.cleaned_data["field_user"]
                user = User.objects.get(username=field_user)
                user.backend = "django.contrib.auth.backends.ModelBackend"
                login(request, user)
                messages.info(request, "{} {}".format(_("Welcome "), user.username))
                return redirect("/")
            except User.DoesNotExist:
                messages.warning(request, _("Invalid credentials"))
                return redirect(request.META["HTTP_REFERER"])
        else:
            messages.warning(request, _("Error validating username"))

    form = forms.FakeLoginForm()
    return render(
        request,
        "fakelogin/modal.html",
        {
            "form": form,
        },
    )
