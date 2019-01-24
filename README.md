# Graph Signal Processing tutorial using the [PyGSP]

[![Binder](https://mybinder.org/badge.svg)][binder_lab]
&nbsp; (Jupyter [lab][binder_lab] or [notebook][binder_notebook])

Presented at the [GraphSiP] summer school by [Michaël Defferrard](http://deff.ch) and [Nicolas Tremblay](http://www.gipsa-lab.fr/~nicolas.tremblay).
GraphSiP is about Graph Signal Processing with Applications to 3D Clouds of Points and Neuroscience.

[pygsp]: https://github.com/epfl-lts2/pygsp
[graphsip]: https://graphsip.sciencesconf.org

We suggest you follow the [installation guide](#installation) to setup your own computer.
If you don't succeed, you can work in the cloud using [binder][binder_lab].

[binder_lab]: https://mybinder.org/v2/gh/mdeff/pygsp_tutorial_graphsip/master?urlpath=lab
[binder_notebook]: https://mybinder.org/v2/gh/mdeff/pygsp_tutorial_graphsip/master?urlpath=tree

## Content

The material covers the following topics:
1. [Graphs: creation, models, properties, visualization][graphs]
1. [Spectral Graph Theory: spectral clustering, Laplacian eigenmaps][spectral]
1. [Graph signals: gradient, divergence, smoothness][signals]
1. [Fourier: modes, transform][fourier]
1. [Filters: filterbanks, filtering, approximations][filters]
1. [Applications to point clouds: denoising and curvature estimation][point_clouds]
1. [Applications to neuroscience: fMRI signals on brain connectome][neuroscience]

[graphs]: https://nbviewer.jupyter.org/github/mdeff/pygsp_tutorial_graphsip/blob/outputs/notebooks/01_graphs.ipynb
[spectral]: https://nbviewer.jupyter.org/github/mdeff/pygsp_tutorial_graphsip/blob/outputs/notebooks/02_spectral.ipynb
[signals]: https://nbviewer.jupyter.org/github/mdeff/pygsp_tutorial_graphsip/blob/outputs/notebooks/03_signals.ipynb
[fourier]: https://nbviewer.jupyter.org/github/mdeff/pygsp_tutorial_graphsip/blob/outputs/notebooks/04_fourier.ipynb
[filters]: https://nbviewer.jupyter.org/github/mdeff/pygsp_tutorial_graphsip/blob/outputs/notebooks/05_filters.ipynb
[point_clouds]: https://nbviewer.jupyter.org/github/mdeff/pygsp_tutorial_graphsip/blob/outputs/notebooks/06_point_clouds.ipynb
[neuroscience]: https://nbviewer.jupyter.org/github/mdeff/pygsp_tutorial_graphsip/blob/outputs/notebooks/07_neuroscience.ipynb

The content is inspired by the following resources:

* A [tutorial][ntds_tutorial] and an [assignment][ntds_assignment] from the course [A Network Tour of Data Science][ntds] taught at EPFL.
* The [tutorials from the PyGSP documentation][pygsp_tutorials].

[ntds]: https://github.com/mdeff/ntds_2017
[ntds_tutorial]: https://nbviewer.jupyter.org/github/mdeff/ntds_2017/blob/outputs/demos/08_pygsp.ipynb
[ntds_assignment]: https://nbviewer.jupyter.org/github/mdeff/ntds_2017/blob/outputs/assignments/04_solution.ipynb
[pygsp_tutorials]: https://pygsp.readthedocs.io/en/stable/tutorials

## Installation

For a local installation, you will need [git], [Python >= 3.6][python], [Jupyter], and packages from the
[Python scientific stack][scipy]. If you don't know how to install those on
your platform, we recommend to install [Miniconda], a distribution of the
[conda] package and environment manager. Please follow the below instructions
to install it and create an environment for the course.

1. Download the Python 3.x installer for Windows, macOS, or Linux from
   <https://conda.io/miniconda.html> and install with default settings. Skip
   this step if you have conda already installed (from [Miniconda] or
   [Anaconda]). Linux users may prefer to use their package manager.
   * Windows: Double-click on the `.exe` file.
   * macOS: Run `bash Miniconda3-latest-MacOSX-x86_64.sh` in your terminal.
   * Linux: Run `bash Miniconda3-latest-Linux-x86_64.sh` in your terminal.
1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Install git with `conda install git`.
1. Download this repository by running
   `git clone https://github.com/mdeff/pygsp_tutorial_graphsip` or by pressing the green "Clone or download" button on the top of this page.
1. Create an environment with `conda create --name pygsp_tutorial_graphsip`.
   (you can also do this by launching Anaconda Navigator --> Environments --> Create)
1. Activate the environment with `conda activate pygsp_tutorial_graphsip`
   (or `activate pygsp_tutorial_graphsip`, or `source activate pygsp_tutorial_graphsip`).
1. Within this environment, run `conda install jupyter numpy scipy matplotlib networkx scikit-learn` and `pip install pygsp`.

Every time you want to work, do the following:

1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Activate the environment with `conda activate pygsp_tutorial_graphsip`
   (or `activate pygsp_tutorial_graphsip`, or `source activate pygsp_tutorial_graphsip`).
1. Start Jupyter with `jupyter notebook` or `jupyter lab`. The command should
   open a new tab in your web browser.
1. Edit and run the notebooks from your browser.

You can try to run the Jupyter notebook `mini_test.ipynb` to make sure that the main toolboxes are at least callable.

[git]: https://git-scm.com
[python]: https://www.python.org
[jupyter]: https://jupyter.org/
[scipy]: https://www.scipy.org
[anaconda]: https://anaconda.org
[miniconda]: https://conda.io/miniconda.html
[conda]: https://conda.io
[conda-forge]: https://conda-forge.org

## License

The content is released under the terms of the [MIT License](LICENSE.txt).
