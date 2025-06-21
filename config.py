# Discord机器人配置文件
import os
from dotenv import load_dotenv

# 加载环境变量（如果存在.env文件）
load_dotenv()

# 从环境变量或直接设置获取Discord Bot Token
# 优先级：环境变量 > 直接设置的值
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', 'YOUR_DISCORD_BOT_TOKEN_HERE')

# 可选：设置命令前缀（默认为 !）
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')

# 可選：設置機器人狀態訊息
BOT_STATUS = os.getenv('BOT_STATUS', '女神400速解 | 輸入help獲取幫助')

# 安全檢查：確保Token已設置
if DISCORD_TOKEN == 'YOUR_DISCORD_BOT_TOKEN_HERE':
    print("⚠️  警告：請先設置您的Discord Bot Token！")
    print("方法1：直接修改config.py檔案中的DISCORD_TOKEN變數")
    print("方法2：創建.env檔案並設置DISCORD_TOKEN=您的Token")
    print("獲取Token: https://discord.com/developers/applications") 