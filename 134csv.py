import csv
import os
import argparse
import sys

parseru = argparse.ArgumentParser("Some Input to split the csv")
parseru.add_argument('CSV File Input', metavar='i', type=argparse.FileType('r'), default=sys.stdin,
                     help='Input .csv filename')
parseru.add_argument('CSV File Output', metavar='o', type=argparse.FileType('w'), default=sys.stdout,
                     help='Output .csv filename')
parseru.add_argument('Number to split output', metavar='r', type=int, help='Number to Split the file')
arguser = parseru.parse_args()


def valargi():
    try:
        if arguser.i == "*.csv":
            print("Good")
        else:
        print("Try again your i argument")
    except ArgumentError:
        print("Invalis -i input try again")
        break


def valargo():
    try:
        if arguser.o == "*.csv":
            print("Good")
        else:
            print("Try again your o argument")
    except ArgumentError:
        print("Invalis -o input try again")
        break


def valargw():
    try:
        if arguser.r == int:
            print("Good")
        else:
            print("Try again your w argument")
    except ArgumentError:
        print("Invalis -w input try again")
        break
