import math

def Calculation(top_right2, top_left2, bottom_right, bottom_left):
    print("opened script")
    A = math.dist(top_right2, top_left2)
    B = math.dist(bottom_right, top_right2)
    C = math.dist(bottom_left, bottom_right)
    D = math.dist(top_left2, bottom_left)

    print("A is:", A)
    print("B is:", B)
    print("C is:", C)
    print("D is:", D)

    h = abs(bottom_right[1]-top_right2[1])
    print("h is:", h)

    # Convert the height from pixels to centimeters
    h_pixels = h
  
    #CHANGE! according to real life distances
    h_cm = 5 #CHANGE! according to real life distances
  
    pixels_per_cm = h_pixels/h_cm


    print("height in pixels:", h_pixels)
    print("height in cm:", h_cm)
    print("pixels per cm:", pixels_per_cm)

    with open('ConversionFactor1.txt', 'a') as f:
        f.write(f"height in pixels: {h_pixels}\n")
        f.write(f"height in cm: {h_cm}\n")
        f.write(f"px/cm-scale factor: {pixels_per_cm}\n")

    with open('Height trapeze1.txt', 'a') as f:
        f.write(f"height is: {h}\n")

    return pixels_per_cm
