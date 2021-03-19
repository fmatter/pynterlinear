# pynterlinear

## Install
You will need a working python (3) installation.
Then install with `pip install pynterlinear`.
To grab the development version from gitlab, use `python -m pip install git+https://gitlab.com/florianmatter/pynterlinear.git`.

## What it does
The main functionality of `pynterlinear` is generating nicely formatted interlinear text, a frequently used notation in the linguistic literature.
I originally wrote it for my personal LaTeX setup, but it has grown in functionality.
You can use it in your own python scripts, just take a look at the `__init__.py` and `csv2latex.py` files.

## Commands
Pynterlinear also provides two command-line hooks which take CSV files as their input.
These CSV files need to be structured as in the following example:

|Example_ID|Language_ID|Sentence                            |Segmentation                      |Gloss                                       |Translation                       |Source                |
|----------|-----------|------------------------------------|----------------------------------|--------------------------------------------|----------------------------------|----------------------|
|unu-1     |unua1237   |arres soxa tuen                     |ares soxa tue-n                   |person one brother-3SG                      |someone's brother                 |pearce2015grammar[140]|
|unu-2     |unua1237   |Vin nge i-rav-i dabangon ngo imrebe?|βin ŋe i-ɾav-i dabaŋo-n ŋo i-mɾebe|woman PROX 3SG-take-TR belly-3SG DEM 3SG-how|How did this woman get that belly?|pearce2015grammar[249]|
|…|…|…|…|…|…|…|

### `csv2word`

- arguments:
  - A csv file containing examples
  - A list of Example_IDs from the csv file. If none are specified, all will be printed.
	
- options:
  - `-f`, `--file`:  A text file containing a linebreak-separated list of Example_IDs. IDs on the same line separated by a space will be printed as a multi-part example.
  - `-t`, `--tabs`: Use tabs instead of tables.
  
### `csv2latex`


You can also use `pynterlinear` in your own python scripts.