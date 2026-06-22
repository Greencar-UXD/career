#!/bin/zsh
# 공개 포트폴리오 사이트 갱신·배포 (Greencar-UXD/portfolio · GitHub Pages)
# career-docs에서 포트폴리오·케이스를 변환→공개 repo에 푸시. Pages가 자동 재배포.
# 사용: zsh tools/publish-site.sh
set -e
SRC="$(cd "$(dirname "$0")/.." && pwd)"        # career-docs (비공개)
PUB="${1:-$(dirname "$SRC")/portfolio-public}" # 공개 사이트 작업 폴더(기본: 형제 폴더)

if [ ! -d "$PUB/.git" ]; then
  echo "▶ 공개 사이트 저장소 클론 → $PUB"
  gh repo clone Greencar-UXD/portfolio "$PUB"
fi
echo "▶ 사이트 빌드(전화번호 제거·ASCII 파일명)"
python3 "$SRC/tools/build_site.py" "$SRC" "$PUB"
cd "$PUB"
git add -A
git commit -m "update portfolio site" || { echo "변경 없음"; exit 0; }
git push
echo "✓ 배포 트리거됨 → https://greencar-uxd.github.io/portfolio/ (1~2분 내 반영)"
