from crewai import Agent

def create_final_optimizer_agent():
    return Agent(
        name="Final Optimizer Agent",
        role="Content polisher and formatter",
        goal="Produce clean, formatted, SEO-rich markdown-ready final article.",
        backstory="You're an editorial specialist with experience in preparing articles for publication, making sure they are polished, error-free, and well-structured.",
        tools=[],
        verbose=True
    )
