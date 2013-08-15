# Create your views here.
from django.http import HttpRequest, HttpResponse
from util import get_ip_address_from_request

def home(request):

    ipaddr = get_ip_address_from_request(request)
    response = HttpResponse(ipaddr, content_type="text/plain")
    return response
