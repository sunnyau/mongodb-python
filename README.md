# mongodb-python

## Download and install miniconda 3

https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

Open Anaconda Prompt to run `conda` command

## VS Code setup for python extension

https://www.youtube.com/watch?v=D2cwvpJSBX4&t=400s

Go to VS Code -> Extension -> Python Microsoft ( This is a python extension for formatting etc ) 

```
(base) C:\Users\sunny\workspace\mongodb-python>conda create --name mongodb_env
Channels:
 - defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
    current version: 25.1.1
    latest version: 25.3.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\sunny\miniconda3\envs\mongodb_env



Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate mongodb_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) C:\Users\sunny\workspace\mongodb-python>conda activate mongodb_env

(mongodb_env) C:\Users\sunny\workspace\mongodb-python>
```

## How to run Anaconda prompt in VS Code?

https://code.visualstudio.com/docs/python/environments

To activate the Anaconda environment in VSCode, you need to select it as your Python interpreter. Open the Command Palette ( Ctrl+Shift+P ), type Python: Select Interpreter , and hit Enter. A list of available interpreters will appear. Select the one that corresponds to your Anaconda environment.

### install pymongo in conda prompt

C:\Users\sunny\workspace\mongodb-python>conda install pymongo

## pymongo

https://pymongo.readthedocs.io/en/stable/tutorial.html

## run python

