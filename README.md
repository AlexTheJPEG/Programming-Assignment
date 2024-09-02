# Programming Assignment

## How to run
This project uses [Poetry](https://python-poetry.org/) to manage Python dependencies. First install Poetry, then clone this repository to somewhere on your computer. Then in a terminal, run `poetry install --no-root` in the root directory (containing `pyproject.toml`), and finally run `poetry run python parse.py`.

Alternatively, simply install [Pillow](https://pillow.readthedocs.io/en/stable/) using `pip` then run `python parse.py` in the terminal.

## Results
<img src="results/com.apalon.ringtones new.png" width="200">
<img src="results/com.dropbox.android new.png" width="200">
<img src="results/com.giphy.messenger-1 new.png" width="200">
<img src="results/com.giphy.messenger-2 new.png" width="200">
<img src="results/com.google.android.apps.transalte new.png" width="200">
<img src="results/com.pandora.android new.png" width="200">
<img src="results/com.yelp.android new.png" width="200">

## Solution and notes
The program parses through every `.xml` and `.png` pair in `Programming-Assignment-Data/` and outputs its results in `results/`. For every `.xml` and `.png` pair, it finds every node that has its `clickable` property set to `"true"`, scrapes its boundary box denoted in the `bounds` property as `[x1,y1][x2,y2]`, and creates a new image that draws a yellow rectangle for every boundary box.

Instead of using an XML parser, I chose to use regular expression matching, because there is an error with `com.apalon.ringtones.xml` about a mismatched tag and I was only looking for the `clickable` and `bounds` properties anyway.

The only third-party library I used for my solution is the [Pillow](https://pillow.readthedocs.io/en/stable/) library for image creation and manipulation.