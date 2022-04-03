import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25) #the server(smtp.gmail.com : exp for the gamil )and the port of the smtp protocol
server.ehlo()

with open('passwd.txt', 'r') as f:
    passwd = f.read()

server.login('you email', passwd) #ur email password in the file passwd.txt

msg=MIMEMultipart()
msg['from'] = 'ur name '
msg['to'] = 'email of the target '
msg['subject'] = 'TEST MAIL CLIENT '

with open('message.txt', 'r') as f: #the content of the email in a message.txt file
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'image.jpg' #adding a photo as attachment
attachment = open(filename, 'rb') #mode rb for reading photo

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('header', f'attachment; filename={filename}')

text = msg.as_string()
server.sendmail('ur email', 'target-email', text)





