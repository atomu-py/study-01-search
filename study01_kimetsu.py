import csv
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# 課題4.リストをcsvから読み込み
source = []
with open(r"D:\06_Python\900_code\110_study01\kimetsu.csv", "r", encoding="utf-8") as f:
    contents = csv.reader(f)
    for row in contents:
        source = row
        # 10行目が「source.append(row)」だとうまくいきませんでした。調べましたがよくわからず、理由を知りたいです。
        print(source)
### 検索ツール
# 課題1.入力したワードでリスト検索をする
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    # 課題2.結果が存在した場合と、しなかった場合で分岐
    if word in source:
        print("{}が見つかりました".format(word))

    else:
        print("{}が見つかりませんでした。リストに追加します".format(word))
        # 課題3.リストに入力文字がなければ、追加
        source.append(word)
        print(source)

if __name__ == "__main__":
    search()
