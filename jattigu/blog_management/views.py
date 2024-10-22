from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import BlogPost, BlogCategory
from .forms import BlogPostForm  # Assuming you have a form for creating a blog post

# View to list all blog posts
def blog_post_list(request):
    """Displays a list of all blog posts."""
    posts = BlogPost.objects.all().order_by('-published_at')
    return render(request, 'blog/blog_post_list.html', {'posts': posts})

# View to display details of a specific blog post
def blog_post_detail(request, pk):
    """Displays details of a specific blog post."""
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_post_detail.html', {'post': post})

# View to create a new blog post
def create_blog_post(request):
    """Allows users to create a new blog post."""
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.created_at = timezone.now()
            if not blog_post.category:
                default_category = BlogCategory.objects.filter(name='Default').first()
                blog_post.category = default_category
            blog_post.save()
            # form.save_m2m()  # Save the many-to-many tags
            return redirect('blog_post_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

# View to list all blog categories
def blog_category_list(request):
    """Displays a list of all blog categories."""
    categories = BlogCategory.objects.all()
    return render(request, 'blog/blog_category_list.html', {'categories': categories})

# View to display details of a specific blog category
def blog_category_detail(request, pk):
    """Displays details of a specific blog category and its posts."""
    category = get_object_or_404(BlogCategory, pk=pk)
    posts = BlogPost.objects.filter(category=category, is_published=True).order_by('-published_at')
    return render(request, 'blog/blog_category_detail.html', {'category': category, 'posts': posts})

