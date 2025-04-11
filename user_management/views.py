from django.shortcuts import render
from .models import Profile

def update(request):
    
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        
        profile.name = request.POST.get('new_name')
        profile.email_address = request.POST.get('new_email_address')
        profile.save()
    
    context = {'profile': profile}
    
    return render(request, 'user_management/update.html', context)
