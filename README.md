# Graph signal processing tutorials using the [pyGSP]

[![Binder](https://mybinder.org/badge.svg)][binder_lab]
&nbsp; (Jupyter [lab][binder_lab] or [notebook][binder_notebook])

Presented at the [graphSIP] summer school by [Michaël Defferrard](http://deff.ch) and [Nicolas Tremblay](http://www.gipsa-lab.fr/~nicolas.tremblay).

[pygsp]: https://github.com/epfl-lts2/pygsp
[graphsip]: https://graphsip.sciencesconf.org

We suggest you follow the [installation guide](#installation) to setup your own
computer.

## Content

The material covers the following topics:
* representation of graphs and signals
* some standard graph models (e.g. Erdos-Renyi, Barabasi-Albert)
* graph construction (e.g. from point clouds)
* graph operators: Laplacian and difference
* smoothness of graph signals
* graph Fourier basis: eigenvectors and spectrum
* applications: spectral clustering, Laplacian eigenmap
* graph Fourier transform
* filtering by convolution in Fourier
* some standard filters & filterbanks
* fast filtering with polynomial approximations
* application: denoising with low-pass filtering as the solution to an optimization problem (maybe EEG / fMRI data), curvature estimation with wavelets (point cloud / shape)
* convex optimization on graph
* application: semi-supervized learning with Thikonov / TV prior

Optional / advanced:
* deep learning on graphs, i.e. learning graph filters
  * application: semantic segmentation of point clouds
* spectrum estimation by filtering random signals
  * application: spectral clustering, Laplacian eigenmap
* stationarity

## Installation

For a local installation, you will need [git], [Jupyter], and packages from the
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
   `git clone https://github.com/mdeff/pygsp_tutorial_graphsip`.
1. Create an environment with `conda create --name pygsp_tutorial_graphsip`. 
   (you can also do this by launching Anaconda Navigator --> Environments --> Create)
1. Activate the environment with `conda activate pygsp_tutorial_graphsip`
   (or `activate pygsp_tutorial_graphsip`, or `source activate pygsp_tutorial_graphsip`).
1. Within this environment, run `conda install Jupyter numpy scipy matplotlib` and `pip install pygsp`.

Every time you want to work, do the following:

1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Activate the environment with `conda activate pygsp_tutorial_graphsip`
   (or `activate pygsp_tutorial_graphsip`, or `source activate pygsp_tutorial_graphsip`).
1. Start Jupyter with `jupyter notebook` or `jupyter lab`. The command should
   open a new tab in your web browser.
1. Edit and run the notebooks from your browser.

You can try to run the Jupyter notebook 'mini_test.ipynb' to make sure that the main 
4 toolboxes are at least callable. 

[git]: https://git-scm.com
[Jupyter]: https://jupyter.org/
[scipy]: https://www.scipy.org
[anaconda]: https://anaconda.org
[miniconda]: https://conda.io/miniconda.html
[conda]: https://conda.io
[conda-forge]: https://conda-forge.org

## License

The content is released under the terms of the [MIT License](LICENSE.txt).
