# Housekeeper

A custom Alexa skill for the A-Ms.

`interaction_model.json` _should_ be the latest interaction model build in the
Alexa dev portal. Don't count on this being correct, but use it for quick
reference!


### Intent ideas
- [ ] Send an email to Katie/Innes with our availabilty for the next month
  - Also for any time interval
  - Might also want details of the events before/after available windows.
- [ ] Check if we are free on a given date.
  - "Ask house keeper if we are free tomorrow/next Thursday'
  - "Ask house keeper if we are free on the 23rd of October'
  -- This will probably require the use of arrow/maya for converting human time
  specifications into date times.
  -- Check to see if Alexa can do this for us?
- [ ] Check todoist tasks by project name
  - This will need to first pull all project name -> ID mappings and then get
  the projects.
- [ ] Check todoist tasks by due date
  - Simple querying via the API
- [ ] Create a new todoist task
  - Default to inbox but allow specific project as well.
- [ ] Maintain the shopping list
  - Store in Todoist for easy editing: the Alexa shopping list is a pain!
- [ ] Email the shopping list to Katie/Innes
- [ ] Add a predefined set of tasks to todoist
  - Packing for going on holiday
  - Katie being ill
  - Morning routine for the girls
- [ ] Read out all tasks in a given project
  - "What is left to do on 'morning routine'"
- [ ] Check when Innes can come home today
  - Requires adding an API to STATs or assuming that toggl is correct!
  - "Assuming Innes has been recording everything correctly in toggle, he can
  finish at XXXX today"


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
