import pytest
from smtp_mailhog_testing import mail_client


@pytest.fixture
def url():
    return "mailserver.ornl.gov"


def test_send_email(url):
    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"
    message = "Test"

    mail_client.send_mail(sender_email, receiver_email, message, url=url)

    
