#!/usr/bin/env python3
"""
女神400速解 Discord機器人安裝腳本
"""

import subprocess
import sys
import os

def install_dependencies():
    """安裝必要的依賴包"""
    print("📦 正在安裝依賴包...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 依賴包安裝成功")
        return True
    except subprocess.CalledProcessError:
        print("❌ 依賴包安裝失敗")
        return False

def setup_config():
    """設置配置"""
    print("\n⚙️  設置機器人配置...")
    
    token = input("請輸入您的Discord Bot Token: ").strip()
    if not token:
        print("❌ Token不能為空")
        return False
    
    # 更新config.py檔案
    try:
        with open("config.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        content = content.replace("YOUR_DISCORD_BOT_TOKEN_HERE", token)
        
        with open("config.py", "w", encoding="utf-8") as f:
            f.write(content)
        
        print("✅ 配置檔案更新成功")
        return True
    except Exception as e:
        print(f"❌ 配置檔案更新失敗: {e}")
        return False

def show_instructions():
    """顯示使用說明"""
    print("\n" + "="*50)
    print("🎉 安裝完成！")
    print("="*50)
    print("\n📋 接下來的步驟:")
    print("1. 確保您的Discord機器人已創建並獲得必要權限")
    print("2. 將機器人邀請到您的Discord伺服器")
    print("3. 執行機器人:")
    print("   python3 run_bot.py")
    print("   或")
    print("   python3 bot.py")
    print("\n🔗 有用的連結:")
    print("• Discord開發者門戶: https://discord.com/developers/applications")
    print("• 詳細說明: 請查看 README.md 檔案")
    print("\n💡 使用方法:")
    print("• 在Discord中直接輸入1-4位數字(0-3)")
    print("• 輸入 'help' 或 '幫助' 獲取幫助")
    print("• 輸入 '!goddess 1102' 使用命令模式")

def main():
    """主函數"""
    print("🚀 女神400速解 Discord機器人安裝程式")
    print("="*50)
    
    # 檢查Python版本
    if sys.version_info < (3, 8):
        print("❌ Python版本過低，需要Python 3.8或更高版本")
        sys.exit(1)
    
    print(f"✅ Python版本檢查通過: {sys.version.split()[0]}")
    
    # 安裝依賴
    if not install_dependencies():
        print("\n❌ 安裝失敗，請手動執行:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    # 設置配置
    if not setup_config():
        print("\n❌ 配置失敗，請手動編輯 config.py 檔案")
        sys.exit(1)
    
    # 顯示說明
    show_instructions()

if __name__ == "__main__":
    main() 