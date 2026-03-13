from app.database import questions_collection


def get_next_question(current_difficulty):

    question = questions_collection.find_one(
        {"difficulty": {"$gte": current_difficulty}},
        sort=[("difficulty", 1)]
    )

    return question


def update_difficulty(current_difficulty, correct):

    if correct:
        new_difficulty = min(current_difficulty + 0.1, 1.0)
    else:
        new_difficulty = max(current_difficulty - 0.1, 0.1)

    return new_difficulty