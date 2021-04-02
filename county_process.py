import json
from bs4 import BeautifulSoup
import sys
from html2text import html2text
import re
from multiprocessing import Pool, freeze_support



R = re.compile("\d+.\d+%")


PATTERNS = (
    "African American",
    "Black",
    "Native American",
    "Asian",
    "Pacific Islander",
    "other races",
    "Hispanic",
    "Latino",
    "White",
    "white",
)


def distances(txt):
    demos = {}
    idx_percentages = [m.start(0) for m in re.finditer("\d+.\d+%", txt)]
    percentages = R.findall(txt)
    #print("percentages:", percentages)
    #print("idx_percentages", idx_percentages)
    for pattern in PATTERNS:
        if pattern in txt:
            #print("pattern:", pattern)
            idx_pattern = txt.index(pattern)
            distances = [abs(idx_pattern - i_perc) for i_perc in idx_percentages]
            #print("distances:", distances)
            if len(distances):
                min_dist = min(distances)
                min_idx = distances.index(min_dist)
                demos[pattern] = percentages[min_idx]
    return demos




def demo_count(txt):
    count = 0
    for pattern in PATTERNS:
        if pattern in str(txt):
            count += 1
    return count


def do_process(t):
    url, content = t
    soup = BeautifulSoup(content,'html.parser')
    cands = [(demo_count(p), p) for p in soup.find_all('p')]
    counts = [count for (count, p) in cands]
    best = max(counts)
    best_idx = counts.index(best)
    paragraph = str(cands[best_idx][1])

    my_db = {}
    txt = html2text(paragraph)
    my_db[url] = distances(txt), txt
    print(".", end="")
    sys.stdout.flush()
    return my_db

def main():
    print("Reading DB...", end="")
    sys.stdout.flush()
    db = json.loads(open("countydb.json").read())
    print("Done")
    sys.stdout.flush()

    args = []
    for url in list(db.keys()):
        args.append((url, db[url]))

    with Pool(20) as p:
        ret_list = p.map(do_process, args)

    print("Writing DB")
    sys.stdout.flush()

    demodb = {}

    for d in ret_list:
        demodb.update(d)

    content = json.dumps(demodb,indent=2)
    with open("countydemodb.json","w") as fp:
        fp.write(content)
    print("Done")

if __name__ == "__main__":
    freeze_support()
    ret = main()