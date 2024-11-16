budget = float(input())
season = input()

accommodation = ""
cost = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        cost = 0.30 * budget
        accommodation = "Camp"
    elif season == "winter":
        cost = 0.70 * budget
        accommodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        cost = 0.40 * budget
        accommodation = "Camp"
    elif season == "winter":
        cost = 0.80 * budget
        accommodation = "Hotel"
else:
    destination = "Europe"
    cost = 0.90 * budget
    accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {cost:.2f}")
