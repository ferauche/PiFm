#!/usr/bin/python

from subprocess import call


def play_sound( filename ):
   call(["./pifm", filename, "100.3"])
   return
