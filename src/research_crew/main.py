#!/usr/bin/env python
import warnings
from datetime import datetime
from src.research_crew.crew import ResearchCrewAgents
from pathlib import Path
from typing import Dict
import asyncio

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run(inputs=None):
    """
    Run the crew.
    """
    if not inputs:
        inputs = {
            'topic': 'Leading open source AI agent frameworks',
            'current_year': str(datetime.now().year)
        }
    
    try:
        crew = ResearchCrewAgents().crew()
        return crew, crew.kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train(train_param : Dict = None):
    """
    Train the crew for a given number of iterations.
    """
    if not train_param:
        train_param =  {"n_iterations": int(3),
                        "filename" : Path("./train_data.pkl"), 
                        "inputs": { "topic": "AI LLMs"}
                        }   
    try:
        crew = ResearchCrewAgents().crew()
        return crew, crew.train(**train_param)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay(replay_param : Dict = None):
    """
    Replay the crew execution from a specific task.
    """
    if not replay_param:
        replay_param =  {
            "task_id": int(3),
            }  
    try:
        crew = ResearchCrewAgents().crew()
        return crew, crew.replay(**replay_param)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test(test_param : Dict = None):
    """
    Test the crew execution and returns the results.
    """
    if not test_param:
        test_param =  {
                        "n_iterations": int(3),
                        "openai_model_name" : Path("./train_data.pkl"), 
                        "inputs": {
                                    "topic": "AI LLMs",
                                    "current_year": str(datetime.now().year)
                                }
                        } 
    try:
        crew = ResearchCrewAgents().crew()
        return crew, crew.test(**test_param)
    
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
    

