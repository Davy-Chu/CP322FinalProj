PROJECT DESCRIPTION
I guess we can copy paste the description from the writeup when we make it

SETUP INSTRUCTIONS(Windows)
1. Before cloning open terminal into the directory and make sure to have conda installed https://www.anaconda.com/download/success Miniconda x64 is good enough for this project. ^Follow instructions on site for installation

2. After cloning, create a conda venv and activate it using:

conda create -n mbertproj python=3.11 -y
conda active mbertproj

3. Install dependencies using: pip install -r requirements.txt

After that you should be able to run the project on your local machine.

NOTE: There may be ipynbkernel issues with the .ipynb files, if you encounter them you may have to run: 

python -m ipykernel install --name mbertproj --display-name "Python (mbertproj)"

and then switch to the newly made kernel by clicking on:

Current kernel(top right of .ipynb)->Existing python environments-> mbertproj(Python 3.11.14)

FILE STRUCTURE
So far everything is in the base folder, with all the code being written in test.ipynb and datasets being in the base project folder, however we should move all the files into their respective folders eventually.