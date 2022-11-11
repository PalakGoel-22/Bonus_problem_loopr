import os

root_path = "C:/Bonus_problem"

inp_text = os.path.join(root_path, 'Sample_text.txt')

print('Reading the file.....')

with open(inp_text, 'r') as file:
  content = file.read()
  words = content.split(' ')

word_count = {}


for word in words:
  if word not in word_count:
    word_count[word] = 1
  else:
    word_count[word] += 1

most_idx = int(list(word_count.values()).index(max(word_count.values())))

most_word = str(list(word_count.keys())[most_idx])

print(f'Most frequent word in the Sample_text.txt is {most_word}, occured a total of {max(word_count.values())}')


with open(f'{root_path}/output.txt', 'w') as file:
  content = content.replace(most_word,'loopr')
  file.write(content)

print(f"Replaced {most_word} with loopr, saving output in output.txt")

