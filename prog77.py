# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("harshithaigglur@gmail.com", "harshi123")
 
# message to be sent
message = "hello"
 
# sending the mail
s.sendmail("harshithaigglur@gmail.com", "harshithaigglur@gmail.com", message)
 
# terminating the session
s.quit()
"print" 
