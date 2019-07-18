import smtplib
from email.message import EmailMessage

email_content = '''Dear Sir/Madam,

I am sending you an e-mail with Python. I hope you like it.

Kind regards,
Kate
'''

email = EmailMessage()
email['subject'] = 'Test email'
email['From'] = 'katuhis@yandex.ru'
email['To'] = 'katuhis82@gmail.com'

email.set_content(email_content)


smtp_connector = smtplib.SMTP(host='smtp.yandex.ru', port=587)
smtp_connector.starttls()
smtp_connector.login('katuhis@yandex.ru', 'MadeInGermany1995-2011')

smtp_connector.send_message(email)
smtp_connector.quit()
