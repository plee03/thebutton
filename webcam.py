#!/usr/bin/env python
import sys
from SimpleCV import Image, Camera

def main(argv):
    cam = Camera()
    img = cam.getImage()
    img.save("img.jpg")
    


if __name__ == "__main__": main(sys.argv)
