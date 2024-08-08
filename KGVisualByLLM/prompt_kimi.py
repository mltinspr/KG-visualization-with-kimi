# 简单提示
simple_prompt = "How to self study Generative Artificial Intelligence in 2024?"

# 在提示中添加一个简单的提示“一步一步地思考”可以指导模型更顺序和逻辑的回应，更适合生成知识图谱。
step_by_step_prompt = "How to self study Generative Artificial Intelligence in 2024? Let's think step by step."

# 指定人格或角色是另一种有用方法。
persona_prompt = '''
How to self study Generative Artificial Intelligence in 2024?
You are a Course Instructor who designs a progressive syllabus based on the above question. 
Break it down into modules which contains a list the topics, concepts, or themes.
'''

# 生成格式化输出
generate_format_output_prompt = '''
How to self study Generative Artificial Intelligence in 2024?
Answer: Let's think step by step.
Provide Answer in JSON format.
'''

# 提供精确指导
provide_specific_instructions_prompt = '''
How to self study Generative Artificial Intelligence in 2024?
You are a Course Instructor who designs a progressive syllabus based on the Question. 
Break it down into modules which contains a list the topics, concepts, or themes.

Please response follow the  under asks:
Format Text above as a list of JSON objects with keys "input", "output" and "module".
"input" and "output" represent one and only one key concept respectively and "output" has dependency on "input".
Keep consistent and concise wordings (two to three phrases) for "input" and "output".
Do not include Module in the "input" or "output".
"module" is a numeric value indicates the Module in the syllabus.
'''

# 少样本提示
few_shot_prompt = f'''
How to self study Generative Artificial Intelligence in 2024?
There is a text you can reference inner $ bracket:
$
Please response follow the under asks:
Format Text above as a list of JSON objects with keys "input", "output" and "module".
"input" and "output" represent one and only one key concept respectively and "output" has dependency on "input".
Keep consistent and concise wordings (two to three phrases) for "input" and "output".
Do not include Module in the "input" or "output".
"module" is a numeric value indicates the Module in the syllabus.
The content of response do not have any other characters, just give the list of JSON objects is ok.
Extract all concepts within the bracket and after ```e.g.``` as seperate "output" objects.
An example:
"""
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
"""
'''
