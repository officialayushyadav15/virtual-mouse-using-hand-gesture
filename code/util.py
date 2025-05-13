import numpy as np

def get_angle(a,b,c):
    radians = np.arctan2( c[1] - b[1] , c[0] - b[0] ) - np.arctan2( a[1] - b[1] , a[0] - b[0] ) # taking the defrence between the angle created by ab and x-axis and bc and xaxis
    angle = np.abs(np.degrees(radians)) # using np.abs and nb.degrees we are converting radians into actual angle values i.e. in degrees
    return angle

def get_distance(landmark_list):
    if len(landmark_list) < 2:
        return
    
    (x1,y1),(x2,y2) = landmark_list[0], landmark_list[1]
    L = np.hypot(x2-x1,y2-y1) # calculating euclidian distance between two points using np.hypot i.e. hpotenuse 
    return np.interp(L, [0,1], [0,1000]) # since distance is small hence multiplying it by 1000