import time
from app.tasks import call_lead_task

LEADS = [
    {"id": "1", "phone": "+9715XXXXXXXX"},
    {"id": "2", "phone": "+9715YYYYYYYY"}
]

CALL_INTERVAL_SECONDS = 15  # SAFE pacing

def run_campaign():
    for lead in LEADS:
        call_lead_task.delay(lead["phone"], lead["id"])
        time.sleep(CALL_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_campaign()
