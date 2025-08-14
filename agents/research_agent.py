from crewai import Agent

def create_research_agent():
    return Agent(
        name="Research Agent",
        role="Topic researcher",
        goal="Gather accurate and up-to-date information using APIs and tools.",
        backstory="You're a specialist in deep web research and can pull the most relevant data using APIs like Tavily, Google, and scholarly sources.",
        tools=[],
        verbose=True
    )
