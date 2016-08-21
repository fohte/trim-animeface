import os
import urllib.request

import cv2


class FaceDetector(object):

    def __init__(self, cascade_file):
        f = _get_filepath(cascade_file)
        self.cascade = cv2.CascadeClassifier(f)

    def detect(self, filename, size=(24, 24)):
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        faces = self.cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=size)

        for (x, y, w, h) in faces:
            yield image[y:y + h, x:x + w]


def _get_filepath(f):
    if _is_url(f):
        return _download_file(f)

    elif os.path.isfile(f):
        return f

    else:
        raise FileNotFoundError(f)


def _is_url(path):
    return ':' in path


def _download_file(url):
    return urllib.request.urlretrieve(url)[0]
