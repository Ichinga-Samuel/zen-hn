from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView as _LogoutView
from django.views.generic.edit import UpdateView
from .forms import CreateUserForm
from .models import User
from base.scripts.get_images import pick_random_image
from base.utils import BreadCrumb
from allauth.account.views import PasswordChangeView, PasswordSetView, PasswordResetView, PasswordResetFromKeyView


class LogoutView(_LogoutView):
    http_method_names = _LogoutView.http_method_names + ['get']

class UserCreateView(FormView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    slug_field = 'username'
    model = User
    login_url = reverse_lazy('login')
    fields = ("username", "email", "about", "avatar", "profile_picture")
    template_name = 'user_account/user_update_form.html'

    def test_func(self):
        return self.request.user == self.get_object()

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.object.username})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_account/profile.html'
    context_object_name = 'me'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # alls = self.object.stories.all().order_by('created')
        # rated = self.object.stories.order_by('-score')[0]
        context["breadcrumbs"] = [BreadCrumb(name="Home", url=reverse_lazy('home'))]
        context["title"] = "Profile"
        context["person"] = pick_random_image('persons')
        # context['rated'] = rated
        # context['count'] = len(alls)
        # context['recent'] = alls[0]
        return context
