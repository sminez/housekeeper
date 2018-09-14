# Housekeeper

A custom Alexa skill for managing day to day family information. A lot of this
will likely end up be specific to me so YMMV.

`interaction_model.json` _should_ be the latest interaction model build in the
Alexa dev portal. Don't count on this being correct, but use it for quick
reference!


### Intent ideas
- [ ] Send an email with our availabilty for the next month
  - Also for any time interval
  - Might also want details of the events before/after available windows.
- [x] Check if we are free on a given date.
  - "Ask house keeper if we are free tomorrow/next Thursday'
  - "Ask house keeper if we are free on the 23rd of October'
  -- This will probably require the use of arrow for converting human time
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
- [ ] Email the shopping list
- [ ] Add a predefined set of tasks to todoist
  - Packing for going on holiday
  - Katie being ill
  - Morning routine for the girls
- [ ] Read out all tasks in a given project
  - "What is left to do on 'morning routine'"
- [ ] Check when I can come home today based on toggl hours
  - "Assuming [name] has been recording everything correctly in toggle, they can
  finish at [time] today"


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


### AWS Lambda
The zip file created using build-zip.sh needs to be uploaded to AWS Lambda and
the alexa skill needs to be registered as a trigger (this involved adding the
relative ARNs to the skill and the lambda in order to authenticate them with one
another)


### Alexa dev portal
Management of the skill itself if done in the amazon developer portal, _not_ in
the AWS dashbaord! You will need to open the "Test" tab and enable beta testing
for your skill, this will allow you to use it on any Alexa device registered
under the same email address as the one you are using for the developer portal
account.
