#!/usr/bin/env python3
"""
Fetches GitHub Trending + Reddit + HN every run.
Saves to inbox/YYYY-MM-DD_phase0.md for manual review.
"""

import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

INBOX_DIR = os.path.join(os.path.dirname(__file__), "..", "inbox")
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}


def fetch_github_trending(limit=15):
    url = "https://github.com/trending?since=weekly"
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    results = []
    for repo in soup.select("article.Box-row")[:limit]:
        name_tag = repo.select_one("h2 a")
        if not name_tag:
            continue
        name = " ".join(name_tag.get_text().split())
        link = "https://github.com" + name_tag["href"].strip()
        desc_tag = repo.select_one("p")
        desc = desc_tag.get_text(strip=True) if desc_tag else ""
        stars_tag = repo.select_one("a[href$='/stargazers']")
        stars = stars_tag.get_text(strip=True) if stars_tag else ""
        results.append({"name": name, "link": link, "desc": desc, "stars": stars})
    return results


def fetch_reddit(subreddit, limit=10):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=week&limit={limit}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    results = []
    for post in r.json()["data"]["children"]:
        p = post["data"]
        results.append({
            "name": p["title"],
            "link": "https://reddit.com" + p["permalink"],
            "traction": f"{p['score']} upvotes · {p['num_comments']} comments",
        })
    return results


def fetch_hn(limit=10):
    url = f"https://hn.algolia.com/api/v1/search?tags=show_hn&hitsPerPage={limit}"
    r = requests.get(url, timeout=10)
    results = []
    for hit in r.json()["hits"]:
        results.append({
            "name": hit.get("title", ""),
            "link": hit.get("url") or f"https://news.ycombinator.com/item?id={hit['objectID']}",
            "traction": f"{hit.get('points', 0)} points · {hit.get('num_comments', 0)} comments",
        })
    return results


def build_section(title, items, show_desc=False):
    lines = [f"## {title}\n\n"]
    for item in items:
        lines.append(f"### {item['name']}\n")
        lines.append(f"Link: {item['link']}\n")
        if show_desc and item.get("desc"):
            lines.append(f"Description: {item['desc']}\n")
        if item.get("stars"):
            lines.append(f"Stars this week: {item['stars']}\n")
        if item.get("traction"):
            lines.append(f"Traction: {item['traction']}\n")
        lines.append("What made me stop: \n\n")
    return lines


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(INBOX_DIR, f"{date_str}_phase0.md")

    if os.path.exists(filepath):
        print(f"Already fetched today: {filepath}")
        return

    print("Fetching GitHub Trending...")
    github = fetch_github_trending()

    print("Fetching r/LocalLLaMA...")
    reddit_llm = fetch_reddit("LocalLLaMA")

    print("Fetching r/ChatGPTCoding...")
    reddit_coding = fetch_reddit("ChatGPTCoding")

    print("Fetching HN Show HN...")
    hn = fetch_hn()

    lines = [f"# Phase 0 Capture — {date_str}\n\n"]
    lines += build_section("GitHub Trending (Weekly)", github, show_desc=True)
    lines += build_section("r/LocalLLaMA — Top This Week", reddit_llm)
    lines += build_section("r/ChatGPTCoding — Top This Week", reddit_coding)
    lines += build_section("HN — Show HN Recent", hn)

    os.makedirs(INBOX_DIR, exist_ok=True)
    with open(filepath, "w") as f:
        f.writelines(lines)

    print(f"Saved: {filepath}")


if __name__ == "__main__":
    main()
