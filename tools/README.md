# 색인(인덱싱) 도구

영등포 사이트(`https://yeongdeungpo-massage1.pages.dev`)를 네이버·구글·빙에 가장 빠르게 등록·색인시키기 위한 도구 모음입니다.

빌드(`python build.py`)를 실행하면 다음이 자동 생성됩니다.

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 색인 대상 전체 URL + `lastmod` |
| `rss.xml` | 네이버 서치어드바이저 RSS 제출용 피드 |
| `robots.txt` | 두 사이트맵(`sitemap.xml`, `rss.xml`) 경로 안내 |
| `ffce108031f63445339b568a26fa3ce3.txt` | IndexNow 소유확인 키 파일(루트) |
| 모든 페이지 `<head>` | 네이버 소유확인 메타 태그 포함 |

> 순서 요약: **① 배포 → ② 네이버·구글 소유확인 + 사이트맵/RSS 제출 → ③ `python tools/indexnow.py` 로 빙·네이버 즉시 통보 → (선택) ④ 구글 Indexing API**

---

## 0. 먼저 배포

이 커밋을 푸시하면 Cloudflare Pages가 자동 배포합니다. 아래 URL이 200으로 떠야 다음 단계가 동작합니다.

- 사이트맵: `/sitemap.xml`
- RSS: `/rss.xml`
- IndexNow 키: `/ffce108031f63445339b568a26fa3ce3.txt`

---

## 1. 네이버 등록 (메인페이지 등록)

1. **네이버 서치어드바이저** → 사이트 등록: `https://yeongdeungpo-massage1.pages.dev/`
2. 소유확인: **HTML 태그** 방식 선택 → 이미 모든 페이지 `<head>`에
   `<meta name="naver-site-verification" content="8245b35f14db981b695e5bf4df4fda6798e08709">` 가 들어 있으므로 바로 "확인".
3. **요청 → 사이트맵 제출**: `sitemap.xml`
4. **요청 → RSS 제출**: `rss.xml`
5. **웹 페이지 수집** 에서 메인 URL(`/`)을 직접 입력해 "수집 요청" → 메인페이지 즉시 등록.

> 네이버는 IndexNow 참여사이므로 3·4단계 외에 `tools/indexnow.py` 통보도 함께 받습니다.

## 2. 구글 등록

1. **Google Search Console** → 속성 추가(URL 접두어): `https://yeongdeungpo-massage1.pages.dev/`
2. 소유확인: `content/site.py` 의 `GOOGLE_SITE_VERIFICATION` 에 발급 코드를 넣고 `python build.py` 재배포하면 메타 태그가 출력됩니다. (또는 DNS·HTML 파일 방식)
3. **색인 → Sitemaps** 에 `sitemap.xml`, `rss.xml` 제출.
4. **URL 검사** 에 메인 URL 입력 → "색인 생성 요청" → 메인페이지 즉시 요청.

## 3. IndexNow 즉시 통보 (빙·네이버·얀덱스)

배포가 끝난 뒤:

```bash
# 전체 일괄 통보 (최초 1회)
python tools/indexnow.py

# 글 새로 올릴 때마다 해당 URL만 통보
python tools/indexnow.py /magazine/new-post/
python tools/indexnow.py https://yeongdeungpo-massage1.pages.dev/seoul/yeongdeungpo-gu/yeoui-dong/
```

표준 라이브러리만 사용하며, HTTP 200/202 응답이면 정상 접수입니다.

## 4. (선택) 구글 Indexing API

구글은 IndexNow에 참여하지 않습니다. 더 빠른 통보가 필요하면:

```bash
pip install google-auth
export GOOGLE_APPLICATION_CREDENTIALS=/path/service_account.json
python tools/google_indexing.py            # 전체
python tools/google_indexing.py /some/page/  # 특정 URL
```

준비물·권한은 `tools/google_indexing.py` 상단 주석 참고. (Search Console에 서비스 계정을 **소유자**로 추가해야 함)

---

## sitemap ping 관련 안내

구글(`google.com/ping?sitemap=`)과 빙의 **사이트맵 ping 엔드포인트는 2023년에 폐지**되어 더 이상 동작하지 않습니다(404). 그래서 ping 스크립트는 만들지 않았습니다. 대신:

- **빙·네이버**: IndexNow (`tools/indexnow.py`) — 사실상 ping의 대체재
- **구글**: Search Console 사이트맵 제출 + (선택) Indexing API

가 현재 가장 빠르고 공식적인 방법입니다.

## 자동화

`.github/workflows/indexnow.yml` 를 활성화하면 `main` 푸시 후 배포 대기 시간을 두고
변경 URL을 IndexNow로 자동 통보합니다(저장소 Actions 사용 설정 필요).
