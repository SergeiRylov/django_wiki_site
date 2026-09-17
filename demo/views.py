from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from demo import forms

TITLE = "Demo page"


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    """Demo page"""

    breadcrumbs = [
        (None, TITLE),
    ]

    if request.POST:
        if request.POST.get("submit") == "delete":
            form = forms.IndexForm()
            messages.error(request, "Delete successful")
        else:
            form = forms.IndexForm(request.POST)
            if form.is_valid():
                messages.info(request, "Save successful")
    else:
        form = forms.IndexForm()

    context = {"title": TITLE, "breadcrumbs": breadcrumbs, "form": form}
    return render(request, "demo/index.html", context)


@user_passes_test(lambda u: u.is_superuser)
def modal(request):
    form = forms.FakeLoginForm

    context = {
        "title": TITLE,
        "form": form,
        # "contacts": contacts_page,
    }
    return render(request, "tst/modal.html", context)


def index_full(request):

    return render(request, "tst/index-full.html")
