from crewai import Agent

def create_body_writer_agent():
    return Agent(
        name="Body Writer Agent",
        role="Main content writer",
        goal="Expand SEO outline into structured and informative sections.",
        backstory="You are a content writer skilled in expanding outlines into rich, SEO-optimized, structured sections with depth and clarity.",
        tools=[],
        verbose=True,
        
        
    )
