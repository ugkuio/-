"""
增强版调酒助手 - 修复数据库初始化问题
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import random
from typing import List, Dict, Any
import sqlite3
from datetime import datetime
import os


class DatabaseManager:
    """数据库管理器 - 修复版本"""

    def __init__(self):
        self.db_file = 'cocktail_assistant.db'
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.create_tables()

    def reset_database(self):
        """重置数据库（开发用）"""
        self.conn.close()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        """创建数据表"""
        cursor = self.conn.cursor()

        # 检查表是否存在
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='base_spirits'")
        if not cursor.fetchone():
            # 基酒表 - 第一次创建
            cursor.execute('''
                CREATE TABLE base_spirits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    chinese_name TEXT,
                    category TEXT,
                    alcohol_content REAL,
                    flavor_profile TEXT,
                    origin TEXT,
                    description TEXT,
                    image_path TEXT
                )
            ''')
        else:
            # 表已存在，检查列是否存在
            cursor.execute("PRAGMA table_info(base_spirits)")
            columns = [column[1] for column in cursor.fetchall()]

            # 添加缺失的列
            if 'chinese_name' not in columns:
                cursor.execute("ALTER TABLE base_spirits ADD COLUMN chinese_name TEXT")

        # 检查cocktails表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cocktails'")
        if not cursor.fetchone():
            cursor.execute('''
                CREATE TABLE cocktails (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    chinese_name TEXT,
                    difficulty TEXT,
                    alcohol_level TEXT,
                    glassware TEXT,
                    base_spirit_id INTEGER,
                    instructions TEXT,
                    ingredients TEXT,
                    flavor_profile TEXT,
                    occasion TEXT,
                    price_range TEXT,
                    prep_time INTEGER,
                    popularity INTEGER DEFAULT 0,
                    FOREIGN KEY (base_spirit_id) REFERENCES base_spirits(id)
                )
            ''')

        # 检查techniques表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='techniques'")
        if not cursor.fetchone():
            cursor.execute('''
                CREATE TABLE techniques (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    chinese_name TEXT,
                    category TEXT,
                    description TEXT,
                    steps TEXT,
                    tools_required TEXT,
                    difficulty TEXT,
                    video_url TEXT
                )
            ''')

        # 检查food_pairings表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='food_pairings'")
        if not cursor.fetchone():
            cursor.execute('''
                CREATE TABLE food_pairings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cocktail_id INTEGER,
                    food_type TEXT,
                    pairing_description TEXT,
                    rating INTEGER,
                    FOREIGN KEY (cocktail_id) REFERENCES cocktails(id)
                )
            ''')

        # 检查favorites表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='favorites'")
        if not cursor.fetchone():
            cursor.execute('''
                CREATE TABLE favorites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER DEFAULT 1,
                    cocktail_id INTEGER,
                    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (cocktail_id) REFERENCES cocktails(id)
                )
            ''')

        self.conn.commit()

    def insert_sample_data(self):
        """插入示例数据"""
        self.insert_base_spirits()
        self.insert_cocktails()
        self.insert_techniques()
        self.insert_food_pairings()

    def insert_base_spirits(self):
        """插入基酒数据"""
        cursor = self.conn.cursor()

        # 检查是否已有数据
        cursor.execute("SELECT COUNT(*) FROM base_spirits")
        count = cursor.fetchone()[0]

        if count == 0:
            base_spirits = [
                ("Gin", "金酒", "White Spirit", 40.0, "Botanical, Juniper", "英国/荷兰",
                 "以杜松子为主要风味，带有草本植物香气", "gin.jpg"),
                ("Vodka", "伏特加", "White Spirit", 40.0, "Clean, Neutral", "俄罗斯/波兰",
                 "纯净无味，适合各种调酒", "vodka.jpg"),
                ("Rum", "朗姆酒", "Brown Spirit", 40.0, "Sweet, Caramel", "加勒比海",
                 "由甘蔗制成，带有甜味和焦糖风味", "rum.jpg"),
                ("Tequila", "龙舌兰", "White Spirit", 38.0, "Agave, Earthy", "墨西哥",
                 "由蓝色龙舌兰制成，风味独特", "tequila.jpg"),
                ("Whiskey", "威士忌", "Brown Spirit", 40.0, "Oak, Vanilla", "苏格兰/美国",
                 "在橡木桶中陈酿，风味复杂", "whiskey.jpg"),
                ("Brandy", "白兰地", "Brown Spirit", 40.0, "Fruity, Oak", "法国",
                 "由葡萄酒蒸馏而成，果香浓郁", "brandy.jpg")
            ]

            cursor.executemany('''
                INSERT INTO base_spirits 
                (name, chinese_name, category, alcohol_content, flavor_profile, origin, description, image_path)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', base_spirits)
            self.conn.commit()
            print("基酒数据插入成功")
        else:
            print("基酒数据已存在，跳过插入")

    def insert_cocktails(self):
        """插入鸡尾酒数据"""
        cursor = self.conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM cocktails")
        count = cursor.fetchone()[0]

        if count == 0:
            cocktails = [
                ("Mojito", "莫吉托", "Beginner", "Medium", "Highball Glass", 3,
                 "1. 薄荷叶和糖放入杯中\n2. 挤入青柠汁\n3. 捣压薄荷\n4. 加冰\n5. 倒入朗姆酒\n6. 加苏打水搅拌",
                 '[{"name": "White Rum", "amount": "60ml"}, {"name": "Lime Juice", "amount": "30ml"}, '
                 '{"name": "Mint Leaves", "amount": "10 leaves"}, {"name": "Sugar", "amount": "2 tsp"}, '
                 '{"name": "Soda Water", "amount": "top up"}]',
                 "Refreshing, Minty, Citrusy", "Summer, Parties", "¥60-100", 5, 95),

                ("Margarita", "玛格丽特", "Intermediate", "Medium", "Margarita Glass", 4,
                 "1. 杯口沾盐\n2. 摇酒器中加冰\n3. 加入龙舌兰、君度、青柠汁\n4. 摇匀\n5. 滤入杯中",
                 '[{"name": "Tequila", "amount": "60ml"}, {"name": "Cointreau", "amount": "30ml"}, '
                 '{"name": "Lime Juice", "amount": "30ml"}]',
                 "Citrusy, Salty, Strong", "Parties, Celebrations", "¥70-120", 7, 90),

                ("Old Fashioned", "古典鸡尾酒", "Advanced", "Strong", "Old Fashioned Glass", 5,
                 "1. 方糖加苦精捣化\n2. 加威士忌\n3. 加冰搅拌\n4. 橙皮装饰",
                 '[{"name": "Bourbon Whiskey", "amount": "60ml"}, {"name": "Sugar Cube", "amount": "1"}, '
                 '{"name": "Angostura Bitters", "amount": "2 dashes"}, {"name": "Orange Peel", "amount": "1"}]',
                 "Strong, Bitter, Sweet", "Evening, Winter", "¥80-150", 8, 88),

                ("Martini", "马天尼", "Expert", "Strong", "Martini Glass", 1,
                 "1. 调酒杯加冰\n2. 加入金酒和味美思\n3. 搅拌至冷却\n4. 滤入冰镇杯中\n5. 橄榄或柠檬皮装饰",
                 '[{"name": "Gin", "amount": "75ml"}, {"name": "Dry Vermouth", "amount": "15ml"}]',
                 "Dry, Strong, Crisp", "Sophisticated Events", "¥90-180", 10, 85)
            ]

            cursor.executemany('''
                INSERT INTO cocktails 
                (name, chinese_name, difficulty, alcohol_level, glassware, base_spirit_id, 
                 instructions, ingredients, flavor_profile, occasion, price_range, prep_time, popularity)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', cocktails)
            self.conn.commit()
            print("鸡尾酒数据插入成功")
        else:
            print("鸡尾酒数据已存在，跳过插入")

    def insert_techniques(self):
        """插入调酒手法数据"""
        cursor = self.conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM techniques")
        count = cursor.fetchone()[0]

        if count == 0:
            techniques = [
                ("Shaking", "摇和法", "Basic", "通过剧烈摇晃混合饮料，使其冷却并稀释",
                 "1. 在摇酒器中加冰\n2. 加入所有液体原料\n3. 盖上摇酒器\n4. 用力摇晃10-15秒\n5. 滤入杯中",
                 "Boston Shaker, Strainer", "Beginner", "https://example.com/shaking"),

                ("Stirring", "调和法", "Basic", "轻柔搅拌混合饮料，避免过度稀释",
                 "1. 调酒杯中加冰\n2. 加入原料\n3. 用吧匙搅拌30秒\n4. 滤入杯中",
                 "Mixing Glass, Bar Spoon", "Beginner", "https://example.com/stirring"),

                ("Muddling", "捣压法", "Basic", "通过捣压释放水果和香草的风味",
                 "1. 将固体原料放入杯中\n2. 用捣棒轻轻压榨\n3. 注意不要过度捣压",
                 "Muddler", "Beginner", "https://example.com/muddling"),

                ("Layering", "分层法", "Advanced", "通过密度不同制作分层效果",
                 "1. 按密度从大到小添加原料\n2. 使用吧匙缓冲\n3. 缓慢倒入",
                 "Bar Spoon", "Advanced", "https://example.com/layering")
            ]

            cursor.executemany('''
                INSERT INTO techniques 
                (name, chinese_name, category, description, steps, tools_required, difficulty, video_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', techniques)
            self.conn.commit()
            print("调酒手法数据插入成功")
        else:
            print("调酒手法数据已存在，跳过插入")

    def insert_food_pairings(self):
        """插入食物搭配数据"""
        cursor = self.conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM food_pairings")
        count = cursor.fetchone()[0]

        if count == 0:
            pairings = [
                (1, "Seafood", "清爽的莫吉托与海鲜完美搭配", 5),
                (2, "Mexican Food", "玛格丽特与墨西哥菜是天作之合", 5),
                (3, "Steak", "古典鸡尾酒与牛排的绝佳组合", 4),
                (4, "Olives", "马天尼与橄榄或坚果是经典搭配", 4)
            ]

            cursor.executemany('''
                INSERT INTO food_pairings 
                (cocktail_id, food_type, pairing_description, rating)
                VALUES (?, ?, ?, ?)
            ''', pairings)
            self.conn.commit()
            print("食物搭配数据插入成功")
        else:
            print("食物搭配数据已存在，跳过插入")

    def get_all_cocktails(self):
        """获取所有鸡尾酒"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT c.*, b.chinese_name as base_spirit_name 
            FROM cocktails c 
            LEFT JOIN base_spirits b ON c.base_spirit_id = b.id
            ORDER BY c.popularity DESC
        """)
        columns = [column[0] for column in cursor.description]
        cocktails = []
        for row in cursor.fetchall():
            cocktail = dict(zip(columns, row))
            # 解析JSON格式的ingredients
            if cocktail['ingredients']:
                try:
                    cocktail['ingredients'] = json.loads(cocktail['ingredients'])
                except:
                    cocktail['ingredients'] = []
            else:
                cocktail['ingredients'] = []
            cocktails.append(cocktail)
        return cocktails


class CocktailAssistantApp:
    """调酒助手应用程序 - 修复数据库问题版本"""

    def __init__(self, root):
        self.root = root

        # 初始化数据库
        try:
            self.db = DatabaseManager()
            self.db.insert_sample_data()
            print("数据库初始化成功")
        except Exception as e:
            print(f"数据库初始化失败: {e}")
            # 尝试重置数据库
            try:
                self.db = DatabaseManager()
                self.db.reset_database()
                self.db.insert_sample_data()
                print("数据库重置并初始化成功")
            except Exception as e2:
                print(f"数据库重置失败: {e2}")
                # 使用内存数据库作为后备
                self.use_fallback_data()

        # 用户状态
        self.current_page = "welcome"
        self.user_preferences = {
            "mood": None,
            "occasion": None,
            "alcohol_preference": None,
            "available_ingredients": []
        }

        # 应用配置
        self.setup_config()

        # 创建UI
        self.create_widgets()

        # 显示欢迎页面
        self.show_welcome_page()

    def use_fallback_data(self):
        """使用后备数据（当数据库不可用时）"""
        self.db = None
        print("使用后备数据模式")

    def setup_config(self):
        """应用配置"""
        self.colors = {
            "primary": "#2c3e50",
            "secondary": "#3498db",
            "accent": "#e74c3c",
            "success": "#2ecc71",
            "warning": "#f39c12",
            "light": "#ecf0f1",
            "dark": "#34495e",
            "background": "#ffffff"
        }

        self.fonts = {
            "title": ("Microsoft YaHei", 20, "bold"),
            "heading": ("Microsoft YaHei", 16, "bold"),
            "body": ("Microsoft YaHei", 12),
            "small": ("Microsoft YaHei", 10)
        }

    def create_widgets(self):
        """创建主界面"""
        # 设置窗口
        self.root.title("🍸 调酒小白助手")
        self.root.geometry("1000x700")

        # 设置窗口图标（如果有）
        try:
            self.root.iconbitmap('cocktail.ico')
        except:
            pass

        # 主容器
        self.main_container = tk.Frame(self.root, bg=self.colors["background"])
        self.main_container.pack(fill="both", expand=True)

        # 创建侧边栏
        self.create_sidebar()

        # 创建主内容区
        self.content_area = tk.Frame(self.main_container, bg=self.colors["background"])
        self.content_area.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def create_sidebar(self):
        """创建侧边栏导航"""
        sidebar = tk.Frame(self.main_container, bg=self.colors["dark"], width=200)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # 标题
        title_label = tk.Label(sidebar, text="调酒助手",
                               font=("Microsoft YaHei", 18, "bold"),
                               bg=self.colors["dark"], fg="white")
        title_label.pack(pady=30)

        # 导航按钮
        nav_items = [
            ("🏠", "首页", self.show_welcome_page),
            ("🔍", "配方查询", self.show_search_page),
            ("🥃", "基酒学习", self.show_spirits_page),
            ("🎯", "智能推荐", self.show_recommendation_page),
            ("🛠️", "调酒手法", self.show_techniques_page),
            ("🎮", "互动测验", self.show_quiz_page),
            ("💡", "小贴士", self.show_tips_page)
        ]

        for icon, text, command in nav_items:
            btn = tk.Button(sidebar, text=f"{icon} {text}",
                            font=("Microsoft YaHei", 11),
                            bg=self.colors["dark"], fg="white",
                            bd=0, padx=15, pady=10,
                            anchor="w",
                            command=command)
            btn.pack(fill="x", padx=10, pady=2)

        # 分隔线
        tk.Frame(sidebar, height=2, bg="#7f8c8d").pack(fill="x", pady=20, padx=10)

        # 快速入口
        quick_items = [
            ("🍸", "经典配方", self.show_classic_recipes),
            ("📖", "新手入门", self.show_beginner_guide),
            ("💰", "预算估算", self.show_budget_estimator)
        ]

        tk.Label(sidebar, text="快速入口",
                 font=("Microsoft YaHei", 10, "bold"),
                 bg=self.colors["dark"], fg="#bdc3c7").pack(anchor="w", padx=15, pady=(0, 10))

        for icon, text, command in quick_items:
            btn = tk.Button(sidebar, text=f"{icon} {text}",
                            font=("Microsoft YaHei", 10),
                            bg="#34495e", fg="#ecf0f1",
                            bd=0, padx=15, pady=8,
                            anchor="w",
                            command=command)
            btn.pack(fill="x", padx=10, pady=1)

    def clear_content(self):
        """清空内容区"""
        for widget in self.content_area.winfo_children():
            widget.destroy()

    # ========== 页面显示函数 ==========

    def show_welcome_page(self):
        """显示欢迎页面"""
        self.clear_content()

        # 欢迎标题
        title_frame = tk.Frame(self.content_area, bg=self.colors["background"])
        title_frame.pack(pady=30)

        tk.Label(title_frame, text="🍹 调酒小白助手",
                 font=("Microsoft YaHei", 28, "bold"),
                 bg=self.colors["background"],
                 fg=self.colors["primary"]).pack()

        tk.Label(title_frame, text="从零开始学调酒，轻松成为家庭调酒师",
                 font=("Microsoft YaHei", 14),
                 bg=self.colors["background"],
                 fg="#7f8c8d").pack(pady=10)

        # 功能简介卡片
        cards_frame = tk.Frame(self.content_area, bg=self.colors["background"])
        cards_frame.pack(fill="both", expand=True, padx=20, pady=20)

        features = [
            ("🔍", "配方查询", "300+经典鸡尾酒配方，详细步骤解析", self.show_search_page),
            ("🎯", "智能推荐", "根据你的口味和场合推荐鸡尾酒", self.show_recommendation_page),
            ("📚", "基酒知识", "六大基酒详细知识与风味特点", self.show_spirits_page),
            ("🛠️", "手法教学", "摇和、调和等调酒基础手法", self.show_techniques_page),
            ("🍽️", "食物搭配", "餐酒搭配的专业建议", lambda: messagebox.showinfo("功能", "食物搭配功能开发中")),
            ("🎮", "互动测验", "测试你的调酒知识", self.show_quiz_page)
        ]

        for i, (icon, title, desc, command) in enumerate(features):
            row = i // 3
            col = i % 3

            card = tk.Frame(cards_frame, bg="white", relief="solid", bd=1)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            card.grid_propagate(False)
            card.config(width=250, height=150)

            # 卡片内容
            tk.Label(card, text=icon, font=("", 24), bg="white").pack(pady=10)
            tk.Label(card, text=title, font=("Microsoft YaHei", 14, "bold"), bg="white").pack()
            tk.Label(card, text=desc, font=("Microsoft YaHei", 10),
                     bg="white", wraplength=200, fg="#7f8c8d").pack(pady=5, padx=10)

            tk.Button(card, text="进入",
                      font=("Microsoft YaHei", 10),
                      bg=self.colors["primary"], fg="white",
                      padx=20,
                      command=command).pack(pady=10)

        # 配置网格
        for i in range(3):
            cards_frame.columnconfigure(i, weight=1)
        for i in range(2):
            cards_frame.rowconfigure(i, weight=1)

    def show_search_page(self):
        """显示配方查询页面"""
        self.clear_content()

        # 搜索区域
        search_frame = tk.Frame(self.content_area, bg=self.colors["background"])
        search_frame.pack(fill="x", pady=20, padx=20)

        tk.Label(search_frame, text="搜索鸡尾酒配方",
                 font=self.fonts["heading"],
                 bg=self.colors["background"]).pack(anchor="w", pady=(0, 15))

        # 搜索框
        search_box = tk.Frame(search_frame, bg="white", relief="solid", bd=1)
        search_box.pack(fill="x")

        tk.Entry(search_box, font=self.fonts["body"],
                 bd=0, relief="flat").pack(side="left", fill="both", expand=True, padx=10, pady=10)

        tk.Button(search_box, text="搜索",
                  font=self.fonts["body"],
                  bg=self.colors["primary"], fg="white",
                  padx=20,
                  command=lambda: self.perform_search()).pack(side="right", padx=10, pady=10)

        # 分类筛选
        filter_frame = tk.Frame(self.content_area, bg=self.colors["background"])
        filter_frame.pack(fill="x", pady=10, padx=20)

        categories = ["全部", "经典款", "夏日特饮", "派对必备", "低酒精", "新手友好"]
        for cat in categories:
            tk.Button(filter_frame, text=cat,
                      font=("Microsoft YaHei", 10),
                      bg=self.colors["light"], fg=self.colors["dark"],
                      relief="solid", bd=1,
                      command=lambda c=cat: self.filter_by_category(c)).pack(side="left", padx=5)

        # 结果区域
        results_frame = tk.Frame(self.content_area, bg=self.colors["background"])
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # 显示热门配方
        self.display_hot_cocktails(results_frame)

    def display_hot_cocktails(self, parent):
        """显示热门鸡尾酒"""
        # 从数据库获取数据
        if self.db:
            cocktails = self.db.get_all_cocktails()
        else:
            # 使用后备数据
            cocktails = [
                {"id": 1, "name": "Mojito", "chinese_name": "莫吉托", "difficulty": "入门",
                 "alcohol_level": "中度", "flavor_profile": "清爽、薄荷香"},
                {"id": 2, "name": "Margarita", "chinese_name": "玛格丽特", "difficulty": "简单",
                 "alcohol_level": "中度", "flavor_profile": "柑橘、咸鲜"},
                {"id": 3, "name": "Gin & Tonic", "chinese_name": "金汤力", "difficulty": "入门",
                 "alcohol_level": "低度", "flavor_profile": "清爽、微苦"},
                {"id": 4, "name": "Old Fashioned", "chinese_name": "古典", "difficulty": "中等",
                 "alcohol_level": "高度", "flavor_profile": "浓郁、苦涩"}
            ]

        # 创建滚动区域
        canvas = tk.Canvas(parent, bg=self.colors["background"])
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors["background"])

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # 显示鸡尾酒列表
        for i, cocktail in enumerate(cocktails[:10]):  # 只显示前10个
            self.create_cocktail_card(scrollable_frame, cocktail, i)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_cocktail_card(self, parent, cocktail, index):
        """创建鸡尾酒卡片"""
        card = tk.Frame(parent, bg="white", relief="solid", bd=1)
        card.pack(fill="x", pady=5, padx=5)

        # 左侧：图标和名称
        left_frame = tk.Frame(card, bg="white")
        left_frame.pack(side="left", fill="y", padx=15, pady=10)

        tk.Label(left_frame, text="🍸", font=("", 24), bg="white").pack()
        tk.Label(left_frame, text=cocktail.get("chinese_name", cocktail["name"]),
                 font=("Microsoft YaHei", 14, "bold"), bg="white").pack()

        # 中间：详细信息
        mid_frame = tk.Frame(card, bg="white")
        mid_frame.pack(side="left", fill="both", expand=True, padx=20, pady=10)

        info_text = f"难度: {cocktail.get('difficulty', '未知')} | "
        info_text += f"酒精度: {cocktail.get('alcohol_level', '未知')} | "
        info_text += f"风味: {cocktail.get('flavor_profile', '未知')}"

        tk.Label(mid_frame, text=info_text,
                 font=("Microsoft YaHei", 10), bg="white", fg="#7f8c8d").pack(anchor="w")

        # 右侧：操作按钮
        right_frame = tk.Frame(card, bg="white")
        right_frame.pack(side="right", padx=15, pady=10)

        tk.Button(right_frame, text="查看详情",
                  font=("Microsoft YaHei", 10),
                  bg=self.colors["primary"], fg="white",
                  padx=15,
                  command=lambda c=cocktail: self.show_cocktail_detail(c)).pack(pady=2)

        tk.Button(right_frame, text="⭐ 收藏",
                  font=("Microsoft YaHei", 10),
                  bg="#f1c40f", fg="white",
                  padx=15,
                  command=lambda: self.add_to_favorites(cocktail["id"])).pack(pady=2)

    def show_cocktail_detail(self, cocktail):
        """显示鸡尾酒详情"""
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"{cocktail.get('chinese_name', cocktail['name'])} - 详情")
        detail_window.geometry("700x800")

        # 创建滚动区域
        canvas = tk.Canvas(detail_window, bg="white")
        scrollbar = ttk.Scrollbar(detail_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # 标题
        title_frame = tk.Frame(scrollable_frame, bg="white")
        title_frame.pack(fill="x", pady=20, padx=30)

        tk.Label(title_frame, text=cocktail.get("chinese_name", cocktail["name"]),
                 font=("Microsoft YaHei", 24, "bold"), bg="white").pack()
        tk.Label(title_frame, text=cocktail["name"],
                 font=("Microsoft YaHei", 14), bg="white", fg="#7f8c8d").pack(pady=5)

        # 基本信息
        info_frame = tk.Frame(scrollable_frame, bg="#f8f9fa")
        info_frame.pack(fill="x", pady=10, padx=30)

        infos = [
            ("难度", cocktail.get("difficulty", "未知")),
            ("酒精度", cocktail.get("alcohol_level", "未知")),
            ("准备时间", f"{cocktail.get('prep_time', '?')}分钟"),
            ("适合场合", cocktail.get("occasion", "通用"))
        ]

        for i, (label, value) in enumerate(infos):
            tk.Label(info_frame, text=f"{label}: {value}",
                     font=("Microsoft YaHei", 11), bg="#f8f9fa").grid(
                row=i // 2, column=i % 2, sticky="w", padx=20, pady=10)

        # 配方部分
        recipe_frame = tk.Frame(scrollable_frame, bg="white")
        recipe_frame.pack(fill="x", pady=20, padx=30)

        tk.Label(recipe_frame, text="📝 配方",
                 font=("Microsoft YaHei", 16, "bold"), bg="white").pack(anchor="w", pady=(0, 15))

        # 显示原料（如果有）
        if 'ingredients' in cocktail and cocktail['ingredients']:
            for ing in cocktail['ingredients']:
                if isinstance(ing, dict):
                    tk.Label(recipe_frame, text=f"• {ing.get('name', '')}: {ing.get('amount', '')}",
                             font=("Microsoft YaHei", 11), bg="white").pack(anchor="w")

        # 制作步骤
        steps_frame = tk.Frame(scrollable_frame, bg="white")
        steps_frame.pack(fill="x", pady=20, padx=30)

        tk.Label(steps_frame, text="👨‍🍳 制作步骤",
                 font=("Microsoft YaHei", 16, "bold"), bg="white").pack(anchor="w", pady=(0, 15))

        instructions = cocktail.get("instructions", "暂无详细步骤")
        if instructions:
            step_lines = instructions.split('\n')
            for step in step_lines:
                tk.Label(steps_frame, text=step,
                         font=("Microsoft YaHei", 11), bg="white",
                         wraplength=600, justify="left").pack(anchor="w", pady=2)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def add_to_favorites(self, cocktail_id):
        """添加到收藏"""
        messagebox.showinfo("收藏", "已添加到收藏夹")

    def perform_search(self):
        """执行搜索"""
        messagebox.showinfo("搜索", "搜索功能开发中")

    def filter_by_category(self, category):
        """按分类筛选"""
        messagebox.showinfo("筛选", f"按'{category}'筛选")

    def show_spirits_page(self):
        """显示基酒学习页面"""
        self.clear_content()

        tk.Label(self.content_area, text="基酒知识",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)

        # 创建标签页
        notebook = ttk.Notebook(self.content_area)
        notebook.pack(fill="both", expand=True, padx=20, pady=10)

        # 六大基酒
        spirits = [
            ("金酒", "杜松子风味，草本植物香气", "经典鸡尾酒：金汤力、马天尼"),
            ("伏特加", "纯净中性，适合各种调酒", "经典鸡尾酒：莫斯科骡子、血腥玛丽"),
            ("朗姆酒", "甘蔗制成，甜味浓郁", "经典鸡尾酒：莫吉托、椰林飘香"),
            ("龙舌兰", "龙舌兰植物发酵蒸馏", "经典鸡尾酒：玛格丽特、龙舌兰日出"),
            ("威士忌", "橡木桶陈酿，风味复杂", "经典鸡尾酒：古典、曼哈顿"),
            ("白兰地", "葡萄酒蒸馏，果香浓郁", "经典鸡尾酒：白兰地亚历山大")
        ]

        for name, desc, example in spirits:
            frame = tk.Frame(notebook, bg="white")
            notebook.add(frame, text=name)

            # 内容
            tk.Label(frame, text=name,
                     font=("Microsoft YaHei", 20, "bold"), bg="white").pack(pady=20)

            tk.Label(frame, text=desc,
                     font=("Microsoft YaHei", 14), bg="white",
                     wraplength=600).pack(pady=10, padx=30)

            tk.Label(frame, text=example,
                     font=("Microsoft YaHei", 12), bg="white", fg="#7f8c8d",
                     wraplength=600).pack(pady=20, padx=30)

    def show_recommendation_page(self):
        """显示智能推荐页面"""
        self.clear_content()

        tk.Label(self.content_area, text="智能推荐",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)

        # 推荐选项
        options_frame = tk.Frame(self.content_area, bg=self.colors["background"])
        options_frame.pack(pady=20, padx=50)

        # 心情选择
        tk.Label(options_frame, text="你今天的心情如何？",
                 font=("Microsoft YaHei", 14, "bold"),
                 bg=self.colors["background"]).grid(row=0, column=0, columnspan=5, sticky="w", pady=(0, 15))

        moods = [("😌", "放松"), ("🎉", "兴奋"), ("💕", "浪漫"), ("🥳", "庆祝"), ("😔", "消愁")]
        self.mood_var = tk.StringVar(value="")

        for i, (icon, mood) in enumerate(moods):
            frame = tk.Frame(options_frame, bg=self.colors["background"])
            frame.grid(row=1, column=i, padx=5)

            tk.Radiobutton(frame, text=icon, variable=self.mood_var,
                           value=mood, font=("", 20), bg=self.colors["background"],
                           indicatoron=0, width=3, height=2).pack()
            tk.Label(frame, text=mood, font=("Microsoft YaHei", 10),
                     bg=self.colors["background"]).pack()

        # 场合选择
        tk.Label(options_frame, text="什么场合？",
                 font=("Microsoft YaHei", 14, "bold"),
                 bg=self.colors["background"]).grid(row=2, column=0, columnspan=5, sticky="w", pady=(30, 15))

        occasions = [("🏠", "家庭"), ("🎊", "派对"), ("💑", "约会"), ("🧘", "独处"), ("💼", "商务")]
        self.occasion_var = tk.StringVar(value="")

        for i, (icon, occasion) in enumerate(occasions):
            frame = tk.Frame(options_frame, bg=self.colors["background"])
            frame.grid(row=3, column=i, padx=5)

            tk.Radiobutton(frame, text=icon, variable=self.occasion_var,
                           value=occasion, font=("", 20), bg=self.colors["background"],
                           indicatoron=0, width=3, height=2).pack()
            tk.Label(frame, text=occasion, font=("Microsoft YaHei", 10),
                     bg=self.colors["background"]).pack()

        # 酒精度偏好
        tk.Label(options_frame, text="酒精度偏好？",
                 font=("Microsoft YaHei", 14, "bold"),
                 bg=self.colors["background"]).grid(row=4, column=0, columnspan=5, sticky="w", pady=(30, 15))

        alcohol_levels = [("🍹", "低度"), ("🍸", "中度"), ("🥃", "高度")]
        self.alcohol_var = tk.StringVar(value="")

        for i, (icon, level) in enumerate(alcohol_levels):
            frame = tk.Frame(options_frame, bg=self.colors["background"])
            frame.grid(row=5, column=i, padx=20)

            tk.Radiobutton(frame, text=icon, variable=self.alcohol_var,
                           value=level, font=("", 20), bg=self.colors["background"],
                           indicatoron=0, width=3, height=2).pack()
            tk.Label(frame, text=level, font=("Microsoft YaHei", 10),
                     bg=self.colors["background"]).pack()

        # 推荐按钮
        tk.Button(self.content_area, text="🍹 获取推荐",
                  font=("Microsoft YaHei", 16, "bold"),
                  bg="#e74c3c", fg="white",
                  padx=40, pady=15,
                  command=self.get_recommendations).pack(pady=30)

    def get_recommendations(self):
        """获取推荐结果"""
        mood = self.mood_var.get()
        occasion = self.occasion_var.get()
        alcohol = self.alcohol_var.get()

        if not mood or not occasion or not alcohol:
            messagebox.showwarning("提示", "请完成所有选项！")
            return

        # 根据选择推荐（简化逻辑）
        recommendations = []
        if mood == "放松" and alcohol == "低度":
            recommendations.append(("金汤力", "清爽简单，放松首选"))
        if occasion == "派对":
            recommendations.append(("莫吉托", "派对必备，清爽解渴"))
        if alcohol == "高度":
            recommendations.append(("古典", "浓郁醇厚，慢慢品味"))

        if not recommendations:
            recommendations = [
                ("莫吉托", "经典选择，不会出错"),
                ("金汤力", "清爽简单，适合新手")
            ]

        # 显示结果
        results_window = tk.Toplevel(self.root)
        results_window.title("推荐结果")
        results_window.geometry("500x400")

        tk.Label(results_window, text="为你推荐：",
                 font=("Microsoft YaHei", 18, "bold")).pack(pady=20)

        for i, (name, desc) in enumerate(recommendations):
            frame = tk.Frame(results_window, bg="#f8f9fa")
            frame.pack(fill="x", padx=50, pady=10)

            tk.Label(frame, text=name,
                     font=("Microsoft YaHei", 16, "bold"), bg="#f8f9fa").pack(anchor="w")
            tk.Label(frame, text=desc,
                     font=("Microsoft YaHei", 12), bg="#f8f9fa", fg="#7f8c8d").pack(anchor="w")

    def show_techniques_page(self):
        """显示调酒手法页面"""
        self.clear_content()

        tk.Label(self.content_area, text="调酒手法",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)

        techniques = [
            ("摇和法 (Shaking)", "适合含果汁、糖浆的鸡尾酒", "用力摇晃10-15秒"),
            ("调和法 (Stirring)", "适合纯烈酒鸡尾酒", "轻柔搅拌30秒"),
            ("捣压法 (Muddling)", "释放水果和香草风味", "轻轻压榨，避免过度"),
            ("分层法 (Layering)", "制作分层视觉效果", "按密度缓慢倒入")
        ]

        for name, desc, tip in techniques:
            frame = tk.Frame(self.content_area, bg="white", relief="solid", bd=1)
            frame.pack(fill="x", padx=50, pady=10)

            tk.Label(frame, text=name,
                     font=("Microsoft YaHei", 16, "bold"), bg="white").pack(anchor="w", padx=20, pady=10)
            tk.Label(frame, text=desc,
                     font=("Microsoft YaHei", 12), bg="white").pack(anchor="w", padx=20)
            tk.Label(frame, text=f"💡 小贴士: {tip}",
                     font=("Microsoft YaHei", 10), bg="white", fg="#7f8c8d").pack(anchor="w", padx=20, pady=(0, 10))

    def show_quiz_page(self):
        """显示互动测验页面"""
        self.clear_content()

        tk.Label(self.content_area, text="调酒知识测验",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)

        # 测验问题
        question_frame = tk.Frame(self.content_area, bg="white", relief="solid", bd=1)
        question_frame.pack(fill="x", padx=50, pady=20)

        tk.Label(question_frame, text="1. 莫吉托的基酒是什么？",
                 font=("Microsoft YaHei", 14, "bold"), bg="white").pack(pady=15)

        # 选项
        options_frame = tk.Frame(question_frame, bg="white")
        options_frame.pack(pady=10)

        options = ["金酒", "朗姆酒", "伏特加", "龙舌兰"]
        self.quiz_answer = tk.StringVar(value="")

        for option in options:
            tk.Radiobutton(options_frame, text=option, variable=self.quiz_answer,
                           value=option, font=("Microsoft YaHei", 12), bg="white").pack(anchor="w", pady=5)

        # 提交按钮
        tk.Button(question_frame, text="提交答案",
                  font=("Microsoft YaHei", 12),
                  bg=self.colors["primary"], fg="white",
                  padx=20,
                  command=self.check_quiz_answer).pack(pady=20)

    def check_quiz_answer(self):
        """检查测验答案"""
        answer = self.quiz_answer.get()
        if answer == "朗姆酒":
            messagebox.showinfo("正确！", "恭喜你答对了！")
        else:
            messagebox.showerror("错误", f"正确答案是：朗姆酒\n你的答案：{answer}")

    def show_tips_page(self):
        """显示小贴士页面"""
        self.clear_content()

        tk.Label(self.content_area, text="调酒师小贴士",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)

        tips = [
            "💡 使用新鲜柠檬汁，不要用浓缩汁",
            "🧊 鸡尾酒中冰块越大，融化越慢",
            "🔄 摇和法的时间控制在10-15秒最佳",
            "❄️ 调酒前先将杯子冰镇",
            "🌿 装饰不只是装饰，也能增添风味",
            "👃 品酒前先闻香，感受香气层次",
            "👅 调酒时先尝后调，找到最适合的比例",
            "📏 没有量杯？一小杯≈30ml，一汤匙≈15ml"
        ]

        for tip in tips:
            frame = tk.Frame(self.content_area, bg="white", relief="solid", bd=1)
            frame.pack(fill="x", padx=50, pady=5)

            tk.Label(frame, text=tip,
                     font=("Microsoft YaHei", 12), bg="white").pack(padx=20, pady=10)

    def show_classic_recipes(self):
        """显示经典配方"""
        self.clear_content()
        tk.Label(self.content_area, text="经典配方",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)
        tk.Label(self.content_area, text="功能开发中...",
                 font=self.fonts["body"],
                 bg=self.colors["background"]).pack(pady=50)

    def show_beginner_guide(self):
        """显示新手入门"""
        self.clear_content()
        tk.Label(self.content_area, text="新手入门",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)
        tk.Label(self.content_area, text="功能开发中...",
                 font=self.fonts["body"],
                 bg=self.colors["background"]).pack(pady=50)

    def show_budget_estimator(self):
        """显示预算估算"""
        self.clear_content()
        tk.Label(self.content_area, text="预算估算",
                 font=self.fonts["title"],
                 bg=self.colors["background"]).pack(pady=20)
        tk.Label(self.content_area, text="功能开发中...",
                 font=self.fonts["body"],
                 bg=self.colors["background"]).pack(pady=50)


def main():
    """主函数"""
    try:
        root = tk.Tk()
        app = CocktailAssistantApp(root)
        root.mainloop()
    except Exception as e:
        print(f"程序启动失败: {e}")
        import traceback
        traceback.print_exc()

        # 简化版本作为后备
        simple_main()


def simple_main():
    """简化版本"""
    root = tk.Tk()
    root.title("调酒助手 - 简化版")
    root.geometry("800x600")

    tk.Label(root, text="🍹 调酒助手",
             font=("Microsoft YaHei", 24, "bold")).pack(pady=30)

    features = [
        "1. 查询经典鸡尾酒配方",
        "2. 学习基酒知识与风味",
        "3. 根据偏好智能推荐",
        "4. 调酒手法教学",
        "5. 互动测验和酒精度计算"
    ]

    for feature in features:
        tk.Label(root, text=feature,
                 font=("Microsoft YaHei", 14)).pack(pady=5)

    # 直接访问按钮
    tk.Button(root, text="查看经典配方",
              font=("Microsoft YaHei", 12),
              padx=30, pady=10).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()