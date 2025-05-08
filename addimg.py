import re
import os

index_file_path = 'index.html'
output_file_path = 'SmilesDrawer/output.html'

if not os.path.exists(index_file_path):
    print(f"错误：文件 '{index_file_path}' 不存在。")
elif not os.path.exists(output_file_path):
    print(f"错误：文件 '{output_file_path}' 不存在。")
else:
    try:
        with open(output_file_path, 'r', encoding='utf-8') as f:
            output_content = f.read()

        img_tags = re.findall(r'<img .*?>', output_content, re.IGNORECASE | re.DOTALL)

        if not img_tags:
            print(f"警告：在 '{output_file_path}' 中没有找到 <img> 标签。脚本将不会修改 '{index_file_path}'。")
            exit()

        print(f"从 '{output_file_path}' 提取到 {len(img_tags)} 个 <img> 标签。")

        with open(index_file_path, 'r', encoding='utf-8') as f:
            index_content = f.read()

        img_iterator = iter(img_tags)

        def replace_td_with_img(match):
            try:
                img_tag = next(img_iterator)
                return f'<td>{img_tag.strip()}</td>'
            except StopIteration:

                print("警告：<img> 标签数量少于空的 <td> 标签数量。剩余的 <td> 将保持为空。")
                return '<td></td>'

        modified_index_content, num_replacements = re.subn(
            r'<td\b[^>]*>\s*</td>',
            replace_td_with_img,
            index_content,
            flags=re.IGNORECASE | re.DOTALL
        )

        print(f"在 '{index_file_path}' 中替换了 {num_replacements} 个空的 <td> 标签。")

        try:
            next(img_iterator)
            print("警告：<img> 标签数量多于空的 <td> 标签数量。部分 <img> 标签未使用。")
        except StopIteration:
            pass

        with open(index_file_path, 'w', encoding='utf-8') as f:
            f.write(modified_index_content)

        print(f"成功将 <img> 标签插入到 '{index_file_path}'。")

    except Exception as e:
        print(f"处理文件时发生错误：{e}")
