from django.shortcuts import render, redirect


from .models import Categoriy, Name_testing
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout




# Create your views here.
def main_page(request):
    categoriy = Categoriy.objects.all()
    return render(request, 'test_user/index.html', {'categotiy': categoriy})


class login_views(LoginView):
    form_class = AuthenticationForm
    template_name = 'test_user/login.html'

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= 'Log in')
        return dict(list(context.item()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('main')


def logut(request):
    logout(request)
    return redirect('login')



def register(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, 'Ошибка добавления ползователя')

    else:
        form = CustomUserCreationForm()
    return render(request, 'test_user/register.html', {'form':form})

def test_them(request, pk):
    Name_testing = Name_testing.objects.filter(categoriy_id = pk)
    return render(request, 'button.html', {'tests': Name_testing})
