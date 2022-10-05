# Python Best Practices
## Project Structuring
    my_project             # Root directory of the project
    ├── code               # Source codes
    ├── input              # Input files
    ├── output             # Output files
    ├── config             # Configuration files
    ├── notebooks          # Project related Jupyter notebooks (for experimental code)
    ├── requirements.txt   # List of external package which are project dependency
    └── README.txt         # Project README


### Folder Contents
The names of the folders are fairly straight forward, the `code` folder contains the different modules (.py) related to the project. The `input` and `output` folders contain the input and output files. The `config` folder contains the associated parameter files such as `yaml`, or `json` files and the `notebook` folder contains the Jupyter Notebook files.

The `requirements.txt` contains a list of all the external python packages needed for the project. This makes it easy to install these dependencies on a different system or to rerun the project. The `README.txt` contains the what, why and how of the project as well as some examples on how to run the project with sample use cases.


## Code Formating
### Module Structure
Modules are the python files (.py) containing the executable code, functions, classes, etc. At the top of the each module there is generally a module definition that describes what the module does, who create the module and when it was created. The module definition follows this template:

    """Short Discription

    Long Description
    
    Author: Name and Email 
    
    Created: Date

    """

After the module description we need to clearly segregate the parts of the module including: imports, functions, global variables, run time. Each of these parts should be segmented by comment lines.

### Function Structure
Functions are the basics blocks of code that will perform specific tasks. Generally modules consist of several functions to complete a project outcome. To inform the user what a function does we start the function with a definition following this template:

    """
    Description

    Parameters:
    parameter_1: data type
        parameter_1 description
    parameter_2: data type
        parameter_2 description
        
    Returns:
    output_1: data type
        output_1 description
    output_2: data type
        output_2 description
    """

After relevant code lines are added to the function making sure to separate blocks of codes with comments and commenting what different lines of code do.

### Naming Convention
Every one has there own formating for naming conventions and is generally quite subjective. Below are some recommendations to follow.

- **Module Name:** Modules should have short, all-lowercase names (`my_python_module.py`).

- **Function Name:** Functions should be lowercase with words separated by underscores. Adding verbs is recommended (`perform_python_function()`).

- **Variable Name:** Variables are similar to functions but without verbs (`python_variable`).

- **Constant Name:** Constants or Global Variables are usually defined on a module level and are written in all capital letters with underscores separating words (`PYTHON_CONSTANT`).

### Commenting
There are three different types of comments: Block Comments, Inline Comments, and Documentation Strings. Make use of each of these forms of commenting to help future you and future users understand your code.

- **Block Comments:** These are used to separate sections of code lines to explain what each section does. These are done above the different sections of code.

- **Inline Comments:** These are added at the end of a line of code. These describe what is happing in the specific line of code. These are particularly important for complex lines of code.

- **Documentation Strings:** These are used to document modules and functions. It is recommended to use """ at the beginning and end of a docstring to have multi-line comments.

## Documentation
Documentation is a must when creating different modules. This is usually found within the README.txt file associated with every module. Luckily for us if we follow the recommendations above most of the work is done for us. We can use the docstrings found within the module and function definitions to help us build the base of the documentation.

## Virtual Environments
Virtual environments are very useful when building different modules for different projects. This can be kept in the config folder as well as within the requirements.txt file. These environments have their own dependency trees and package version that are specific to this project. 


```python

```
