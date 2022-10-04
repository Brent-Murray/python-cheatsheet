# Anaconda Environments
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Creating Environments will allow users to run sets of code related to each environment without having issue with versions and dependencies.

### How to Create An Empty Anaconda Environment

To create a new Anaconda Environment in the run `conda env create -n env_name`. This will create an Anaconda Environment with no packages installed. *If you would like to run a specific version of Python in you environment run `conda env create -n env_name python=<version number>`.*

### How to Install Packages to an Anaconda Environment

Once you have an environment created you can then add packages to it by running `conda install -n env_name <package name>` in the Anaconda Prompt. Similarly to installing a specific Python version you can install specific versions of packages as well by running `conda install -n env_name <package name>=<version number>`.

*Replace 'env_name' with the name of the environment you want to create*

*If a new library or an update is required it is important to export a YAML or Text file as to have a backup in case the new package or update breaks the dependencies.*

## Cloning Environments
There are three ways to clone environments: creating a Direct Clone; using YAML files or using Text files.

### Creating a Direct Clone
To create a direct clone of an environment on your machine in Anaconda Prompt run `conda create --name myclone --clone myenv`. This creates a new virtual environment on the machine with the same packages and dependencies as the original environment. A benefit to this method is that there are no files being used to create the environment. The downside of this methods is that it must be on the same machine.

*Replace 'myclone' and 'myenv' to the appropriate names of the environment you wish to create and clone respectively.*

### Using YAML Files
To create a clone of a Virtual Environment activate the environment in the Anaconda Prompt and then run `conda env export > environment.yml`. This creates a file in the current directory with all of the information to create a clone.

*Replace 'environment.yml' to the name of the yml file you would like create.*

To create the clone, in a new session of Anaconda Prompt run `conda env create -f environment.yml`. This will create a clone with the same name stored in the YAML file. A benefit to this method is that you can create a clone on a completely separate machine.

*Replace 'environment.yml' to match the newly created yml file.*

### Using Text Files
Very similar to creating an environment with a YAML file, creating an environment with a text file requires you to create an text file with the packages and dependencies. To do this, in Anaconda Prompt run `conda list --explicit > environment.txt`.

*Replace 'environment.txt' to the name of the text file you would like to create.*

To create the clone, in a new session of Anaconda Prompt run `conda create --name myenv --file environment.txt`. This allows you to create a new environment with a user defined name which is beneficial when the user has many environments already created. You are also able to use this method to create a clone on a completely separate machine.

*Replace 'myenv' and 'environment.txt' to the name of the new environment you wish to create and the environment packages text file you just created respectively.*

*Once a clone of an environment has been created one can update and install new packages to this newly created environment. If something were to break between the dependencies there will still be a back up of the original environment saved.*

## Restoring Environments
Errors occur and sometimes we need to restore our environments to a previous state. Anaconda stores a history of the changes that were made to the environment. This allows us to restore our environments to a previous version. To list the history of each change within the current environment run `conda list --revision`. We can then restore our environment to one of these previous versions by running `conda install --revision=REVNUM`.

*Replace REVNUM with the appropriate revision number.*
