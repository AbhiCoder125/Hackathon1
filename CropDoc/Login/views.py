from django.shortcuts import render

from .models import UserLogin

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = UserLogin.objects.get(username=username, password=password)
            return render(request, 'login/success.html', {'user': user})
        except UserLogin.DoesNotExist:
            error_message = "Invalid username or password."
            return render(request, 'Login/farmlogin.html', {'error_message': error_message})
    
    return render(request, 'Login/farmlogin.html')