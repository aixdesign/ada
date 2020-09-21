# ada
Autonomous Dialogue Agent for AIxDesign community on Slack


## Requirements
- Bot User OAuth Access Token
- Google API service account key (json)

Once you have received the tokens and files above, please keep it private! Do not share or commit to repo!
Suggestions: 
- add `SLACK_TOKEN` to your environment variables. 
- if you did not rename the account key file given to you, it should be ignored in `.gitignore`. Otherwise, make sure this file is ignored before committing code to repo! Add filename to `GOOGLE_KEY` variable at the top of `main.py`.