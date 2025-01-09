# sum_exceed.py
total = 0
for num in range(1, 100):  # Arbitrary upper limit
    total += num
    if total > 50:
        print(f"Sum exceeded 50: {total}")
        break
