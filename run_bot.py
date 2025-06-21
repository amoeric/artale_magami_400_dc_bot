#!/usr/bin/env python3
"""
女神400速解 Discord機器人啟動腳本
"""

import sys
import os

def check_dependencies():
    """檢查必要的依賴包是否已安裝"""
    try:
        import discord
        print("✅ discord.py 已安裝")
    except ImportError:
        print("❌ discord.py 未安裝")
        print("請執行: pip install discord.py")
        return False
    
    try:
        import dotenv
        print("✅ python-dotenv 已安裝")
    except ImportError:
        print("⚠️  python-dotenv 未安裝（可選）")
        print("如需使用.env檔案，請執行: pip install python-dotenv")
    
    return True

def check_config():
    """檢查配置是否正確"""
    try:
        from config import DISCORD_TOKEN
        if DISCORD_TOKEN == "YOUR_DISCORD_BOT_TOKEN_HERE":
            print("❌ Discord Bot Token 未設置")
            print("請編輯 config.py 檔案或創建 .env 檔案設置您的Token")
            return False
        print("✅ Discord Bot Token 已設置")
        return True
    except ImportError:
        print("❌ 無法匯入配置檔案")
        return False

def main():
    """主函數"""
    print("🚀 正在啟動女神400速解 Discord機器人...")
    print("=" * 50)
    
    # 檢查Python版本
    if sys.version_info < (3, 8):
        print("❌ Python版本過低，需要Python 3.8或更高版本")
        sys.exit(1)
    
    print(f"✅ Python版本: {sys.version}")
    
    # 檢查依賴
    if not check_dependencies():
        print("\n請先安裝必要的依賴包:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    # 檢查配置
    if not check_config():
        print("\n配置檢查失敗，請檢查您的Discord Bot Token設置")
        sys.exit(1)
    
    print("=" * 50)
    print("🎉 所有檢查通過，正在啟動機器人...")
    
    # 匯入並執行機器人
    try:
        from bot import bot
        from config import DISCORD_TOKEN
        bot.run(DISCORD_TOKEN)
    except KeyboardInterrupt:
        print("\n👋 機器人已停止執行")
    except Exception as e:
        print(f"\n❌ 啟動失敗: {e}")
        print("請檢查您的網路連線和Token是否正確")

if __name__ == "__main__":
    main() 