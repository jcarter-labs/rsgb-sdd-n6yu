import re,html,sys
src=open('/Users/N6YU/Projects/rsgb-sdd-n6yu/masterplan/masterplan-generator.md').read()
secs=[]
for m in re.finditer(r'^## (\d)\. ([^:]+): (.+?) \*\((.+?)\)\*\n(.*?)(?=^## )',src,re.M|re.S):
    n,name,sub,how,body=m.groups()
    prompts=re.findall(r'```\n(.*?)\n```',body,re.S)
    lines=[l for p in prompts for l in p.split('\n') if l.strip()]
    rows=[]
    for l in lines:
        mm=re.match(r'(RULE|DRAFT|USER INPUT): (.*)',l)
        rows.append((mm.group(1),mm.group(2)))
    secs.append((n,name,sub,how,rows))
assert [len(s[4]) for s in secs]==[5,5,5,5],[len(s[4]) for s in secs]
fs=float(sys.argv[1]) if len(sys.argv)>1 else 30
def sec(s):
    n,name,sub,how,rows=s
    r=''.join(f'<div class="row"><span class="tag {t.split()[0].lower()}">{t.lower()}</span><p>{html.escape(x)}</p></div>' for t,x in rows)
    return f'<section><h2><span class="n">{n}</span> {name}<span class="sub"> {html.escape(sub)}</span></h2><div class="how">{html.escape(how)}</div>{r}</section>'
page=f'''<!doctype html><meta charset=utf-8><style>
html,body{{margin:0;background:#fffff8}}
body{{width:3200px;height:1500px;box-sizing:border-box;padding:46px 70px;font-family:Palatino,"Palatino Linotype","Book Antiqua",Georgia,serif;color:#111;font-size:{fs}px;line-height:1.28}}
.cols{{display:grid;grid-template-columns:1fr 1fr;column-gap:110px}}
section{{margin-bottom:34px}}
h2{{font-weight:normal;font-size:1.5em;margin:0;line-height:1.1}}
h2 .n{{font-style:italic;color:#8a1c1c}}
h2 .sub{{font-style:italic;color:#444;font-size:.78em}}
.how{{font-size:.7em;font-variant:small-caps;letter-spacing:.06em;color:#666;margin:2px 0 10px;border-bottom:1px solid #999;padding-bottom:7px}}
.row{{display:grid;grid-template-columns:5.2em 1fr;column-gap:14px;margin:0 0 9px}}
.row p{{margin:0}}
.tag{{font-variant:small-caps;letter-spacing:.06em;font-size:.82em;color:#777;text-align:right;padding-top:.12em;white-space:nowrap}}
.tag.rule{{color:#8a1c1c;font-weight:bold}}
.tag.user{{color:#111;font-weight:bold}}
</style><body><div class="cols"><div>{sec(secs[0])}{sec(secs[1])}</div><div>{sec(secs[2])}{sec(secs[3])}</div></div>'''
open(sys.argv[2] if len(sys.argv)>2 else 'gen.html','w').write(page)
