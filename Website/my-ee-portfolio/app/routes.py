from flask import Blueprint, render_template
import os
import re

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/projects")
def projects():
    projects_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "projects")
    )
    project_files = [f for f in os.listdir(projects_dir) if f.endswith(".md")]
    projects = []
    for filename in project_files:
        filepath = os.path.join(projects_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Safely get title, description, and date
        title_line = lines[0].strip() if len(lines) > 0 else "Untitled"
        if title_line.lower().startswith("# project title:"):
            title = title_line[len("# project title:") :].strip()
        else:
            title = title_line
        description = lines[4].strip() if len(lines) > 4 else ""
        date = lines[8].strip() if len(lines) > 8 else ""
        content = "".join(lines)
        projects.append(
            {
                "title": title,
                "description": description,
                "date": date,
                "content": content,
            }
        )
    return render_template("projects.html", projects=projects)


@main.route("/essays")
def essays():
    essays_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "essays")
    )
    essay_files = [f for f in os.listdir(essays_dir) if f.endswith(".tex")]
    essays = []
    for filename in essay_files:
        filepath = os.path.join(essays_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Extract \title{...}, \author{...}, \date{...}, introduction, main content, and conclusion sections
        title_match = re.search(r"\\title\{(.+?)\}", content)
        author_match = re.search(r"\\author\{(.+?)\}", content)
        date_match = re.search(r"\\date\{(.+?)\}", content)
        intro_match = re.search(
            r"\\section\*?\{[Ii]ntroduction\}(.*?)(\\section|\Z)", content, re.DOTALL
        )
        main_match = re.search(
            r"\\section\*?\{[Mm]ain\s+[Cc]ontent\}(.*?)(\\section|\Z)",
            content,
            re.DOTALL,
        )
        conclusion_match = re.search(
            r"\\section\*?\{[Cc]onclusion\}(.*?)(\\section|\Z)", content, re.DOTALL
        )
        title = title_match.group(1).strip() if title_match else "Untitled"
        author = author_match.group(1).strip() if author_match else ""
        date = date_match.group(1).strip() if date_match else ""
        introduction = intro_match.group(1).strip() if intro_match else ""
        main_content = main_match.group(1).strip() if main_match else ""
        conclusion = conclusion_match.group(1).strip() if conclusion_match else ""
        essays.append(
            {
                "title": title,
                "author": author,
                "date": date,
                "introduction": introduction,
                "main_content": main_content,
                "conclusion": conclusion,
                "content": content,
            }
        )
    return render_template("essays.html", essays=essays)
