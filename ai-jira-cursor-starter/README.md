# Cursor AI Jira Planning Starter

Open this folder in Cursor alongside a sample repository (or copy `.cursor/skills` into the target repo). The six project skills are discovered automatically.

## Workflow
1. Place or open your target repository in Cursor. Replace `examples/feature.md` with the real requirement.
2. In Cursor Agent, invoke `/codebase-analysis` and ask it to inspect the target repo.
3. Invoke `/requirement-analysis`, `/architecture-review`, `/specification-generation`, `/task-decomposition`, and `/test-planning` in that order.
4. Have a separate Cursor conversation assess each artifact against the matching YAML rubric. Rate each criterion 0-5 with evidence; weighted skill score = sum(criterion weight * rating/5)/100. Overall = sum(skill weight * skill score/5) for skill scores out of 5.
5. Run `python scripts/evaluate.py outputs/jira-plan.json` to validate the Jira JSON. This is only a structural checker, not a quality score.
6. Review findings and refine once. Human approval before Jira import.

## Notes
No Jira credentials or automatic ticket creation are included. Do not submit private company code to an unapproved model. The `outputs/` directory is intentionally initially empty.
