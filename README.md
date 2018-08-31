# Housekeeper

A custom Alexa skill for the A-Ms

## How to use the build tool

```bash
sudo docker build -t lambda-builder .
sudo docker run -i -t -v $PWD:/code lambda-builder ./build-zip.sh project-name
```

This produces a .zip file which can be uploaded manually to lambda

## Project structure
If any other projects are created that need to use the build tool then they need
to have the following directory structure:

- project
  - src
    - myscript.py
  - requirements.txt
