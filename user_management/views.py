from django.shortcuts import render
from .models import Profile

def update(request, id):
    
    profile = Profile.objects.get(id=id)
    
    if request.method == 'POST':
        
        profile.name = request.POST.get('new_name')
        profile.email_address = request.POST.get('new_email_address')
        profile.save()
    
    context = {'profile': profile}
    
    return render(request, 'update.html', context)
