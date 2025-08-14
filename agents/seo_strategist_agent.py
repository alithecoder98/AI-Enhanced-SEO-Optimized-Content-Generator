from crewai import Agent

def create_seo_strategist_agent():
    return Agent(
        name="SEO Strategist Agent",
        role="SEO and keyword optimizer",
        goal="Extract high-ranking keywords and structure content for maximum SEO impact.",
        backstory="You’re a digital marketing expert focused on making content rank using keywords, metadata, and structure.",
        tools=[],
        verbose=True
    )
