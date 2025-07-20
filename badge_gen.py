#!/usr/bin/env python3
import argparse

# Badge templates for common README badges
BADGES = {
    "build": "![Build Status](https://img.shields.io/github/actions/workflow/status/{repo}/build.yml)",
    "coverage": "![Coverage](https://img.shields.io/codecov/c/github/{repo})",
    "version": "![PyPI Version](https://img.shields.io/pypi/v/{pkg})",
    "license": "![License](https://img.shields.io/github/license/{repo})",
    "last_commit": "![Last Commit](https://img.shields.io/github/last-commit/{repo})"
}

def generate_badges(repo, pkg=None, badges=None):
    if badges is None:
        badges = ["build", "coverage", "version", "license", "last_commit"]
    
    output = []
    for badge in badges:
        if badge == "version" and pkg:
            output.append(BADGES[badge].format(pkg=pkg))
        else:
            output.append(BADGES[badge].format(repo=repo))
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(
        description="Generate README badges in markdown format for a GitHub repo or PyPI package."
    )
    parser.add_argument("repo", metavar="REPO", type=str, 
                       help="GitHub repository in 'owner/repo' format")
    parser.add_argument("--package", "-p", type=str, 
                       help="PyPI package name, if different from repo name")
    parser.add_argument("--badges", "-b", nargs='+', choices=BADGES.keys(), 
                       default=None, help="Specify which badges to generate")

    args = parser.parse_args()
    
    badges_markdown = generate_badges(args.repo, args.package, args.badges)
    print("\nGenerated Badges Markdown:\n")
    print(badges_markdown)

if __name__ == "__main__":
    main()
