# src/llm.py

import os
from openai import OpenAI

class LLM:
    def __init__(self):
        self.client = OpenAI()

    def generate_daily_report(self, markdown_content, dry_run=False):
        prompt = (f"你是一个github开源项目分析师，擅长分析热门开源项目的进展和未来发展情况。以下是项目的最新进展，根据功能合并同类项，形成一份简报，简报的内容必须是中文，至少包含：1）新增功能；2）主要改进；3"
                  f"）修复问题；此外，还要再分析项目的潜在发展方向和当前进展中的趋势: \n{markdown_content}")
        if dry_run:
            with open("daily_progress/prompt.txt", "w+") as f:
                f.write(prompt)
            return "DRY RUN"

        print("Before call GPT")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt}
            ]
        )
        print("After call GPT")
        print(response)
        return response.choices[0].message.content
