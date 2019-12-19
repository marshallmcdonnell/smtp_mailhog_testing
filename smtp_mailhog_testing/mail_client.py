import argparse
import smtplib


def send_mail(sender_email, receiver_email, message, url="localhost", port=1025):
    with smtplib.SMTP(url, port) as server:
        server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="localhost")
    args = parser.parse_args()

    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    send_mail(sender_email, receiver_email, message, url=args.url)
