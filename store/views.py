from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q

# login required decorator
# django will check whether a user is logged in before executing the view
from django.contrib.auth.decorators import login_required

from cart.contexts import cart_contents
from .models import Product

from store.forms import ProductAdminForm

def index(request):
    """ 
    A view to return the index page 
    """
    #print(cart_contents)
    return render(request, 'store/index.html')

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
        # if 'sort' in request.GET:
        #     sortkey = request.GET['sort']
        #     sort = sortkey
            
        #     if sortkey == 'name':
        #         sortkey = 'lower_name'
        #         products = products.annotate(lower_name=Lower('name'))
            
        #     if sortkey == 'manufacturer':
        #         sortkey = 'manufacturer__name'
            
        #     if 'direction' in request.GET:
        #         direction = request.GET['direction']
        #         if direction == 'desc':
        #             sortkey = f'-{sortkey}'
        #     products = products.order_by(sortkey)
            
        if 'manufacturer' in request.GET:
            manufacturer = request.GET['manufacturer'].split(',')
            products = products.filter(manufacturer__manufacturer__in=manufacturer)
            #manufacturer = Manufacturer.objects.filter(manufacturer__in=manufacturer)

        if 'year' in request.GET:
            year = request.GET['year'].split(',')
            products = products.filter(release_decade__release_decade__in=year)
            #manufacturer = Manufacturer.objects.filter(manufacturer__in=manufacturer)

        if 'cpu' in request.GET:
            cpu = request.GET['cpu'].split(',')
            products = products.filter(cpu__cpu__in=cpu)
            #manufacturer = Manufacturer.objects.filter(manufacturer__in=manufacturer)

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
        'current_sorting': current_sorting,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'store/product_detail.html', context)


@login_required
def add_new_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductAdminForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save() # saving the product
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductAdminForm()
        
    template = 'store/add_new_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        
        # instance flag is used to indicate that we are updating the selected product
        # request.files is required for the image upload; 
        # when Django handles a file upload, the file data ends up placed in request.FILES
        form = ProductAdminForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductAdminForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'store/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('store'))