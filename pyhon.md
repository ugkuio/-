
# Python程序设计基础大作业
## 题目：调酒助手
## 班级: 测控四班
## 姓名: 刘佳佳
## 学号: 3023202172

# 项目名称 (Project Name)
# 调酒助手小程序

调酒助手是一款为调酒初学者设计的智能桌面应用程序，提供配方查询、基酒学习、智能推荐等功能，帮助用户轻松入门调酒。

## 项目简介 (Description)


调酒助手是一款专为调酒初学者设计的桌面应用程序，它解决了新手在入门调酒时面临的三大核心难题：不知道从何学起、担心成本过高、害怕操作复杂。通过将专业的调酒知识系统化、直观化，本应用降低了调酒学习的门槛，让每个人都能在家中轻松制作出专业级的鸡尾酒。

# 主要功能与解决的问题
1. 智能配方查询系统
功能：集成300+经典鸡尾酒配方数据库，支持关键词搜索、分类筛选和详细步骤展示

解决问题：传统学习方式需要购买多本调酒书籍或在不同网站查找，信息分散且质量参差不齐。本应用将所有配方集中管理，确保信息的准确性和完整性。

2. 基酒知识库
功能：详细解析六大基酒（金酒、伏特加、朗姆酒、龙舌兰、威士忌、白兰地）的风味特点、产地故事和搭配建议

解决问题：初学者往往对基酒种类和特性感到困惑，本应用通过系统化的分类和直观的讲解，帮助用户建立完整的基酒知识体系。

3. 个性化智能推荐
功能：基于用户的心情、场合和酒精度偏好，通过算法推荐最合适的鸡尾酒

解决问题：面对众多配方，初学者往往不知道如何选择。智能推荐系统根据用户的具体需求提供个性化建议，减少选择困难。

4. 调酒手法教学
功能：四种基础调酒手法（摇和法、调和法、捣压法、分层法）的详细图文教学

解决问题：调酒手法是调酒的核心技能，但视频教程往往不够系统。本应用将每种手法分解为具体步骤，配合注意事项，帮助用户掌握正确技巧。

5. 互动学习体验
功能：调酒知识小测验、收藏功能、步骤追踪

解决问题：传统学习方式单调枯燥，本应用通过测验和互动元素增加学习趣味性，帮助巩固知识。

# 技术特性与创新
1. 现代化桌面应用架构
使用Python的tkinter框架构建响应式图形界面，支持Windows、macOS和Linux多平台

采用MVC（模型-视图-控制器）设计模式，确保代码的可维护性和可扩展性

2. 智能数据管理系统
SQLite数据库存储所有配方和用户数据，支持本地化管理和隐私保护

实现动态数据库迁移机制，支持应用的无缝升级和数据扩展

3. 用户体验优化设计
侧边栏导航系统，直观的功能分区和快速访问

卡片式布局配合滚动区域，适应不同屏幕尺寸

完善的错误处理和用户反馈机制，提升应用稳定性

4. 可扩展的模块化设计
每个功能模块独立开发，支持插件式扩展

预留API接口，未来可支持在线更新和社区分享功能

# 项目特色与价值
1. 教育性与实用性的平衡
不仅提供配方，更注重调酒原理和技巧的教学

从理论到实践的全方位指导，培养用户的调酒思维

2. 成本控制的现实考量
提供预算估算功能，帮助用户合理规划调酒设备采购

推荐替代材料和工具，降低入门门槛

3. 专业内容的通俗化呈现
将专业的调酒术语转化为通俗易懂的语言

通过图标、颜色和视觉元素增强信息传达效果

4. 持续学习与进步追踪
收藏功能记录用户喜欢的配方


## 难度等级介绍

根据大作业难度等级评定标准，本项目评定为四星难度。

# 符合四星难度的具体条款和原因分析：
1. 使用中型框架实现较为复杂的图形界面 
框架选择：本项目使用tkinter作为GUI框架，tkinter是Python的标准GUI工具包，属于中型框架

界面复杂度：

实现了侧边栏导航系统，支持8个主要功能模块

多页面内容管理系统，支持页面切换和状态保持

卡片式布局设计，美观且用户友好

滚动区域和复杂布局控件（Canvas、Notebook等）

多窗口管理（主窗口+多个子窗口）

2. 综合多种Python应用场景，实现较为复杂的桌面应用程序开发 
数据库应用：使用SQLite实现数据持久化，设计了5个数据表（基酒表、鸡尾酒表、手法表、搭配表、收藏表）

GUI开发：完整的图形用户界面，包括多种控件和交互元素

数据处理：JSON数据解析、结构化数据管理、数据验证

算法设计：智能推荐算法（基于用户偏好匹配）、测验评分系统

文件操作：数据库文件管理、异常处理、数据备份

面向对象编程：多个类设计（DatabaseManager、CocktailAssistantApp等）、模块化架构

3. 实现基于图形用户界面的桌面应用程序开发，并实现有意义的功能 
完整应用流程：从欢迎页面到功能选择，再到详细操作和结果展示的完整用户体验

实用功能集：8个主要功能模块，覆盖调酒学习的各个方面

专业内容：基于真实调酒知识的数据库和教学内容

用户互动：测验系统、收藏功能、个性化推荐


## 安装 (Installation)
git clone https://github.com/ugkuio/-.git
cd "cocktail-assistant"

# 直接运行
python main.py


## 使用方法（usage）
基本使用
1. 启动程序
# 克隆项目后进入目录
cd cocktail-assistant

# 运行主程序
python main.py
运行后，您将看到主界面：


2. 代码结构示例
虽然这是一个桌面应用程序，但您可以通过以下方式扩展功能：

python
# 示例：添加新的鸡尾酒到数据库
import sqlite3

def add_cocktail_to_database():
    conn = sqlite3.connect('cocktail_assistant.db')
    cursor = conn.cursor()
    
    new_cocktail = (
        "Cosmopolitan",  # 英文名
        "大都会",        # 中文名
        "Intermediate",  # 难度
        "Medium",        # 酒精度
        "Martini Glass", # 酒杯类型
        2,               # 基酒ID（2=伏特加）
        "制作步骤...",   # 制作步骤
        '[{"name": "Vodka", "amount": "45ml"}, {"name": "Cointreau", "amount": "15ml"}]',
        "Citrus, Cranberry, Sweet",  # 风味描述
        "Party, Celebration",        # 适合场合
        "¥80-120",                   # 价格范围
        7                            # 准备时间
    )
    
    cursor.execute('''
        INSERT INTO cocktails (name, chinese_name, difficulty, alcohol_level, 
                             glassware, base_spirit_id, instructions, ingredients, 
                             flavor_profile, occasion, price_range, prep_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', new_cocktail)
    
    conn.commit()
    conn.close()
    print("新鸡尾酒添加成功！")

# 调用函数
if __name__ == "__main__":
    add_cocktail_to_database()
功能使用指南
1. 配方查询功能

操作步骤：

点击侧边栏"🔍 配方查询"

在搜索框中输入鸡尾酒名称

或使用分类筛选功能

点击鸡尾酒卡片查看详细配方

代码示例（模拟搜索）：

python
# 模拟搜索功能
def search_cocktail(keyword):
    """
    搜索鸡尾酒
    :param keyword: 搜索关键词
    :return: 匹配的鸡尾酒列表
    """
    conn = sqlite3.connect('cocktail_assistant.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM cocktails 
        WHERE name LIKE ? OR chinese_name LIKE ?
        ORDER BY popularity DESC
    ''', (f'%{keyword}%', f'%{keyword}%'))
    
    results = cursor.fetchall()
    conn.close()
    return results

# 使用示例
results = search_cocktail("莫吉托")
print(f"找到 {len(results)} 个结果")
2. 智能推荐功能

操作步骤：

点击侧边栏"🎯 智能推荐"

选择心情、场合和酒精度偏好

点击"获取推荐"按钮

查看个性化推荐结果

推荐算法原理：

python
def recommend_cocktail(mood, occasion, alcohol_level):
    """
    基于用户偏好推荐鸡尾酒
    :param mood: 心情
    :param occasion: 场合
    :param alcohol_level: 酒精度偏好
    :return: 推荐鸡尾酒列表
    """
    # 推荐规则映射
    rules = {
        ("放松", "家庭", "低度"): ["Gin & Tonic", "Mojito"],
        ("庆祝", "派对", "中度"): ["Margarita", "Cosmopolitan"],
        ("浪漫", "约会", "低度"): ["Bellini", "Pina Colada"],
        ("兴奋", "派对", "高度"): ["Long Island Iced Tea", "Tequila Sunrise"],
        ("消愁", "独处", "高度"): ["Old Fashioned", "Whiskey Sour"]
    }
    
    # 查找匹配规则
    key = (mood, occasion, alcohol_level)
    if key in rules:
        return rules[key]
    else:
        # 默认推荐
        return ["Mojito", "Gin & Tonic", "Margarita"]
3. 基酒学习功能

操作步骤：

点击侧边栏"🥃 基酒学习"

选择不同的基酒标签页

查看基酒的详细信息

学习相关的鸡尾酒配方

数据库查询示例：

python
def get_spirit_details(spirit_id):
    """
    获取基酒详细信息
    :param spirit_id: 基酒ID
    :return: 基酒信息字典
    """
    conn = sqlite3.connect('cocktail_assistant.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM base_spirits WHERE id = ?
    ''', (spirit_id,))
    
    spirit = cursor.fetchone()
    
    # 获取该基酒相关的鸡尾酒
    cursor.execute('''
        SELECT name, chinese_name, difficulty 
        FROM cocktails 
        WHERE base_spirit_id = ?
        LIMIT 5
    ''', (spirit_id,))
    
    cocktails = cursor.fetchall()
    conn.close()
    
    return {
        "spirit": spirit,
        "cocktails": cocktails
    }
4. 互动测验功能

操作步骤：

点击侧边栏"🎮 互动测验"

阅读问题并选择答案

提交答案查看正确与否

学习答案解析

测验系统示例：

python
class QuizSystem:
    def __init__(self):
        self.questions = [
            {
                "question": "莫吉托的基酒是什么？",
                "options": ["金酒", "朗姆酒", "伏特加", "龙舌兰"],
                "answer": 1,
                "explanation": "莫吉托起源于古巴，使用古巴特产的白朗姆酒作为基酒。"
            },
            {
                "question": "马天尼通常用什么酒杯？",
                "options": ["马天尼杯", "古典杯", "高球杯", "飓风杯"],
                "answer": 0,
                "explanation": "马天尼杯是专门为马天尼设计的V形杯，有助于保持低温。"
            }
        ]
        self.score = 0
    
    def check_answer(self, question_index, selected_option):
        """检查答案是否正确"""
        correct = self.questions[question_index]["answer"]
        if selected_option == correct:
            self.score += 10
            return True, self.questions[question_index]["explanation"]
        else:
            return False, self.questions[question_index]["explanation"]
    
    def get_score(self):
        """获取当前分数"""
        return self.score
高级用法
1. 自定义数据库
您可以通过修改数据库来添加自己的配方：

python
import json

# 创建自定义鸡尾酒数据
custom_cocktail = {
    "name": "My Special Cocktail",
    "chinese_name": "我的特调",
    "ingredients": [
        {"name": "Vodka", "amount": "45ml"},
        {"name": "Orange Juice", "amount": "90ml"},
        {"name": "Grenadine", "amount": "15ml"}
    ],
    "instructions": "1. 加冰\n2. 倒入伏特加\n3. 加入橙汁\n4. 滴入红石榴糖浆",
    "difficulty": "Beginner"
}

# 保存为JSON文件
with open('custom_cocktails.json', 'w', encoding='utf-8') as f:
    json.dump([custom_cocktail], f, ensure_ascii=False, indent=2)
2. 扩展功能模块
您可以添加新的功能模块：

python
# new_module.py
import tkinter as tk
from tkinter import ttk

class NewFeature:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame)
        self.create_widgets()
    
    def create_widgets(self):
        """创建界面组件"""
        tk.Label(self.frame, text="新功能模块", 
                font=("Microsoft YaHei", 16, "bold")).pack(pady=20)
        
        # 添加更多组件...
    
    def get_frame(self):
        """返回框架"""
        return self.frame

# 在主程序中添加
# self.new_feature = NewFeature(self.content_area)
# self.new_feature.get_frame().pack()
3. 数据导出功能
python
def export_data(format_type="json"):
    """
    导出数据
    :param format_type: 导出格式，支持json、csv
    """
    conn = sqlite3.connect('cocktail_assistant.db')
    cursor = conn.cursor()
    
    # 获取所有鸡尾酒
    cursor.execute("SELECT * FROM cocktails")
    cocktails = cursor.fetchall()
    
    if format_type == "json":
        import json
        data = []
        for cocktail in cocktails:
            data.append({
                "name": cocktail[1],
                "chinese_name": cocktail[2],
                "ingredients": json.loads(cocktail[8]) if cocktail[8] else []
            })
        
        with open('cocktails_export.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    elif format_type == "csv":
        import csv
        with open('cocktails_export.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Chinese Name', 'Difficulty'])
            for cocktail in cocktails:
                writer.writerow([cocktail[1], cocktail[2], cocktail[3]])
    
    conn.close()
    print(f"数据已导出为 {format_type} 格式")
命令行工具
程序还提供了简单的命令行接口：

bash
# 查看帮助
python main.py --help

# 指定数据库路径
python main.py --db custom_database.db

# 重置数据库
python main.py --reset-db

# 导出数据
python main.py --export-json
python main.py --export-csv
配置选项
创建 config.ini 文件来自定义程序设置：

ini
[database]
path = cocktail_assistant.db
backup_on_start = true

[interface]
language = zh_CN
theme = light
font_size = 12

[recommendation]
default_mood = 放松
default_occasion = 家庭
default_alcohol = 中度
在程序中读取配置：

python
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_path = config.get('database', 'path', fallback='cocktail_assistant.db')
language = config.get('interface', 'language', fallback='zh_CN')
故障排除
常见问题
程序启动失败

bash
# 检查Python版本
python --version

# 检查依赖
python -c "import tkinter; print('tkinter可用')"
数据库问题

python
# 重新初始化数据库
from database import DatabaseManager
db = DatabaseManager()
db.reset_database()
db.insert_sample_data()
界面显示异常

python
# 检查字体设置
import tkinter.font
fonts = tkinter.font.families()
print("可用字体:", fonts)

## 贡献（Contributing）
欢迎贡献代码！请参考贡献指南。(Contributions are welcome! Please refer to the Contributing Guidelines.)

## 许可证 (License)
本项目使用MIT许可证。(This project is licensed under the MIT License.)

## 联系方式 (Contact)
邮箱       molina161@tju.edu.cn
GitHub账号 ugkuio