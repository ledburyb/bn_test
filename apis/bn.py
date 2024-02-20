import requests

# TODO: In a real production environment this would come from env, add if time
MEMBERS_API_URL = "https://bn-hiring-challenge.fly.dev/members.json"
ROLES_API_URL = "https://bn-hiring-challenge.fly.dev/jobs.json"

def fetch_candidates():
    # TODO: In a more fleshed out system this would need error handling
    # and possibly a retry mechanism depending on how it's invoked
    return requests.get(MEMBERS_API_URL).json()

def fetch_roles():
    return requests.get(ROLES_API_URL).json()
