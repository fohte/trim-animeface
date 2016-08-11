import argparse
import glob
import os

import cv2

import detector

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('input', type=str, nargs='+')
    parser.add_argument('--output-dir', '-o', type=str, default='out')
    parser.add_argument('--cascade-file', '-c', type=str,
                        default='https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml')

    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    d = detector.AnimeFaceDetector(args.cascade_file)

    if len(args.input) == 1 and '*' in args.input[0]:
        files = glob.iglob(args.input[0])
    else:
        files = args.input

    for filepath in files:
        if not os.path.exists(filepath):
            print('WARNING: {} is not found. Skip detect.'.format(filepath))
            continue

        srcfilename, ext = os.path.splitext(os.path.basename(filepath))
        faces = d.detect(filepath)
        for i, img in enumerate(faces):
            cv2.imwrite('{}/{}_{}{}'.format(output_dir,
                                            srcfilename, i, ext), img)
