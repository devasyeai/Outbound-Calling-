import asyncio
from livekit import api
from livekit.protocol.sip import CreateSIPParticipantRequest
from app.config import SIP_OUTBOUND_TRUNK_ID

lkapi = api.LiveKitAPI()

async def dial_number(phone: str, lead_id: str):
    req = CreateSIPParticipantRequest(
        sip_trunk_id=SIP_OUTBOUND_TRUNK_ID,
        sip_call_to=phone,
        room_name=f"lead-{lead_id}",
        participant_identity=f"call-{lead_id}",
        participant_name="Dubai Nurse Recruitment",
        wait_until_answered=True
    )
    await lkapi.sip.create_sip_participant(req)
