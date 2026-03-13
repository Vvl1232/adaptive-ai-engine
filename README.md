# AI-Driven Adaptive Diagnostic Engine 🚀

## 📋 Project Overview
A **smart adaptive testing platform** that dynamically adjusts question difficulty based on user performance. Uses **FastAPI** backend with **MongoDB Atlas** for scalable data storage and **Gemini AI** (optional) for personalized study plans.

**Key Features:**
- ✅ Adaptive question difficulty adjustment
- ✅ RESTful API with FastAPI
- ✅ MongoDB Atlas integration
- ✅ AI-powered study plan generation
- ✅ Production-ready structure

**Perfect for:** EdTech internships, AI/ML assessments, adaptive learning systems.

## 🏗️ System Architecture
```
[Frontend] --> [FastAPI Backend] --> [MongoDB Atlas]
                         |
                [Gemini AI] (Study Plans)
```

**Components:**
- **FastAPI**: High-performance API server with auto-generated OpenAPI docs
- **MongoDB**: Questions & user sessions storage
- **Adaptive Engine**: Difficulty-based question selection
- **AI Planner**: Gemini-powered personalized study recommendations

## 🗄️ MongoDB Schema

### `questions` Collection
```json
{
  "_id": ObjectId,
  "question": "What is photosynthesis?",
  "options": ["A", "B", "C", "D"],
  "correct_answer": "B",
  "difficulty": 0.7,
  "topic": "Biology"
}
```

### `user_sessions` Collection
```json
{
  "_id": ObjectId,
  "user_id": "user123",
  "current_difficulty": 0.5,
  "session_history": [...],
  "weak_topics": ["Algebra", "Geometry"]
}
```

## 🧠 Adaptive Algorithm Logic
1. **Start**: `current_difficulty = 0.5`
2. **Next Question**: Find lowest difficulty question `>= current_difficulty`
3. **Answer Feedback**:
   - ✅ **Correct**: `difficulty = min(difficulty + 0.1, 1.0)`
   - ❌ **Incorrect**: `difficulty = max(difficulty - 0.1, 0.1)`
4. **Repeat** until assessment complete

**Math**: Elo-inspired adjustment with bounds [0.1, 1.0]

## 🔌 API Endpoints

| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| `GET` | `/` | Health check | - | `{"message": "Adaptive Testing Engine Running"}` |
| `GET` | `/next-question` | Get next adaptive question | - | `{"_id": "...", "question": "...", "difficulty": 0.7}` |
| `POST` | `/submit-answer` | Submit answer & update difficulty | `{"correct": true}` | `{"new_difficulty": 0.6}` |
| `POST` | `/study-plan` | Generate AI study plan | `{"weak_topics": ["Algebra"]}` | `{"study_plan": ["Practice quadratics", ...]}` |

**Interactive Docs**: Available at `/docs` after startup!

## 🚀 Quick Setup

1. **Clone & Install**
```bash
git clone <repo-url>
cd ai-adaptive-diagnostic-engine
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your MongoDB Atlas URI & DB name
```

3. **Run Server**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. **Test API**
- Health: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`
- Next Question: `http://localhost:8000/next-question`

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

**Future Enhancements:**
- [ ] User authentication & persistent sessions
- [ ] Question bank seeding script
- [ ] Real-time multiplayer testing
- [ ] Advanced ML difficulty prediction

## 📊 Tech Stack
```
Backend: FastAPI + Uvicorn
Database: MongoDB Atlas + PyMongo
AI: Google Gemini API
Dev: Python 3.10+, python-dotenv
```

---
**Built for** EdTech Innovation | **Ready for** Production Deployment
