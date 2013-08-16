from django.http import HttpRequest, HttpResponse
from util import get_ip_address_from_request
from models import Trap, TrapRecord


def main_trap(request, descriptor=None):
    """
        It's a trap! :)
    """

    # register access!
    if descriptor:

        # find the trap being used.
        which_trap = Trap.objects.filter(descriptor=descriptor)
        if not which_trap:
            which_trap = Trap.objects.filter(descriptor="root")
            if not which_trap:
                raise Exception("No root trap!")

            which_trap = which_trap[0]

        record = TrapRecord(trap=which_trap)
        record.ip_addr = get_ip_address_from_request(request)
        record.save()

        # successfully logged, display something
        response = HttpResponse("Server error!", content_type="text/plain")
        return response

    else:
        # no descriptor, show create trap page.
        pass

    ipaddr = get_ip_address_from_request(request)
    response = HttpResponse(ipaddr, content_type="text/plain")
    return response
