# 💻 AI Code Gen Tools

AI代码生成工具，支持多语言代码生成、模板、脚手架。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 💻 函数生成
- 🏗️ 类生成
- 🔌 API生成
- 🖥️ CLI工具生成
- 📦 项目脚手架
- 🔄 代码转换

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_code_gen_tools import create_tools

tools = create_tools()

# 函数生成
func = tools.generate_function("斐波那契数列", "Python")

# 类生成
cls = tools.generate_class("用户管理", "Python")

# API生成
api = tools.generate_api("用户CRUD", "fastapi")

# CLI生成
cli = tools.generate_cli("文件管理", "click")

# 项目脚手架
scaffold = tools.generate_scaffold("Web应用", ["认证", "数据库"])

# 代码转换
converted = tools.convert_code(code, "Python", "JavaScript")
```

## 📁 项目结构

```
ai-code-gen-tools/
├── tools.py       # 代码生成工具核心
└── README.md
```

## 📄 许可证

MIT License
