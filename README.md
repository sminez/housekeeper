# Housekeeper

A custom Alexa skill for the A-Ms


### SSML
Alexa uses Speach Synthesis Markup Language to allow you to give expression to
the way your responses are said. Details here:
    https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html


### Building and deploying
The official AWS docs on deploying a zipped archive to lambda are found here:
    https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

This has been scripted as part of `build-zip.sh` so running that will create a
new archive.

NOTE:
  - zip archives are gitignored
  - secrets.py is gitignored and will need to be present in the `src` directory
  in order for everything to work.


### Lambda
The lambda function can be found here:
    https://eu-west-1.console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/house-keeper?newFunction=true&tab=graph


### Alexa dev portal
Management of the skill itself if done here:
    https://developer.amazon.com/alexa/console/ask/build/custom/amzn1.ask.skill.923c4841-d79c-4f8d-b511-5d8334e8b63e/development/en_GB/invocation

Note that the user account is under sminez@gmail.com
