from datetime import datetime


balance = 0
FILE_NAME = "ledger.txt"


def save_transaction(date, kind, content, money):
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(
            f"{date},{kind},{content},{money}\n"
        )


def show_transactions():

    print("\n====== 거래 내역 ======")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:

            for line in file:
                date, kind, content, money = line.strip().split(",")

                print(
                    f"{date} | {kind} | {content} | {money}원"
                )

    except FileNotFoundError:
        print("거래 내역이 없습니다.")


def add_transaction():

    global balance

    date = datetime.now().strftime("%Y-%m-%d")

    kind = input("구분 (수입/지출): ")
    content = input("내용: ")
    money = int(input("금액: "))


    if kind == "수입":
        balance += money

    elif kind == "지출":
        balance -= money


    save_transaction(
        date,
        kind,
        content,
        money
    )


    print("\n저장 완료")
    print("현재 잔액:", balance)



while True:

    print("""
========================

      회계 프로그램

========================

1. 거래 입력
2. 거래 조회
3. 종료

""")

    menu = input("선택 : ")


    if menu == "1":
        add_transaction()


    elif menu == "2":
        show_transactions()


    elif menu == "3":
        print("프로그램 종료")
        break