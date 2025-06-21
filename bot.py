import discord
from discord.ext import commands
import re
from config import DISCORD_TOKEN

# 设置机器人权限
intents = discord.Intents.default()
intents.message_content = True

# 创建机器人实例
bot = commands.Bot(command_prefix='!', intents=intents)

# 结果映射表（从HTML代码中提取）
RESULT_MAP = {
    "0011": "211", "0101": "121", "0110": "112", "1011": "022",
    "1012": "031", "1021": "013", "1101": "202", "1102": "301",
    "1110": "220", "1120": "310", "1201": "103", "1210": "130",
    "2112": "004", "2121": "040", "2211": "400"
}

@bot.event
async def on_ready():
    print(f'{bot.user} 已成功登入！')
    print('女神400速解機器人已準備就緒')

@bot.event
async def on_message(message):
    # 忽略機器人自己的訊息
    if message.author == bot.user:
        return
    
    content = message.content.strip()
    
    # 處理被@的情況，提取實際的命令內容
    if bot.user.mentioned_in(message):
        # 移除所有mention標籤，只保留實際內容
        content = re.sub(r'<@!?\d+>', '', content).strip()
    
    # 如果內容為空（只有mention），顯示幫助
    if not content:
        content = 'help'
    
    help_text = """
🎮 **女神400速解 - 使用說明**

**使用方法：**
依序輸入「全空」、「隊長在左」、「隊長在中」、「隊長在右」時的 NPC 數字，機器人會自動算出答案

**輸入格式：**
• 直接輸入 1-4 位數字（例如：1102）
• 支援部分輸入查看可能結果

**範例：**
• 輸入 `1102` → 輸出 `301`
• 輸入 `11` → 顯示所有以11開頭的可能結果

**數字說明：**
• 0 = 全空
• 1 = 隊長在左
• 2 = 隊長在中  
• 3 = 隊長在右

祝你遊戲愉快！ 🎉
    """
    
    # 幫助命令
    if content.lower() in ['幫助', 'help', '帮助']:
        await message.channel.send(help_text)
        return
    
    # 檢查是否為數字輸入
    if re.match(r'^[0-3]{1,4}$', content):
        result = calculate_result(content)
        
        # 創建嵌入訊息，讓回覆更美觀
        embed = discord.Embed(
            title="女神400速解",
            color=0x3b82f6  # 藍色
        )
        
        if len(content) == 4:
            if result:
                embed.add_field(
                    name=f"輸入：{content}",
                    value=f"**答案：{result}**",
                    inline=False
                )
                embed.color = 0x10b981  # 綠色
            else:
                embed.add_field(
                    name=f"輸入：{content}",
                    value="❌ 無對應結果",
                    inline=False
                )
                embed.color = 0xef4444  # 紅色
        else:
            if result:
                embed.add_field(
                    name=f"部分輸入：{content}",
                    value=f"可能結果：**{result}**",
                    inline=False
                )
                embed.color = 0xf59e0b  # 黃色
            else:
                embed.add_field(
                    name=f"部分輸入：{content}",
                    value="❌ 無可能結果",
                    inline=False
                )
                embed.color = 0xef4444  # 紅色
        
        await message.channel.send(embed=embed)
        return
    
    # 如果輸入的不是有效數字且被@了或包含數字，顯示幫助
    if (bot.user.mentioned_in(message) or re.search(r'\d', content)) and content.lower() not in ['幫助', 'help', '帮助']:
        await message.channel.send(help_text)
        return
    
    # 處理其他命令
    await bot.process_commands(message)

def calculate_result(input_code):
    """
    根據輸入的代碼計算結果
    """
    if len(input_code) == 4:
        # 完整4位數字，直接查找
        return RESULT_MAP.get(input_code)
    else:
        # 部分輸入，找所有匹配的結果
        matches = []
        for key, value in RESULT_MAP.items():
            if key.startswith(input_code):
                matches.append(value)
        
        if matches:
            return '、'.join(sorted(set(matches)))  # 去重並排序
        else:
            return None

@bot.command(name='goddess', aliases=['女神'])
async def goddess_command(ctx, *, code=None):
    """
    命令版本的女神400速解
    使用方法: !goddess 1102 或 !女神 1102
    """
    if code is None:
        await ctx.send("請輸入1-4位數字，例如：`!goddess 1102`")
        return
    
    code = code.strip()
    if not re.match(r'^[0-3]{1,4}$', code):
        await ctx.send("請輸入有效的1-4位數字（只能包含 0-3）")
        return
    
    result = calculate_result(code)
    
    embed = discord.Embed(title="女神400速解", color=0x3b82f6)
    
    if len(code) == 4:
        if result:
            embed.add_field(name=f"輸入：{code}", value=f"**答案：{result}**", inline=False)
            embed.color = 0x10b981
        else:
            embed.add_field(name=f"輸入：{code}", value="❌ 無對應結果", inline=False)
            embed.color = 0xef4444
    else:
        if result:
            embed.add_field(name=f"部分輸入：{code}", value=f"可能結果：**{result}**", inline=False)
            embed.color = 0xf59e0b
        else:
            embed.add_field(name=f"部分輸入：{code}", value="❌ 無可能結果", inline=False)
            embed.color = 0xef4444
    
    await ctx.send(embed=embed)

# 启动机器人
if __name__ == "__main__":
    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        print(f"啟動機器人時出錯: {e}")
        print("請檢查您的Discord Bot Token是否正確設置") 