import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_tag = '<main id="main-content">'
e_tag = '<section id="practice-l1">'

s = text.find(s_tag)
e = text.find(e_tag)
print(f"Indices: s={s}, e={e}")

if s != -1 and e != -1:
    content = text[s + len(s_tag):e].strip()
    out_path = os.path.join('data', 'fsa_reference_extracted.html')
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(content)
    print(f"Successfully extracted {len(content)} characters to {out_path}")
else:
    print("Could not find start or end tags in index.html")
