from fastapi import FastAPI
from app.adaptive_engine import get_next_question, update_difficulty
from app.ai_plan import generate_study_plan
app = FastAPI()

current_difficulty = 0.5


@app.get("/")
def home():
    return {"message": "Adaptive Testing Engine Running"}


@app.get("/next-question")
def next_question():

    global current_difficulty

    question = get_next_question(current_difficulty)

    if question:
        question["_id"] = str(question["_id"])
        return question

    return {"message": "No question found"}


@app.post("/submit-answer")
def submit_answer(correct: bool):

    global current_difficulty

    current_difficulty = update_difficulty(current_difficulty, correct)

    return {
        "new_difficulty": current_difficulty
    }
@app.post("/study-plan")
def study_plan(weak_topics: list[str]):

    plan = generate_study_plan(weak_topics)

    return {
        "study_plan": plan
    }