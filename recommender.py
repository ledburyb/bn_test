from utils.text_analysis import extract_location_preferences, extract_job_title_keywords

def match_score(candidate_location_preferences, candidate_job_titles, job_title, job_location):
    score = 0

    # If the candidate hasn't mentioned a location then any job locations are valid
    if not candidate_location_preferences["positive"]:
        score = 1
    elif job_location in candidate_location_preferences["positive"]:
        score = 1

    if job_location in candidate_location_preferences["negative"]:
        score = 0

    for title in candidate_job_titles:
        if title in job_title or job_title in title:
            score += 1

    return score

def fetch_recommendations(candidate, roles):
    candidate_location_preferences = extract_location_preferences(candidate["bio"])
    candidate_job_titles = extract_job_title_keywords(candidate["bio"])

    scored_roles = []
    for role in roles:
        score = match_score(candidate_location_preferences, candidate_job_titles, role["title"].lower(), role["location"].lower())
        scored_roles.append({"score": score, "role": role})

    scored_roles.sort(key=lambda i: i["score"])
    scored_roles.reverse()

    # Filter out roles without a job title and location match
    return [role["role"] for role in scored_roles if role["score"] >= 2]

def fetch_all_recommendations(candidates, roles):
    for candidate in candidates:
        recommendations = fetch_recommendations(candidate, roles)
        print(candidate["name"])
        if not recommendations:
            print("No suggested jobs")
        else:
            for recommendation in recommendations:
                print(recommendation["title"], ",", recommendation["location"])
        print("-------------\n\n")