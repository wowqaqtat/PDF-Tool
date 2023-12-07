# PDF批量转换工具
# 2023年10月26日
# V1.0


"""
打包方式
pyinstaller -F -n PDF批量转换工具 main.py
"""

import os  # 操作系统相关
import tkinter as tk  # GUI相关
from tkinter import messagebox  # 提示框
from tkinter import filedialog  # 文件对话框
from docx2pdf import convert  # word处理
from PIL import Image  # 图像处理
from datetime import datetime  # 日期和时间
import uuid  # 生成唯一标识符
import windnd  # 文件拖拽

current_date = datetime.now().strftime('%Y%m%d%H%M%S')  # 获取当前日期


def word_to_pdf(input_file, output_file):
    """将word转换为pdf"""
    convert(input_file, output_file)


def image_to_pdf(input_files, output_file):
    """将图片转换为pdf"""
    images = [Image.open(file) for file in input_files]
    images[0].save(output_file, save_all=True, append_images=images[1:])


def batch_convert(input_files, output_dir):
    """批量转化为pdf文件"""
    for file in input_files:
        file_name, file_ext = os.path.splitext(file)
        file_name = os.path.basename(file)
        if file_ext == '.docx':
            output_file = os.path.join(
                output_dir, f'{file_name}_{current_date}_{id(uuid.uuid4())}.pdf')
            word_to_pdf(file, output_file)

        elif file_ext in ['.jpg', '.png', '.gif']:
            output_file = os.path.join(
                output_dir, f'{file_name}_{current_date}_{id(uuid.uuid4())}.pdf')
            image_to_pdf([file], output_file)
        else:
            messagebox.showerror(title='文件格式错误', message='请选择docx/png/jpg文件')
    messagebox.showinfo(title='成功', message='转换成功')
    os.startfile(output_dir)  # 查看保存位置


def select_input_files():
    """选择多个文件"""
    input_files = filedialog.askopenfilenames()
    input_files_listbox.delete(0, tk.END)
    for file in input_files:
        input_files_listbox.insert(tk.END, file)


def dragged_files(files):
    """文件拖拽事件"""
    for file in files:
        path = file.decode('gbk')
        input_files_listbox.insert(tk.END, path)
        print(path)


def select_output_dir():
    """选择保存位置"""
    output_dir = os.path.join(os.getcwd(), "Output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_dir = filedialog.askdirectory(initialdir=output_dir)
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(tk.END, output_dir)


def start_conversion():
    """开始转换"""
    input_files = [file for file in input_files_listbox.get(0, tk.END)]
    output_dir = output_dir_entry.get()
    if not input_files:
        messagebox.showerror("错误", "请选择要转换的文件")
        return
    if not output_dir:
        messagebox.showerror("错误", "请选择保存位置")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    batch_convert(input_files, output_dir)


def welcome():
    """欢迎使用"""
    print("############################")
    print("欢迎使用PDF批量转换工具")
    print("更新时间：2023年10月26日")
    print("版本：v1.0")
    print("############################")


if __name__ == '__main__':
    welcome()
    input_files = []  # 输入文件列表
    # 初始化输出路径
    output_dir = os.path.join(os.getcwd(), "Output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    root = tk.Tk()
    root.title('PDF批量转换工具')
    windnd.hook_dropfiles(root, func=dragged_files)  # 处理文件拖拽事件

    input_files_frame = tk.Frame(root)
    input_files_frame.pack(padx=10, pady=10)
    tk.Label(input_files_frame, text='输入：').pack(side=tk.LEFT)
    input_files_listbox = tk.Listbox(input_files_frame, width=50)
    input_files_listbox.pack(side=tk.LEFT)
    tk.Button(input_files_frame, text='选择文件',
              command=select_input_files).pack(side=tk.LEFT)

    output_dir_frame = tk.Frame(root)
    output_dir_frame.pack(padx=10, pady=10)
    tk.Label(output_dir_frame, text='输出：').pack(side=tk.LEFT)
    output_dir_entry = tk.Entry(output_dir_frame, width=50)
    output_dir_entry.pack(side=tk.LEFT)
    tk.Button(output_dir_frame, text='保存位置',
              command=select_output_dir).pack(side=tk.LEFT)
    output_dir_entry.insert(tk.END, output_dir)

    convert_frame = tk.Frame(root)
    convert_frame.pack(padx=10, pady=10)
    tk.Button(convert_frame, text='开始转换',
              command=start_conversion).pack(side=tk.LEFT)

    root.mainloop()
