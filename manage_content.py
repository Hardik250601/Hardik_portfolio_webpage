#!/usr/bin/env python3
"""
Portfolio Content Manager - Add projects/blogs to content.json
Run: python manage_content.py
"""

import json
import os
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
CONTENT_FILE = ROOT / "content.json"
IMAGES_DIR = ROOT / "images"


def load_content():
    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_content(data):
    with open(CONTENT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved to {CONTENT_FILE}")


def copy_image(src_path, dest_name):
    """Copy image to images/ folder, return relative path."""
    src = Path(src_path)
    if not src.exists():
        print(f"ERROR: File not found: {src}")
        return None
    dest = IMAGES_DIR / dest_name
    shutil.copy2(src, dest)
    print(f"Copied image to {dest}")
    return f"images/{dest_name}"


def get_input(prompt, required=True, default=""):
    while True:
        val = input(f"{prompt}{' [' + default + ']' if default else ''}: ").strip()
        if val:
            return val
        if default:
            return default
        if not required:
            return ""
        print("⚠️  Required field.")


def get_multiline(prompt):
    print(f"{prompt} (end with empty line):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)


def get_list(prompt, item_name="item"):
    items = []
    print(f"{prompt} (empty to finish):")
    while True:
        val = input(f"  {item_name}: ").strip()
        if not val:
            break
        items.append(val)
    return items


def slugify(text):
    return text.lower().replace(" ", "-").replace("&", "and").replace(".", "").replace(",", "")


def add_project(data):
    print("\n=== ADD NEW PROJECT ===\n")

    title = get_input("Project Title")
    slug = slugify(title)
    short_summary = get_input("Short Summary (for list cards)")
    full_description = get_multiline("Full Description (markdown supported)")

    # Main image
    main_img = ""
    while not main_img:
        img_path = get_input("Main Image Path (local file)")
        ext = Path(img_path).suffix
        dest_name = f"project-{slug}-main{ext}"
        main_img = copy_image(img_path, dest_name)

    # Supportive images
    supportive = []
    print("\nSupportive Images (optional):")
    while True:
        img_path = get_input(f"  Image path (or Enter to finish)", required=False)
        if not img_path:
            break
        ext = Path(img_path).suffix
        idx = len(supportive) + 1
        dest_name = f"project-{slug}-support{idx}{ext}"
        copied = copy_image(img_path, dest_name)
        if copied:
            supportive.append(copied)

    # Links
    github_link = get_input("GitHub Repo URL (optional)", required=False)
    linkedin_link = get_input("LinkedIn Post URL (optional)", required=False)
    demo_link = get_input("Live Demo URL (optional)", required=False)

    # Tech stack
    tech_stack = get_list("Tech Stack (one per line)", "Technology")

    # Metrics
    metrics = {}
    print("\nMetrics (key=value, empty to finish):")
    while True:
        key = get_input("  Key", required=False)
        if not key:
            break
        val = get_input(f"  Value for '{key}'")
        metrics[key] = val

    # Case study
    print("\n--- Case Study ---")
    problem = get_multiline("Problem Statement")
    architecture = get_multiline("Architecture / Solution")
    outcomes = get_list("Outcomes (one per line)", "Outcome")
    future_roadmap = get_list("Future Roadmap (one per line)", "Item")

    project = {
        "slug": slug,
        "title": title,
        "short_summary": short_summary,
        "main_image": main_img,
        "supportive_images": supportive,
        "full_description": full_description,
        "github_link": github_link,
        "github_blurb": "Source code and documentation available on GitHub." if github_link else "",
        "linkedin_link": linkedin_link,
        "demo_link": demo_link,
        "tech_stack": tech_stack,
        "metrics": metrics,
        "case_study": {
            "problem": problem,
            "architecture": architecture,
            "outcomes": outcomes,
            "future_roadmap": future_roadmap
        }
    }

    data["projects"].insert(0, project)  # Add to top
    save_content(data)
    print(f"\nProject '{title}' added!")


def add_blog(data):
    print("\n=== ADD NEW BLOG POST ===\n")

    title = get_input("Blog Title")
    slug = slugify(title)
    date_str = get_input("Date (e.g., September 26, 2026)", default=datetime.now().strftime("%B %d, %Y"))
    short_summary = get_input("Short Summary (for list cards)")
    content = get_multiline("Full Content (HTML supported)")

    blog = {
        "slug": slug,
        "title": title,
        "date": date_str,
        "short_summary": short_summary,
        "content": content
    }

    data["blogs"].insert(0, blog)
    save_content(data)
    print(f"\nBlog post '{title}' added!")


def list_content(data):
    print("\n=== CURRENT CONTENT ===\n")
    print("PROJECTS:")
    for i, p in enumerate(data["projects"], 1):
        print(f"  {i}. {p['title']} ({p['slug']})")
    print(f"\nBLOGS:")
    for i, b in enumerate(data["blogs"], 1):
        print(f"  {i}. {b['title']} ({b['slug']})")


def main():
    print(">>> Portfolio Content Manager")
    print("=" * 40)

    data = load_content()
    list_content(data)

    print("\nWhat would you like to do?")
    print("  1. Add Project")
    print("  2. Add Blog Post")
    print("  3. Exit")

    choice = input("\nChoice (1/2/3): ").strip()

    if choice == "1":
        add_project(data)
    elif choice == "2":
        add_blog(data)
    elif choice == "3":
        print("Bye!")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()