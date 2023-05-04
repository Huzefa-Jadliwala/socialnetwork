from django.shortcuts import render
from django.views import View

#function is used to direct the user to the landing page  
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')
# Create your views here.
