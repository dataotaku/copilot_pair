"""
매일 강우량을 기록하는 프로그램을 작성하세요. 강우량은 음수값이 될 수 없으므로, 음수값이 입력되면 거부해야 합니다.
이 프로그램은 강우량이 기록된 일수, 비가 내린 일수, 해당기간의 강우량 및 하루 중 내린 최대 강우량을 출력해야 합니다.
또한 9999라는 값이 입력되면 프로그램이 종료되어야 합니다.
"""

def main():
    days = 0
    rainy_days = 0
    total_rainfall = 0
    max_rainfall = 0

    while True:
        rainfall = int(input("Enter today's rainfall amount: "))
        if rainfall == 9999:
            break
        if rainfall < 0:
            print("Rainfall amount cannot be negative.")
            continue
        days += 1
        total_rainfall += rainfall
        if rainfall > 0:
            rainy_days += 1
        if rainfall > max_rainfall:
            max_rainfall = rainfall

    print(f"Number of days: {days}")
    print(f"Number of rainy days: {rainy_days}")
    print(f"Total rainfall: {total_rainfall}")
    print(f"Maximum rainfall in a day: {max_rainfall}")


# def main():
#     days = 0
#     rainy_days = 0
#     total_rainfall = 0
#     max_rainfall = 0

#     while True:
#         rainfall = int(input("Enter today's rainfall amount: "))
#         if rainfall == 9999:
#             break
#         if rainfall < 0:
#             print("Rainfall amount cannot be negative.")
#             continue
#         days += 1
#         total_rainfall += rainfall
#         if rainfall > 0:
#             rainy_days += 1
#         if rainfall > max_rainfall:
#             max_rainfall = rainfall

#     print(f"Number of days: {days}")
#     print(f"Number of rainy days: {rainy_days}")
#     print(f"Total rainfall: {total_rainfall}")
#     print(f"Maximum rainfall in a day: {max_rainfall}")

if __name__ == "__main__":
    main()