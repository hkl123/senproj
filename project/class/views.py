from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import View
from .models import Class, Assignment, Calendar, Item
from .forms import SignUp

# Create your views here.


class Index(generic.ListView):
    template_name = 'class/index.html'

    def get_queryset(self):
        return Class.objects.all()


class ClassInfo(generic.DetailView):
    model = Class
    template_name = 'class/classinfo.html'


class Home(generic.ListView):
    template_name = 'class/home.html'

    def get_queryset(self):
        return Class.objects.all()


class Assignments(generic.ListView):
    template_name = 'class/assignments.html'

    def get_queryset(self):
        return Class.objects.raw('SELECT * FROM Class_Assignment')


class StudentList(generic.DetailView):
    model = Class
    template_name = 'class/studentlist.html'


class Points(generic.DetailView):
    model = Class
    template_name = 'class/points.html'


class Store(generic.ListView):
    template_name = 'class/store.html'

    def get_queryset(self):
        return Class.objects.raw('SELECT * FROM Class_Item')


class Calendar(generic.ListView):
    template_name = 'class/calendar.html'

    def get_queryset(self):
        return Class.objects.raw('SELECT * FROM Class_Calendar')


class MakeClass(CreateView):
    model = Class
    fields = ['name', 'code']


class UpdateClass(UpdateView):
    model = Class
    fields = ['name', 'code']


class DeleteClass(DeleteView):
    model = Class
    success_url = reverse_lazy('class:home')


class MakeAssignment(CreateView):
    model = Assignment
    fields = ['Class', 'name', 'description', 'points_value']


class UpdateAssignment(UpdateView):
    model = Assignment
    fields = ['Class', 'name', 'description', 'points_value']


class MakeCalEntry(CreateView):
    model = Calendar
    fields = ['Class', 'date', 'event']


class UpdateCalEntry(UpdateView):
    model = Calendar
    fields = ['Class', 'date', 'event']


class MakeItem(CreateView):
    model = Item
    fields = ['name', 'price', 'RedemptionPage']


class UpdateItem(UpdateView):
    model = Item
    fields = ['name', 'price']


class SignUpPage(View):
    form_class = SignUp
    template_name = 'class/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            tempUser = form.save(commit=False)
            tempEmail = form.cleaned_data['email']
            tempPassword = form.cleaned_data['password']
            tempUsername = form.cleaned_data['username']
            tempUser.set_password(tempPassword)
            tempUser.save()

            user = authenticate(email=tempEmail, password=tempPassword)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('class:index')

        return render(request, self.template_name, {'form_class': form})





