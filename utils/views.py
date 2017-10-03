from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import get_user_model

User = get_user_model()


class SearchView(ListView):
    template_name = 'utils/search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        self.queryset = User.objects.filter(full_name__icontains=query)
        return super(SearchView, self).get(request,*args,**kwargs)