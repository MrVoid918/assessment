from django.contrib import messages
from django.urls.base import reverse_lazy
from .forms import ClaimsForms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def claim_form_view(request):
    if request.method == 'POST':
        form = ClaimsForms(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "Claim submitted successfully!")
            return HttpResponseRedirect(reverse_lazy("home"))
        else:
            messages.error(request, "Invalid form submission")
            messages.error(request, form.errors)
    else:
        form = ClaimsForms()
    return render(request, "claims/submit.html", {"form": form})
