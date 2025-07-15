import json

# === Updated Manhattan Plan with sample completions ===
updated_manhattan_plan = {
    "Manhattan AI Engineer Dream Plan": {
        "Month 1–3: Core Skills + 1 Project": {
            "Python + Data Skills": {
                "Learn Python (OOP, if/else, functions, files)": True,
                "Work with Pandas, NumPy": True,
                "Understand ML basics (regression, KNN)": False
            },
            "Project 1 - AI Portfolio Generator": {
                "Streamlit input form for resume": True,
                "Use Gemini to auto-generate sections": True,
                "Design HTML output + PDF": False,
                "Push to GitHub": True
            },
            "Git & GitHub": {
                "Master git add, commit, push": True,
                "Create repo + README": True
            }
        },
        "Month 4–6: Projects + APIs": {
            "ML & APIs": {
                "Learn sklearn + pipelines": False,
                "Use Whisper, ChatGPT APIs": False,
                "Postman testing practice": False
            },
            "Project 2 - Zanpakutō Evaluator": {
                "Track skill progress in JSON": False,
                "Use AI to evaluate and suggest tasks": False
            },
            "Project 3 - Stock ETL Pipeline": {
                "Fetch data from API": False,
                "Clean + store in SQLite": False,
                "Build visual dashboard": False
            }
        },
        "Month 7–9: Advanced AI + NLP": {
            "Backend & Frontend": {
                "Learn Flask / Django REST": False,
                "React basics + connection": False
            },
            "Project 4 - Legal NLP Bot": {
                "Extract IPC/IT Act info": False,
                "Answer legal questions using AI": False
            },
            "Project 5 - Resume Site Generator": {
                "User JSON input → render resume site": False,
                "Auto-fill content with Gemini": False
            },
            "Blog & Portfolio": {
                "Write 1 post/week": False,
                "Publish projects with code explanation": False
            }
        },
        "Month 10–12: Job Hunt Phase": {
            "Job Prep": {
                "Write final resume & host online": False,
                "Finalize GitHub with 5+ projects": False
            },
            "Project 6 - Global Job Recommender": {
                "Live search using job APIs": False,
                "Recommend based on skills & stack": False
            },
            "Networking & Apps": {
                "Apply to 10 remote jobs/week": False,
                "Cold email + LinkedIn outreach": False
            },
            "Interview Practice": {
                "Solve 100+ Leetcode problems": False,
                "Mock system design sessions": False
            }
        }
    }
}

# === Save to file ===
file_path = "/workspaces/plan-tracker/manhattan_ai_plan.json"
with open(file_path, "w") as f:
    json.dump(updated_manhattan_plan, f, indent=2)

print(f"Saved to {file_path}")
