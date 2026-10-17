import json
import boto3
import logging
from botocore.exceptions import ClientError
# ─── Configuration ────────────────────────────────────────────────────────────
# ✅ Replace these with your verified SES email addresses
SENDER_EMAIL    = "you@yourdomain.com"       # Must be verified in SES
RECIPIENT_EMAIL = "you@yourdomain.com"       # Where you receive contact emails
AWS_REGION      = "us-east-1"               # Your SES region
# ──────────────────────────────────────────────────────────────────────────────
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ses = boto3.client("ses", region_name=AWS_REGION)
def lambda_handler(event, context):
    """
    AWS Lambda handler for contact form submissions.
    Triggered via API Gateway (POST /contact).
    """
    # Handle CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return cors_response(200, "OK")
    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return cors_response(400, {"error": "Invalid JSON body"})
    # ── Validate required fields ───────────────────────────────────────────────
    required = ["name", "email", "subject", "message"]
    missing  = [f for f in required if not body.get(f, "").strip()]
    if missing:
        return cors_response(400, {"error": f"Missing fields: {', '.join(missing)}"})
    name    = body["name"].strip()
    email   = body["email"].strip()
    subject = body["subject"].strip()
    message = body["message"].strip()
    logger.info(f"Contact form submission from {name} <{email}>")
    # ── Build email ────────────────────────────────────────────────────────────
    email_subject = f"[Contact Form] {subject}"
    email_body_text = f"""
New contact form submission:
Name:    {name}
Email:   {email}
Subject: {subject}
Message:
{message}
---
Sent via your website contact form.
""".strip()
    email_body_html = f"""
<html>
