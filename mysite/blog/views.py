from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, ContactForm, ContactFormToAdmin, CommentForForm, UserProfileForm
from .models import Post, ContactModelToAdmin, Article, CommentForArticle
from .models import ContactModelToAdmin as Message
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.published.all()
    return render(request, 'main/blog_list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'main/blog_detail.html', {'post': post, 'comments': comments,
                                                     'new_comment': new_comment, 'comment_form': comment_form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    cd = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post.message_to_admin = cd['message']
    else:
        form = ContactForm()
    return render(request, 'main/share.html', {'post': post, 'form': form, 'cd': cd})


def admin_share(request):
    cd = None
    if request.method == 'POST':
        form = ContactFormToAdmin(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactModelToAdmin.objects.create(sent_message=cd['message'], )
    else:
        form = ContactForm()
    return render(request, 'main/share.html', {'form': form, 'cd': cd})


def latest_messages(request):
    if len(Message.objects.all()) >= 5:
        messages = Message.objects.all().order_by('-id')[:5]
    else:
        messages = {'Сообщений меньше пяти'}
    return render(request, 'main/latest_messages.html', {'messages': messages})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    comments_list = article.comments.filter(active=True)

    comment = None

    if request.method == 'POST':
        comment_form = CommentForForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            messages.success(request, f'Комментарий успешно добавлен.')
            return redirect(reverse('blog:article_detail', args=[slug]))
    else:
        comment_form = CommentForForm()
    return render(request, 'main/article_detail.html', {'article': article, 'comment': comment,
                                                        'comment_form': comment_form, 'comments_list': comments_list})


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:user_profile'))  # Перенаправление на страницу профиля для подтверждения изменений
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'main/user_profile.html', {'form': form, 'user': request.user})


# @login_required
# def edit_profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('user_profile')  # Перенаправление на страницу профиля для подтверждения изменений
#     else:
#         form = UserProfileForm(instance=user)
#     return render(request, 'main/edit_profile.html', {'form': form, 'user': user})
