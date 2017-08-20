#!/usr/bin/python 

import RPi.GPIO as GPIO
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(10,GPIO.OUT)

    if (GPIO.input(10) == 0):
      GPIO.output(10,GPIO.HIGH)

    else:
      GPIO.output(10,GPIO.LOW)