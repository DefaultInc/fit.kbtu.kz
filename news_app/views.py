from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment


@login_required(login_url='/auth/login/')
def post_create_view(request):
    """
    post creating function.
    checking all of the fields, if form is valid then saving the post, if there is no image, it will upload it anyway,
    give a message that post created and redirecting to the post itself
    """
    if not request.user.extendeduser.is_manager:
        return render(request, "news_app/Http404.html")
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "news_app/post_create.html", context)


@login_required(login_url='/auth/login/')
def post_detail_view(request, id=None):
    """
    post details function,
    taking id or 404 if it is not exist, give the title and instance to the view.
    """
    instance = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=instance)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = instance
        comment.save()
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
        "comments": comments,
    }
    return render(request, "news_app/post_detail.html", context)


def post_list_view(request):
    """
    shows list of the posts.
     queryset_list - is all of the posts, and there is a paginator in the view.
     code taken from Django documentation - for paginator, check it in the Official Documentation.
    """
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 20)  # Show 20 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
    }
    return render(request, "news_app/post_list.html", context)


@login_required(login_url='/auth/login/')
def post_update_view(request, id=None):
    """
    Takes an instance, form;
    if form is valid opens view with editing posts.
    """
    if not request.user.extendeduser.is_manager:
        return render(request, "news_app/Http404.html")
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Item Saved!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "news_app/post_create.html", context)


@login_required(login_url='/auth/login/')
def post_delete_view(request, id=None):
    """
    Takes an id, by id deleting the post.
    """
    if not request.user.extendeduser.is_manager:
        return render(request, "news_app/Http404.html")
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted!")
    return redirect("news_app:post_list")


def comment_delete_view(request, comment_id=None, post_id=None):
    '''
    Takes an id of comment and ins==id of Post,
    by id of comment deletes comment
    '''
    comment = get_object_or_404(Comment, id=comment_id)
    instance = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        comment.delete()
        messages.success(request, "Your comment successfully deleted!")
    return redirect(instance.get_absolute_url())
