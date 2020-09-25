# FAQ

## How do I build slides?

Install the dependencies: `pip install -r assets/requirements-slides.txt`.

```py
python make.py build
```

Remember to rebuild when `slides.md` get updated.

## How do I develop and live reload?

```py
python make.py live
```

## How to host on github pages?

1. Go to settings.
2. Enable GitHub Pages.

## How to change my favicon?

Replace favicon with something else

## How to save as pdf?

1. Install decktape

```bash
npm install -g decktape
```

2. Run decktape

```bash
decktape "http://localhost:5500" slides.pdf
```
