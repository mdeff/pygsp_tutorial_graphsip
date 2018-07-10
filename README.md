# Graph signal processing tutorials using the [pyGSP]

[![Binder](https://mybinder.org/badge.svg)][binder_lab]
&nbsp; (Jupyter [lab][binder_lab] or [notebook][binder_notebook])

Presented at the [graphSIP] summer school by [Michaël Defferrard](http://deff.ch) and [Nicolas Tremblay](http://www.gipsa-lab.fr/~nicolas.tremblay).

[pygsp]: https://github.com/epfl-lts2/pygsp
[graphsip]: https://graphsip.sciencesconf.org

You can either follow the [installation guide](#installation) to setup your own
computer, or work in the cloud using [binder][binder_lab].

[binder_lab]: https://mybinder.org/v2/gh/mdeff/pygsp_tutorials_graphsip/master?urlpath=lab
[binder_notebook]: https://mybinder.org/v2/gh/mdeff/pygsp_tutorials_graphsip/master?urlpath=tree

## Installation

Click the [binder badge][binder_lab] to play with the notebooks from your
browser without installing anything.

For a local installation, you will need [git], [Python], and packages from the
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
   `git clone https://github.com/mdeff/pygsp_tutorials_graphsip`.
1. Create an environment with the packages required for the course with
   `conda env create -f pygsp_tutorials_graphsip/environment.yml`.

Every time you want to work, do the following:

1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Activate the environment with `conda activate pygsp_tutorials_graphsip`
   (or `activate pygsp_tutorials_graphsip`, or `source activate pygsp_tutorials_graphsip`).
1. Start Jupyter with `jupyter notebook` or `jupyter lab`. The command should
   open a new tab in your web browser.
1. Edit and run the notebooks from your browser.

[git]: https://git-scm.com
[python]: https://www.python.org
[scipy]: https://www.scipy.org
[anaconda]: https://anaconda.org
[miniconda]: https://conda.io/miniconda.html
[conda]: https://conda.io
[conda-forge]: https://conda-forge.org

## License

The content is released under the terms of the [MIT License](LICENSE.txt).
