import re,html,sys
def txt(f):
    t=html.unescape(re.sub(r'<[^>]+>',' ',open(f,errors='ignore').read())); return re.sub(r'\s+',' ',t)
f=sys.argv[1]; t=txt(f); w=int(sys.argv[2]); n=int(sys.argv[3])
for pat in sys.argv[4:]:
    ms=list(re.finditer(pat,t))
    print(f'##### [{pat}] {len(ms)} hits')
    for m in ms[:n]: print('  >', t[max(0,m.start()-w):m.end()+w]); print()
