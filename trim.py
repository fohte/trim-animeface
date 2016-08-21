import argparse
import glob
import os

import cv2
import progressbar

import detector

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('input', type=str, nargs='+')
    parser.add_argument('--output-dir', '-o', type=str, default='out')
    parser.add_argument('--cascade-file', '-c', type=str,
                        default='https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml')
    parser.add_argument('--progress', '-p', action='store_true')
    parser.add_argument('--resize', '-r', type=int, default=-1)

    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    d = detector.AnimeFaceDetector(args.cascade_file)

    if len(args.input) == 1 and '*' in args.input[0]:
        files = glob.glob(args.input[0])
    else:
        files = args.input

    if args.progress:
        progress = progressbar.ProgressBar()
        files = progress(files)

    for filepath in files:
        if not os.path.exists(filepath):
            print(
                '\r\033[KWARNING: {} is not found. Skip detect.'.format(filepath))
            continue

        srcfilename, ext = os.path.splitext(os.path.basename(filepath))
        faces = d.detect(filepath, size=(args.resize, args.resize))
        for i, img in enumerate(faces):
            if args.resize >= 0:
                cv2.resize(img, (args.resize, args.resize))

            cv2.imwrite('{}/{}_{}{}'.format(output_dir,
                                            srcfilename, i, ext), img)
