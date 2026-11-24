
import base64
import requests

from config.settings import (
    GITHUB_API_BASE,
    GITHUB_HEADERS,
    PACKAGE_FILES,
    MAX_TREE_FILES,
    MAX_FILE_SIZE
)


class GitHubAPIError(Exception):
    pass


class GitHubClient:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(GITHUB_HEADERS)

    def _get(self, endpoint, params=None):
        url = f"{GITHUB_API_BASE}{endpoint}"

        try:
            response = self.session.get(
                url,
                params=params,
                timeout=20
            )

        except requests.RequestException as error:
            raise GitHubAPIError(
                f"Unable to connect to GitHub: {error}"
            )

        if response.status_code == 404:
            raise GitHubAPIError(
                "Repository not found or inaccessible. "
                "Check the URL and ensure the repository is public."
            )

        if response.status_code == 403:
            remaining = response.headers.get(
                "X-RateLimit-Remaining"
            )

            if remaining == "0":
                reset = response.headers.get("X-RateLimit-Reset")
                raise GitHubAPIError(
                    f"GitHub API rate limit exceeded. "
                    f"Try again after reset timestamp: {reset}"
                )

            raise GitHubAPIError(
                "GitHub access was forbidden. Check API permissions."
            )

        if response.status_code == 429:
            raise GitHubAPIError(
                "GitHub API rate limit exceeded. Please retry later."
            )

        if response.status_code >= 400:
            raise GitHubAPIError(
                f"GitHub API error: {response.status_code} "
                f"- {response.text[:300]}"
            )

        return response.json()

    def get_repository(self, owner, repo):
        return self._get(f"/repos/{owner}/{repo}")

    def get_languages(self, owner, repo):
        return self._get(
            f"/repos/{owner}/{repo}/languages"
        )

    def get_readme(self, owner, repo):
        data = self._get(
            f"/repos/{owner}/{repo}/readme"
        )

        if data.get("encoding") == "base64":
            content = base64.b64decode(
                data["content"]
            ).decode("utf-8", errors="replace")

            return content[:MAX_FILE_SIZE]

        return ""

    def get_directory_tree(self, owner, repo, branch):
        data = self._get(
            f"/repos/{owner}/{repo}/git/trees/{branch}",
            params={"recursive": "1"}
        )

        tree = data.get("tree", [])

        files = [
            item["path"]
            for item in tree
            if item["type"] == "blob"
        ]

        return {
            "files": files[:MAX_TREE_FILES],
            "truncated": data.get("truncated", False)
            or len(files) > MAX_TREE_FILES
        }

    def get_file_content(self, owner, repo, path):
        data = self._get(
            f"/repos/{owner}/{repo}/contents/{path}"
        )

        if data.get("type") != "file":
            return ""

        if data.get("size", 0) > MAX_FILE_SIZE:
            return "[File skipped: exceeds size limit]"

        if data.get("encoding") == "base64":
            return base64.b64decode(
                data["content"]
            ).decode("utf-8", errors="replace")

        return ""

    def get_package_files(self, owner, repo, file_paths):
        package_data = {}

        for path in file_paths:
            filename = path.split("/")[-1]

            if filename in PACKAGE_FILES:
                try:
                    package_data[path] = self.get_file_content(
                        owner, repo, path
                    )
                except GitHubAPIError:
                    continue

        return package_data

    def analyze_repository(self, owner, repo):
        metadata = self.get_repository(owner, repo)

        default_branch = metadata["default_branch"]

        languages = self.get_languages(owner, repo)

        readme = self.get_readme(owner, repo)

        directory = self.get_directory_tree(
            owner,
            repo,
            default_branch
        )

        packages = self.get_package_files(
            owner,
            repo,
            directory["files"]
        )

        return {
            "metadata": metadata,
            "languages": languages,
            "readme": readme,
            "directory": directory["files"],
            "tree_truncated": directory["truncated"],
            "packages": packages
        }
