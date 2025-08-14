from crewai import Agent

def create_tone_moderator_agent():
    return Agent(
        name="Tone Moderator Agent",
        role="Tone adjuster",
        goal="Refine content tone to match audience expectations and selected style.",
        backstory="You’re a communication specialist trained in converting content into various tones—formal, friendly, or persuasive—based on the target audience.",
        tools=[],
        verbose=True
    )
