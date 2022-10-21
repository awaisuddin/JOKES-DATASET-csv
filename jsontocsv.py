import json

with open('reddit_jokes.json') as f:
  data = json.load(f)
  print(data)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

