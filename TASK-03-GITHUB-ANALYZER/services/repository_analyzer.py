
from pydantic import BaseModel, Field
from typing import List


class Technology(BaseModel):
    name: str
    category: str
    evidence: str


class ArchitectureAnalysis(BaseModel):
    architecture_style: str
    code_organization: str
    important_observations: List[str] = Field(
        default_factory=list
    )


class Recommendation(BaseModel):
    title: str
    problem: str
    suggested_solution: str
    priority: str
    evidence: str


class ContributionOpportunity(BaseModel):
    area: str
    opportunity: str
    rationale: str


class RepositoryAnalysis(BaseModel):

    executive_summary: str

    technologies: List[Technology] = Field(
        default_factory=list
    )

    strengths: List[str] = Field(
        default_factory=list
    )

    architecture: ArchitectureAnalysis

    recommendations: List[Recommendation] = Field(
        min_length=3
    )

    contribution_opportunities: List[
        ContributionOpportunity
    ] = Field(default_factory=list)

    analysis_limitations: List[str] = Field(
        default_factory=list
    )
