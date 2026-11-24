
import re
from urllib.parse import urlparse


def validate_github_repo(repo_input: str):
    """
    Validate GitHub repository URL or owner/repo format.
    Returns (owner, repo).
    """

    if not repo_input or not repo_input.strip():
        raise ValueError("Please enter a GitHub repository URL.")

    repo_input = repo_input.strip().rstrip("/")

    if repo_input.startswith(("https://", "http://")):
        parsed = urlparse(repo_input)

        if parsed.hostname not in ("github.com", "www.github.com"):
            raise ValueError("Please provide a valid GitHub URL.")

        parts = parsed.path.strip("/").split("/")

        if len(parts) < 2:
            raise ValueError("Invalid GitHub repository URL.")

        owner, repo = parts[0], parts[1]

    else:
        parts = repo_input.split("/")

        if len(parts) != 2:
            raise ValueError("Use owner/repository format.")

        owner, repo = parts

    if not re.fullmatch(r"[A-Za-z0-9-]+", owner):
        raise ValueError("Invalid GitHub owner name.")

    if not re.fullmatch(r"[A-Za-z0-9._-]+", repo):
        raise ValueError("Invalid repository name.")

    repo = repo.removesuffix(".git")

    if not repo:
        raise ValueError("Repository name cannot be empty.")

    return owner, repo
