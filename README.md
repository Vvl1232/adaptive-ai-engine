# AI-Driven Adaptive Diagnostic Engine

## Project Overview

This project implements a 1-dimensional adaptive testing prototype that dynamically adjusts question difficulty based on a student's performance.

The system starts at a baseline difficulty level and updates the next question difficulty depending on whether the student answers correctly or incorrectly.

The backend is implemented using FastAPI, and MongoDB Atlas is used to store questions and user session data.

An optional feature integrates Google Gemini API to generate a personalized study plan based on the student's weak topics.

## System Architecture

```
Client
   │
   ▼
FastAPI Backend
   │
   ├── Adaptive Algorithm
   │
   ▼
MongoDB Atlas
   │
   ▼
Gemini API (optional study plan)
```

## Components

- **FastAPI** – REST API for the adaptive testing system
- **MongoDB Atlas** – stores questions and user session data
- **Adaptive Engine** – adjusts difficulty after each response
- **AI Module (Optional)** – generates study plans using Gemini

## MongoDB Schema

### Questions Collection

Each question contains difficulty metadata used by the adaptive algorithm.

Example document:

```json
{
  "question": "Solve: 3x + 5 = 20",
  "options": ["3", "5", "7", "10"],
  "correct_answer": "5",
  "difficulty": 0.4,
  "topic": "Algebra",
  "tags": ["equation"]
}
```

### User Sessions Collection

Tracks the progress of a student during a test session.

```json
{
  "user_id": "user123",
  "current_difficulty": 0.5,
  "session_history": [],
  "weak_topics": ["Algebra"]
}
```

## Adaptive Algorithm

The system uses a simplified adaptive difficulty approach.

**Initial state**
```
difficulty = 0.5
```

**Difficulty update rule**
- correct answer  → difficulty + 0.1
- incorrect answer → difficulty - 0.1

The difficulty value is constrained within:
```
0.1 ≤ difficulty ≤ 1.0
```

The next question is selected from MongoDB using the closest difficulty greater than or equal to the current level.

This approximates a simple Item Response Theory inspired adaptive mechanism.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/next-question` | Returns the next question based on difficulty |
| POST | `/submit-answer` | Updates difficulty based on correctness |
| POST | `/study-plan` | (Optional) Generates AI study plan |

### Example

**GET /next-question**
```json
{
  "question": "What is 12²?",
  "options": ["124","144","154","164"],
  "difficulty": 0.5
}
```

## Running the Project

1. **Clone repository**
   ```
   git clone <repo-url>
   cd adaptive-ai-engine
   ```

2. **Create virtual environment**
   ```
   python -m venv .venv
   ```

   **Activate:**
   
   *Windows*
   ```
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment**

   Create `.env` using `.env.example`.
   
   ```
   MONGO_URI=your_mongodb_connection_string
   DB_NAME=adaptive_test
   GEMINI_API_KEY=optional_api_key
   ```

5. **Run server**
   ```
   uvicorn app.main:app --reload
   ```

6. **API documentation**
   ```
   http://127.0.0.1:8000/docs
   ```

## 🤖 AI Development Log

**Gemini Integration (Bonus Feature):**
```
POST /study-plan
Input: ["Algebra", "Trigonometry"]
Output: Personalized 7-day study roadmap
- Day 1: Quadratic equations (3 videos + 10 problems)
- Day 2: SOH-CAH-TOA fundamentals
- Progress tracking via weak_topics array
```

## 📊 Tech Stack
```
Backend: FastAPI + Uvicorn
Database: MongoDB Atlas + PyMongo
AI: Google Gemini API
Dev: Python 3.10+, python-dotenv
```
**Built for** EdTech Innovation | **Ready for** Production Deployment
