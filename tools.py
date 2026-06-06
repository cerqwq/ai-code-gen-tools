"""
AI Code Gen Tools - AI代码生成工具
支持多语言代码生成、模板、脚手架
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AICodeGenTools:
    """
    AI代码生成工具
    支持：多语言、模板、脚手架
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_function(self, description: str, language: str, style: str = "clean") -> str:
        """生成函数"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{language}写一个函数：

描述：{description}
风格：{style}

要求：
1. 类型提示
2. 文档字符串
3. 错误处理
4. 单元测试"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_class(self, description: str, language: str) -> str:
        """生成类"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{language}写一个类：

描述：{description}

要求：
1. 完整实现
2. 类型提示
3. 文档字符串
4. 设计模式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_api(self, description: str, framework: str = "fastapi") -> str:
        """生成API"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{framework}生成API：

描述：{description}

要求：
1. 完整实现
2. 数据模型
3. 错误处理
4. 文档注释"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_cli(self, description: str, framework: str = "click") -> str:
        """生成CLI工具"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{framework}生成CLI工具：

描述：{description}

要求：
1. 命令定义
2. 参数解析
3. 帮助文档
4. 错误处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_scaffold(self, project_type: str, features: List[str]) -> Dict:
        """生成项目脚手架"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        features_text = ", ".join(features)

        prompt = f"""请生成{project_type}项目脚手架：

功能：{features_text}

请返回JSON格式：
{{
    "structure": "目录结构",
    "files": [
        {{"path": "文件路径", "content": "文件内容"}}
    ],
    "dependencies": ["依赖"],
    "scripts": ["脚本"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"scaffold": content}

    def convert_code(self, code: str, source_lang: str, target_lang: str) -> str:
        """转换代码语言"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下{source_lang}代码转换为{target_lang}：

```{source_lang}
{code[:2000]}
```

要求：
1. 保持功能不变
2. 使用目标语言最佳实践
3. 添加注释"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def explain_code(self, code: str, language: str, level: str = "intermediate") -> str:
        """解释代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{level}水平解释以下{language}代码：

```{language}
{code[:2000]}
```

要求：
1. 整体功能
2. 关键逻辑
3. 重要细节
4. 使用场景"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AICodeGenTools:
    """创建代码生成工具"""
    return AICodeGenTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Code Gen Tools")
    print()

    # 测试
    func = tools.generate_function("斐波那契数列", "Python", "简洁")
    print(func[:300] + "...")
