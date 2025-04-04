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
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            user = None
            if user:
                return render(request, 'Login/farmregister.html')
            else:
                return render(request, 'Login/login.html', {'error': 'Invalid username or password'})
    