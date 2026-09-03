---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Standards

Use these standards whenever creating or editing an assignment README.

## File and Template Requirements

- Store each assignment in its own folder under `assignments/`.
- Name the student-facing assignment file `README.md`.
- Follow [`templates/assignment-template.md`](../../templates/assignment-template.md) exactly.
- Keep the required title, objective, tasks, description, and requirements sections. Do not add unrelated sections.

## Content Requirements

The section headers should reflect the structure in the template, including the exact icon usage.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
- **Tasks**: For each task:
   - Use a specific, action-oriented task name
   - In the Description, clearly state what the student must do.
   - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable
   - Provide example input/output in code blocks if helpful.

Do not include extra sections unless explicitly specified.

## Required Structure

Use the exact heading levels and icons from the template:

```markdown
# 📘 Assignment: [Assignment Title]

## 🎯 Objective

[Brief description]

## 📝 Tasks

### 🛠️ [Task Title]

#### Description
[What the student must do]

#### Requirements
Completed program should:

- [Specific requirement]
```
