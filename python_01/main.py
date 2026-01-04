#!/usr/bin/env python3
"""
调酒新手助手 - 桌面版
专为完全不了解调酒的客户设计
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import sys
import os

# 添加当前目录到路径，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cocktail_assistant import CocktailAssistantApp


def main():
    """主函数"""
    try:
        # 创建主窗口
        root = tk.Tk()
        root.title("调酒小白助手 - 零基础入门")
        root.geometry("900x700")
        root.minsize(800, 600)

        # 设置窗口图标（如果有的话）
        try:
            if os.path.exists("assets/icons/cocktail.ico"):
                root.iconbitmap("assets/icons/cocktail.ico")
        except:
            pass

        # 创建应用实例
        app = CocktailAssistantApp(root)

        # 启动主循环
        root.mainloop()

    except Exception as e:
        print(f"程序启动失败: {e}")
        messagebox.showerror("错误", f"程序启动失败:\n{str(e)}")


if __name__ == "__main__":
    main()