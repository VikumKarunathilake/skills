"""
Better Comments - Python Reference Demonstration
Illustrates production comment conventions in Python.
"""

import time
import hmac
import hashlib
from typing import Dict, Any, Optional

class PaymentWebhookProcessor:
    def __init__(self, signing_secret: str):
        # ! Security Invariant: Signing secret must never be logged or echoed in exceptions
        if not signing_secret or len(signing_secret) < 32:
            raise ValueError("Signing secret must be at least 32 characters long.")
        self._secret = signing_secret.encode('utf-8')

    def process_incoming_payload(self, raw_body: bytes, signature_header: str) -> Dict[str, Any]:
        # ! CRITICAL: Constant-time comparison is mandatory to prevent timing attacks
        expected_sig = hmac.new(self._secret, raw_body, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected_sig, signature_header):
            raise PermissionError("Webhook signature mismatch: potential forgery attempt.")

        # * JSON parsing occurs only AFTER cryptographic integrity check passes
        import json
        event = json.loads(raw_body.decode('utf-8'))

        # ? Question: Should we acknowledge the HTTP 200 immediately and process asynchronous
        # ? jobs via Celery, or execute idempotent updates inline?
        event_type = event.get("type")
        
        # TODO: Add idempotency deduplication check against Postgres webhook_events table
        if event_type == "payment.succeeded":
            return self._handle_success(event)

        # HACK: Upstream payment gateway sends 'charge.refund' instead of 'charge.refunded' in sandbox
        if event_type in ("charge.refunded", "charge.refund"):
            return self._handle_refund(event)

        # NOTE: Unhandled events are logged as warnings rather than failing to prevent webhook retries
        return {"status": "ignored", "event": event_type}

    def _handle_success(self, event: Dict[str, Any]) -> Dict[str, Any]:
        # * Credit user wallet account and dispatch fulfillment notification
        return {"status": "completed", "event_id": event.get("id")}

    def _handle_refund(self, event: Dict[str, Any]) -> Dict[str, Any]:
        # ! Warning: Reversing wallet balance can lead to negative balance if funds were already withdrawn
        return {"status": "refund_queued", "event_id": event.get("id")}
