from django.views.generic import TemplateView
from accounts.forms import UserCreationForm
from django.shortcuts import redirect,reverse

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        kwargs['form']=UserCreationForm()
        return super(HomeView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('profiles:timeline'))
        return super(HomeView, self).get(request,*args,**kwargs)

