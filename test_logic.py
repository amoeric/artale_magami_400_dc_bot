#!/usr/bin/env python3
"""
測試女神400速解邏輯
"""

# 结果映射表（从HTML代码中提取）
RESULT_MAP = {
    "0011": "211", "0101": "121", "0110": "112", "1011": "022",
    "1012": "031", "1021": "013", "1101": "202", "1102": "301",
    "1110": "220", "1120": "310", "1201": "103", "1210": "130",
    "2112": "004", "2121": "040", "2211": "400"
}

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

def test_complete_inputs():
    """測試完整4位數字輸入"""
    print("🧪 測試完整4位數字輸入:")
    print("-" * 30)
    
    test_cases = ["1102", "0011", "2211", "1234"]  # 最後一個應該失敗
    
    for case in test_cases:
        result = calculate_result(case)
        if result:
            print(f"✅ {case} → {result}")
        else:
            print(f"❌ {case} → 無對應結果")
    print()

def test_partial_inputs():
    """測試部分輸入"""
    print("🧪 測試部分輸入:")
    print("-" * 30)
    
    test_cases = ["11", "01", "22", "9"]  # 最後一個應該失敗
    
    for case in test_cases:
        result = calculate_result(case)
        if result:
            print(f"✅ {case} → {result}")
        else:
            print(f"❌ {case} → 無可能結果")
    print()

def test_edge_cases():
    """測試邊界情況"""
    print("🧪 測試邊界情況:")
    print("-" * 30)
    
    # 測試空輸入
    result = calculate_result("")
    print(f"空輸入: {result}")
    
    # 測試單個數字
    for i in range(4):
        result = calculate_result(str(i))
        print(f"輸入 {i}: {result if result else '無結果'}")
    
    print()

def show_all_mappings():
    """顯示所有映射關係"""
    print("📋 完整映射表:")
    print("-" * 30)
    
    for key, value in sorted(RESULT_MAP.items()):
        print(f"{key} → {value}")
    print()

def main():
    """主測試函數"""
    print("🚀 女神400速解邏輯測試")
    print("=" * 50)
    
    test_complete_inputs()
    test_partial_inputs()
    test_edge_cases()
    show_all_mappings()
    
    print("✅ 測試完成！")

if __name__ == "__main__":
    main() 