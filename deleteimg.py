import re
import os

file_path = 'index.html'

if not os.path.exists(file_path):
    print(f"错误：文件 '{file_path}' 不存在。")
else:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'<td><img.*?</td>'

        modified_content = re.sub(pattern, '<td></td>', content, flags=re.IGNORECASE | re.DOTALL)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)

        print(f"成功删除 '{file_path}' 文件中的 img 标签。")

    except Exception as e:
        print(f"处理文件时发生错误：{e}")
