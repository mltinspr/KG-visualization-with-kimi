import json
import openai
from APIKeys import *
from langchain import llms
from prompt_gpt import question
from pyvis.network import Network
from langchain.chains import LLMChain
from IPython.lib.display import IFrame
from prompt_kimi import persona_prompt
from prompt_gpt import persona_template
from prompt_kimi import few_shot_prompt
from json.decoder import JSONDecodeError
from langchain.prompts import PromptTemplate


class KGVisualizer:
    """
    项目来源：https://www.visual-design.net/post/llm-prompt-engineering-techniques-for-knowledge-graph
    """

    def __init__(self, use_gpt: bool = False):
        self._kimi_api_key = KIMI_KEY
        self._gpt_api_key = OPENAI_KEY
        self.client = openai.OpenAI(api_key=self._kimi_api_key, base_url="https://api.moonshot.cn/v1")
        self.net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white', notebook=True,
                           cdn_resources='in_line', directed=True)
        self.use_gpt = use_gpt

    @staticmethod
    def chat(client: openai.OpenAI, prompt: str) -> str:
        try:
            # 向 kimi 服务器发送聊天请求
            completion = client.chat.completions.create(
                model="moonshot-v1-8k",
                messages=[
                    {"role": "system",
                     "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，"
                                "准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，"
                                "不可翻译成其他语言。"
                     },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
            )
        except Exception as e:
            print(f'An error occurred:{e.args}. Follow https://platform.moonshot.cn/docs to get more details.')
            return ''
        # 获取并打印助手的响应
        response = completion.choices[0].message.content
        print(response)
        return response

    def generate_data_with_gpt(self) -> list[dict]:
        # 初始化提示模板和 GPT 模型
        # prompt_template = PromptTemplate(template=persona_template, input_variables=['question'])
        # gpt = llms.OpenAI(api_key=self._gpt_api_key, max_tokens=1000, base_url="https://api.chatanywhere.tech")
        # chain = LLMChain(prompt=prompt_template, llm=gpt)

        # 使用 GPT 模型根据问题生成文本
        # text = chain.run(question)

        # 初始化 few-shot 提示模板并运行，以格式化响应
        # few_shot = PromptTemplate(template=few_shot_prompt, input_variables=["text"])
        # few_shot_chain = LLMChain(prompt=few_shot, llm=gpt)
        # formatted_response = few_shot_chain.run(text)

        # 从格式化响应中提取 JSON 列表
        # json_response = formatted_response[:formatted_response.rfind("}") + 1] + "]"
        # json_list = json.loads(json_response)
        # return json_list
        raise NotImplementedError("Need OPENAI_KEY to test")

    def generate_data_with_kimi(self) -> list[dict]:
        # 通过chat函数与Kimi进行对话，获取补充文本
        supplement_text = self.chat(self.client, persona_prompt)
        # 在few_shot_prompt中查找美元符号的位置，以准备插入补充文本
        add_location = few_shot_prompt.find('$')
        # 将补充文本插入到few_shot_prompt中适当的位置
        mixed_prompt = few_shot_prompt[:add_location + 1] + supplement_text + few_shot_prompt[add_location:]

        # 使用混合的提示与Kimi进行对话，并格式化模型的响应
        formatted_response: str = self.chat(self.client, mixed_prompt)

        try:
            # 尝试解析格式化后的响应为JSON列表
            json_response = formatted_response[formatted_response.find("["):formatted_response.rfind("}") + 1] + "]"
            json_list: list[dict] = json.loads(json_response)
        except JSONDecodeError:
            # 如果解析失败，尝试将响应解析为一个个单独的JSON对象，然后封装成列表
            json_response = "[" + formatted_response[
                                  formatted_response.find("{"):formatted_response.rfind("}") + 1] + "]"
            json_list: list[dict] = json.loads(json_response)
        return json_list

    def visualize_kg(self, graph_data: list[dict]) -> None:
        # 遍历图谱数据，添加节点和边
        for i in graph_data:
            input_node = i["input"]
            output_node = i["output"]
            # 为输入节点和输出节点添加标题信息，标题中包含模块号
            self.net.add_node(input_node, title=input_node + f'module{i["module"]}')
            self.net.add_node(output_node, title=output_node + f'module{i["module"]}')
            self.net.add_edge(input_node, output_node)

        # 生成HTML代码并写入文件，以展示知识图谱
        html = self.net.generate_html(notebook=True)
        with open("KG.html", "w+", encoding='utf-8') as use_utf8:
            use_utf8.write(html)
        # 在Jupyter notebook中显示生成的HTML，如果不在notebook环境中运行则此行无效
        IFrame("KG.html", width='100%', height='750px')

    def schedule(self) -> None:
        if not self.use_gpt:
            json_list = self.generate_data_with_kimi()
        else:
            json_list = self.generate_data_with_gpt()
        # 使用生成的JSON列表来可视化知识图谱
        self.visualize_kg(json_list)


if __name__ == '__main__':
    print(KGVisualizer.__doc__)
    kg_visualizer = KGVisualizer()
    kg_visualizer.schedule()
