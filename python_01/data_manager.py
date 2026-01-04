"""
数据管理模块
存储所有的鸡尾酒、问题和用户数据
"""

import json
import os
from typing import Dict, List, Any, Optional


class DataManager:
    """数据管理器"""

    def __init__(self):
        self.cocktails = self._load_cocktails()
        self.questions = self._load_questions()
        self.user_data = {}

    def _load_cocktails(self) -> Dict[str, Dict]:
        """加载鸡尾酒数据"""
        cocktails = {
            "gin_tonic": {
                "id": "gin_tonic",
                "name": "金汤力",
                "english_name": "Gin & Tonic",
                "description": "最经典的入门鸡尾酒！清爽简单，像有气泡的柠檬水",
                "base_spirit": "金酒",
                "difficulty": "⭐ 非常简单",
                "taste": "清爽、微苦、气泡感",
                "occasion": "随时都能喝，尤其适合夏天",
                "icon": "🍋",
                "color": "#6ab7ff",
                "ingredients": [
                    {"name": "金酒", "amount": "45ml（大约3汤匙）", "icon": "🥃"},
                    {"name": "汤力水", "amount": "一听（约200ml）", "icon": "🥤"},
                    {"name": "青柠角", "amount": "1个", "icon": "🍋"},
                    {"name": "冰块", "amount": "装满杯子", "icon": "🧊"}
                ],
                "steps": [
                    {"number": 1, "title": "准备杯子", "description": "找一个高杯子，加满冰块"},
                    {"number": 2, "title": "加入金酒", "description": "倒入金酒，大约到杯子1/4处"},
                    {"number": 3, "title": "加入青柠", "description": "挤入青柠汁，把青柠角也扔进去"},
                    {"number": 4, "title": "完成", "description": "倒满汤力水，轻轻搅拌一下"}
                ],
                "tips": [
                    "不用精确到1ml，差不多就行！",
                    "冰块越多越好，饮料会更清爽",
                    "第一次做不好看很正常，好喝就行",
                    "可以边尝边调，找到自己喜欢的比例"
                ],
                "price": "80-150元",
                "total_budget": "100-200元",
                "serving_size": "1-2人",
                "prep_time": "3分钟"
            },
            "mojito": {
                "id": "mojito",
                "name": "莫吉托",
                "english_name": "Mojito",
                "description": "古巴经典，清爽夏日首选！薄荷的清凉配上青柠的酸爽",
                "base_spirit": "朗姆酒",
                "difficulty": "⭐⭐ 简单",
                "taste": "清爽、薄荷香、微甜",
                "occasion": "夏天必备，朋友聚会",
                "icon": "🌿",
                "color": "#4cd964",
                "ingredients": [
                    {"name": "朗姆酒", "amount": "45ml", "icon": "🥃"},
                    {"name": "青柠", "amount": "半个", "icon": "🍋"},
                    {"name": "薄荷叶", "amount": "10片", "icon": "🌿"},
                    {"name": "白糖", "amount": "2茶匙", "icon": "🍚"},
                    {"name": "苏打水", "amount": "适量", "icon": "🥤"},
                    {"name": "冰块", "amount": "装满杯子", "icon": "🧊"}
                ],
                "steps": [
                    {"number": 1, "title": "准备薄荷", "description": "薄荷叶轻轻拍醒，放入杯中"},
                    {"number": 2, "title": "加入青柠和糖", "description": "青柠挤汁，和糖一起放入"},
                    {"number": 3, "title": "捣压", "description": "轻轻捣压，释放香味"},
                    {"number": 4, "title": "加冰和酒", "description": "加满冰块，倒入朗姆酒"},
                    {"number": 5, "title": "完成", "description": "倒满苏打水，轻轻搅拌"}
                ],
                "tips": [
                    "薄荷叶轻轻拍一下就好，不要捣烂",
                    "没有白糖可以用蜂蜜代替",
                    "苏打水可以用雪碧代替，更甜一些"
                ],
                "price": "80-120元",
                "total_budget": "100-180元",
                "serving_size": "1-2人",
                "prep_time": "5分钟"
            },
            "screwdriver": {
                "id": "screwdriver",
                "name": "螺丝起子",
                "english_name": "Screwdriver",
                "description": "橙汁加伏特加！早上喝就像有酒精的橙汁",
                "base_spirit": "伏特加",
                "difficulty": "⭐ 非常简单",
                "taste": "酸甜、像橙汁",
                "occasion": "早午餐、轻松时刻",
                "icon": "🍊",
                "color": "#ff9f43",
                "ingredients": [
                    {"name": "伏特加", "amount": "45ml", "icon": "🥃"},
                    {"name": "橙汁", "amount": "150ml", "icon": "🧃"},
                    {"name": "橙片", "amount": "装饰用", "icon": "🍊"},
                    {"name": "冰块", "amount": "适量", "icon": "🧊"}
                ],
                "steps": [
                    {"number": 1, "title": "准备杯子", "description": "杯中加入冰块"},
                    {"number": 2, "title": "加入伏特加", "description": "倒入伏特加"},
                    {"number": 3, "title": "完成", "description": "倒满橙汁，用勺子搅拌几下"}
                ],
                "tips": [
                    "用新鲜橙汁味道更好",
                    "可以加一点橙子果肉",
                    "早上喝一杯，精神一整天"
                ],
                "price": "70-130元",
                "total_budget": "90-180元",
                "serving_size": "1人",
                "prep_time": "2分钟"
            },
            "margarita": {
                "id": "margarita",
                "name": "玛格丽特",
                "english_name": "Margarita",
                "description": "龙舌兰经典调酒，盐边提升风味层次，拍照特别好看",
                "base_spirit": "龙舌兰",
                "difficulty": "⭐⭐⭐ 有点技巧",
                "taste": "酸甜、咸味、柑橘香",
                "occasion": "聚会、约会、拍照",
                "icon": "🌵",
                "color": "#ff6b6b",
                "ingredients": [
                    {"name": "龙舌兰", "amount": "45ml", "icon": "🥃"},
                    {"name": "君度", "amount": "20ml", "icon": "🍊"},
                    {"name": "青柠汁", "amount": "25ml", "icon": "🍋"},
                    {"name": "盐", "amount": "适量", "icon": "🧂"},
                    {"name": "冰块", "amount": "适量", "icon": "🧊"}
                ],
                "steps": [
                    {"number": 1, "title": "准备盐边", "description": "用青柠擦湿杯口，蘸一圈盐"},
                    {"number": 2, "title": "摇酒", "description": "所有材料加冰，摇匀8-10秒"},
                    {"number": 3, "title": "完成", "description": "滤入杯中，加冰装饰"}
                ],
                "tips": [
                    "盐边不要蘸太多，会太咸",
                    "没有摇酒壶可以用带盖的瓶子",
                    "拍照时找好光线，特别出片"
                ],
                "price": "100-180元",
                "total_budget": "150-250元",
                "serving_size": "1人",
                "prep_time": "5分钟"
            },
            "whiskey_coke": {
                "id": "whiskey_coke",
                "name": "威士忌可乐",
                "english_name": "Whiskey Coke",
                "description": "最简单的威士忌喝法！加点可乐更好入口",
                "base_spirit": "威士忌",
                "difficulty": "⭐ 非常简单",
                "taste": "微甜、有焦糖味",
                "occasion": "晚上放松时喝",
                "icon": "🥃",
                "color": "#8b4513",
                "ingredients": [
                    {"name": "威士忌", "amount": "45ml", "icon": "🥃"},
                    {"name": "可乐", "amount": "一听", "icon": "🥤"},
                    {"name": "柠檬片", "amount": "可选", "icon": "🍋"},
                    {"name": "冰块", "amount": "适量", "icon": "🧊"}
                ],
                "steps": [
                    {"number": 1, "title": "准备杯子", "description": "杯中加冰块"},
                    {"number": 2, "title": "加入威士忌", "description": "倒入威士忌"},
                    {"number": 3, "title": "完成", "description": "倒满可乐，轻轻搅拌"}
                ],
                "tips": [
                    "用可口可乐或百事可乐都可以",
                    "威士忌和可乐比例可以自己调整",
                    "加片柠檬更好看"
                ],
                "price": "90-200元",
                "total_budget": "120-250元",
                "serving_size": "1人",
                "prep_time": "2分钟"
            }
        }
        return cocktails

    def _load_questions(self) -> List[Dict]:
        """加载问题数据"""
        questions = [
            {
                "id": 1,
                "title": "你喜欢什么样的口味？",
                "description": "选一个你最感兴趣的",
                "options": [
                    {
                        "id": "A",
                        "icon": "🍋",
                        "title": "清爽的",
                        "description": "像柠檬水、汽水",
                        "recommends": ["gin_tonic", "mojito"]
                    },
                    {
                        "id": "B",
                        "icon": "🍬",
                        "title": "甜甜的",
                        "description": "像果汁、可乐",
                        "recommends": ["whiskey_coke", "screwdriver"]
                    },
                    {
                        "id": "C",
                        "icon": "🍊",
                        "title": "果味的",
                        "description": "像橙汁、热带水果",
                        "recommends": ["margarita", "screwdriver"]
                    },
                    {
                        "id": "D",
                        "icon": "🤷",
                        "title": "我也不知道",
                        "description": "随便试试",
                        "recommends": ["gin_tonic", "whiskey_coke"]
                    }
                ]
            },
            {
                "id": 2,
                "title": "你想要的酒精度是？",
                "description": "选择你喜欢的强度",
                "options": [
                    {
                        "id": "A",
                        "icon": "🍹",
                        "title": "低一点",
                        "description": "像啤酒，不容易醉",
                        "recommends": ["gin_tonic", "mojito"]
                    },
                    {
                        "id": "B",
                        "icon": "🥂",
                        "title": "中等",
                        "description": "微醺的感觉",
                        "recommends": ["margarita", "screwdriver"]
                    },
                    {
                        "id": "C",
                        "icon": "🥃",
                        "title": "高一点",
                        "description": "有劲儿！",
                        "recommends": ["whiskey_coke", "margarita"]
                    }
                ]
            },
            {
                "id": 3,
                "title": "这次调酒主要是为了？",
                "description": "选择你的使用场景",
                "options": [
                    {
                        "id": "A",
                        "icon": "🎉",
                        "title": "朋友聚会",
                        "description": "要简单好做",
                        "recommends": ["gin_tonic", "whiskey_coke"]
                    },
                    {
                        "id": "B",
                        "icon": "💑",
                        "title": "约会/浪漫时刻",
                        "description": "要好看",
                        "recommends": ["margarita", "mojito"]
                    },
                    {
                        "id": "C",
                        "icon": "😌",
                        "title": "自己在家放松",
                        "description": "要方便",
                        "recommends": ["screwdriver", "whiskey_coke"]
                    },
                    {
                        "id": "D",
                        "icon": "📸",
                        "title": "拍照发朋友圈",
                        "description": "要漂亮",
                        "recommends": ["margarita", "mojito"]
                    }
                ]
            },
            {
                "id": 4,
                "title": "你的预算是？（买酒的钱）",
                "description": "选择你的预算范围",
                "options": [
                    {
                        "id": "A",
                        "icon": "💰",
                        "title": "100元以内",
                        "description": "买1瓶酒试试",
                        "recommends": ["gin_tonic", "screwdriver"]
                    },
                    {
                        "id": "B",
                        "icon": "💰💰",
                        "title": "100-300元",
                        "description": "可以买2-3瓶",
                        "recommends": ["margarita", "whiskey_coke"]
                    },
                    {
                        "id": "C",
                        "icon": "💰💰💰",
                        "title": "不差钱",
                        "description": "推荐最好的！",
                        "recommends": ["margarita", "whiskey_coke"]
                    }
                ]
            }
        ]
        return questions

    def save_user_data(self, data: Dict):
        """保存用户数据"""
        self.user_data.update(data)

    def get_recommendation(self, answers: Dict) -> str:
        """根据答案推荐鸡尾酒"""
        # 统计每个鸡尾酒的推荐次数
        scores = {}

        for q_id, answer in answers.items():
            question = next((q for q in self.questions if q["id"] == int(q_id)), None)
            if question:
                option = next((opt for opt in question["options"] if opt["id"] == answer), None)
                if option:
                    for cocktail_id in option["recommends"]:
                        scores[cocktail_id] = scores.get(cocktail_id, 0) + 1

        # 如果没有匹配，返回默认
        if not scores:
            return "gin_tonic"

        # 返回得分最高的鸡尾酒
        return max(scores.items(), key=lambda x: x[1])[0]

    def get_cocktail_by_id(self, cocktail_id: str) -> Optional[Dict]:
        """根据ID获取鸡尾酒"""
        return self.cocktails.get(cocktail_id)

    def get_all_cocktails(self) -> List[Dict]:
        """获取所有鸡尾酒"""
        return list(self.cocktails.values())

    def get_faqs(self) -> List[Dict]:
        """获取常见问题"""
        faqs = [
            {
                "question": "Q: 买不到推荐的酒怎么办？",
                "answer": "A: 用其他白色透明的酒代替（比如伏特加），味道会变，但也能喝！调酒最重要的是开心，不是完美。"
            },
            {
                "question": "Q: 没有量杯怎么量45ml？",
                "answer": "A: 大约3汤匙，或者倒满一个小酒杯（2两杯）。其实不用太精确，差不多就行！"
            },
            {
                "question": "Q: 我不喜欢这个味道怎么办？",
                "answer": "A: 多加果汁或汽水！调酒就是调到自己喜欢为止。第一次可以少放点酒，多放饮料。"
            },
            {
                "question": "Q: 可以不加冰吗？",
                "answer": "A: 可以，但冰镇一下更好喝。如果没冰，可以提前把材料放冰箱冷藏。"
            },
            {
                "question": "Q: 喝不完的酒怎么保存？",
                "answer": "A: 盖好盖子放阴凉处，能放很久（一两年都没问题）。别放冰箱，除非开了很久。"
            },
            {
                "question": "Q: 我想尝试更复杂的怎么办？",
                "answer": "A: 先把这个做好！熟练了再试其他的。我们已经准备好了进阶教程，等你准备好了就点'下一步建议'。"
            }
        ]
        return faqs