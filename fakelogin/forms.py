from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class FakeLoginForm(forms.Form):
    def _users():
        users = []
        for u in User.objects.filter(is_active=True).order_by("username"):
            name = u.username
            full_name = u.get_full_name()
            if full_name == "":
                full_name = name
            else:
                full_name = f"{name} ({full_name})"
            users.append([name, full_name])
        return users

    field_user = forms.ChoiceField(choices=_users, label=_("Select user"))
