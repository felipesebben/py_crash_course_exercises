glossary = {
    'list': 'brackets',
    'method': 'action',
    'for': 'loop',
    'get': 'choice',
    'range': 'series'
}

list = glossary['list']
method = glossary['method']
for4 = glossary['for']
get = glossary['get']
range = glossary['range']

print(f"List, {list}")
print(f"\nMethod, {method}")
print(f"\nFor, {for4}")
print(f"\nGet, {get}")
print(f"\nRange, {range}")

for meaning, value in glossary.items():
    print(f"\nMeaning: {meaning}")
    print(f"Value: {value}")
