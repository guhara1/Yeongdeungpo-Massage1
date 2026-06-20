# 바로GO — 영등포 출장마사지·홈타이 안내 사이트

영등포구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
전화예약: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(바로GO)·전화·BASE_URL·텔레그램·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/WebPage/FAQPage JSON-LD)
  areas.py          # 지역별: 영등포구 허브 + 대표 동 9개
  stations.py       # 역세권: 허브 + 16개 역
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  about.py          # 운영자 소개(E-E-A-T)
assets/             # CSS(프리미엄 팔레트·오렌지 CTA), 모바일 내비 JS
```

URL 구조: 지역 페이지는 `/seoul/yeongdeungpo-gu/`, 역세권은 `/seoul/yeongdeungpo-gu/station/` 하위에 생성됩니다.

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 9개만 (영등포본동·영등포동·여의동·당산동·도림동·문래동·양평동·신길동·대림동) — 숫자 행정동 페이지 없음 (당산1·2동, 양평1·2동, 신길1·3·4·5·6·7동, 대림1·2·3동은 대표 동으로 통합)
- 역은 역 1개당 페이지 1개 — 환승역도 URL 하나, 출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 메뉴명·URL 에 "출장마사지" 반복 없음 — 키워드는 Title·H1·첫 문단에서만 자연스럽게 사용
- 방문형 사이트(오프라인 주소 없음)이므로 LocalBusiness 계열 스키마 미사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. 필요 시 `content/site.py`의 `TELEGRAM_URL`(제작·제휴 문의 채널) 확인
3. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
4. Google Search Console에 `sitemap.xml` 제출
