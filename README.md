# pynterlinear

This is a python package which provides several functionalities for handling glossed interlinear text.
It provides three main functions.

## `convert_to_expex`
This function takes a dictionary as an argument and returns a LaTeX 
The dictionary has the following required keys:
* `id`
* `obj`
* `gloss`
* `trans`

optional arguments:

* `language`
* `surface`
* `source`

if `for_beamer` is true, then a key `glottocode` is also required.