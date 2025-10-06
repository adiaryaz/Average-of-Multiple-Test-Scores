def main():
    try:
        n = int(input())
        if n <= 0:
            print("NoProceed")
            return
    except ValueError:
        print("NoProceed")
        return

    total_score = 0

    for i in range(n):
        try:
            score = float(input())
            if score < 0 or score > 100:
                print("NoProceed")
                return
            total_score += score
        except ValueError:
            print("NoProceed")
            return

    average_score = total_score / n
    print(f"{average_score:.1f}")

if __name__ == "__main__":
    main()