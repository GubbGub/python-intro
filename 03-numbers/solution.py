minutes = 135
print(f"{minutes} minutes = {minutes // 60} h {minutes % 60} min")

total = 1_000_000
days = total // 86400          # 86400 seconds in a day
total %= 86400                 # keep the leftover
hours = total // 3600
total %= 3600
mins = total // 60
secs = total % 60
print(f"1000000 seconds = {days} days, {hours} h, {mins} min, {secs} s")
