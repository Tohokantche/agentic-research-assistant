from  src.research_crew.crew import ResearchCrewAgents

def test_all_agent_initialization():
    crew=ResearchCrewAgents()
    assert crew.researcher() is not None
    assert crew.analyst() is not None
    assert crew.writer() is not None

def test_all_tasks_initializable():
    crew=ResearchCrewAgents()
    assert crew.research_task() is not None
    assert crew.analysis_task() is not None
    assert crew.writing_task() is not None

def test_researcher_has_tool():
    crew =ResearchCrewAgents()
    researcher = crew.researcher()
    assert len(researcher.tools) >= 2, "Researcher agent should have at least two tools"
    assert any("ScrapeWebsiteTool" in str(tool.__class__) for tool in researcher.tools)
    assert any("SerperDevTool" in str(tool.__class__) for tool in researcher.tools)


def test_crew_creation():
    crew_instance = ResearchCrewAgents()
    crew=crew_instance.crew()
    assert crew is not None
    assert len(crew.tasks)==3, "Crew should exactly have 3 tasks"
    assert len(crew.agents)==3, "Crew should exactly have 3 agents"
