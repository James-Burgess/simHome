#!/usr/bin/python 

import RPi.GPIO as GPIO
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9,GPIO.OUT)

    if (GPIO.input(9) == 0):
      GPIO.output(9,GPIO.HIGH)

    else:
      GPIO.output(9,GPIO.LOW)