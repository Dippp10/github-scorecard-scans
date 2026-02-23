import requests

# ========== CONFIG ==========
GITHUB_USERNAME = "Dippp10" # Replace with your GitHub username
OUTPUT_FILE = "REPO_SCORECARDS.md"

# GitHub API URL to fetch user's repos
API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"

# ========== FETCH REPOS ==========
response = requests.get(API_URL)
repos = response.json()

if isinstance(repos, dict) and repos.get("message"):
    print("Error fetching repositories:", repos.get("message"))
    exit(1)

# ========== GENERATE MARKDOWN ==========
md_lines = ["# Repository Scorecards\n"]

for repo in repos:
    name = repo["name"]
    repo_url = repo["html_url"]

    # Shields.io badges
    stars_badge = f"![Stars](https://img.shields.io/github/stars/{GITHUB_USERNAME}/{name})"
    issues_badge = f"![Open Issues](https://img.shields.io/github/issues/{GITHUB_USERNAME}/{name})"
    
    # Security Scorecard badge
    security_badge = f"![Security Score](https://api.securityscorecards.dev/projects/github.com/{GITHUB_USERNAME}/{name}/badge)"

    # Add to markdown
    md_lines.append(f"## [{name}]({repo_url})")
    md_lines.append(f"{stars_badge} {issues_badge} {security_badge}\n")

# ========== WRITE FILE ==========
with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(md_lines))

print(f"Scorecards Markdown generated: {OUTPUT_FILE}")


On Mon, 23 Feb 2026, 11:56 am DIPIKA VAMAN KANTAPPA POOJARI, <deepikakarthik697@gmail.com> wrote:

    import requests

    # ========== CONFIG ==========
    GITHUB_USERNAME = "YOUR_USERNAME" # Replace with your GitHub username
    OUTPUT_FILE = "REPO_SCORECARDS.md"

    # GitHub API URL to fetch user's repos
    API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"

    # ========== FETCH REPOS ==========
    response = requests.get(API_URL)
    repos = response.json()

    if isinstance(repos, dict) and repos.get("message"):
        print("Error fetching repositories:", repos.get("message"))
        exit(1)

    # ========== GENERATE MARKDOWN ==========
    md_lines = ["# Repository Scorecards\n"]

    for repo in repos:
        name = repo["name"]
        repo_url = repo["html_url"]

        # Shields.io badges
        stars_badge = f"![Stars](https://img.shields.io/github/stars/{GITHUB_USERNAME}/{name})"
        issues_badge = f"![Open Issues](https://img.shields.io/github/issues/{GITHUB_USERNAME}/{name})"
        
        # Security Scorecard badge
        security_badge = f"![Security Score](https://api.securityscorecards.dev/projects/github.com/{GITHUB_USERNAME}/{name}/badge)"

        # Add to markdown
        md_lines.append(f"## [{name}]({repo_url})")
        md_lines.append(f"{stars_badge} {issues_badge} {security_badge}\n")

    # ========== WRITE FILE ==========
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(md_lines))

    print(f"Scorecards Markdown generated: {OUTPUT_FILE}")

