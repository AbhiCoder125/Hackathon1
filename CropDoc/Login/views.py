from django.shortcuts import render

from .models import User

def Registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        
        user = User.objects.create(
                username=username,
                email=email,
                password=password,
        )    
    return render(request, 'Login/farmregister.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username, password=password)
            return render(request, 'Login/farmregister.html', {'user': user})
        except User.DoesNotExist:
            error_message = "Invalid username or password."
            return render(request, 'Login/farmregister.html', {'error': error_message})
    return render(request, 'Login/farmlogin.html')
