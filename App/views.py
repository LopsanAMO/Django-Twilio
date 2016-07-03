from django.shortcuts import render
from django.views.shorcouts import View

class Home(View):
    def get(self, request):
        template_name = 'weas.html'
        return render(request, template_name)

    def post(self, request):
