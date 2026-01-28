#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Swagger API JSON 转换工具
将 Swagger 导出的 api.json 转换为:
1. 人类可读的 Markdown 文档
2. 适合 AI 助手阅读的精简文档
"""

import json
import re
from collections import defaultdict
from pathlib import Path


def load_swagger_json(file_path: str) -> dict:
    """加载 Swagger JSON 文件"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def simplify_schema_name(name: str) -> str:
    """简化 schema 名称，去除冗长的包名前缀"""
    # 提取最后一部分有意义的名称
    parts = name.split(".")
    # 找到有意义的部分
    meaningful_parts = []
    for part in parts:
        if (
            part
            and not part.startswith("cms-platform")
            and part
            not in ["internal", "controller", "model", "vo", "logic", "utils", "api"]
        ):
            meaningful_parts.append(part)

    if meaningful_parts:
        return "".join(meaningful_parts)

    # 如果没有找到有意义的部分，取最后两个部分
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return name


def get_simple_type(prop: dict, schemas: dict) -> str:
    """获取属性的简化类型描述"""
    if "$ref" in prop:
        ref = prop["$ref"].replace("#/components/schemas/", "")
        return simplify_schema_name(ref)

    prop_type = prop.get("type", "any")
    prop_format = prop.get("format", "")

    if prop_type == "array":
        items = prop.get("items", {})
        if "$ref" in items:
            ref = items["$ref"].replace("#/components/schemas/", "")
            return f"[]{simplify_schema_name(ref)}"
        item_type = items.get("type", "any")
        return f"[]{item_type}"

    if prop_type == "integer":
        return "int64" if "int64" in prop_format else "int"

    if prop_type == "file":
        return "file"

    return prop_type


def resolve_schema(ref: str, schemas: dict) -> dict:
    """解析 schema 引用并返回完整的 schema"""
    schema_name = ref.replace("#/components/schemas/", "")
    return schemas.get(schema_name, {})


def format_properties(
    properties: dict, required: list, schemas: dict, indent: int = 0
) -> list:
    """格式化属性列表"""
    lines = []
    indent_str = "  " * indent

    for prop_name, prop_info in properties.items():
        is_required = prop_name in required
        prop_type = get_simple_type(prop_info, schemas)
        description = prop_info.get("description", "")
        required_mark = " *(必填)*" if is_required else ""

        if description:
            lines.append(
                f"{indent_str}- `{prop_name}` ({prop_type}): {description}{required_mark}"
            )
        else:
            lines.append(f"{indent_str}- `{prop_name}` ({prop_type}){required_mark}")

        # 如果是引用类型，展开其属性（仅一层）
        if "$ref" in prop_info:
            ref_schema = resolve_schema(prop_info["$ref"], schemas)
            if ref_schema and ref_schema.get("properties"):
                ref_props = ref_schema.get("properties", {})
                ref_required = ref_schema.get("required", [])
                for sub_name, sub_info in ref_props.items():
                    sub_required_mark = " *(必填)*" if sub_name in ref_required else ""
                    sub_type = get_simple_type(sub_info, schemas)
                    sub_desc = sub_info.get("description", "")
                    if sub_desc:
                        lines.append(
                            f"{indent_str}  - `{sub_name}` ({sub_type}): {sub_desc}{sub_required_mark}"
                        )
                    else:
                        lines.append(
                            f"{indent_str}  - `{sub_name}` ({sub_type}){sub_required_mark}"
                        )

    return lines


def generate_markdown_docs(swagger_data: dict) -> str:
    """生成人类可读的 Markdown 文档"""
    lines = []
    lines.append("# API 接口文档")
    lines.append("")
    lines.append("> 本文档由 Swagger JSON 自动生成")
    lines.append("")

    schemas = swagger_data.get("components", {}).get("schemas", {})
    paths = swagger_data.get("paths", {})

    # 按 tag 分组
    apis_by_tag = defaultdict(list)
    for path, methods in paths.items():
        for method, details in methods.items():
            if isinstance(details, dict):
                tags = details.get("tags", ["未分类"])
                for tag in tags:
                    apis_by_tag[tag].append(
                        {"path": path, "method": method.upper(), "details": details}
                    )

    # 按 tag 排序并生成文档
    sorted_tags = sorted(apis_by_tag.keys())

    # 生成目录
    lines.append("## 目录")
    lines.append("")
    for tag in sorted_tags:
        anchor = tag.replace(" ", "-").replace(".", "").lower()
        lines.append(f"- [{tag}](#{anchor})")
    lines.append("")
    lines.append("---")
    lines.append("")

    for tag in sorted_tags:
        apis = apis_by_tag[tag]
        lines.append(f"## {tag}")
        lines.append("")

        for api in apis:
            details = api["details"]
            summary = details.get("summary", "无描述")
            lines.append(f"### {summary}")
            lines.append("")
            lines.append(f"**{api['method']}** `{api['path']}`")
            lines.append("")

            # 请求参数
            request_body = details.get("requestBody", {})
            parameters = details.get("parameters", [])

            if parameters:
                lines.append("**查询参数:**")
                lines.append("")
                for param in parameters:
                    param_name = param.get("name", "")
                    param_desc = param.get("description", "")
                    param_required = param.get("required", False)
                    param_schema = param.get("schema", {})
                    param_type = get_simple_type(param_schema, schemas)
                    required_mark = " *(必填)*" if param_required else ""
                    if param_desc:
                        lines.append(
                            f"- `{param_name}` ({param_type}): {param_desc}{required_mark}"
                        )
                    else:
                        lines.append(f"- `{param_name}` ({param_type}){required_mark}")
                lines.append("")

            if request_body:
                content = request_body.get("content", {})
                json_content = content.get("application/json", {})
                schema = json_content.get("schema", {})

                if "$ref" in schema:
                    ref_schema = resolve_schema(schema["$ref"], schemas)
                    properties = ref_schema.get("properties", {})
                    required = ref_schema.get("required", [])

                    if properties:
                        lines.append("**请求体:**")
                        lines.append("")
                        lines.extend(format_properties(properties, required, schemas))
                        lines.append("")

            # 响应
            responses = details.get("responses", {})
            if "200" in responses:
                resp = responses["200"]
                resp_content = resp.get("content", {})
                json_resp = resp_content.get("application/json", {})
                resp_schema = json_resp.get("schema", {})

                if "$ref" in resp_schema:
                    ref_name = resp_schema["$ref"].replace("#/components/schemas/", "")
                    ref_schema = schemas.get(ref_name, {})
                    properties = ref_schema.get("properties", {})

                    if properties:
                        lines.append("**响应:**")
                        lines.append("")
                        lines.extend(format_properties(properties, [], schemas))
                        lines.append("")

            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def generate_ai_docs(swagger_data: dict) -> str:
    """生成适合 AI 助手阅读的精简文档"""
    lines = []
    lines.append("# CMS 平台 API 参考文档 (AI 版)")
    lines.append("")
    lines.append("本文档提供 API 接口的精简描述，适合 AI 助手快速理解和使用。")
    lines.append("")

    schemas = swagger_data.get("components", {}).get("schemas", {})
    paths = swagger_data.get("paths", {})

    # 按 tag 分组
    apis_by_tag = defaultdict(list)
    for path, methods in paths.items():
        for method, details in methods.items():
            if isinstance(details, dict):
                tags = details.get("tags", ["未分类"])
                for tag in tags:
                    apis_by_tag[tag].append(
                        {"path": path, "method": method.upper(), "details": details}
                    )

    sorted_tags = sorted(apis_by_tag.keys())

    # 快速索引
    lines.append("## API 快速索引")
    lines.append("")
    lines.append("| 模块 | 接口 | 方法 | 路径 |")
    lines.append("|------|------|------|------|")

    for tag in sorted_tags:
        apis = apis_by_tag[tag]
        for api in apis:
            summary = api["details"].get("summary", "").lstrip("0123456789. ")
            lines.append(f"| {tag} | {summary} | {api['method']} | `{api['path']}` |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # 详细接口信息
    lines.append("## 接口详情")
    lines.append("")

    for tag in sorted_tags:
        apis = apis_by_tag[tag]
        tag_simple = tag.lstrip("0123456789. ")
        lines.append(f"### {tag_simple}")
        lines.append("")

        for api in apis:
            details = api["details"]
            summary = details.get("summary", "无描述").lstrip("0123456789. ")
            lines.append(f"#### {summary}")
            lines.append(f"- **方法**: {api['method']}")
            lines.append(f"- **路径**: `{api['path']}`")

            # 请求参数
            request_body = details.get("requestBody", {})
            parameters = details.get("parameters", [])

            if parameters:
                params_list = []
                for param in parameters:
                    param_name = param.get("name", "")
                    param_schema = param.get("schema", {})
                    param_type = get_simple_type(param_schema, schemas)
                    is_required = param.get("required", False)
                    req_mark = "*" if is_required else ""
                    params_list.append(f"`{param_name}{req_mark}`:{param_type}")
                lines.append(f"- **查询参数**: {', '.join(params_list)}")

            if request_body:
                content = request_body.get("content", {})
                json_content = content.get("application/json", {})
                schema = json_content.get("schema", {})

                if "$ref" in schema:
                    ref_schema = resolve_schema(schema["$ref"], schemas)
                    properties = ref_schema.get("properties", {})
                    required = ref_schema.get("required", [])

                    if properties:
                        params_list = []
                        for prop_name, prop_info in properties.items():
                            prop_type = get_simple_type(prop_info, schemas)
                            is_required = prop_name in required
                            req_mark = "*" if is_required else ""
                            params_list.append(f"`{prop_name}{req_mark}`:{prop_type}")
                        lines.append(f"- **请求体**: {', '.join(params_list)}")

            # 响应简述
            responses = details.get("responses", {})
            if "200" in responses:
                resp = responses["200"]
                resp_content = resp.get("content", {})
                json_resp = resp_content.get("application/json", {})
                resp_schema = json_resp.get("schema", {})

                if "$ref" in resp_schema:
                    ref_name = resp_schema["$ref"].replace("#/components/schemas/", "")
                    simple_name = simplify_schema_name(ref_name)
                    lines.append(f"- **响应**: `{simple_name}`")

            lines.append("")

    # 数据模型
    lines.append("---")
    lines.append("")
    lines.append("## 核心数据模型")
    lines.append("")

    # 筛选重要的 model (vo 模型)
    important_schemas = {}
    for name, schema in schemas.items():
        if ".vo." in name or "vo." in name.lower():
            simple_name = simplify_schema_name(name)
            if simple_name not in important_schemas:
                important_schemas[simple_name] = schema

    for name, schema in sorted(important_schemas.items()):
        properties = schema.get("properties", {})
        if not properties:
            continue

        lines.append(f"### {name}")
        lines.append("")
        lines.append("| 字段 | 类型 | 描述 |")
        lines.append("|------|------|------|")

        for prop_name, prop_info in properties.items():
            prop_type = get_simple_type(prop_info, schemas)
            description = prop_info.get("description", "-")
            lines.append(f"| `{prop_name}` | {prop_type} | {description} |")

        lines.append("")

    # 添加使用提示
    lines.append("---")
    lines.append("")
    lines.append("## 使用说明")
    lines.append("")
    lines.append("1. 带有 `*` 标记的参数为必填参数")
    lines.append("2. 所有 POST 请求使用 `application/json` 格式")
    lines.append("3. 分页接口通常需要提供 `current`(当前页) 和 `size`(每页条数) 参数")
    lines.append("4. 删除接口通常接收 `ids` 数组参数")
    lines.append(
        "5. 响应格式统一包含 `code`, `message`, `data` 字段(data 内容为上述响应类型)"
    )
    lines.append("")

    return "\n".join(lines)


def main():
    """主函数"""
    # 获取当前脚本所在目录
    script_dir = Path(__file__).parent
    input_file = script_dir / "api.json"

    if not input_file.exists():
        print(f"错误: 找不到输入文件 {input_file}")
        return

    print(f"正在加载 Swagger JSON: {input_file}")
    swagger_data = load_swagger_json(str(input_file))

    # 生成 Markdown 文档
    print("正在生成人类可读的 Markdown 文档...")
    markdown_docs = generate_markdown_docs(swagger_data)
    markdown_output = script_dir / "API_文档.md"
    with open(markdown_output, "w", encoding="utf-8") as f:
        f.write(markdown_docs)
    print(f"已生成: {markdown_output}")

    # 生成 AI 文档
    print("正在生成 AI 助手适用的文档...")
    ai_docs = generate_ai_docs(swagger_data)
    ai_output = script_dir / "API_文档_AI版.md"
    with open(ai_output, "w", encoding="utf-8") as f:
        f.write(ai_docs)
    print(f"已生成: {ai_output}")

    print("\n完成! 生成了以下文件:")
    print(f"  - {markdown_output.name}: 适合人类阅读的完整文档")
    print(f"  - {ai_output.name}: 适合 AI 助手使用的精简文档")


if __name__ == "__main__":
    main()
