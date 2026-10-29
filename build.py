"""Ghép slides/<id>.html (thứ tự trong deck.json) thành index.html xem được ở local.
python3 build.py  →  index.html ;  xem: python3 -m http.server 8791  →  http://localhost:8791
Phím: ← → / Space chuyển slide · N bật/tắt ghi chú người nói · F toàn màn hình · O xem tổng quan
Video: tự phát (tắt tiếng) khi vào slide, dừng khi rời slide; bấm vào video để bật tiếng / tua."""
import json
from pathlib import Path

HERE = Path(__file__).parent

PAGE = """<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#16181D">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns=%%27http://www.w3.org/2000/svg%%27 viewBox=%%270 0 64 64%%27%%3E%%3Crect width=%%2764%%27 height=%%2764%%27 rx=%%2714%%27 fill=%%27%%23E2492F%%27/%%3E%%3Cpath d=%%27M18 20h28v6H35v20h-6V26H18z%%27 fill=%%27white%%27/%%3E%%3C/svg%%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,700;0,800;1,400&family=Lora:ital,wght@0,500;1,500&display=swap">
<style>
:root{--paper:#F5F1EA;--card:#FFFDF8;--ink:#16181D;--muted:#4B5160;--soft:#6A6F7A;--line:#D9D2C4;
 --red:#E2492F;--red-d:#C73A22;--red-l:#F08A6E;--blue:#2C5FC7;--green:#2F8F5B;--gold:#E8B53A}
html,body{margin:0;height:100%%;background:#0d0e11;overflow:hidden}
#stage{position:absolute;left:50%%;top:50%%;width:1920px;height:1080px;transform-origin:50%% 50%%}
section{position:absolute;inset:0;box-sizing:border-box;overflow:hidden;display:flex;flex-direction:column;
 font-family:'Be Vietnam Pro',Arial,sans-serif;background:var(--paper);color:var(--ink);padding:112px 128px 160px;gap:40px}
section.dark{background:var(--ink);color:var(--paper)}
section:not(.on){display:none!important}
section *{margin:0;box-sizing:border-box}
section ul,section ol{padding-left:1.2em}
.kicker{font-size:24px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--red-d)}
.dark .kicker{color:var(--red-l)}
h1{font-size:104px;font-weight:800;line-height:1.05;text-wrap:balance}
h2{font-size:64px;font-weight:700;line-height:1.12;text-wrap:balance}
.lead{font-size:34px;line-height:1.4;color:var(--muted)} .dark .lead{color:#C9CED8}
.src{position:absolute;left:128px;bottom:56px;width:1664px;font-size:22px;color:var(--soft)}
.dark .src{color:#8A90A0}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:32px;display:flex;flex-direction:column;gap:12px}
.dark .card{background:#1F2229;border-color:#2E323B}
.card h3{font-size:38px;font-weight:700;line-height:1.2} .card p{font-size:30px;line-height:1.4}
.stat p{font-size:28px;color:var(--muted);margin-top:8px} p.big,.stat p.big{font-size:96px;font-weight:800;line-height:1;margin:0}
.fill{flex:1;min-height:0}
.dark .stat p{color:#C9CED8}
.row{display:flex;gap:40px;align-items:stretch} .col{display:flex;flex-direction:column;gap:24px}
.pill{display:inline-block;font-size:24px;font-weight:700;padding:6px 16px;border-radius:999px;background:var(--red);color:#fff}
video,.shot{border-radius:16px;background:#000;display:block}
.q{font-family:Lora,serif;font-style:italic}
aside{display:none}
#notes{position:fixed;left:0;right:0;bottom:0;max-height:38vh;overflow:auto;background:#1d2027ee;color:#e8e6e1;
 font:18px/1.5 'Be Vietnam Pro',sans-serif;padding:16px 24px;display:none;white-space:pre-wrap}
#bar{position:fixed;right:16px;bottom:12px;color:#888;font:14px sans-serif}
body.ov #stage{display:none} #ov{display:none} body.ov #ov{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;padding:16px;
 height:100%%;overflow:auto;box-sizing:border-box} #ov div{color:#ddd;font:14px sans-serif;background:#222;padding:10px;cursor:pointer;border-radius:6px}
</style></head><body>
<div id="stage">%(slides)s</div><div id="ov"></div><div id="notes"></div><div id="bar"></div>
<script>
const S=[...document.querySelectorAll('#stage>section')],st=document.getElementById('stage'),nt=document.getElementById('notes'),bar=document.getElementById('bar');
let i=Math.max(0,Math.min(S.length-1,(parseInt(location.hash.slice(1))||1)-1)),notes=false;
function fit(){const k=Math.min(innerWidth/1920,innerHeight/1080);st.style.transform=`translate(-50%%,-50%%) scale(${k})`;}
function show(n){i=Math.max(0,Math.min(S.length-1,n));S.forEach((s,j)=>s.classList.toggle('on',j===i));
 document.querySelectorAll('video').forEach(v=>{if(!S[i].contains(v))v.pause()});
 S[i].querySelectorAll('video').forEach(v=>{if(v.preload==='none')v.preload='metadata'});
 S[i].querySelectorAll('video[data-auto]').forEach(v=>{v.muted=true;v.currentTime=0;v.play().catch(()=>{})});
 (S[i+1]||{querySelectorAll:()=>[]}).querySelectorAll('video').forEach(v=>{if(v.preload==='none')v.preload='metadata'});
 const a=S[i].querySelector('aside');nt.textContent=a?a.textContent.trim():'';nt.style.display=notes&&a?'block':'none';
 bar.textContent=(i+1)+' / '+S.length;history.replaceState(null,'','#'+(i+1));}
addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();show(i+1)}else if(['ArrowLeft','PageUp'].includes(e.key))show(i-1);
 else if(e.key==='n'||e.key==='N'){notes=!notes;show(i)}else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
 else if(e.key==='o'||e.key==='O'){document.body.classList.toggle('ov')}else if(e.key==='Home')show(0);else if(e.key==='End')show(S.length-1);});
addEventListener('click',e=>{if(document.body.classList.contains('ov')||e.target.closest('video'))return;e.clientX>innerWidth/2?show(i+1):show(i-1)});
const ov=document.getElementById('ov');S.forEach((s,j)=>{const d=document.createElement('div');const h=s.querySelector('h1,h2');
 d.textContent=(j+1)+'. '+(h?h.textContent:s.id);d.onclick=()=>{document.body.classList.remove('ov');show(j)};ov.appendChild(d)});
let tx=null;addEventListener('touchstart',e=>{tx=e.touches[0].clientX},{passive:true});
addEventListener('touchend',e=>{if(tx===null||e.target.closest('video'))return;const dx=e.changedTouches[0].clientX-tx;tx=null;if(Math.abs(dx)>50)show(i+(dx<0?1:-1))},{passive:true});
addEventListener('resize',fit);fit();show(i);
</script></body></html>"""


def main():
    deck = json.loads((HERE / 'deck.json').read_text())
    # video chỉ tải khi tới slide (preload="none" → JS đổi sang metadata), tránh kéo ~36 MB lúc mở trang
    parts = [(HERE / 'slides' / f'{sid}.html').read_text().replace('<video ', '<video preload="none" ')
             for sid in deck['order']]
    (HERE / 'index.html').write_text(PAGE % {'title': deck['title'], 'desc': deck.get('description', ''), 'slides': '\n'.join(parts)})
    print(f'index.html · {len(parts)}/{len(deck["order"])} slide')


if __name__ == '__main__':
    main()
