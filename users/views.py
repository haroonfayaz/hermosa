from django.views import View
from users.models import User
from users.forms import UserRegistrationForm
from django.shortcuts import redirect,render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home.html'

class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request,'home.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.name = form.cleaned_data['name']
            user.contact = form.cleaned_data['contact']
            user.save()
            return redirect('registration_success')
        return render(request, 'home.html', {'form': form})


