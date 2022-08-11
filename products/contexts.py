from products.models import Manufacturer, ReleaseDecade


def filter_listing(request):
    """
    function to list all filters
    """
    context = {}
    context["manufacturer"] = Manufacturer.objects.all()
    context["release_decade"] = ReleaseDecade.objects.all()
    return context