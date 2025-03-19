import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
import math
from CalcTrap import *

# Can use IMREAD flags to do different pre-processing of image files,
# like making them grayscale or reducing the size.
# https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
haystack_img = cv.imread('Haystack1.png', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('Needle.png', cv.IMREAD_UNCHANGED)
tweedle_img = cv.imread('Tweedle.png', cv.IMREAD_UNCHANGED)

# There are 6 comparison methods to choose from:
# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
# You can see the differences at a glance here:
# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
# Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
result = cv.matchTemplate(haystack_img, needle_img,  cv.TM_CCOEFF_NORMED)

# Perform template matching for tweedle
result2 = cv.matchTemplate(haystack_img, tweedle_img, cv.TM_CCOEFF_NORMED)

# You can view the result of matchTemplate() like this:
cv.imshow('Result', result)
cv.waitKey()

cv.imshow('Result', result2)
cv.waitKey()

# If you want to save this result to a file, you'll need to normalize the result array
# from 0..1 to 0..255, see:
# https://stackoverflow.com/questions/35719480/opencv-black-image-after-matchtemplate
cv.imwrite('result_CCOEFF_NORMED1.jpg', result * 255)

# Automatically get the needle image dimensions
needle_h, needle_w = needle_img.shape[:2]  # Only need the first two elements for height and width
tweedle_h, tweedle_w = tweedle_img.shape[:2]  # Only need the first two elements for height and width

#Open a file in write mode
with open('HaystackOutput1.txt', 'w') as f:
    #Get the best match position from the match result.
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    #and for tweedle
    min_val2, max_val2, min_loc2, max_loc2 = cv.minMaxLoc(result2)

    #for needle
    #Top-left corner
    top_left = max_loc

    #Top-right corner (same y, but x shifted by the width of the needle)
    top_right = (top_left[0] + needle_w, top_left[1])

    #Bottom-left corner (same x, but y shifted by the height of the needle)
    bottom_left = (top_left[0], top_left[1] + needle_h)

    #Bottom-right corner (shift x by width and y by height)
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    #for tweedle
    top_left2 = max_loc2
    top_right2 = (top_left2[0] + tweedle_w, top_left2[1])
    bottom_left2 = (top_left2[0], top_left2[1] + tweedle_h)
    bottom_right2 = (top_left2[0] + tweedle_w, top_left2[1] + tweedle_h)

    print(f"Top-left corner: {top_left}")
    print(f"Top-right corner: {top_right}")
    print(f"Bottom-left corner: {bottom_left}")
    print(f"Bottom-right corner: {bottom_right}")
    print('Best match confidence: %s' % max_val)

    f.write(f"Top-left corner: {top_left}\n")
    f.write(f"Top-right corner: {top_right}\n")
    f.write(f"Bottom-left corner: {bottom_left}\n")
    f.write(f"Bottom-right corner: {bottom_right}\n")
    f.write('Best match confidence: %s\n' % max_val)

    print(f"Top-left corner 2: {top_left2}")
    print(f"Top-right corner 2: {top_right2}")
    print(f"Bottom-left corner 2: {bottom_left2}")
    print(f"Bottom-right corner 2: {bottom_right2}")
    print('Best match confidence 2: %s' % max_val2)

    f.write(f"Top-left corner 2: {top_left2}\n")
    f.write(f"Top-right corner 2: {top_right2}\n")
    f.write(f"Bottom-left corner 2: {bottom_left2}\n")
    f.write(f"Bottom-right corner 2: {bottom_right2}\n")
    f.write('Best match confidence 2: %s\n' % max_val2)

# If the best match value is greater than 0.8, we'll trust that we found a match
threshold = 0.8
if max_val >= threshold:
    print('Found needle.')

if max_val2 >= threshold:
    print('Found tweedle.')

    # Draw a rectangle on our screenshot to highlight where we found the needle.
    # The line color can be set as an RGB tuple
    cv.rectangle(haystack_img, top_left, bottom_right,
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    cv.rectangle(haystack_img, top_left2, bottom_right2, color=(255, 0, 0), thickness=2,
                 lineType=cv.LINE_4)  # Blue for tweedle

    # You can view the processed screenshot like this:
    cv.imshow('Result', haystack_img)
    cv.waitKey()
    # Or you can save the results to a file.
    # imwrite() will smartly format our output image based on the extension we give it
    # https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce
    cv.imwrite('resultHaystack1.jpg', haystack_img)

    #plot the corner coordinates as safety measure

    #Convert to RGB (matplotlib uses RGB while OpenCV uses BGR)
    haystack_img_rgb = cv.cvtColor(haystack_img, cv.COLOR_BGR2RGB)
    needle_img_rgb = cv.cvtColor(needle_img, cv.COLOR_BGR2RGB)
    tweedle_img_rgb = cv.cvtColor(tweedle_img, cv.COLOR_BGR2RGB)

    plt.figure(1) 
    plt.imshow(haystack_img_rgb)
    plt.axis('off')
  
    corner_colors = ['red', 'green', 'blue', 'yellow']
    corner_colors2 = ['purple', 'orange', 'cyan', 'pink']

    plt.plot(top_left[0], top_left[1], 'o', color=corner_colors[0], markersize=2)
    plt.plot(top_right[0], top_right[1], 'o', color=corner_colors[1], markersize=2)
    plt.plot(bottom_left[0], bottom_left[1], 'o', color=corner_colors[2], markersize=2)
    plt.plot(bottom_right[0], bottom_right[1], 'o', color=corner_colors[3], markersize=2)

    plt.plot([top_left[0], top_right[0]], [top_left[1], top_right[1]], color='cyan', linewidth=0.5)  # Top edge
    plt.plot([top_right[0], bottom_right[0]], [top_right[1], bottom_right[1]], color='cyan', linewidth=0.5)  # Right edge
    plt.plot([bottom_right[0], bottom_left[0]], [bottom_right[1], bottom_left[1]], color='cyan', linewidth=0.5)  # Bottom edge
    plt.plot([bottom_left[0], top_left[0]], [bottom_left[1], top_left[1]], color='cyan', linewidth=0.5)  # Left edge

    plt.plot(top_left2[0], top_left2[1], 'o', color=corner_colors2[0], markersize=2)
    plt.plot(top_right2[0], top_right2[1], 'o', color=corner_colors2[1], markersize=2)
    plt.plot(bottom_left2[0], bottom_left2[1], 'o', color=corner_colors2[2], markersize=2)
    plt.plot(bottom_right2[0], bottom_right2[1], 'o', color=corner_colors2[3], markersize=2)

    plt.plot([top_left2[0], top_right2[0]], [top_left2[1], top_right2[1]], color='purple', linewidth=0.5)
    plt.plot([top_right2[0], bottom_right2[0]], [top_right2[1], bottom_right2[1]], color='purple', linewidth=0.5)
    plt.plot([bottom_right2[0], bottom_left2[0]], [bottom_right2[1], bottom_left2[1]], color='purple', linewidth=0.5)
    plt.plot([bottom_left2[0], top_left2[0]], [bottom_left2[1], top_left2[1]], color='purple', linewidth=0.5)

    plt.title('Matched Regions with Colored Corners')
    plt.savefig('HaystackColorMatched1.png')

    plt.figure(2)
    x_coords_needle = [top_left[0], top_right[0], bottom_right[0], bottom_left[0],
                        top_left[0]]  # Loop back to the first point
    y_coords_needle = [top_left[1], top_right[1], bottom_right[1], bottom_left[1], top_left[1]]

    x_coords_tweedle = [top_left2[0], top_right2[0], bottom_right2[0], bottom_left2[0],
                        top_left2[0]]  # Loop back to the first point
    y_coords_tweedle = [top_left2[1], top_right2[1], bottom_right2[1], bottom_left2[1], top_left2[1]]

    plt.plot(x_coords_needle, y_coords_needle, 'o-', color='green', label='Needle')
    plt.scatter([top_left[0], top_right[0], bottom_left[0], bottom_right[0]],
                [top_left[1], top_right[1], bottom_left[1], bottom_right[1]],
                color=corner_colors, s=100)
  
    plt.plot(x_coords_tweedle, y_coords_tweedle, 'o-', color='blue', label='Tweedle')
    plt.scatter([top_left2[0], top_right2[0], bottom_left2[0], bottom_right2[0]],
                [top_left2[1], top_right2[1], bottom_left2[1], bottom_right2[1]],
                color=corner_colors2, s=100)
  
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal', adjustable='box')

    plt.title('Needle and tweedle coordinates')
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.grid(True) 
    plt.savefig('NeedleTweedlePlot1.png', format='png', bbox_inches='tight')

    pixels_per_cm = Calculation(top_right2, top_left2, bottom_right, bottom_left)
    print("Calc was called + executed")
  
else:
    print('Needle not found.')
