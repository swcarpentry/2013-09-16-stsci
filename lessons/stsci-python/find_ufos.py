'''

This script searches for UFOs

'''

def grab_ufo_shapes( filename  ):

    contents = open( filename ).readlines()

    all_shapes = set()

    for line in contents[1:]:
        line = line.split()

        all_shapes.add( line[4] )


    return all_shapes

shapes = grab_ufo_shapes( )
