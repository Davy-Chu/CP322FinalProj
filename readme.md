PROJECT DESCRIPTION
Through parameter optimization and class selection, this project optimizes both mBERT and XLM-RoBERTa models to effectively classify sentiment of German, Spanish, and French training data. We further enhanced the effectiveness of our model by training it on all language data in our dataset, and then evaluating it on the test dataset of one language

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
data -> location of dataset, all data files are located here, there are 3 subfolders that will have
        all csv's(train, test, val) related to that language.

results -> contains results from the classification report for all models tested.

src -> Contains subfolders for each model that was tested, these subfolders contain the notebook
       files for each experiment conducted in this project.

readme.md -> README file

requirements.txt -> required installations