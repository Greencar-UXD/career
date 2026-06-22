#!/usr/bin/env python3
# career-docs(비공개)의 포트폴리오·케이스 → 공개 사이트(portfolio repo)용으로 변환.
# 전화번호 제거 · 파일명 ASCII화 · 04 포트폴리오를 index.html로.
# 사용: python3 tools/build_site.py <career-docs경로> <portfolio-public경로>
import sys, os, re, shutil

src, pub = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(pub, "assets"), exist_ok=True)

mapping = {
    "04_포트폴리오_강민관.html": "index.html",
    "04A_케이스_디지털빌딩OS.html": "case-buildingos.html",
    "04B_케이스_Gcar_v2.html": "case-gcar.html",
    "04C_케이스_로보택시연구.html": "case-robotaxi.html",
}
for srcname, dstname in mapping.items():
    with open(os.path.join(src, srcname), encoding="utf-8") as f:
        html = f.read()
    for k, v in mapping.items():          # 내부 링크 ASCII화
        html = html.replace(k, v)
    html = html.replace('<span>010-2104-0663</span>', '').replace('010-2104-0663', '')
    with open(os.path.join(pub, dstname), "w", encoding="utf-8") as f:
        f.write(html)
for css in ("cobalt-doc.css", "ds-components.css", "portfolio.css"):
    shutil.copy(os.path.join(src, "assets", css), os.path.join(pub, "assets", css))
open(os.path.join(pub, ".nojekyll"), "w").close()
print("공개 사이트 빌드 완료 →", pub)
