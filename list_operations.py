participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]
scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]
qualification_score = 70
distinction_score = 90


def show_all_participants():
    print("\n===== All Participants =====")
    for name, scr in zip(participants, scores):
        status = "NOT QUALIFIED"
        if scr >= distinction_score:
            status = "DISTINCTION"
        elif scr >= qualification_score:
            status = "QUALIFIED"
        print(f"Name: {name}, Score: {scr}, Status: {status}")


def add_new_participant():
    print("\n----- Add New Participant -----")
    name = input("Enter participant name: ").strip()
    if len(name) == 0:
        print("Error: Name cannot be empty, not added.")
        return
    if name in participants:
        print(f"Notice: {name} is already registered, not added.")
        return

    score_str = input("Enter score: ").strip()
    if not score_str.isdigit():
        print("Error: Score must be a number, not added.")
        return
    score = int(score_str)
    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100, not added.")
        return

    participants.append(name)
    scores.append(score)
    print(f"Successfully registered: {name}, score {score}")


def search_participant():
    print("\n----- Search Participant -----")
    target = input("Enter name to search: ").strip()
    if target not in participants:
        print(f"{target} not found.")
        return
    idx = participants.index(target)
    scr = scores[idx]
    print(f"Found: {target}, Score: {scr}")
    if scr >= distinction_score:
        print("Status: DISTINCTION")
    elif scr >= qualification_score:
        print("Status: QUALIFIED")
    else:
        print("Status: NOT QUALIFIED")


def check_any_all():
    has_distinction = any(s >= distinction_score for s in scores)
    all_passed = all(s >= 50 for s in scores)
    print("\n----- Global Condition Check -----")
    print(f"Any participant with distinction: {has_distinction}")
    print(f"All participants scored at least 50: {all_passed}")


def update_score():
    print("\n----- Update Participant Score -----")
    target = input("Enter name for score update: ").strip()
    if target not in participants:
        print(f"{target} does not exist, cannot update.")
        return
    idx = participants.index(target)
    new_score_str = input("Enter new score: ").strip()
    if not new_score_str.isdigit():
        print("Error: Score must be a number, update failed.")
        return
    new_score = int(new_score_str)
    if new_score < 0 or new_score > 100:
        print("Error: Score must be between 0‑100, update failed.")
        return
    scores[idx] = new_score
    print(f"{target}'s score has been updated to {new_score}")


def withdraw_participant():
    print("\n----- Remove Participant -----")
    target = input("Enter name to withdraw: ").strip()
    if target not in participants:
        print(f"{target} does not exist, cannot remove.")
        return
    idx = participants.index(target)
    participants.pop(idx)
    scores.pop(idx)
    print(f"Participant {target} has been removed")


def show_scoreboard():
    print("\n===== SCOREBOARD (Descending Order) =====")
    paired = list(zip(participants, scores))
    sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=True)
    for rank, (name, scr) in enumerate(sorted_pairs, start=1):
        status = "NOT QUALIFIED"
        if scr >= distinction_score:
            status = "DISTINCTION"
        elif scr >= qualification_score:
            status = "QUALIFIED"
        print(f"Rank {rank:2d} | {name:<18} | Score:{scr:3d} | {status}")
    return sorted_pairs


def calc_statistics(sorted_pairs):
    print("\n===== Statistics =====")
    high = max(scores)
    low = min(scores)
    avg = sum(scores) / len(scores)

    count_highest = scores.count(high)
    count_lowest = scores.count(low)
    count_distinction = len([s for s in scores if s >= distinction_score])
    count_qualified = len([s for s in scores if s >= qualification_score and s < distinction_score])
    count_not_qualified = len([s for s in scores if s < qualification_score])

    print(f"Highest score: {high}, Number of participants with highest score: {count_highest}")
    print(f"Lowest score: {low}, Number of participants with lowest score: {count_lowest}")
    print(f"Average score: {avg:.2f}")
    print(f"Number of distinctions: {count_distinction}")
    print(f"Number of qualified participants: {count_qualified}")
    print(f"Number of not qualified participants: {count_not_qualified}")
    return high, low, avg, count_highest, count_lowest, count_distinction, count_qualified, count_not_qualified


def final_report():
    sorted_pairs = show_scoreboard()
    calc_statistics(sorted_pairs)


def main():
    while True:
        print("\n======== MENU ========")
        print("1. Show all participants")
        print("2. Add new participant")
        print("3. Search participant")
        print("4. Check any‑all conditions")
        print("5. Update participant score")
        print("6. Withdraw participant")
        print("7. Scoreboard and final report")
        print("0. Exit program")
        opt = input("Enter option number: ").strip()
        if opt == "1":
            show_all_participants()
        elif opt == "2":
            add_new_participant()
        elif opt == "3":
            search_participant()
        elif opt == "4":
            check_any_all()
        elif opt == "5":
            update_score()
        elif opt == "6":
            withdraw_participant()
        elif opt == "7":
            final_report()
        elif opt == "0":
            print("Program terminated.")
            break
        else:
            print("Invalid input, please choose again.")


if __name__ == "__main__":
    main()
