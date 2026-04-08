from fastapi import FastAPI
from backend.schemas import GenerateRequest, PipelineResponse
from backend.pipeline import run_pipeline

app = FastAPI()


@app.post("/generate", response_model=PipelineResponse)
def generate(req: GenerateRequest):

    initial, review, refined = run_pipeline(req.grade, req.topic)

    return {
        "initial_output": initial,
        "review": review,
        "refined_output": refined
    }