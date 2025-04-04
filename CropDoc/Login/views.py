from django.shortcuts import render

from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username, password=password)
            return render(request, 'login/success.html', {'user': user})
        except User.DoesNotExist:
            error_message = "Invalid username or password."
            return render(request, 'Login/farmlogin.html', {'error_message': error_message})
    
    return render(request, 'Login/farmlogin.html')