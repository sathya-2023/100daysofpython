import time
import sys

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0-1, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i/3600)
    # print(f"00:00:{seconds:02}")
    sys.stdout.write(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}")
    sys.stdout.flush()
    time.sleep(1)
print("\ntime's up")