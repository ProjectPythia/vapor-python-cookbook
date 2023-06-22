<img src="vapor_logo_bg.png" alt="vapor logo in front of a wildfire data visualization" width="100%"/>

# VAPOR Python Cookbook

[![nightly-build](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml)

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

(Add content for this section, e.g., "The foundational content includes ... ")

### Example Workflows

(Add content for this section, e.g., "Example workflows include ... ")

## Running the Notebooks

```{note}
VAPOR requires a GPU ... !
```

### Running on Your Own Machine

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