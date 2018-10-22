import time
import datetime
import math
import random
import colorsys

from neopixel import *

# LED strip configuration:
LED_COUNT = 16          # Number of LED pixels.
LED_PIN = 18                    # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10                    # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 30  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False              # True to invert the signal (when using NPN transistor level shift)

def clearDemLeds():
  for i in range(0, strip.numPixels(), 1):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(0.2)

def revClear():
 for i in range(strip.numPixels()-1,-1,-1):
        strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(0.2)

def lightDemLeds():
  for i in range(0, strip.numPixels(), 1):
        r = int(colors[i][0]* 255)
        g = int(colors[i][1]* 255)
        b = int(colors[i][2]* 255)
        strip.setPixelColor(i, Color(r, g, b))
        print("i: %s, r: %s, g: %s, b:%s"%(i,r, g, b))
        strip.show()
        time.sleep(0.2)

def revDemLeds():
  colors2 = [colorsys.hsv_to_rgb(1.0/strip.numPixels()*i, 1, 1) for i in range(strip.numPixels(), 0,-1)]


 # print(range(strip.numPixels(),0,-1))

  for i in range(strip.numPixels()-1, -1,-1):
        r = int(colors2[i][0]* 255)
        g = int(colors2[i][1]* 255)
        b = int(colors2[i][2]* 255)
        strip.setPixelColor(i, Color(r, g, b))
        print("i: %s,r: %s, g: %s, b:%s"%(i, r, g, b))
        strip.show()
        time.sleep(0.2)



# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
     # Intialize the library (must be called once before other functions).

    strip.begin()

    colors = [colorsys.hsv_to_rgb(1.0/strip.numPixels()*i, 1, 1) for i in range(0, strip.numPixels())]
    print(colors)

    while True:
        lightDemLeds()
        clearDemLeds()
        revDemLeds()
        revClear()
