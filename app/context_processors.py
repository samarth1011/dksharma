from .models import ServiceCategory


def service_categories(request):
    return {
        'service_categories': ServiceCategory.objects.filter(parent__isnull=True).prefetch_related('children', 'services')
    }