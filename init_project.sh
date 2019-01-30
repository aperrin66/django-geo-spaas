#!/bin/bash

# set project name
PROJECT_NAME=project
if [ ! -d "$PROJECT_NAME" ]; then

    # Control will enter here if $DIRECTORY doesn't exist.
    # create project dir
    django-admin startproject $PROJECT_NAME
    # copy default settings
    cp tests/*.py $PROJECT_NAME/$PROJECT_NAME/
    # migrate data to database
    python $PROJECT_NAME/manage.py migrate
    # add metadata to Vocabularies
    python $PROJECT_NAME/manage.py update_vocabularies

fi
