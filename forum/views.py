from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, ThreadCategory
from .forms import CommentForm


class ThreadList:
    def __call__(self, request):
        categories = ThreadCategory.objects.all()
        user_threads = []
        
        if request.user.is_authenticated:
            try:
                user_threads = request.user.profile.threads.all()
            except:
                pass
        
        return render(request, 'forum/index.html', {
            'categories': categories,
            'user_threads': user_threads,
        })


class ThreadDetail:
    def __call__(self, request, pk):
        thread = get_object_or_404(Thread, pk=pk)
        related_threads = Thread.objects.filter(category=thread.category).exclude(pk=thread.pk)
        
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
        
        return render(request, 'forum/detail.html', {
            'thread': thread,
            'related_threads': related_threads,
            'comments': thread.comment_set.all(),  
            'form': form,
            'is_owner': request.user.is_authenticated and thread.author and thread.author.user == request.user,
        })
