# IgG versus Fab neutralization

Quantitative analysis by [Jesse Bloom](https://jbloomlab.org/) of virus neutralization by IgG versus Fab antibody forms accounting for IgG avidity and the possibility of ligand depletion for potent antibodies.

The `marimo` notebook [notebook.py](notebook.py) contains a detailed description of the model.
The `conda` environment for running this notebook is in [environment.yml](environment.yml).

To export the notebook to a standalone HTML notebook file run:

    marimo export html notebook.py -o notebook.html

This will create the HTML rendering of the notebook [notebook.html](notebook.html) as well as the standalone interactive chart [chart.html](chart.html) created by the notebook. Note you need `marimo`, `pandas`, and `altair` to be installed.

To view these directly, go to the GitHub Pages rendering at [https://jbloomlab.github.io/IgG-vs-Fab-neutralization](https://jbloomlab.github.io/IgG-vs-Fab-neutralization).

The file [actual_RSV-F_data.csv](actual_RSV-F_data.csv) has some actual data for RSV F that is plotted by the notebook.
