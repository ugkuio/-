"""
自定义UI组件
提供更美观、易用的界面元素
"""

import tkinter as tk
from tkinter import ttk


# 移除类型注解导入，直接使用Python内置类型

class GradientFrame(tk.Canvas):
    """渐变背景画布"""

    def __init__(self, parent, color1: str, color2: str, **kwargs):
        super().__init__(parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        """绘制渐变背景"""
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()

        limit = width

        for i in range(limit):
            # 计算渐变颜色
            r = int(int(self.color1[1:3], 16) + (int(self.color2[1:3], 16) - int(self.color1[1:3], 16)) * i / limit)
            g = int(int(self.color1[3:5], 16) + (int(self.color2[3:5], 16) - int(self.color1[3:5], 16)) * i / limit)
            b = int(int(self.color1[5:7], 16) + (int(self.color2[5:7], 16) - int(self.color1[5:7], 16)) * i / limit)

            color = f'#{r:02x}{g:02x}{b:02x}'

            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)

        self.lower("gradient")


class ModernButton(tk.Frame):
    """现代化按钮"""

    def __init__(self, parent, text: str, icon: str = "",
                 command=None,
                 bg_color: str = "#6ab7ff",
                 fg_color: str = "white",
                 hover_color: str = "#4a97df",
                 **kwargs):
        super().__init__(parent, **kwargs)

        self.command = command
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_color = hover_color

        # 创建按钮画布
        self.canvas = tk.Canvas(self, highlightthickness=0,
                                bg=self.bg_color, bd=0)
        self.canvas.pack(fill="both", expand=True)

        # 绘制圆角矩形
        self.rect = self.canvas.create_rectangle(0, 0, 0, 0,
                                                 fill=self.bg_color,
                                                 outline=self.bg_color,
                                                 width=0)

        # 添加文本和图标
        self.text_id = self.canvas.create_text(0, 0, text=f"{icon} {text}",
                                               fill=self.fg_color,
                                               font=("Microsoft YaHei", 11, "bold"))

        # 绑定事件
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<Enter>", self._on_enter)
        self.canvas.bind("<Leave>", self._on_leave)
        self.bind("<Configure>", self._update_canvas)

    def _update_canvas(self, event=None):
        """更新画布大小"""
        width = self.winfo_width()
        height = self.winfo_height()

        # 更新矩形位置和圆角
        padding = 5
        self.canvas.coords(self.rect, padding, padding, width - padding, height - padding)

        # 更新文本位置
        self.canvas.coords(self.text_id, width / 2, height / 2)

    def _on_click(self, event):
        """点击事件"""
        if self.command:
            self.command()

    def _on_enter(self, event):
        """鼠标进入"""
        self.canvas.config(bg=self.hover_color)
        self.canvas.itemconfig(self.rect, fill=self.hover_color, outline=self.hover_color)

    def _on_leave(self, event):
        """鼠标离开"""
        self.canvas.config(bg=self.bg_color)
        self.canvas.itemconfig(self.rect, fill=self.bg_color, outline=self.bg_color)


class CardFrame(tk.Frame):
    """卡片式容器"""

    def __init__(self, parent, title: str = "", icon: str = "",
                 bg_color: str = "#f8f9fa",
                 border_color: str = "#dee2e6",
                 **kwargs):
        super().__init__(parent, **kwargs)

        # 配置样式
        self.config(bg=bg_color, bd=1, relief="solid",
                    highlightbackground=border_color,
                    highlightthickness=1)

        # 标题栏
        if title:
            title_frame = tk.Frame(self, bg=bg_color)
            title_frame.pack(fill="x", padx=10, pady=(10, 5))

            if icon:
                tk.Label(title_frame, text=icon, bg=bg_color,
                         font=("Microsoft YaHei", 14)).pack(side="left", padx=(0, 5))

            tk.Label(title_frame, text=title, bg=bg_color,
                     font=("Microsoft YaHei", 12, "bold"),
                     fg="#333").pack(side="left")

        # 内容区域
        self.content_frame = tk.Frame(self, bg=bg_color)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=5)

    def get_content_frame(self):
        """获取内容框架"""
        return self.content_frame


class ProgressBar(tk.Frame):
    """进度条"""

    def __init__(self, parent, total: int = 100,
                 color: str = "#6ab7ff", **kwargs):
        super().__init__(parent, **kwargs)

        self.total = total
        self.current = 0
        self.color = color

        # 创建进度条背景
        self.canvas = tk.Canvas(self, height=8, bg="#e9ecef",
                                highlightthickness=0)
        self.canvas.pack(fill="x")

        # 进度条前景
        self.progress = self.canvas.create_rectangle(0, 0, 0, 8,
                                                     fill=self.color,
                                                     outline=self.color)

        # 进度文本
        self.label = tk.Label(self, text="0%", bg=self["bg"],
                              font=("Microsoft YaHei", 9),
                              fg="#666")
        self.label.pack(side="right")

    def set_progress(self, value: int):
        """设置进度"""
        self.current = min(value, self.total)
        progress = self.current / self.total

        # 更新进度条
        width = self.canvas.winfo_width()
        self.canvas.coords(self.progress, 0, 0, width * progress, 8)

        # 更新文本
        self.label.config(text=f"{int(progress * 100)}%")


class IconLabel(tk.Frame):
    """带图标的标签"""

    def __init__(self, parent, text: str, icon: str = "",
                 icon_size: int = 16, **kwargs):
        super().__init__(parent, **kwargs)

        self.config(bg=parent["bg"])

        # 图标
        if icon:
            tk.Label(self, text=icon, bg=self["bg"],
                     font=("Segoe UI Emoji", icon_size)).pack(side="left", padx=(0, 8))

        # 文本
        tk.Label(self, text=text, bg=self["bg"],
                 font=("Microsoft YaHei", 10),
                 justify="left").pack(side="left")


class StepIndicator(tk.Frame):
    """步骤指示器"""

    def __init__(self, parent, steps, current: int = 0, **kwargs):
        super().__init__(parent, **kwargs)

        self.steps = steps
        self.current = current
        self.config(bg=parent["bg"])

        # 创建步骤
        for i, step in enumerate(self.steps):
            step_frame = tk.Frame(self, bg=self["bg"])
            step_frame.pack(side="left", padx=10)

            # 步骤编号
            number_bg = "#6ab7ff" if i <= current else "#cccccc"
            number_fg = "white" if i <= current else "#666666"

            number_label = tk.Label(step_frame, text=str(i + 1),
                                    bg=number_bg, fg=number_fg,
                                    font=("Microsoft YaHei", 10, "bold"),
                                    width=3, height=1)
            number_label.pack()

            # 步骤名称
            step_label = tk.Label(step_frame, text=step,
                                  bg=self["bg"], fg=number_fg,
                                  font=("Microsoft YaHei", 9))
            step_label.pack(pady=(3, 0))

            # 连接线（除了最后一个）
            if i < len(self.steps) - 1:
                line = tk.Frame(step_frame, height=1, width=20, bg="#cccccc")
                line.place(in_=number_label, relx=1.0, rely=0.5,
                           x=5, y=0, anchor="w")

    def set_current(self, step: int):
        """设置当前步骤"""
        self.current = step
        # 重新创建
        self.destroy()
        self.__init__(self.master, self.steps, step)