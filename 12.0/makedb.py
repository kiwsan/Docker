import os
import sys

try:    
    print "\tAttempting to connect to database..."
    
    os.environ['USER']
    os.environ['HOST']
    os.environ['PORT']
    os.environ['PASSWORD']

    print "connected!"
except:
    print "failed!"

    print "done!"