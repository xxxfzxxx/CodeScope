import json

data = []
with open('./results/program_synthesis_eval_gemini.jsonl', 'r') as f:
    for line in f:
        try:
            data.append(json.loads(line))
        except Exception as e:
            continue

processed_data = []
for item in data:
    for i in range(5):  # Loop over program_synthesis_0 to program_synthesis_4
        key = f'program_synthesis_{i}'
        if key in item:
            try:
                jsonobj = json.loads(item[key].replace('\n', '\\n').replace('\t', '\\t'))
                new_item = {
                    'src_uid': item['src_uid'],
                    'lang_cluster': item['lang_cluster'],
                    'difficulty': item['difficulty'],
                    'testcases': item['testcases'],
                    'lang': jsonobj[0]['lang'],
                    'source_code': jsonobj[0]['target code']
                }
                processed_data.append(new_item)
            except Exception as e:
                continue

# Write the processed data to a new JSONL file
with open('./results/postprocessed_program_synthesis_gemini.jsonl', 'w') as f:
    for item in processed_data:
        json.dump(item, f)
        f.write('\n')