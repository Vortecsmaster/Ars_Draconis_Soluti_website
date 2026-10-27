#!/usr/bin/env python3
"""Small stdlib structural gate, not full JSON Schema validation. Run from repository root."""
import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
errors=[]; count=0
for kind,folder,suffix in [('task-result','tasks','.result.json'),('audit-result','audits','.audit.json'),('sprint-result','sprints','.result.json')]:
    schema=json.loads((root/'schemas'/f'{kind}.schema.json').read_text())
    for path in sorted((root/'reports'/folder).glob('*'+suffix)):
        count+=1
        try:data=json.loads(path.read_text())
        except (ValueError,OSError) as e:errors.append(f'{path}: JSON error {e}');continue
        if not isinstance(data,dict):errors.append(f'{path}: must be object');continue
        for field in schema['required']:
            if field not in data:errors.append(f'{path}: missing {field}')
        for field in data:
            if field not in schema['properties']:errors.append(f'{path}: unexpected {field}')
        if data.get('schema_version')!='1.0.0':errors.append(f'{path}: incorrect schema_version')
        for field,definition in schema['properties'].items():
            if field in data and 'enum' in definition and data[field] not in definition['enum']:
                errors.append(f'{path}: unexpected value for {field}')
print(f'Inspected {count} report(s); {len(errors)} basic validation error(s).')
for e in errors:print(e,file=sys.stderr)
if errors:sys.exit(1)
print('Reminder: use a real Draft 2020-12 JSON Schema validator for full schema compliance.')
