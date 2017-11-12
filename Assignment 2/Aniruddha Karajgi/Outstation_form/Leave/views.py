from django.views import generic
from .models import Leave
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login     # verifies login
from django.views.generic import View
from .forms import ChiefLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth


class LeaveListView(generic.ListView):
    model = Leave
    template_name = 'Leave/leave_list_view.html'
    context_object_name = 'all_leaves'

    def get_queryset(self):
        return Leave.objects.all()


class LeaveAddView(CreateView):
    model = Leave
    fields = ['name', 'hostel_name', 'departure_date', 'arrival_date']


class Register(View):
    form_class = ChiefLogin
    template_name = 'Leave/chiefregister.html'

    # displays blank form
    def get(self, request):
        form = self.form_class(None)
        # default data none, user fills data
        return render(request, self.template_name, {'form': form})

    # processes form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)   # doesn't directly save it to database

            # cleaned and formatted data (eg. uniform date format)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # returns user content if valid auth..
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    auth.login(request, user)  # logged in
                    return redirect('Leave:leave_list_view')

        return render_to_response(request, self.template_name, {'form': form})


def login_view(request):
    # context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:

            if user.is_active:
                auth.login(request, user)
                # Redirect to index page.

                if user.username == "Mahavir":
                    return redirect('Leave:chief_view')

                else:
                    return redirect('Leave:leave_list_view')

            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")

        else:
            # Return an 'invalid login' error message.
            print("invalid login details " + username + " " + password)
            return render(request, 'Leave/chieflogin.html')

    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'Leave/chieflogin.html')


def logout_view(request):
    logout(request)
    return redirect('Leave:login_view')


def chief_view(request):
    if request.user.is_authenticated():
        if request.user.username == "Mahavir":
            unapproved_leaves = Leave.objects.filter(approval=False)

            data = {
                'unapproved_leaves': unapproved_leaves
            }
            return render(request, 'Leave/leave_approve_view.html', data)

        else:
            return redirect('Leave:leave_list_view')

    elif not request.user.is_authenticated():
        return redirect('Leave:login_view')


def leave_approve_view(request):
    unapproved_leaves = Leave.objects.filter(approval=False)

    for leave in unapproved_leaves:
        if not leave.approval:
            leave.approval = True
            leave.save()

    return HttpResponseRedirect("chief_view/")
