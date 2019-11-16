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

## Maintaining the Textbook
If you are in charge of maintaining and updating the textbook, the next section details the steps you need. 
### One-time Setup
Only follow these steps the first time you set up your computer to maintain the textbook. 
1. Create a local copy of this repo with 
```
cd desireddirectory #where you want the local copy to be stored
git clone https://github.com/stat88/textbook.git
```
Maintence of the textbook requires installing Docker, as Docker containers will allow you to view changes to the textbook on your local machine before they are visible to the public. If there are any issues with the Docker program, see [this tutorial](https://jupyterbook.org/guide/publish/book-html.html#Docker)

2. Follow the instructions for installing [Docker](https://hub.docker.com/search/?type=edition&offering=community) containers for your specific operating system (Mac, Windows, etc)

3. Once Docker has been installed, open a terminal and type
```
docker pull emdupre/jupyter-book
```
4. Next we want to set up the command that will be used whenever the textbook is updated. 

	a. Find the full path to the local copy of the textbook repo (i.e. it should not contain `./` or `../`. The easiest way to do this is to `cd` into your local copy of the repo and then type `pwd`. Save this path in a place you can find later (e.g. the notes app)
	
	b. In the same place you saved the full path, copy this command:
	```
	docker run --rm --security-opt label:disable  \
   		-v /full/path/to/your/book:/srv/jekyll \
   		-p 4000:4000 \
   		-it -u 1000:1000 \
   		emdupre/jupyter-book
	```
	And replace the `full/path/to/your/book` with the full path you found earlier. For example, mine looks like:
	```
	docker run --rm --security-opt label:disable  \
   		-v /Users/franciemcquarrie/Documents/stat88_fa19/textbook:/srv/jekyll \
   		-p 4000:4000 \
   		-it -u 1000:1000 \
   		emdupre/jupyter-book bundle exec jekyll serve --host 0.0.0.0
	```
	c. Keep track of this command so you can access it whenever you update the textbook. 
	
### Updating the textbook
This section details the process that undertaken everytime the textbook needs to be updated (whether it's a new section or a typo update)

1. `cd` into your local copy of the textbook repo
2. `git pull` to collect any updates that had been pushed to the remote copy by other collaborators
3.  If applicable, add your new chapter/section notebooks to the appropriate `content/notebooks` directory. 
4.  If a new section was added, update your `toc.yml` file
	- The tutorial has a script for autoupdating this, but when I attempted the script, it overwrote the "Home", and "Search" sections, so this is not ideal
		- If you do want to use this path, `cd` into the directory _above_ the textbook repo and run
		```
		jupyter-book toc textbook
		```
	- **Easiest and preferred** solution: Manually add the new section titles and urls to the `toc.yml` file. See file and comments at the top for examples of structure and syntax for this file. 
5.  Re-build your book. This needs to be done whether you've added a new section or simply fixed a typo. `cd` into into the directory _above_ the textbook repo and run
	```
	jupyter-book build textbook
	```
6. You'll want to preview your changes locally before publishing the changes to everyone, which can be done with the Docker container you set up earlier. 

	a. Find the docker command you saved from item 3 in the previous section, and copy and paste the command into your terminal (Since the command is multi-line, I've found it easiest to copy the command from where it's saved in my notes app and paste it into the terminal all at once. 
	
	b. Hit enter. 
	
	c. This command instructs Docker to open the container that hosts a local version of the textbook. This command may take up to 15 seconds to run. 
	
	d. When the terminal output displays the line
	```
	Jekyll Feed: Generating feed for posts
                    done in 16.819 seconds.
	```
	Then you're ready to view a local copy of the textbook. 
	
	e. Look for the line 
	```
	Server address: http://0.0.0.0:4000/textbook/
	```
	Copy the resulting http address and paste it into your browser window. 
	
	f. Review the changes made to the textbook to make sure they were implemented correctly. E.g., make sure typos were fixed, or if a new section was added, make sure all of the `#NO CODE` cells are hidden. 
	
	g. Once the changes have been previewed and approved, close the Docker instance by `ctrl-c`
	
7. Commit and push changes to github
	```
	cd path-to-textbook
	git add .
	git commit -m "updating textbook"
	git push
	```
	
## Miscellaneous Notes
1. If you want to hide conents of a cell, but display the output of a cell (for example, hiding the code that generated a graph, but displaying the resulting graph), then you need to edit the meta-data of the cell.
	a. In your jupyter notebook of the section, go to the header and click `View` -> `Cell Toolbar` -> `Edit Metadata`. Each cell should have a button in the upper right hand corner to edit that cells meta data. 
	
	b. In any cell that is marked with `#NO CODE` (e.g. want to hide code), replace the meta data with
	```
	{
  	 "tags": [
    	   "remove_input"
          ],
          "trusted": true
        }
	```
