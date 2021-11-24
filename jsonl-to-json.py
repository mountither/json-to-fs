import json
with open('data.jsonl') as f:
    data = [json.loads(line) for line in f]

with open('data.json', 'w') as wf:
    json.dump(data, wf, indent=4, ensure_ascii=False)