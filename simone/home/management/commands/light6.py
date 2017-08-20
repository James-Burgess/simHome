#!/usr/bin/python 

import RPi.GPIO as GPIO
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)

    if (GPIO.input(22) == 0):
      GPIO.output(22,GPIO.HIGH)

    else:
      GPIO.output(22,GPIO.LOW)