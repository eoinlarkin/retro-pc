from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q

from cart.contexts import cart_contents
from .models import Product, Manufacturer

def index(request):
    """ 
    A view to return the index page 
    """
    #print(cart_contents)
    return render(request, 'products/index.html')

def store_view(request):
    """ 
    A view to show all products, including sorting and search queries 
    """
    
    products = Product.objects.all()
    query = None # setting blank query for search on page load
    manufacturer = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'manufacturer':
                sortkey = 'manufacturer__name'
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'manufacturer' in request.GET:
            manufacturer = request.GET['manufacturer'].split(',')
            products = products.filter(manufacturer__name__in=manufacturer)
            manufacturer = Manufacturer.objects.filter(name__in=manufacturer)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))
            
            # using django Q to drive search:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': manufacturer,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/store.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)