import numpy as np

def draw_library():
    libraries=["a national library", "a public library", "an university library"];
    print("This is {library}.".format(library=np.random.choice(libraries)));
