from fastapi import FastAPI
from linkedin_scraper import search_linkedin
from scorer import score_candidates
from message_generator import generate_messages

app = FastAPI()

@app.post("/get_candidates")
def get_candidates(job_description: str):
    candidates = search_linkedin(job_description)
    scored = score_candidates(candidates, job_description)
    top5 = scored[:5]
    messages = generate_messages(top5, job_description)

    result = []
    for i in range(len(top5)):
        result.append({
            "name": top5[i]["name"],
            "linkedin_url": top5[i]["url"],
            "headline": top5[i]["headline"],
            "fit_score": top5[i]["score"],
            "outreach_message": messages[i]
        })
    return result
