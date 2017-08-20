#!/usr/bin/python 

import RPi.GPIO as GPIO
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)

    if (GPIO.input(18) == 0):
      GPIO.output(18,GPIO.HIGH)

    else:
      GPIO.output(18,GPIO.LOW)