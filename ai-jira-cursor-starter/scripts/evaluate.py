import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
path=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'outputs/jira-plan.json'
plan=json.loads(path.read_text())
epic=plan['epic']; stories=epic['stories']; errors=[]; ids=set()
for s in stories:
    if not s.get('acceptance_criteria'): errors.append(f"{s.get('id')}: missing acceptance criteria")
    if not s.get('requirement_ids'): errors.append(f"{s.get('id')}: missing requirement traceability")
    for t in s.get('tasks',[]):
        if t['id'] in ids: errors.append(f"duplicate task id: {t['id']}")
        ids.add(t['id'])
        if not t.get('test_notes'): errors.append(f"{t['id']}: missing test notes")
        if not t.get('affected_files'): errors.append(f"{t['id']}: missing file impact")
for s in stories:
    for t in s.get('tasks',[]):
        for dep in t.get('dependencies',[]):
            if dep not in ids: errors.append(f"{t['id']}: unknown dependency {dep}")
print(json.dumps({'stories':len(stories),'tasks':len(ids),'errors':errors,'deterministic_checks_passed':not errors},indent=2))
sys.exit(1 if errors else 0)
