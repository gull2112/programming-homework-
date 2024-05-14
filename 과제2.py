def calculate_rectangle_moment(b, h):
    return (b * h ** 3) / 12


def calculate_circle_moment(r):
    import math
    return (math.pi * r ** 4) / 4


def main():
    while True:
        shape = input("계산하려는 단면의 형태를 입력하세요 (직사각형, 원, 종료): ").strip()

        if shape == "종료":
            print("프로그램을 종료합니다.")
            break
        elif shape == "직사각형":
            b = float(input("밑변의 길이를 입력하세요: "))
            h = float(input("높이를 입력하세요: "))
            moment = calculate_rectangle_moment(b, h)
            print(f"직사각형 단면의 2차 모멘트는 {moment} 입니다.")
        elif shape == "원":
            r = float(input("반지름을 입력하세요: "))
            moment = calculate_circle_moment(r)
            print(f"원형 단면의 2차 모멘트는 {moment} 입니다.")
        else:
            print("지원되지 않는 형태입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()
