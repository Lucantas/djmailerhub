import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, BaseLoader

def send_mail(sender, receivers, copies, password, subject, content, login, host, port, data):
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender

        # TODO: Create the plain-text and HTML version of your message   
        parsed = parse_template(content, data)
        content_body = MIMEText(parsed, "html")
        message.attach(content_body)

        with smtplib.SMTP(host, port) as server:
            server.login(login, password)
            server.sendmail(
                sender, receivers, message.as_string()
            )
            print("Done sending mail!")
    except Exception as e:
        print("Erro ao enviar email com parâmetros: {0}, [{1}], {2}, {3}".format(sender, ",".join(receivers), content, host))
        print(e)


def parse_template(content, values):
    rtemplate = Environment(loader=BaseLoader).from_string(content)
    return rtemplate.render(**values)

