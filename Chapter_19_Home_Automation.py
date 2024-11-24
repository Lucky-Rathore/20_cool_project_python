# Chapter_19_Home_Automation
# To install the required library, run:
# pip install RPi.GPIO

import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
relay_pin = 18  # Change to the appropriate pin where the relay is connected
GPIO.setup(relay_pin, GPIO.OUT)

def turn_on_device():
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Device turned ON!")

def turn_off_device():
    GPIO.output(relay_pin, GPIO.LOW)
    print("Device turned OFF!")

try:
    while True:
        command = input("Enter command (on/off/exit): ").strip().lower()
        if command == "on":
            turn_on_device()
        elif command == "off":
            turn_off_device()
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")
finally:
    GPIO.cleanup()