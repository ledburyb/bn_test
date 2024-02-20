from apis.bn import fetch_candidates, fetch_roles
from recommender import fetch_all_recommendations

def main():
    candidates = fetch_candidates()
    roles = fetch_roles()
    fetch_all_recommendations(candidates, roles)

if __name__ == "__main__":
    main()
