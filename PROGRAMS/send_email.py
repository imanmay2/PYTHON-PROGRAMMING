
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('manmaychakarborty@gmail.com','1@3$5^7*')
server.sendmail('manmaycoder@gmail.com','manmaychakarborty@gmail.com','hello')
