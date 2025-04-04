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
        return render(request, 'login/success.html', {'user': user})    
    return render(request, 'Login/farmregister.html')