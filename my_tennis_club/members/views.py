from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MembersForm
from django.contrib.auth.decorators import login_required

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))

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


def memberlist_view(request):
    context = {}

    context["dataset"] = Member.objects.all()

    return render(request, "crud/listview.html", context)

@login_required
def memberdetail_view(request, id):
    context = {}
    
    context["data"] = Member.objects.get(id = id)

    return render(request, "crud/detailview.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(Member, id = id)

    form = MembersForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    
    context["form"] = form

    return render(request, "crud/updateview.html", context)

def delete_view(request, id):
    context = {}

    obj = get_object_or_404(Member, id = id)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect("/")
    
    return render(request, "crud/deleteview.html", context)

def update_or_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Member, id=id)

    if request.method == "POST":
        # Check if the form was submitted for update
        if 'update' in request.POST:
            form = MembersForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(f"/list")

        # Check if the form was submitted for delete
        if 'delete' in request.POST:
            obj.delete()
            return HttpResponseRedirect("/list")

    else:
        form = MembersForm(instance=obj)

    context["form"] = form
    context["id"] = id

    return render(request, "crud/update_or_delete_view.html", context)