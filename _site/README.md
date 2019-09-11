# Stat 88 Textbook

This textbook was built with Jupyter Books, using the following [tutorial](https://jupyter.org/jupyter-book/guide/01_overview.html).

## Structure

Only three folders need to be edited:

- `_config.yml`: Change carefully. Only change
	- The textbook logo 
	- Presences of "Interact" or "Download" buttons
	- paths/urls if the website url ever changes
- `content`: Where all notebooks that hold section content are stored
	- For example,  `content/notebooks/Chapter_01/00_Fundamentals.ipynb` is displayed when you click on the chapter title ("intro" text for the chapter).
	- `content/notebooks/Chapter_1/01_Probabilities_as_Proportions.ipynb` is displayed when you click on the section 1.1 link. 
- `_data/toc.yml`: Table of Contents. This needs to be updated whenever a new section or chapter is added 
	- Each chapter and each section has a title (denoted by the `- title:` yml marker), and then a `url:` which is the path to the notebook you want displayed when that title is clicked on.
		- Don't list file suffixes in path (e.g. `.ipynb`, `.md`)
	- First chapter of `toc.yml` is commented with notes about what each thing is. 

## Updating the textbook

1.  Add your new chapter/section notebooks to the appropriate `content/notebooks` directory. 
2.  Update your `toc.yml` file
	- The tutorial has a script for autoupdating this, but when I attempted the script, it overwrote the "Home", and "Search" sections, so this is not ideal
		- If you do want to use this path, `cd` into the directory _above_ the textbook repo and run
		```
		jupyter-book toc textbook
		```
	- Easiest solution: Manually add the new section titles and urls to the `toc.yml` file.
3.  Re-build your book. `cd` into into the directory _above_ the textbook repo and run
	```
	jupyter-book build textbook
	```
4. Push to github
	```
	git add .
	git commit -m "updating textbook"
	git push
	```