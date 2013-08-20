from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from maustrep.forms import TrapForm
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

        record = TrapRecord(trap=which_trap[0])
        record.ip_addr = get_ip_address_from_request(request)
        record.save()

    else:

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


def register_trap(request, descriptor=None):
    """
        Creating new traps...
    """
    if request.method == 'POST':
        form = TrapForm(request.POST)

        if form.is_valid():

            desc = form.cleaned_data['descriptor']

            if desc == 'register' or desc == 'list':
                return HttpResponse("Uh OH, invalid descriptor!!", content_type="text/plain")

            which_trap = Trap.objects.filter(descriptor=desc)

            if which_trap:
                return HttpResponse("Uh OH, trap already exists!!", content_type="text/plain")

            try:
                form.save()
            except Exception as e:
                return HttpResponse("Uh OH, shit happened!!", content_type="text/plain")

        else:
            return HttpResponse("Uh OH, Invalid Info!!", content_type="text/plain")

        return HttpResponse("OPa GanGNam Style!!", content_type="text/plain")

    else:
        if request.method == 'GET':
            form = TrapForm()

    return render(request, 'register_trap.html', {'form': form})


def list_trap_records(request):
    """
        Listing records for a trap...
    """

    if request.method == 'POST':
        form = TrapForm(request.POST)

        if form.is_valid():
            desc = form.cleaned_data['descriptor']
            passwd = form.cleaned_data['password']


        which_trap = Trap.objects.filter(descriptor=desc)

        if not which_trap:
            return HttpResponse("Uh OH, Invalid Info!!", content_type="text/plain")

        tmp_passwd = make_password(passwd, "some_salt")

        if which_trap[0].password != tmp_passwd:
            return HttpResponse("Uh OH, Invalid Info!!", content_type="text/plain")

        records = TrapRecord.objects.filter(trap=which_trap[0])

        return render(request, 'list_records.html', {'records': records})

    elif request.method == 'GET':
        form = TrapForm()
        return render(request, 'list_trap_input.html', {'form': form})
