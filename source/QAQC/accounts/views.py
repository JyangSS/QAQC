from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm, PasswordResetForm, ChangePasswordForm, CustomUserChangeForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.models import Profile
from .models import Profile
from generals.models import Branch, Department
from pprint import pprint
import json
from django.db.models import Count, Q
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView
#from recordmgnts.models import Container
from django.contrib.auth.mixins import LoginRequiredMixin


def mylogin(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active is None and user.is_superuser is None:
                messages.warning(request, f'Account is not activated')
            else:
                # correct username and password login the user
                login(request, user)
                return redirect('accounts:home')

        else:
            messages.warning(request, f'Incorrect username or password')

    return render(request, 'registration/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        email = form.data['email']
        email += "@huayang.com.my"
        username = str(form.data['first_name']) + " " + str(form.data['last_name'])
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = username
            new_form.modify_by = username
            new_form.email = email
            new_form.save()
            messages.success(request, f'Your account has been created')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'forms': form})


def load_department(request):
    branch_id = request.GET.get('branch')
    departments = Department.objects.filter(branch=branch_id)
    if request.user.is_authenticated:
        current_department = request.user.department
        return render(request, 'accounts/dept_dropdown_list.html', {'departments': departments, 'curr_dept': current_department})
    else:
        return render(request, 'accounts/dept_dropdown_list.html', {'departments': departments})


class MyPasswordResetView(auth_views.PasswordResetView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        return super(MyPasswordResetView, self).get(request, *args, **kwargs)


class MyPasswordConfirmView(auth_views.PasswordResetConfirmView):
    form_class = PasswordResetForm


class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        return super(MyPasswordResetCompleteView, self).get(request, *args, **kwargs)


class MyPasswordChangeView(SuccessMessageMixin, auth_views.PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('accounts:profile_page')

    def get_success_message(self, cleaned_data):
        return 'Your password has been changed successfully'


@login_required
def home(request):
    return render(request, 'accounts/home.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def update_profile(request):
    email_name = request.user.email.split('@', 1)[0]
    initial_data = {
        'username': request.user.username,
        'contact': request.user.contact,
        'email': email_name,
        'department': request.user.department,
        'company': request.user.company,
        'branch': request.user.branch,
        'supervisor': request.user.supervisor,
        'is_superuser': request.user.is_superuser,
        'is_staff': request.user.is_staff,
        'is_documentcontroller': request.user.is_documentcontroller
    }
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        email = form.data['email']
        email += "@huayang.com.my"
        if form.is_valid():
            fs = form.save(commit=False)
            fs.email = email
            fs.modify_by = str(request.user)
            fs.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('accounts:profile_page')

    else:
        form = CustomUserChangeForm(initial=initial_data)
    return render(request, 'accounts/profile_update_form.html', {'forms': form})


# class dashboard_view(View):
#     template_name = 'accounts/dashboard.html'

# def json_chart(request):
#     return render(request, 'accounts/dashboard.html')
#
#
# def dashboard_viewDepartment(request):
#     dataset = Department.objects \
#         .values('department') \
#         .exclude(department='') \
#         .annotate(total=Count('department')) \
#         .order_by('department')
#
#     port_display_name = dict()
#     for port_tuple in Department.PORT_CHOICES:
#         port_display_name[port_tuple[0]] = port_tuple[1]
#
#     chart = {
#         'chart': {'type': 'pie'},
#         'title': {'text': 'Titanic Survivors by Ticket Class'},
#         'series': [{
#             'name': 'Department',
#             'data': list(map(lambda row: {'name': port_display_name[row['department']], 'y': row['total']}, dataset))
#         }]
#     }
#
#     return JsonResponse(chart)
