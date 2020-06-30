from tt_wall.app.models import Location


def locations_processor(request):
    return {'locations': Location.objects.all()}
