"""

This script can be used to store errors for a scheduled script which you wouldn't normally get the chance to see.
A txt file, 'errorLog', will be created (if it doesn't already exist) in the same folder as this script.

Requirements: copy 'errorLogger.py' into the same folder as your main scripts and modify your script
to include the code blow:


from errorLogger import LogTheError
import os

try:
    your code here
except Exception as e:
    LogTheError(e, os.path.basename(__file__))


"""

import traceback
import smtplib
from email.mime.text import MIMEText
from datetime import datetime


#  The 'exception' variable isn't used here, it will be used by your script.
def LogTheError(exception, scriptName):
    with open("errorLog.txt", "a") as file:  # the 'a' means that anything new will be added to the end of the text
        file.write(f"Exception occurred on, {datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}, in scipt: {scriptName}:\n")
        # file.write(str(exception) + "\n")
        # file.write("Traceback:\n")
        file.write(traceback.format_exc() + "\n\n")

    # E-mail Variables:
    fromEmail = 'test@gmail.com'  # Email sender
    toEmail = ['person1@gmail.com, person2@gmail.com']
    smtpServer = 'email.server.com'  # SMTP Server Name
    smtpPort = 00000  # SMTP Server port

    SUBJECT = f'Error Log - {scriptName}'
    TEXT = f"An Error has occured.  \nPlease check the latest error in: 'FILE PATH OF ERROR LOG HERE'"

    msg = MIMEText(TEXT)
    msg['Subject'] = SUBJECT
    msg['From'] = fromEmail
    msg['To'] = ", ".join(toEmail)

    with smtplib.SMTP(smtpServer, smtpPort) as smtp:
        smtp.send_message(msg)
    print("Successfully sent email")

