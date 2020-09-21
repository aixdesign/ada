import os
import pygsheets
import random
from slack import WebClient
from datetime import datetime

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
# CHANNEL_ID = "CJ7QVGVT2"
GOOGLE_KEY = 'aixd-convo-bot-d8680aa62efb.json'

def slackBotMessage(message):
    # connect to api and create client
    sc = WebClient(token=SLACK_TOKEN)
    sc.chat_postMessage(channel='_dev_test', text=message)
    print("Message successfully sent to slack channel!")

# access db (google sheets)
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1wl7EfOAvyCYHPcmn5tp2w6LCD_5IBiysKH_aiOTMMac/edit?usp=sharing"
gc = pygsheets.authorize(service_file=GOOGLE_KEY)
sheet = gc.open_by_url(SPREADSHEET_URL).sheet1

# analyze sheet to select data area
rows = sheet.rows
cols = sheet.cols

# get questions
# questions = sheet.get_all_values(include_tailing_empty=False, include_tailing_empty_rows=False)
questions = sheet.get_all_records(head=2)

# rules for selecting question based on frequency and last post date?

# randomly select question through index number
n_questions = len(questions)
n_q = random.choice(range(0, n_questions-1))
q = questions[n_q]['Question']
print(q)

# form message to send in slack
# randomize intro for question eg. Howdy/Hello/Sup, etc. Here's a prompt for today. Feel free to answer or discuss below! :)
intro_txts = ["How's it going? Here's a prompt for today: \n",
             "Howdy! Here's something to talk about: \n"]

intro_txt = random.choice(intro_txts)

# send message in slack
msg = intro_txt + q
slackBotMessage(msg)

# update datetime for posting
date = str(datetime.now())
sheet.update_value((n_q+3, 3), date)
