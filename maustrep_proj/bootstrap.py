from django.db.utils import DatabaseError
from maustrep.models import Trap

if __name__ == '__main__':

    # create root trap if it doesnt exist.
    trap = Trap.objects.filter(descriptor="root")
    if not trap:
        trap = Trap()
        trap.descriptor = "root"
        trap.set_password("S3xG0Dx01")

        try:
            trap.save()
        except DatabaseError as e:
            print e
            print "Error bootstraping!"