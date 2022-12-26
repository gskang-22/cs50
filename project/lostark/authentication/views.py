from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse

# Create your views here.

class UsernameView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if str(username).isalnum():
            return

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')