# 使用

- Python 3+
- 保证当前工作目录在 `tools`，否则可能无法使用。
- 使用前执行 `pip install -r requirements.txt` 安装依赖

## make_catalog.py

```bash
py make_catalog.py
```

先在 raw 目录中以 csv 格式编写好虚拟主播团体和个人的基本信息，然后通过这个脚本生成接口数据。

它会将 `raw/groups.csv` 与 `raw/vtubers/*` 下的 csv 数据生成 API 格式要求的 JSON 并保存至 `room/vtubers_catalog.json` 与 `room/vtubers/*.json`

## update_raw_vtubers_csv.py

```bash
py update_raw_vtubers_csv.py
```

更新 raw 目录内的虚拟主播个人基本信息，如 B 站帐号显示名、头像。

房间号 `room` 栏是必填的，如果 `uid` 没有填写会自动获取并保存。
