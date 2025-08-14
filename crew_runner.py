# crew_runner.py
from llm_config import llm_config
from crewai import Crew, Task
from agents import (
    create_research_agent,
    create_seo_strategist_agent,
    create_intro_writer_agent,
    create_body_writer_agent,
    create_conclusion_agent,
    create_tone_moderator_agent,
    create_discriminator_agent,
    create_final_optimizer_agent,
)
from config import settings

def run_crew(topic: str, tone: str, audience: str, word_count: int):
    print(f"\n🚀 Starting content generation for: '{topic}'\n")

    # 1) Create agents (no llm kwarg)
    agents = {
        "research":      create_research_agent(),
        "seo":           create_seo_strategist_agent(),
        "intro":         create_intro_writer_agent(),
        "body":          create_body_writer_agent(),
        "conclusion":    create_conclusion_agent(),
        "tone":          create_tone_moderator_agent(),
        "discriminator": create_discriminator_agent(),
        "finalizer":     create_final_optimizer_agent(),
    }

    # 2) Inject Gemini LLM + ensure text-only behavior
    for a in agents.values():
        a.llm = llm_config
        # hard-disable any tool usage to avoid tool-call objects
        try:
            a.tools = []
        except AttributeError:
            pass
        if hasattr(a, "function_call"):
            setattr(a, "function_call", "none")

    # 3) Define tasks
    tasks = [
        Task(
            description=f"Research the topic: '{topic}' and gather key insights.",
            expected_output="5–7 factual bullet points relevant to the topic, based on credible sources.",
            agent=agents["research"],
        ),
        Task(
            description="Use research to generate an SEO-optimized structure and keywords.",
            expected_output="List of SEO keywords, H1/H2 outline, and a suggested meta description.",
            agent=agents["seo"],
        ),
        Task(
            description="Write an engaging introduction based on the topic and SEO outline.",
            expected_output="One introductory paragraph (around 100–150 words).",
            agent=agents["intro"],
        ),
        Task(
            description="Expand on the article's main body based on the structure.",
            expected_output="2–3 well-structured paragraphs using suggested keywords.",
            agent=agents["body"],
        ),
        Task(
            description="Write a conclusion and call-to-action tailored to the target audience.",
            expected_output="One closing paragraph with persuasive CTA, aligned to the tone.",
            agent=agents["conclusion"],
        ),
        Task(
            description=f"Unify the content and rewrite it in a '{tone}' tone for '{audience}'.",
            expected_output="Full rewritten content with improved fluency, tone consistency, and engagement.",
            agent=agents["tone"],
        ),
        Task(
            description="Review the content for SEO, tone, grammar, and readability. Suggest improvements.",
            expected_output="Scored evaluation (out of 10) and specific rewrite suggestions.",
            agent=agents["discriminator"],
        ),
        Task(
            description="Incorporate improvements and finalize a polished, SEO-friendly markdown output.",
            expected_output="Final cleaned-up article with markdown formatting, optimized for publishing.",
            agent=agents["finalizer"],
        ),
    ]

    # 4) Run
    crew = Crew(agents=list(agents.values()), tasks=tasks, verbose=True)
    return crew.kickoff()
