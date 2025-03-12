"""This module contains the configuration for the Hydrological Analysis Tool."""
# Using Llama.
# from typing import Literal
# import dspy as dspy

# lm = dspy.LM(
#     "ollama_chat/llama3.2:1b", api_base="http://localhost:11434/api/chat", api_key=""
# )
# dspy.configure(lm=lm)

#Using Groq.
import os
from typing import Literal
import dspy
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("groq_api_key")

lm = dspy.LM(
    "llama-3.2-1b-preview",
    api_base="https://api.groq.com/openai/v1/",
    api_key= groq_api_key
)
dspy.configure(lm=lm)


class Analysis(dspy.Signature):
    """Create a hydrological analysis from the input data."""

    context: str = dspy.InputField(
        default="You are a geologist. Based on the provided groundwater level, criticality, and location, generate a short but insightful assessment. Mention potential risks, causes of water scarcity, and suggest 1-2 mitigation measures. Limit your response to 2 concise sentences.",
        desc="Context to be used for the analysis",
    )
    location: str = dspy.InputField(desc="Location for analysis")
    groundwater_level: str = dspy.InputField(desc="Groundwater level at the location")
    criticality: Literal["Low", "Moderate", "High"] = dspy.InputField(
        desc="Criticality based on groundwater level"
    )
    recommendations: str = dspy.OutputField(
        desc="Recommendations considering urbanization and water demand"
    )
    potential_risks: str = dspy.OutputField(
        desc="Potential risks considering urbanization and water demand"
    )
    causes_of_water_scarcity: str = dspy.OutputField(
        desc="Causes of water scarcity considering urbanization and water demand"
    )
    mitigation_measures: str = dspy.OutputField(
        desc="Mitigation measures considering urbanization and water demand"
    )
