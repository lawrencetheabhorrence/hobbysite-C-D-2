from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, ThreadCategory
from .forms import CommentForm

def thread_list(request):
    categories = ThreadCategory.objects.all()
    user_threads = []
    
    if request.user.is_authenticated:
        try:
            user_threads = request.user.profile.threads.all()
        except:
            pass
    
    info = {
        'categories': categories,
        'user_threads': user_threads,
    }
    return render(request, 'forum/index.html', info)

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    related_threads = Thread.objects.filter(category=thread.category).exclude(pk=thread.pk)[:2]
    comments = thread.comment_set.all().order_by('created_on')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.profile
            comment.thread = thread
            comment.save()
            return redirect('forum:thread_detail', pk=thread.pk)
    else:
        form = CommentForm()
    
    info = {
        'thread': thread,
        'related_threads': related_threads,
        'comments': comments,
        'form': form,
        'is_owner': request.user.is_authenticated and thread.author and thread.author.user == request.user,
    }
    return render(request, 'forum/detail.html', info)
