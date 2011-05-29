from models import *

def main(request):
    context = { 'navigations' : Navigation.objects.filter(publish=True), }
    return context