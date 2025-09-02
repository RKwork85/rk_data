# """
# @Description: 递归获取所有文件夹和文件路径并保存为树形结构
# @Author: rkwork
# """

# import os

# def generate_tree(root_path, prefix=""):
#     """
#     递归生成目录树（包含文件）
#     """
#     tree_str = ""
#     items = os.listdir(root_path)
#     items.sort()
#     for i, name in enumerate(items):
#         path = os.path.join(root_path, name)
#         connector = "└── " if i == len(items) - 1 else "├── "
#         tree_str += prefix + connector + name + "\n"
#         if os.path.isdir(path):
#             extension = "    " if i == len(items) - 1 else "│   "
#             tree_str += generate_tree(path, prefix + extension)
#     return tree_str


# def save_tree(root_path, output_file="tree.txt"):
#     """
#     保存目录树到文件
#     """
#     tree_str = root_path + "\n" + generate_tree(root_path)
#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write(tree_str)
#     print(f"目录树已保存到 {output_file}")


# if __name__ == "__main__":
#     # 修改为你要扫描的目录
#     root_directory = "./"  
#     save_tree(root_directory, "tree.txt")

from datetime import datetime


def today_date():
    """
    返回当天的日期（去掉时分秒），只保留年月日
    """
    return datetime.now().replace(microsecond=0)

print(today_date())
    