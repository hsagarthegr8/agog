from .models import log, Log


class ActivityMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ActivityMixin, self).get_context_data(**kwargs)
        context['notifications'] = Log.objects.filter(user2=self.request.user).exclude(user1=self.request.user)
        context['recents'] = Log.objects.filter(user1=self.request.user)
        return context


class EventLogMixin(object):

    @property
    def action(self):
        return "{}_{}".format(
            self.action_kind,
            self.model._meta.verbose_name.upper().replace(" ", "_")
        )

    @property
    def extra_data(self):
        return {}

    @property
    def user(self):
        if self.request.user.is_authenticated():
            return self.request.user
        return None

    def log_action(self):
        log(
            user1=self.user,
            action=self.action,
            extra=self.extra_data,
            obj=getattr(self, "object", None)
        )

    def form_valid(self, form):
        response = super(EventLogMixin, self).form_valid(form)
        self.log_action()
        return response
