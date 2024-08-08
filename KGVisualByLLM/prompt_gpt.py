# 问题设置
question = 'How to self study Generative Artificial Intelligence in 2024?'

simple_template = '''Question: {question}'''

step_by_step_template = '''Question: {question} Let's think step by step.'''

persona_template = '''
Question: {question}
You are a Course Instructor who designs a progressive syllabus based on the Question.
Break it down into modules which contains a list the topics, concepts, or themes.
'''

formatted_template = '''
Question: {question}
Answer: Let's think step by step.
Provide Answer in JSON format.
'''

specific_instruction_template = '''
Text: {text}
Response:
Format Text above as a list of JSON objects with keys "input", "output" and "module".
"input" and "output" represent one and only one key concept respectively and "output" has dependency on "input".
Keep consistent and concise wordings (two to three phrases) for "input" and "output".
Do not include Module in the "input" or "output".
"module" is a numeric value indicates the Module in the syllabus.
'''

few_shot_template = '''
Text: {text}

Response:
Format Text above as a list of JSON objects with keys "input", "output" and "module".
"input" and "output" represent one and only one key concept respectively and "output" has dependency on "input".
Keep consistent and concise wordings (two to three phrases) for "input" and "output".
Do not include Module in the "input" or "output".
"module" is a numeric value indicates the Module in the syllabus.

Extract all concepts within the bracket and after ```e.g.``` as seperate "output" objects.
The content of response please don't have other characters, just give the list of JSON objects with keys "input", "output" and "module".
An example:
```
Text: "Module 6: \
- A (e.g. B, C)"

Response:
{{
    "input": "A",
    "output": "B",
    "module": 6
}},
{{
    "input": "A",
    "output": "C",
    "module": 6
}}

```
'''
