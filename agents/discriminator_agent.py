from crewai import Agent

def create_discriminator_agent():
    return Agent(
        name="Discriminator Agent",
        role="Content critic and validator",
        goal="Critique grammar, coherence, readability, and SEO alignment.",
        backstory="You're a senior content editor and NLP expert who evaluates content rigorously for quality, tone, and SEO-readiness.",
        tools=[],
        verbose=True
    )
