from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import datetime, time
import os, sys
import numpy as np
from threading import Thread
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

# instatiate flask app
app = Flask(__name__)  # , template_folder='./templates')


@app.route('/')
def hello():
    ob = refresh()
    print(ob)
    # if ob is True:
    return render_template("/index.html/")
    # else:
    #     print("bad")
    #     return render_template("/404.html")


def refresh():
    ok, frame = webcam.read()
    gaze.refresh(frame)
    return gaze_error(frame)
    # frame = gaze.annotated_frame()


def gaze_error(frame):
    # print(gaze.is_center())
    gaze.refresh(frame)
    return gaze.is_center()


@app.route('/404')
def error():
    return render_template('404.html/')


@app.route('/isValid')
def isValid():
    print("here")
    if refresh():
        print("hi")
        return '', 204
    else:
        print(123)
        return '', 302  # 302 moved


# @app.route('/error.html')
# def error():
#    return render_template('index.html')
if __name__ == "__main__":
    app.run()
