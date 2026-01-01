import asyncio
from app.celery_app import celery
from app.dialer import dial_number

@celery.task
def call_lead_task(phone: str, lead_id: str):
    asyncio.run(dial_number(phone, lead_id))
