from store.models import Manufacturer, ReleaseDecade, Cpu


def filter_listing(request):
    """
    function to list all filters
    """
    context = {}
    context["manufacturer"] = Manufacturer.objects.all()
    context["release_decade"] = ReleaseDecade.objects.all()
    context["cpu"] = Cpu.objects.all()
    return context