# pynterlinear

## Install
You will need a working python (3) installation.
Then install with `pip install pynterlinear`.
To grab the development version from gitlab, use `python -m pip install git+https://gitlab.com/florianmatter/pynterlinear.git`.

## What it does
The main functionality of `pynterlinear` is generating nicely formatted interlinear text, a frequently used notation in the linguistic literature.
I originally wrote it for my personal LaTeX setup, but it has grown in functionality.
You can use it in your own python scripts, just take a look at the `__init__.py` and `csv2latex.py` files.
It also provides two command-line hooks which take CSV files as their input.
These CSV files need to be structured as follows:

|Example_ID|Language_ID|Sentence                            |Segmentation                      |Gloss                                       |Translation                       |Source                |
|----------|-----------|------------------------------------|----------------------------------|--------------------------------------------|----------------------------------|----------------------|
|unu-1     |unua1237   |arres soxa tuen                     |ares soxa tue-n                   |person one brother-3SG                      |someone's brother                 |pearce2015grammar[140]|
|unu-2     |unua1237   |Vin nge i-rav-i dabangon ngo imrebe?|βin ŋe i-ɾav-i dabaŋo-n ŋo i-mɾebe|woman PROX 3SG-take-TR belly-3SG DEM 3SG-how|How did this woman get that belly?|pearce2015grammar[249]|

## `csv2word`

## `csv2latex`


You can also use `pynterlinear` in your own python scripts.