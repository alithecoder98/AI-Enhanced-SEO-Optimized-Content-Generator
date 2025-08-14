from crewai import Agent

def create_conclusion_agent():
    return Agent(
        name="Conclusion Agent",
        role="Conclusion and CTA writer",
        goal="Summarize the content and include a persuasive call to action.",
        backstory="You're an expert at writing strong conclusions that reinforce the topic and drive reader engagement or conversions.",
        tools=[],
        verbose=True
    )
