import numpy as np

def draw_school():
    schools=["an elementary school", "a middle school", "a high school"];
    print("This is {school}.".format(school=np.random.choice(schools)));
