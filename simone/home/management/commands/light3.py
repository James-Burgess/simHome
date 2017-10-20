#!/usr/bin/python 

import RPi.GPIO as GPIO
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)

    if (GPIO.input(27) == 0):
      GPIO.output(27,GPIO.HIGH)

    else:
      GPIO.output(27,GPIO.LOW)