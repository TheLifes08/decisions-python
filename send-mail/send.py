import os
import smtplib
import sys
from configparser import ConfigParser

def send_email(emails):
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, 'mail.ini')

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config file mail.ini not found!")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")
    subject = cfg.get("smtp", "subject")
    body_text = cfg.get("smtp", "body_text")
    username = cfg.get("smtp", "username")
    password = cfg.get("smtp", "password")
    
    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % ', '.join(emails),
        "Subject: %s" % subject ,
        "",
        body_text
    ))

    print("Sending emails, please wait...")
    server = smtplib.SMTP_SSL(host, 465)
    server.login(username, password)
    server.sendmail(from_addr, emails, BODY)
    print("Finish!")
    server.quit()
 
print("*** SendMail by Rodion Kolovanov ***")
print("Starting...")
emails = []
file = open("maillist.txt", 'r')

num = 0

for line in file:
    newline = ''
    num = num + 1
    if(line[-1] == '\n'):
        newline = line[0:-1]
    else:
        newline = line
    emails.append(newline)

stringinfo = "Found " + str(num) + " emails from maillist.txt"

print(stringinfo)

send_email(emails)
sys.exit(0)