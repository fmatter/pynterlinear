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

|<sub>Example_ID</sub>|<sub>Language_ID</sub>|<sub>Sentence</sub>                            |<sub>Segmentation</sub>                      |<sub>Gloss</sub>                                       |<sub>Translation</sub>                       |<sub>Source</sub>                |
|---------------------|----------------------|-----------------------------------------------|---------------------------------------------|-------------------------------------------------------|---------------------------------------------|---------------------------------|
|<sub>unu-1</sub>     |<sub>unua1237</sub>   |<sub>arres soxa tuen</sub>                     |<sub>ares soxa tue-n</sub>                   |<sub>person one brother-3SG</sub>                      |<sub>someone's brother</sub>                 |<sub>pearce2015grammar[140]</sub>|
|<sub>unu-2</sub>     |<sub>unua1237</sub>   |<sub>Vin nge i-rav-i dabangon ngo imrebe?</sub>|<sub>βin ŋe i-ɾav-i dabaŋo-n ŋo i-mɾebe</sub>|<sub>woman PROX 3SG-take-TR belly-3SG DEM 3SG-how</sub>|<sub>How did this woman get that belly?</sub>|<sub>pearce2015grammar[249]</sub>|
|<sub>bon-1</sub>     |<sub>bona1250</sub>   |<sub>ɕaʑə d͡ʐama=nə koʁol-t͡ɕə</sub>           |<sub>ɕaʑə d͡ʐama=nə koʁol-t͡ɕə</sub>         |<sub>child window=ACC shatter-PFV</sub>                |<sub>The child shattered the window.</sub>   |<sub>fried2010baoantu[215]</sub> |


### `csv2word`

Arguments:
  - A csv file containing examples
  - A list of Example_IDs from the csv file. If none are specified, all will be printed.
	
Options:
  - `-f`, `--file`:  A text file containing a linebreak-separated list of Example_IDs. IDs on the same line separated by a space will be printed as a multi-part example.
  - `-t`, `--tabs`: Use tabs instead of tables.

Output: A file `csv2word_export.docx` which contains the specified examples from the CSV. If such a file is already present, `csv2word` will simply append the new examples (and hopefully get the numbering right).

An example workflow could then look as follows:

1. compile a list of examples in a CSV file. This will also make it very easy to share it as a [`CLDF`](https://github.com/cldf/cldf) dataset, and to check it for consistency with [`pyIGT`](https://github.com/cldf/pyigt).
2. create a list of Example_IDs you want to use in your document, for example `examples.txt` with the following content:
```
unu-1 unu-2
bon-1
```
3. generate a `.docx` using `--file examples.txt`
4. copy-paste formatted examples into your document.

Of course, you can also add and generate examples as you go along. If you keep the `csv2word_export.docx` in place, the numbering should be correct.
You can manually change the last number in `csv2word_export.docx` and `pynterlinear` will start from there when adding more examples.
This may be useful if you e.g. have a non-interlinear numbered example in your document, or some other example you insert manually.

### `csv2latex`

…