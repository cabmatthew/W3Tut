from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MembersForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required
def main(request):
    # template = loader.get_template('main.html')
    # return HttpResponse(template.render())
    
    context = {}
    
    return render(request, "main.html", context)

@login_required
def create_view(request):
    context = {}

    # Create object of form
    form = MembersForm(request.POST or None, request.FILES or None)

    # Check if form data is valid
    if form.is_valid():
        # Save the form dta to model
        form.save()
        return HttpResponseRedirect("/list")

    context['form'] = form
    return render(request, "crud/create.html", context)

@login_required
def memberlist_view(request):
    context = {}

    context["dataset"] = Member.objects.all()

    return render(request, "crud/listview.html", context)

@login_required
def memberdetail_view(request, id):
    context = {}
    
    context["data"] = Member.objects.get(id = id)

    return render(request, "crud/detailview.html", context)

@login_required
def update_or_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Member, id=id)

    if request.method == "POST":
        # Check if the form was submitted for update
        if 'update' in request.POST:
            form = MembersForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/list")

        # Check if the form was submitted for delete
        if 'delete' in request.POST:
            obj.delete()
            return HttpResponseRedirect("/list")

    else:
        form = MembersForm(instance=obj)

    context["form"] = form
    context["id"] = id

    return render(request, "crud/update_or_delete_view.html", context)