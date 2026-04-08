from pydantic import BaseModel
from typing import List, Optional

class GenerateRequest(BaseModel):
    grade: int
    topic: str


class MCQ(BaseModel):
    question: str
    options: List[str]
    answer: str


class GeneratorOutput(BaseModel):
    explanation: str
    mcqs: List[MCQ]


class ReviewerOutput(BaseModel):
    status: str
    reasoning:str
    feedback: List[str]


class PipelineResponse(BaseModel):
    initial_output: GeneratorOutput
    review: ReviewerOutput
    refined_output: Optional[GeneratorOutput]