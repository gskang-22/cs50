from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse

# Create your views here.

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if str(username).isalnum():
            return JsonResponse({'username_error': 'username contains non-alphanumeric characters'}, status=400)
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')