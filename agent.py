from livekit.agents import VoiceAgent

RECRUITER_PROMPT = """
You are a professional recruiter calling from Dubai.

Ask:
1. Are you interested in nursing jobs in Dubai?
2. How many years of experience do you have?
3. Do you have a DHA or equivalent license?

Be polite, professional, and brief.
"""

agent = VoiceAgent(
    instructions=RECRUITER_PROMPT,
    voice="female",
    language="en"
)

if __name__ == "__main__":
    agent.run()
