import uuid

from django.shortcuts import redirect, render


def hello_world(request):
    guid = '{{{0}}}'.format(str(uuid.uuid1()))
    return render(request, 'common/hello_world.html', {'guid': guid})

