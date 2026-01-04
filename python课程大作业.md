
# Python程序设计基础大作业
## 题目：XXXX
## 班级: 测控四班
## 姓名: 刘佳佳
## 学号: 3023202172

--------------------------

## 1. 课程考核办法
* 成绩组成：大作业成绩×90%+平时成绩和作业×10%
* 大作业成绩考核：学生自主命题，确定大作业题目。
* 大作业成绩考核：难度等级系数×6%+完成度×70%。根据选择题目涉及的内容，评定大作业难度等级（详见后面文档）
---------------------
## 2. 大作业难度等级评定标准
### 2.1 五星难度（具备以下特点之一）
1. 程序部署在集群服务器上，可对大规模数据进行处理。
2. 使用大型框架实现复杂图形界面。
3. 综合使用多种前后端框架实现基于BS结构的应用程序。
4. 使用多线程技术实现高并发复杂应用。
5. 多机，多操作系统或多语言混合开发复杂应用程序。
6. 与单片机结合，实现在嵌入式硬件下的Python应用程序开发，并实现较为复杂的功能，包括远程部署及代码调试，版本升级等。
### 2.2 四星难度（具备以下特点之一）
1. 使用中型框架实现较为复杂的图形界面
2. 使用某种框架实现基于BS结构的应用程序
3. 使用多线程技术实现并发应用开发
4. 基于Linux操作系统开发较为复杂的应用程序
5. 在嵌入式硬件下开发应用程序并实现一定的功能
6. 综合多种Python应用场景，实现较为复杂的桌面应用程序开发
7. 基于神经网络算法的算法改进、数据集采集算法改进等，并最终搭建网络实现功能
8. 针对特定科学计算的需求，实现算法改进，基于WEB架构，实现功能，达到发布标准
### 2.3 三星难度（具备以下特点之一）
1. 实现基于图形用户界面的桌面应用程序开发，并实现一些有意义的功能
2. 基于BS结构的应用程序开发
3. 制定针对特定科学计算的需求，算法改进，在本地实现功能。
4. 基于神经网络算法模型的搭建，实现功能，改进性能等。

### 2.4 二星难度 （具备以下特点之一）

1. 编写1000行左右的代码程序；
2. 能够发布/打包程序，实现一定的功能，如科学计算、数据可视化、基本爬虫等；
2. 基于Python实现了一些创意性的功能；
-----------------------------------------
## 3. 大作业格式要求（参考典型readme文件书写规范）

1. **使用Markdown格式**： 采用Markdown（.md文件扩展名）编写，易于阅读和编辑，支持丰富的格式。

2. **基本结构和内容**：
* 项目名称和简介： 清晰的项目名称（H1标题```#```），用一段简洁的段落清晰的介绍项目功能和目标。
* 安装： 详细的安装步骤，包括依赖和环境，通常使用`pip install`命令。
* 使用方法： **提供代码示例、截图或动图**，演示如何使用项目主要功能。
* 贡献： 说明如何参与项目贡献，例如提交bug、提交代码，可链接到CONTRIBUTING.md。
* 许可证： 明确项目许可证类型（如MIT、Apache 2.0），并包含LICENSE文件。
* 其他建议
  * 目录： 内容较多时方便导航。
  * 项目状态： 说明开发阶段（alpha、beta、稳定版）。
  * 更新日志： 记录版本更新信息。
  * 致谢： 感谢贡献者。
  * 联系方式： 方便用户反馈，如邮箱或者github，gitee账号等。

3. **提交方式：**

    基于gitee平台提交

-----------------------
## 4. 一个典型的README模板
# 项目名称 (Project Name)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](可选，构建状态)
[![PyPI version](https://badge.fury.io/py/your-package-name.svg)](可选，PyPI版本)
[![License](https://img.shields.io/badge/license-MIT-blue)](许可证)

一句话简洁描述项目的功能和目标。(A short and clear description of the project's functionality and purpose.)

## 项目简介 (Description)

更详细的介绍项目的功能、特性和解决的问题。(A more detailed introduction to the project's features, functionalities, and the problems it solves.)

## 难度等级介绍

请在此说明自己选择课题的难度等级，并结合前面的“大作业难度等级评定标准”进行详细说明，包括具体是哪一条？为什么？给出详细原因。

### 注意：此条一定要有，是成绩评定的重要标准

## 安装 (Installation)

使用pip安装：(Installation using pip:)

```bash
pip install your-package-name
```
或者从源代码安装：(Or install from source:)
```
git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)
cd your-repo
python setup.py install
```
## 使用方法（usage）
提供基本的使用示例。(Provide basic usage examples.)
```
import your_package

# 示例代码 (Example code)
result = your_package.some_function(arguments)
print(result)
```
更详细的用法请参考完整文档 (Link to more detailed documentation if available)

    
插入网络图片命令：

![Markdown Logo](https://markdown-here.com/img/icon256.png "Markdown Logo")

插入本地图片命令：

    假设你的Markdown文件是README.md，图片是路径是：images/logo.png，则在README.md中插入图片的语法应为：

    ![Logo](images/logo.png "公司Logo")


## 贡献（Contributing）
欢迎贡献代码！请参考贡献指南。(Contributions are welcome! Please refer to the Contributing Guidelines.)

## 许可证 (License)
本项目使用MIT许可证。(This project is licensed under the MIT License.)

## 联系方式 (Contact)
你的邮箱或GitHub账号。(Your email address or GitHub username.)