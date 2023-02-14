from django.shortcuts import render, redirect
#import Jetson.GPIO as GPIO

# set the GPIO pin for the LED
LED_GPIO = 18

# initialize the GPIOs
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_GPIO, GPIO.OUT)

# Create your views here.
def led_on(request):
    #GPIO.output(LED_GPIO, GPIO.HIGH)
    return redirect('led')

def led_off(request):
    #GPIO.output(LED_GPIO, GPIO.LOW)
    return redirect('led')

def led(request):
    return render(request, 'led.html')

# clean up the GPIOs when the server shuts down
#def cleanup():
    #GPIO.cleanup()

#import atexit
#atexit.register(cleanup)
