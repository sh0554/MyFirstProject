def save_contact():
    name = input("이름: ")
    phone = input("전화번호: ")

    with open("contacts.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{phone}\n")

    print("저장되었습니다.")


def show_contacts():
    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            print("\n===== 주소록 =====")
            print(file.read())
    except FileNotFoundError:
        print("저장된 연락처가 없습니다.")


while True:
    print("\n===== 주소록 프로그램 =====")
    print("1. 연락처 저장")
    print("2. 연락처 보기")
    print("3. 종료")

    menu = input("메뉴 선택: ")

    if menu == "1":
        save_contact()

    elif menu == "2":
        show_contacts()

    elif menu == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다.")