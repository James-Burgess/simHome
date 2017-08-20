#!/usr/bin/python 

import RPi.GPIO as GPIO
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)

    if (GPIO.input(17) == 0):
      GPIO.output(17,GPIO.HIGH)

    else:
      GPIO.output(17,GPIO.LOW)