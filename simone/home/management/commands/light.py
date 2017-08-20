#!/usr/bin/python 

import RPi.GPIO as GPIO
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.OUT)

    if (GPIO.input(4) == 0):
      GPIO.output(4,GPIO.HIGH)

    else:
      GPIO.output(4,GPIO.LOW)







