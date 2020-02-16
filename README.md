Danmaqua API 数据仓库
======

这里是存放 Danmaqua 项目 API 数据的仓库，将同步到 GitHub 和 Coding.net（码云）并生成静态页面提供临时的 API 服务。

## 传送门

GitHub 主数据仓库：https://github.com/danmaqua/danmaqua-data

Coding.net 中国大陆数据仓库：https://fython.coding.net/p/danmaqua/d/damaqua-data/git

[客户端源码](https://github.com/fython/danmaqua-android)

[API 文档](https://github.com/fython/danmaqua-android/blob/master/docs/API_DATA.md)

## 如何修改、更新数据

### 增加、更新虚拟主播目录

目录数据目前为人工采集，采集目标为在哔哩哔哩拥有官方直播账号的虚拟主播，不限语言地区，非官方认证的转播帐号不予收集。

采集到的虚拟主播以企业/团体分类，个人势的虚拟主播会一并分到一个名为 “个人势” 的团体。

更新方式有以下两种途径：

#### 1. 普通用户

[新建 Issues](https://github.com/danmaqua/danmaqua-data/issues/new) 进行反馈

#### 2. 对 Git 操作熟悉的用户

在 `raw` 目录中， `groups.csv` 负责存放虚拟主播企业/团体的分类，数据列有三列：

- `name`：企业/团体简写，只能写小写英文数字和下划线。
- `title`：企业/团体正式名称
- `icon`：企业/团体的头像地址（可留空）

在 `raw/vtubers` 目录中，存放虚拟主播个人公开信息，建议按企业/团体分类保存为一个 csv 文件，数据列有六列：

- `uid`：哔哩哔哩用户 ID
- `room`：哔哩哔哩直播间号码
- `name`：哔哩哔哩用户名称
- `group`：所属企业/团体的对应 `name`
- `description`：主播说明
- `face`：头像地址

以上存放在 `raw` 的文件均为原始数据，并非 Danmaqua 客户端实际访问的，为便于编辑仍必须优先提交数据到 `raw` 中。

保存信息在 `raw` 文件夹中后，可以使用数据整理工具的 `make_catalog.py` 将 `csv` 数据转换为 `json` 数据并自动更新到 `room` 文件夹中，完成提交推送后，Danmaqua 客户端就能访问到新的数据了。（数据整理工具使用方法请阅读文档。）

### 增加、更新推荐主播

目前仅支持 [新建 Issues](https://github.com/danmaqua/danmaqua-data/issues/new) 来进行修改。

## 数据整理工具

查看 [tools/README.md](./tools/README.md)

## 贡献须知

本数据目前均为人工整理，因此可能会出现数据过时、主观评价等情况。

其中推荐主播列表内容和顺序会以项目团队成员的喜好为主，社区贡献者如果想要添加推荐
主播，请建立 Issues 或加入项目交流群代替直接 Pull Request，顺序依旧会由团队决定，
敬请理解。

对于头像更新问题，目前考虑通过 Bot 自动检查 Bilibili 主播数据是否更新并提交，有待
实现。
