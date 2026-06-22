# 현대차 지원서류 — HANDOFF (이어가기 안내)

> 다른 기기(개인 맥북)·새 Claude 세션에서 이어가려면 **이 문서를 먼저 읽으세요.**
> 강민관(프로덕트/UX 디자이너, 9년차)의 **현대자동차그룹 UX 지원서류 패키지**. 4개 문서를 하나의 디자인 시스템(Cobalt)으로 통일 제작.

## 저장소 구조 (2개)
- **`Greencar-UXD/career-docs` (비공개)** = 이 작업 저장소. 전체 원본(이력서·자소서·경력기술서·포트폴리오·케이스·마스터)+툴+HANDOFF. **PII 포함 → 반드시 비공개.** 로컬 `~/Downloads/현대차_지원서류`.
- **`Greencar-UXD/portfolio` (공개)** = 라이브 포트폴리오 사이트만(포트폴리오+케이스, 전화번호 제외, 이메일만). **라이브: https://greencar-uxd.github.io/portfolio/** . 로컬 `~/Downloads/portfolio-public`.
- 공개 사이트 갱신: career-docs에서 포트폴리오 수정 후 **`zsh tools/publish-site.sh`** → portfolio repo로 빌드·푸시(Pages 자동 재배포). 절대 이력서·자소서를 공개 repo에 넣지 말 것.

---

## 1. 다른 맥북에서 이어가기 (3단계)
```bash
# 1) 클론  (GitHub 비공개 저장소)
gh repo clone Greencar-UXD/career-docs    # 비공개 작업 저장소
cd career-package

# 2) 1회 환경 구축 (폰트·라이브러리)
zsh tools/setup.sh

# 3) PDF 생성 확인
python3 tools/genpdf.py 01_이력서_강민관
```
- **필요**: macOS · Google Chrome(헤드리스 인쇄) · python3 · gh(또는 git). node·brew 불필요.
- 새 Claude 세션엔 "**HANDOFF.md 읽고 현대차 지원서류 이어가자**"라고 말하면 이 문맥으로 복원됩니다.
- **모바일**: GitHub 앱에서 저장소 열면 PDF가 바로 보입니다. (Drive 동기화 시 Drive 앱에서도)

## 2. 디렉터리
```
00_마스터_경력프로필.md     ← 모든 문서의 기준(사실·표기·제외)  ★먼저 읽기
01_이력서_강민관.html/.pdf
02_경력기술서_강민관.html/.pdf
03_자기소개서_강민관.html/.pdf
04_포트폴리오_강민관.html/.pdf      ← 개요(웹+PDF)
04A_케이스_디지털빌딩OS.html         ← 심화 케이스
assets/cobalt-doc.css               ← 공통 디자인 시스템(이력서·경력·자소서)
assets/portfolio.css                ← 포트폴리오 레이아웃 + Cobalt 비주얼 키트
tools/genpdf.py · tools/setup.sh    ← PDF 생성 파이프라인
.fonts/ (gitignore)                 ← setup.sh가 받는 폰트 원본
```

## 3. 디자인 시스템 — Cobalt — Mono
- 출처: 본인 레포 `Greencar-UXD/design-system` (브랜치 feat/restructure-and-showcase).
- 모노크롬 그레이 + **코발트 액센트 #2d5bff**(절제), 본문/주요액션은 잉크 #14171b.
- 폰트: **Pretendard**(KR+EN) + **Geist Mono**(숫자·기간·DOI). 4px 그리드. 라이트.
- 4개 문서가 `assets/cobalt-doc.css` 토큰을 공유 → 통일감. 수정은 이 파일에서.
- PDF는 사용 글자만 서브셋 임베드(`tools/genpdf.py`) → 85~180KB 경량. (500→400·600→700 매핑)

## 4. 검증된 사실 (절대 기준 — 흔들리지 말 것)
- 경력 **9년차** (2017.07~). 옛 문서의 8/5/10년 표기 폐기.
- 이름 **강민관**. "김현규"는 OCR 오인 — 사용 금지.
- 그린카: 매니저·대표이사 직속 IT전략실 UXD파트. 카셰어링(롯데렌탈). **누적가입 527만+**(공개 수치).
- 핀포인트 빌딩OS TF 기여 **60%**. 회사명 정식표기(카방·알케이웍스·엑스위젯·Taap).
- 석사 게재 논문: 「자율주행 로보택시의 인포테인먼트 UX 구성요소 연구」, 한국디자인리서치학회(KIDRS) 통권36호(2025), **DOI 10.46248/kidrs.2025.3.686**.
- 타깃 = **현대자동차그룹 일반**(SDV·Pleos·Pleos Connect·PBV·로보틱스). 옛 자소서의 **기아(Kia) 잔재 제거 완료**.

## 5. 제외 (이력서·경력기술서·포트폴리오에 넣지 말 것)
- DNL STUDIO 프리랜스 일체(계약·견적·클라이언트). 롯데렌탈/롯데렌터카 CI·BI(모회사 IP). 차량이미지 라이브러리(저작권).
- 그린카·핀포인트 **내부 기밀**: 연령비중·전환율·이탈률·Amplitude 화면·KPI/PTR/DRM·실제 내부 화면 → 일반화.
- 포트폴리오 비주얼은 **Cobalt로 재구성한 추상 UI/다이어그램**(기밀 실화면 대신).

## 6. 현재 상태 / 다음 단계
- ✅ **완성**: 01 이력서(1p) · 02 경력기술서(2p) · 03 자기소개서(2p, 통합본+항목별4문항) · 04 포트폴리오 개요(3p, 웹+PDF).
- ⏳ **다음 = 포트폴리오 심화 케이스 3건** (개요가 이미 링크함):
  - `04A_케이스_디지털빌딩OS` — 존재하나 자리표시 JPG → Cobalt 비주얼로 교체 필요.
  - `04B_케이스_Gcar_v2` — 신규(데이터 기반 상위기획 스토리).
  - `04C_케이스_로보택시연구` — 신규(게재 논문 기반: 방법론·5대 구성요소).
  - ※ 폴더의 옛 `04B_케이스_로보택시`·`04C_케이스_카방`은 이전 초안 — 새 케이스로 대체·정리 예정.
- ⏳ **Drive 업로드**: 방식=구글 드라이브 데스크톱 동기화(사용자 결정). 설치되면 동기화 폴더에 PDF 복사.
- 미결: 현대차 실제 지원 공고·마감 미확정 / .docx는 구버전(정본은 HTML→PDF) / 차량 IVI 목업 보강 검토.

## 7. 작업 방식 메모
- 검증: PDF는 페이지 렌더로 확인(`sips -s format png x.pdf --out /tmp/x.png`, 첫 장). 웹은 /tmp 스테이징 후 프리뷰.
- 디자인 원칙: 과한 설명·중복 지양, 미니멀·통일. 이모지 금지(Cobalt는 라인 아이콘).
