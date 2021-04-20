pages = {}

for i in range(24):
    hour = ""
    if i <= 9:
        hour = "0"+str(i)
    else:
        hour = str(i)

    filename = "pageviews-20190101-"+hour+"0000"
    fin = open(filename, "r", encoding='utf-8', errors='ignore')
    print("-> READING FILE "+hour)

    last_lang = ""
    while True:
        line = fin.readline()
        if not line:
            break

        cur_lang = line[0:2]
        words = line.split(" ")
        pagename = words[1]
        viewcount = words[2]


        if cur_lang != last_lang:
            last_lang = cur_lang
            if cur_lang not in pages:
                pages[cur_lang] = {}

        if pagename not in pages[cur_lang]:
            pages[cur_lang][pagename] = viewcount
        else:
            pages[cur_lang][pagename] += viewcount


    fin.close()

for k in list(pages.keys()):
    fout = open(k, "w", encoding='utf-8', errors='ignore')
    for elem in pages[k]:
        fout.write(elem+" "+pages[k][elem]+"\n")
    fout.close()
