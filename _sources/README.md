# Setting Up Github Pages using Jupyter Book

## Jupyter Book vs Jekyll for Github Pages

Both will generate static site for you, which means you can write your pages in markdown and they will built your html pages based on the layout settings.

(+) Native support for jupyter notebook file (ipynb). While you can put your `ipynb` file to Jekyll (see the example from my page [here](https://azukacchi.github.io/portfolio/purchasing%20intention.html)), it needs to be converted to html first before Jekyll converts it to another html with the predetermined layout settings.

(+) Easier to install since you only need to install `jupyter-book` and `ghp-import` packages in your python environment. Less headache for Windows users since you don't need to install Ruby and/or Linux distribution.

(-) No customized template available for Jupyter Book. Jekyll has plenty of themes (check them [here](https://jekyllthemes.io/)).

If you still wish to build Github Pages using Jekyll, check [my tutorial](https://github.com/azukacchi/azukacchi.github.io) and [my page](https://azukacchi.github.io/).

## Live Version

Check the live version of my Jupyter Book [here](https://azukacchi.github.io/notebooks/).

## Jupyter Book Tutorials

### Assumptions

You are already familiar with:

- git
- command line

### Steps

The official tutorial from Jupyter Book covers pretty much all of the required steps. I added some notes based on my experience:

1. Install Jupyter Book

    Starts from [this page](https://jupyterbook.org/start/your-first-book.html). Make a new environment, solely for making jupyter book and install the package there. I recommend to use Python 3.7.

    ```However, there is a known incompatibility for notebook execution when using Python 3.8.```

2. Tweak Some Files

    Follow the instructions from the beginning until the "Add it to your Table of Contents" part in ["Create your own content file" page](https://jupyterbook.org/start/new-file.html). I repeatedly encountered build failure which coming from Github Actions trying to build the references section in the later step. Remove `references.bib` and comment out the line where it includes references in `_config.yml` file. Proceed to the next steps, starting from "Re-build your book".

3. Prepare `gh-pages` branch

    When you finally get to "Publish your book online with GitHub Pages" part, you will need to setup `gh-pages` branch (step 2). By now, your jupyter book is already available in your repository but not yet deployed as a page. Open your repository in browser (i.e. `https://github.com/azukacchi/notebooks`) then create a branch called `gh-pages`, which will contain all files as your `main` branch. You should have two branches (`main` and `gh-pages`) in your repository. Finish the remaining steps.

    Note that you don't need to make changes to the `gh-pages` branch, only the `main` branch. Any changes made to the `main` branch will be applied by `ghp-import` package by overwriting all files in `gh-pages`. The `gh-pages` is solely used as the source for your Github Pages.

### Notes

When you want to update your book, you should always make your changes to the `main` branch:

```
git add ./*
git commit -m "update xxyyzz"
git push
```

Then rebuild your book, i.e. for my `notebooks` repository:

```
jupyter-book build notebooks/
ghp-import -n -p -f notebooks/_build/html
```
