import csv

PASSWORD = "ngan2021"  # đổi tay ở đây nếu muốn
OUTPUT_FILE = "account.csv"

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["username", "password"])

    for i in range(0, 1000):
        writer.writerow([f"luongclone{i:03d}", PASSWORD])

    for i in range(1000, 2001):
        writer.writerow([f"luongclone{i}", PASSWORD])

print(f"Da tao xong file {OUTPUT_FILE}")
print("Range: luongclone000-999 va luongclone1000-2000")
print(f"Password: {PASSWORD}")
