# Free Deployment

This Flask app is ready for a free Render web service.

## Render

1. Push this folder to a GitHub repository.
2. In Render, create a new **Web Service** from that repository.
3. Use these settings:
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Instance type: Free
4. Add these environment variables in Render:
   - `MAIL_SERVER=smtp.gmail.com`
   - `MAIL_PORT=587`
   - `MAIL_USE_TLS=true`
   - `MAIL_USERNAME=your Gmail address`
   - `MAIL_PASSWORD=your Gmail app password`
   - `MAIL_DEFAULT_SENDER=your Gmail address`
   - `CONTACT_RECIPIENT=the email address that should receive contact form messages`

Do not put the Gmail app password directly in `app.py` or commit it to GitHub.

## PythonAnywhere

PythonAnywhere also has a free beginner account for one Flask web app. Upload this project, install dependencies with:

```bash
pip install -r requirements.txt
```

Then configure the WSGI file to import the Flask app:

```python
from app import app as application
```

PythonAnywhere free accounts have restricted outbound internet access, so Gmail SMTP may not work there on the free plan.
