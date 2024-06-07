//README.md
# Categories Reformating

## Description
This project is a simple example of how to reformat a list of categories in a way that it can be used in a tree structure.

categories_reformating/
    categories_reformater.py
    reformatted_files/
    to_reformat/

The `categories_reformater.py` script reads a file with a list of categories and reformat it in a way that it can be used in a tree structure. The script reads the selected file in the `to_reformat/` dir and writes the reformatted version in the directory `reformatted_files/`.

## How to run
1. Clone this repository
2. run the command: 
    `mkdir to_reformat`
    to create the directory where the file with the categories will be stored
3. Add the file you want to reformat in the directory `to_reformat`
1. Run the script `categories_reformater.py`
2. Follow the instructions in console (choose the file you want to reformat and the number of elements in each category)
3. Check the reformatted categories in the file `reformatted_files/reformatted_categories.md`

Voila!