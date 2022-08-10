from products.models import Manufacturer


def filter_listing(request):
    """
    function to list all filters
    """
    context = {}
    context["manufacturer"] = Manufacturer.objects.all()
    return context