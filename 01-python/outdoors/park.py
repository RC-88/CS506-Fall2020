import numpy as np

def draw_park():
    parks=["a city park", "a neighborhood park", "a cultural park", "a pocket park"];
    print("This is {park}.".format(park=np.random.choice(parks)));
