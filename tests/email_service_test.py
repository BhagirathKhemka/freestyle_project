import os
from unittest.mock import patch
from app.email_service import send_mail_with_mailgun
from dotenv import load_dotenv
load_dotenv()

with patch("requests.post") as mock_post:
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.raise_for_status.return_value = None

    recipient = "test@example.com"
    subject = "Test Subject"
    html_content = "<p>Test Content</p>"

    status_code = send_mail_with_mailgun(
        recipient_address=recipient, 
        subject=subject, 
        html_content=html_content
    )

    assert status_code == 200

    mock_post.assert_called_once_with(
        f"https://api.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages",  
        auth=('api', os.getenv('MAILGUN_API_KEY')),  
        data={
            'from': os.getenv('MAILGUN_SENDER_ADDRESS'),  
            'to': recipient,
            'subject': subject,
            'html': html_content,
        }
    )
