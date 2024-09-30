from django.views.generic import TemplateView

class AllPageView(TemplateView):
    template_name = "allpage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context here
        context['example'] = 'This is an example context variable'
        return context
