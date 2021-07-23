import os

file_lst = []

#Referenced https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/ for getting file paths
for r, d, f in os.walk('.'):
    for file in f:
        if ('.html' in file or 'secret' in file or 'flower' in file) and 'alex' not in file:
            file_lst.append(os.path.join(r,file)[2:])

with open('files.txt','w+') as f:
    f.write('<ul>\n')
    for file in file_lst:
        f.write(f'\t<li><a href="{file}" target="_blank">_____</a></li>\n')
    f.write('</ul>')