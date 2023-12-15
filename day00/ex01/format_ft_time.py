from datetime import datetime

output_string = "Seconds since January 1, 1970: {:,.4f} or {:.2E} in scientific notation"

now = datetime.now()
start = datetime(year=1970, month=1, day=1)

diff_seconds = (now - start).total_seconds()

print(output_string.format(diff_seconds, diff_seconds))
print(start.strftime("%b %d %Y"))

# expected output:
# python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
