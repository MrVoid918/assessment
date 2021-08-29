from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls.base import reverse_lazy
from .forms import ClaimsForms
from .models import Claims
from django.db.models.fields.files import ImageField, FileField
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from assessment.settings import MEDIA_DIR
# Create your views here.


@login_required()
def claim_view(request):
    val = Claims.objects.filter(user=request.user).values('id',
                                                          'name',
                                                          'date_accident',
                                                          'time_accident',
                                                          'claim_status')
    context = {
        "query_results": val
    }
    return render(request, 'claims/view_claims.html', context)


@login_required()
def indv_claim_view(request, id):

    val = get_object_or_404(Claims, id=id)

    if val.user != request.user:
        return HttpResponseForbidden("Not allowed to Access")

    item = dict()
    files = dict()

    for f in val._meta.get_fields()[2:]:

        if type(f) is ImageField or type(f) is FileField:
            # we put filetypes in different dictionaries rather than
            # putting all in same
            files[f.verbose_name] = {
                "path": getattr(val, f.name),
                "filename": str(getattr(val, f.name)).split('/')[-1]
            }
            continue

        if not f.choices:
            item[f.verbose_name] = getattr(val, f.name)
        else:
            shortform_value = getattr(val, f.name)
            choices_dict = dict(f.choices)
            item[f.verbose_name] = choices_dict[shortform_value]

    context = {"id": getattr(val, "id"),
               "item": item,
               "files": files,
               "status": getattr(val, "claim_status")}

    return render(request, 'claims/view_indv_claim.html', context)


@login_required()
def indv_claim_edit(request, id):
    val = get_object_or_404(Claims, id=id)

    if val.user != request.user or val.claim_status == "AC":
        return HttpResponseForbidden("Not allowed to Edit")

    if request.method == "POST":
        if "photo" in request.FILES:
            val.photo.storage.delete(val.photo.name)

        if "pdf_insurance_cover" in request.FILES:
            val.pdf_insurance_cover.storage.delete(
                val.pdf_insurance_cover.name)

        form = ClaimsForms(request.POST, request.FILES, instance=val)
        form.save()
        return HttpResponseRedirect(reverse_lazy("home"))

    form = ClaimsForms(instance=val)
    context = {"form": form}
    return render(request, "claims/edit_indv_claim.html", context)


@login_required()
def indv_claim_delete(request, id):
    val = get_object_or_404(Claims, id=id)

    if val.user != request.user or val.claim_status == "AC":
        return HttpResponseForbidden("Not allowed to Delete")

    val.delete()

    return HttpResponseRedirect(reverse_lazy("claims_view"))


@login_required()
def claim_form_view(request):
    if request.method == 'POST':
        form = ClaimsForms(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=True)
            obj.user = request.user
            obj.save()
            messages.success(request, "Claim submitted successfully!")
            return HttpResponseRedirect(reverse_lazy("home"))
        else:
            messages.error(request, "Invalid form submission")
            messages.error(request, form.errors)
    else:
        form = ClaimsForms()
    return render(request, "claims/submit.html", {"form": form})
