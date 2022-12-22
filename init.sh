#/bin/bash

source ./.env

# if args == -r 

if [ "$1" == "-r" ]; then
    echo "Removing virtual environment"
    rm -rf $VENV_PATH
fi

# create venv if not exists
VENV_PATH=$VENV_PATH
if [ ! -d $VENV_PATH ]; then
    python3 -m venv $VENV_PATH
    echo "Created virtual environment in $VENV_PATH"
    # check if requirements.txt exists
    if [ -f requirements.txt ]; then
        $VENV_PATH/bin/pip install -r requirements.txt
        echo "Installed requirements"
    fi
fi

