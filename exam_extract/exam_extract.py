import re
import os

import glob

input_file = "Wilhelm Olofsson 2022-12-19 (Programmering 1 - Python (2022)).docx"
output_file = "Wilhelm Olofsson 2022-12-19 (Programmering 1 - Python (2022)).html"

os.system(f"pandoc {input_file} -s -o {output_file}")

# Define regex pattern to match the questions and code
pattern = r'\d+\..+?(?=\d+\.)|\d+\..+'

# Read the exam file
with open('{}'.format(output_file), 'r') as file:
    exam_text = file.read()

# Find all matches for the pattern
matches = re.findall(pattern, exam_text, flags=re.DOTALL)

# Create a dictionary to store the questions and code
code_dict = {}

# Loop through the matches and add them to the dictionary
for match in matches:
    # Split the match into the question and code parts
    question, code = match.split('\n', 1)
    # Add the code to the dictionary using the question number as the key
    code_dict[question] = code.strip()

# Write the code snippets to a file
with open('exam_code.html', 'w') as file:
    for key in sorted(code_dict.keys()):
        file.write(f"{key}\n{code_dict[key]}\n\n")
