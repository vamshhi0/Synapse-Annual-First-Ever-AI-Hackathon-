# scorer.py

def score_candidates(candidates, job_description):
    # Dummy scoring logic — you can replace this later with actual rubric logic
    for candidate in candidates:
        headline = candidate.get("headline", "").lower()
        score = 0

        # Sample keyword-based scoring
        if "ml" in headline or "ai" in headline:
            score += 3
        if "engineer" in headline or "developer" in headline:
            score += 2
        if "fintech" in headline or "openai" in headline:
            score += 3
        if "research" in headline:
            score += 2

        candidate["score"] = round(min(score, 10), 2)  # Cap score at 10

    return sorted(candidates, key=lambda x: x["score"], reverse=True)
