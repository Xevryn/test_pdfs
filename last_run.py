from datetime import date

today = date.today()  #2021-06-17

last_run_date = '2021-06-17'

if str(today) == last_run_date:
    print(f"This has already been run for today.  Exiting now")
else:
    with open(__file__, 'r') as f:
        num = 0
        content = f.readlines()
        for line in content:
            if line.startswith('test'):
                content[num] = f"last_run_date = '{today}'\n"
            num += 1
    with open(__file__, 'w') as f:
        f.writelines(content)
