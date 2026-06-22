#!/usr/bin/env python3
# 지원서류 HTML → 경량 PDF (Cobalt 디자인 유지, 사용 글자만 폰트 서브셋)
# 사용: python3 tools/genpdf.py <basename>   예) python3 tools/genpdf.py 01_이력서_강민관
# 사전: tools/setup.sh 1회 실행 (fonttools/brotli + .fonts 폰트 다운로드)
import sys, os, re, io, html, base64, subprocess, time

REPO   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS  = os.path.join(REPO, ".fonts")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
NAME   = sys.argv[1]
SRC    = os.path.join(REPO, NAME + ".html")
OUT    = os.path.join(REPO, NAME + ".pdf")

from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options
from fontTools.varLib.instancer import instantiateVariableFont

def visible_chars(html_text):
    t = re.sub(r"<(style|script)\b[^>]*>.*?</\1>", " ", html_text, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    chars = set(t)
    chars |= set(chr(c) for c in range(0x20, 0x7f))            # ASCII printable
    chars |= set(" ·–—‘’“”…→✓­°−×·‧～")                          # 자주 쓰는 약물
    return {ord(c) for c in chars if c.strip() or c in "  "}

def subset_font(src_path, unicodes, wght=None):
    opts = Options()
    opts.flavor = "woff2"; opts.desubroutinize = True; opts.notdef_outline = True
    opts.recalc_timestamp = False; opts.name_IDs = ["*"]; opts.layout_features = []
    opts.hinting = False; opts.ignore_missing_glyphs = True; opts.ignore_missing_unicodes = True
    font = TTFont(src_path)
    if wght is not None and "fvar" in font:
        instantiateVariableFont(font, {"wght": wght}, inplace=True)   # 가변→정적 인스턴스
    ss = Subsetter(options=opts); ss.populate(unicodes=list(unicodes)); ss.subset(font)
    font.flavor = "woff2"; buf = io.BytesIO(); font.save(buf); return buf.getvalue()

def b64(d): return base64.b64encode(d).decode("ascii")

with open(SRC, encoding="utf-8") as f:
    src_html = f.read()
uni = visible_chars(src_html)

p400 = subset_font(os.path.join(FONTS, "pretendard-var.woff2"), uni, wght=400)
p700 = subset_font(os.path.join(FONTS, "pretendard-var.woff2"), uni, wght=700)
g4   = subset_font(os.path.join(FONTS, "geist-400.woff2"), uni)
g5   = subset_font(os.path.join(FONTS, "geist-500.woff2"), uni)
print(f"subset: pre400 {len(p400)//1024}KB · pre700 {len(p700)//1024}KB · geist {(len(g4)+len(g5))//1024}KB · glyphs~{len(uni)}")

face = ('<style id="embedded-fonts">\n'
 f'@font-face{{font-family:"Pretendard";font-weight:400;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,{b64(p400)}) format("woff2")}}\n'
 f'@font-face{{font-family:"Pretendard";font-weight:700;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,{b64(p700)}) format("woff2")}}\n'
 f'@font-face{{font-family:"Geist Mono";font-weight:400;font-style:normal;src:url(data:font/woff2;base64,{b64(g4)}) format("woff2")}}\n'
 f'@font-face{{font-family:"Geist Mono";font-weight:500;font-style:normal;src:url(data:font/woff2;base64,{b64(g5)}) format("woff2")}}\n'
 '</style>\n')

tmp_html = src_html
tmp_html = re.sub(r'\s*<link[^>]*pretendard[^>]*>', '', tmp_html, flags=re.I)
tmp_html = re.sub(r'\s*<link[^>]*Geist\+Mono[^>]*>', '', tmp_html, flags=re.I)
tmp_html = tmp_html.replace("</head>", face + "</head>", 1)

TMP = os.path.join(REPO, f"_print_{NAME}.html")
with open(TMP, "w", encoding="utf-8") as f:
    f.write(tmp_html)

prof = "/tmp/chrome-pdf-run"
subprocess.run(["pkill", "-f", "chrome-pdf-run"], capture_output=True); time.sleep(0.5)
for p in (OUT, prof):
    if os.path.isdir(p): subprocess.run(["rm", "-rf", p])
    elif os.path.exists(p): os.remove(p)
proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
    f"--user-data-dir={prof}", "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=6000", f"--print-to-pdf={OUT}", "file://" + TMP],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
for _ in range(15):
    time.sleep(1)
    if os.path.exists(OUT) and os.path.getsize(OUT) > 0: break
time.sleep(1); proc.terminate()
try: os.remove(TMP)
except OSError: pass
print(f"OK: {OUT} ({os.path.getsize(OUT)} bytes)" if os.path.exists(OUT) else "FAIL: no PDF")
