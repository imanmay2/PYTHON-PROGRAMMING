
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('manmaychakarborty@gmail.com','')
server.sendmail('manmaycoder@gmail.com','manmaychakarborty@gmail.com','hello')
