<img src="vapor_logo_bg.png" alt="vapor logo in front of a wildfire data visualization" width="100%"/>

# VAPOR Python Cookbook

[![nightly-build](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml)
[![DOI](https://zenodo.org/badge/656355302.svg)](https://zenodo.org/badge/latestdoi/656355302)

This Project Pythia Cookbook provides an overview of the VAPOR Python API with example workflows. 

## Motivation

The Visualization and Analysis Platform for Ocean, Atmosphere, and Solar Researchers (VAPOR) provides an interactive 3D visualization environment for exploratory visual analysis and the production of captivating animations and high-quality images. VAPOR runs on most UNIX and Windows systems equipped with modern 3D graphics cards. 

## Authors

[Nihanth W. Cherukuru](https://github.com/NihanthCW), [Stanislaw 'Stas' Jarosynski](https://github.com/StasJ), [Philip Austin](https://github.com/phaustin)

### Contributors

<a href="https://github.com/NCAR/VAPOR/graphs/contributors">
  <img src="https://github.com/StasJ.png" width="8%" style="border-radius: 50%" />
  <img src="https://github.com/sgpearse.png" width="8%" style="border-radius: 50%" />
  <img src="https://github.com/shaomeng.png" width="8%" style="border-radius: 50%" />
  <img src="https://github.com/clyne.png" width="8%" style="border-radius: 50%" />
  <img src="https://github.com/NihanthCW.png" width="8%" style="border-radius: 50%" />
</a>

## Structure

This cookbook is broken up into two main sections - "Foundations" and "Example Workflows". It is not necessary to go through these sections sequentially. Start with "Example Workflows" if you'd like to see VAPOR in action and get a broad overview of a workflow or start with "Foundations" if you'd like to explore the functionality/options in detail.

### VAPOR Foundations

The foundation section gives a quick overview of the major components of VAPOR python. These include the funcationality to load/read data, set camera parameters, annotations, save animations and images, implementing renderes for data visualization.   

Additionally, the links below can serve as a helpful reference.

::::{grid}
:gutter: 3

:::{grid-item-card} [Discussion Forum](https://vapor.discourse.group)
Discussion forum for VAPOR.
:::

:::{grid-item-card} [Python API Reference](https://ncar.github.io/VaporDocumentationWebsite/pythonAPIReference/classReference.html)
Use this to delve deeper into the python classes
:::

:::{grid-item-card} [VAPOR GUI](https://ncar.github.io/VaporDocumentationWebsite/vaporApplicationReference/quickStartGuide.html)
GUI version provides a graphical interface for VAPOR
:::

::::

### Example Workflows

The example workflows section provides examples showing and end-end pipeline for analysis and visualization using VAPOR python.

## Running the Notebooks

These notebooks cannot be run on Binder at the moment and need to be run on your machine.

### Running on Your Machine

If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the `https://github.com/ProjectPythia/vapor-python-cookbook` repository:

   ```bash
    git clone https://github.com/ProjectPythia/vapor-python-cookbook.git
   ```

1. Move into the `vapor-python-cookbook` directory
   ```bash
   cd vapor-python-cookbook
   ```
1. Create and activate your conda environment from the `environment.yml` file
   ```bash
   conda env create -f vapor_environment.yml
   conda activate vapor-cookbook-dev
   ```
1. Move into the `notebooks` directory and start up Jupyterlab
   ```bash
   cd notebooks/
   jupyter lab
   ```
At this point, you can interact with the notebooks! Make sure to check out the “[Getting Started with Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html)” content from the [Pythia Foundations](https://foundations.projectpythia.org/landing-page.html) material if you are new to Jupyter or need a refresher.