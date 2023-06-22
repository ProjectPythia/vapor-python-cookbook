<img src="vaporLogoBlack.png" alt="thumbnail" width="300"/>

# VAPOR Python Cookbook

[![nightly-build](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml)

This Project Pythia Cookbook covers ... (replace `...` with the main subject of your cookbook ... e.g., _working with radar data in Python_)

## Motivation

(Add a few sentences stating why this cookbook will be useful. What skills will you, "the chef", gain once you have reached the end of the cookbook?)

## Authors

[Nihanth W. Cherukuru](https://github.com/NihanthCW), [Stanislaw 'Stas' Jarosynski](https://github.com/StasJ), [Philip Austin](https://github.com/phaustin)

### Contributors

<a href="https://github.com/ProjectPythia/cookbook-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ProjectPythia/cookbook-template" />
</a>

## Structure

(State one or more sections that will comprise the notebook. E.g., _This cookbook is broken up into two main sections - "Foundations" and "Example Workflows."_ Then, describe each section below.)

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

(Replace "cookbook-example" with the title of your cookbooks)

1. Clone the `https://github.com/ProjectPythia/cookbook-example` repository:

   ```bash
    git clone https://github.com/ProjectPythia/cookbook-example.git
   ```

1. Move into the `cookbook-example` directory
   ```bash
   cd cookbook-example
   ```
1. Create and activate your conda environment from the `environment.yml` file
   ```bash
   conda env create -f environment.yml
   conda activate cookbook-example
   ```
1. Move into the `notebooks` directory and start up Jupyterlab
   ```bash
   cd notebooks/
   jupyter lab
   ```
