# Trim anime face

## Requirements

- Python 3
- OpenCV 2

## Usage

```
python trim.py *.png -o out/
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
