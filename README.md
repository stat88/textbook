# Stat 88 Textbook

This textbook was built with [Jupyter Books](https://jupyterbook.org/en/stable/intro.html). The textbook was originally built by Francie McQuarrie. Shahzar updated the textbook to the new Jupyter Books framework.

## Structure

Only three files/directories need to be edited.
- `_config.yml`: Configuration information about the textbook. Modify this file for things like:
    - changing the logo or favicon;
    - adding or removing launch buttons;
    - changing information about the book.
- `_toc.yml`: Table of contents for the textbook. Modify this file for things like:
    - section and chapter numbering and order;
    - adding or removing sections or chapters.
- `content/`: Content of the textbook. All the notebooks with section and chapter content go here. Modify these files to actually change the content of the sections.

## Maintaining the Textbook
This section details how to maintain the textbook.

### One-time Setup
Follow these steps the first time you set up a computer to modify and maintain the textbook.
1. Create a local copy of this repo by running `git clone https://github.com/stat88/textbook.git` from the command line in whichever folder you want to contain the textbook.
2. Next, you need to install all the required packages. Either of the commands `pip install -r requirements.txt` or `conda install --file requirements.txt` should work. If you have a Windows device, it's preferable to run this in an Anaconda Prompt terminal. This should install the two packages `jupyter-book` and `ghp-import`, which are used for building and deploying the textbook, respectively, and a bunch of other typical packages (e.g. `numpy`, `scipy`, `matplotlib`, etc.) used by the `content/` notebooks.


### Updating the Textbook
These steps detail the process you should go through every time you update the textbook.
1. **Pull:** `cd` into `textbook/`, your local copy of the textbook repo and `git pull origin master` to collect any updates which may have been pushed to the remote copy by other collaborators.
2. **Update:** Make any changes you wish to make. This should (likely) only consist of changes to `_config.yml`, `_toc.yml`, and the files in `content/`.
    - If you added new sections or chapters, update `_toc.yml` as well to reflect your changes.
3. **Build:** `cd` into the directory above `textbook/` (i.e. `cd ..`) and run `jupyter-book build textbook`.
4. **Check:** Open the file `textbook/_build/html/index.html` in your browser to view what the textbook will look like with any changes you've made. Make sure nothing is broken and the changes are as you want them. 
    - See the [Troubleshooting](#troubleshooting) section for any issues you may be having.
    - Take a look at the [Issues](#issues) for problematic parts of the textbook.
5. **Deploy:** `cd` back into `textbook/` (`cd textbook/`) and run `ghp-import -n -p -f _build/html` (the `-n` flag is important, since it adds a `.nojekyll` file which allows GitHub to build the website correctly). This will push the `_build/html` folder to the `gh-pages` branch of the textbook repository, which is configured by GitHub Pages to hold the files for the textbook website. To edit these configurations, from the repository page, go to Settings > Pages.
6. **Push:**  Stage any changes you made (i.e. using `git add [file]`, `git add -u`, `git add .`, etc.), commit your changes with `git commit -m "[description]"` (please include a useful description of any changes you made), and push to the master repository with `git push origin master`.

## Notes
### Troubleshooting
The (Jupyter Book)(https://jupyterbook.org/en/stable/intro.html) website has lots of information about Jupyter Book. Some useful pages are:
- [Anatomy of a Jupyter Book](https://jupyterbook.org/en/stable/start/create.html#anatomy-of-a-jupyter-book)
- [Table of Contents](https://jupyterbook.org/en/stable/structure/configure.html)
- [Configuration Reference](https://jupyterbook.org/en/stable/customize/config.html)
- [References and Cross-References](https://jupyterbook.org/en/stable/content/references.html)
- [Building](https://jupyterbook.org/en/stable/start/build.html)
- [Deploying](https://jupyterbook.org/en/stable/publish/gh-pages.html)

If changes you've made aren't showing up the HTML after building, sometimes deleting `_build` and then building again helps. Jupyter Book will usually only re-build the HTML of notebooks that it thinks have been changed by any edits made, and so this sometimes means that some changes will go unnoticed. Deleting the entire folder and rebuilding forces it to build from scratch, which prevents any old files or code from sticking around. **However, please see the third item in [Issues](#issues)** and make sure you manually add the appropriate files to `_build/html/_images` when you do this.

### Links
Links to the internet should be done as they are usually done in Markdown. However, to cross-link to other pages of the textbook, there is an internal linking system that should be used instead (since it is robust to file structure changes in `/textbook`). This system is described [here](https://jupyterbook.org/en/stable/content/references.html#reference-section-labels).

For example, Section 12.4 Exercise 3 contains a link to Section 12.2. 
1. The flag `(ch12.2)=` was added *before* the primary header of the notebook.
```
(ch12.2)=
## The Distribution of the Estimated Slope ##
```
2. The link to Section 12.2 was changed to `(ch12.2)`.
```
**3.** 
Refer to the regression of active pulse rate on resting pulse rate in [Section 12.2](ch12.2). Here are the estimated values again, along with some additional data.
```

Ideally, every section and subsection should have a flag before the header or subheader. As of July 16, 2022, the only sections/subsections with flags are ones that are linked to by other sections:
- Section 6.2 (linked to by Section 7.1.3),
- Section 5.4 (linked to by Section 7.4 Exercise 4),
- Section 5.4.7 (linked to by Section 11.2),
- Section 12.2 (linked to by Section 12.4 Exercise 3).
Someone should go through the textbook at some point and add flags to all section and subsection headers to make cross-linking easier.

### Datasets
For ease of tracking, the sections that load in a dataset from `data` are enumerated:
- Section 9.4 loads in `baby.csv`;
- Section 12.2 loads in `pulse.csv`;
- Section 12.3 loads in `hodgkins.csv`;
- Section 12.4 loads in `pulse.csv`.

### Issues
The following is a list of somewhat specific cases of weird behavior throughout the textbook.
1. The subheaders **Arranging in a Line** and **Choosing Subsets** in `Chapter_03/00_Random_Counts.ipynb` are done using HTML (i.e. `<h3> ... </h3>`) instead of Markdown (`### ... `), since using Markdown makes Jupyter Book label them as Section 13.1 and 13.2 in the textbook (which results in the *actual* Section 13.1 being displayed as Section 13.3 in the sidebar).
2. The subheader **IID Trials** in `Chapter_04/00_Infinitely_Many_Values.ipynb` are done using HTML for the same reasons as the files in the above bullet point.
3. Section 11.1's visual of four different bias/variance cases is done in HTML instead of Markdown so that the images can be displayed in a table format. This is why the `html_image` option is enabled under `myst_enable_extensions` in `_config.yml`. More importantly, when building the textbook, the images `content/images/bias_lvar.png`, `content/images/lbias_lvar.png`, `content/images/ubias_hvar.png`, and `content/images/ubias_lvar.png` **are not** automatically moved to the `_build/html/_images` folder. If those images are deleted in that folder and the textbook is rebuilt, **they must manually be copied from `content/images/` to `_build/html/_images`**.