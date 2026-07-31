print("===== 나의 메모장 =====")

memo = input("저장할 내용을 입력하세요: ")

with open("memo.txt", "w", encoding="utf-8") as file:
    file.write(memo)

print("저장 완료!")