import numpy as np

def draw_lake():
    lakes=["Lake Tahoe", "Lake Victoria", "Lake Superior", "Lake Erie"];
    print("This is {lake}.".format(lake=np.random.choice(lakes)));
