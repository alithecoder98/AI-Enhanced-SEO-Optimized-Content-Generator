from crewai import Agent

def create_intro_writer_agent():
    return Agent(
        name="Intro Writer Agent",
        role="Engaging introduction crafter",
        goal="Write compelling introductions based on the topic and SEO outline.",
        backstory="You are a copywriter who specializes in hooking readers in the first paragraph with a compelling and informative intro.",
        tools=[],
        verbose=True
    )
