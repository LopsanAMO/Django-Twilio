from django.shortcuts import render
from django.views.shorcouts import View
from .tulio import send_message

class Home(View):
    def get(self, request):
        template_name = 'weas.html'
        return render(request, template_name)

    def post(self, request):
        msg = request.POST.get('message')
        success_template = 'success.html'
        error_template = 'error.html'
        try:
            send_message(msg)
            return render(request, success_template)
        except:
            return render(request, error_template)
