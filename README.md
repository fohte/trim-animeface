# Trim anime face

## Requirements

- Python 3
- OpenCV

## Usage

For example, you trim the anime face from some images with [nagadomi/lbpcascade_animeface](https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml):

```
python trim.py *.png -o out/ -c https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml
```

## Pre-commit

Require:

```
pip install isort
pip install autopep8
```

And you must format python codes before commit:

```
isort *.py -o cv2
autopep8 *.py -a --in-place
```
