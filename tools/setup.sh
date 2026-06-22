#!/bin/zsh
# 현대차 지원서류 — 1회 환경 구축 (macOS)
# PDF 생성에 필요한 폰트(서브셋 원본)·라이브러리 준비. 새 맥북에서 clone 후 한 번 실행하세요.
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
FONTS="$DIR/.fonts"

echo "▶ fonttools · brotli 설치 (pip --user)"
pip3 install --user --quiet fonttools brotli

echo "▶ 폰트 다운로드 → $FONTS"
mkdir -p "$FONTS"
curl -fsSL -o "$FONTS/pretendard-var.woff2" "https://cdn.jsdelivr.net/npm/pretendard@latest/dist/web/variable/woff2/PretendardVariable.woff2"
curl -fsSL -o "$FONTS/geist-400.woff2" "https://cdn.jsdelivr.net/npm/@fontsource/geist-mono@5/files/geist-mono-latin-400-normal.woff2"
curl -fsSL -o "$FONTS/geist-500.woff2" "https://cdn.jsdelivr.net/npm/@fontsource/geist-mono@5/files/geist-mono-latin-500-normal.woff2"

echo ""
echo "✓ 준비 완료."
echo "  PDF 생성:  python3 tools/genpdf.py 01_이력서_강민관"
echo "  (Google Chrome 설치 필요 — 헤드리스 인쇄에 사용)"
