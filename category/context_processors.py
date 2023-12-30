from .models import Category

def cat_menu_links(request):
    links = Category.objects.all()
    return dict(cat_links=links)