# IgG versus Fab neutralization

Quantitative analysis by [Jesse Bloom](https://jbloomlab.org/) of virus neutralization by IgG versus Fab antibody forms accounting for IgG avidity and the possibility of ligand depletion for potent antibodies.

The `marimo` notebook [notebook.py](notebook.py) contains a detailed description of the model.
The `conda` environment for running this notebook is in [environment.yml](environment.yml).

To export the notebook to a standalone HTML notebook file run:

    marimo export html notebook.py -o notebook.html

This will create the HTML rendering of the notebook [notebook.html](notebook.html) as well as the standalone interactive chart [chart.html](chart.html) created by the notebook.
It also creates plots of model-simulated and real RSV F neutralization data in [simulated_vs_actual_curves.pdf](simulated_vs_actual_curves.pdf) and [simulated_vs_actual_curves.svg](simulated_vs_actual_curves.svg).

To view the notebook and interactive chart directly, go to the GitHub Pages rendering at [https://jbloomlab.github.io/IgG-vs-Fab-neutralization](https://jbloomlab.github.io/IgG-vs-Fab-neutralization).

The file [actual_RSV-F_data.csv](actual_RSV-F_data.csv) has some actual data for RSV F that is plotted by the notebook.

## Fonts
The [fonts](fonts/) directory contains font files used for plotting:

- **Comic Neue** (`ComicNeue-Regular.ttf`, `ComicNeue-Bold.ttf`): Used for the simulated data panels which are rendered in matplotlib's xkcd (hand-drawn) style. Comic Neue is a more legible alternative to Humor Sans that properly supports the minus sign glyph.
- **Open Sans** (`OpenSans-Regular.ttf`, `OpenSans-SemiBold.ttf`, `OpenSans-Bold.ttf`): Used for the actual data panels. Open Sans provides semibold weight support for intermediate emphasis between regular and bold text.

These fonts are registered at runtime by the notebook and do not require system-wide installation.
