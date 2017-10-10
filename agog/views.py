from django.views.generic import TemplateView
from accounts.forms import UserCreationForm

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        kwargs['form']=UserCreationForm()
        return super(HomeView, self).get_context_data(**kwargs)