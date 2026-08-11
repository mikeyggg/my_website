import requests
import time
from datetime import datetime

GITHUB_USERNAME = "mikeyggg"

def fetch_projects():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    repos = response.json()

    projects = []
    for i, repo in enumerate(repos, start=1):
        if repo["fork"]:
            continue

        raw_date = repo["created_at"]
        formatted_date = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y")

        projects.append({
            "id": i,
            "title": repo["name"],
            "subtitle": repo["description"] or "No description yet",
            "body": repo["description"] or "No description yet",
            "created_at": formatted_date,
            "github_url": repo["html_url"]
        })

    return projects



CACHE_DURATION = 3600
cache = {"data": None, "timestamp": 0}

def get_projects():
    now = time.time()
    if cache["data"] is None or (now - cache["timestamp"]) > CACHE_DURATION:
        cache["data"] = fetch_projects()
        cache["timestamp"] = now
    return cache["data"]

all_posts = fetch_projects()

