import pandas as pd
import os

# 原始 class_to_idx（根據ImageFolder的設定）
class_to_idx = {
    "0": 0,
    "1": 1,
    "10": 2,
    "11": 3,
    "12": 4,
    "13": 5,
    "14": 6,
    "15": 7,
    "16": 8,
    "17": 9,
    "18": 10,
    "19": 11,
    "2": 12,
    "20": 13,
    "21": 14,
    "22": 15,
    "23": 16,
    "24": 17,
    "25": 18,
    "26": 19,
    "27": 20,
    "28": 21,
    "29": 22,
    "3": 23,
    "30": 24,
    "31": 25,
    "32": 26,
    "33": 27,
    "34": 28,
    "35": 29,
    "36": 30,
    "37": 31,
    "38": 32,
    "39": 33,
    "4": 34,
    "40": 35,
    "41": 36,
    "42": 37,
    "43": 38,
    "44": 39,
    "45": 40,
    "46": 41,
    "47": 42,
    "48": 43,
    "49": 44,
    "5": 45,
    "50": 46,
    "51": 47,
    "52": 48,
    "53": 49,
    "54": 50,
    "55": 51,
    "56": 52,
    "57": 53,
    "58": 54,
    "59": 55,
    "6": 56,
    "60": 57,
    "61": 58,
    "62": 59,
    "63": 60,
    "64": 61,
    "65": 62,
    "66": 63,
    "67": 64,
    "68": 65,
    "69": 66,
    "7": 67,
    "70": 68,
    "71": 69,
    "72": 70,
    "73": 71,
    "74": 72,
    "75": 73,
    "76": 74,
    "77": 75,
    "78": 76,
    "79": 77,
    "8": 78,
    "80": 79,
    "81": 80,
    "82": 81,
    "83": 82,
    "84": 83,
    "85": 84,
    "86": 85,
    "87": 86,
    "88": 87,
    "89": 88,
    "9": 89,
    "90": 90,
    "91": 91,
    "92": 92,
    "93": 93,
    "94": 94,
    "95": 95,
    "96": 96,
    "97": 97,
    "98": 98,
    "99": 99,
}

# 反向對應
idx_to_class = {v: k for k, v in class_to_idx.items()}


def remap_predictions(prediction_path: str, save_path: str = None):
    """
    將 prediction.csv 中的 pred_label 整數類別重新映射回原本的字串類別名。

    Args:
        prediction_path (str): 要讀取的 prediction.csv 路徑。
        save_path (str): 要儲存的 csv 路徑，預設覆蓋原檔案。
    """
    if save_path is None:
        save_path = prediction_path

    df = pd.read_csv(prediction_path)

    if "pred_label" not in df.columns:
        raise ValueError("prediction.csv 缺少欄位 'pred_label'")

    df["pred_label"] = df["pred_label"].map(idx_to_class)
    df.to_csv(save_path, index=False)
    print(f"已轉換為 class name 並儲存為: {save_path}")
