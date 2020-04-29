with open('(Unix format) 2016 10 29 valid data.txt', 'rb') as f:
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
         f.seek(-2, os.SEEK_CUR)
    last_line = f.readline().decode()
    if re.match(r'^\b(\w*wtmp begins\w*)\b\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}$',last_line):
        print('valid')
    else:
        print('invalid')
