from django.shortcuts import render


def index(request):
    return render(request, 'homepages/home.html')

def shop(request):
    return render(request, 'shop/shop_page.html')

def blog(request):
    return render(request, 'blog/blog_page.html')

def about(request):
    return render(request, 'about/about_page.html')

def contact(request):
    return render(request, 'contact/contact_page.html')