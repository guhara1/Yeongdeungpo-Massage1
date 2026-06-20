#!/usr/bin/env python3
"""Google Indexing API 색인 통보 (구글은 IndexNow 미참여).

구글은 IndexNow에 참여하지 않으므로, 빠른 색인 통보가 필요하면 이 스크립트를 씁니다.
공식적으로 Indexing API는 JobPosting·BroadcastEvent 용이지만, 일반 URL 통보에도 흔히
사용됩니다(보장되진 않음). 가장 확실한 경로는 Search Console 사이트맵/rss 제출입니다.

── 사전 준비 (최초 1회) ──
1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
2) 서비스 계정 생성 → JSON 키 다운로드 (예: service_account.json)
3) Google Search Console에서 해당 사이트 속성에 서비스 계정 이메일을
   "소유자(Owner)" 권한으로 추가
4) 의존성 설치:  pip install google-auth

── 사용법 ──
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service_account.json
  python tools/google_indexing.py                       # sitemap 전체 통보
  python tools/google_indexing.py https://.../some/page/  # 특정 URL만
  python tools/google_indexing.py --delete https://.../old/  # 삭제 통보

쿼터: 기본 하루 200건. 분당 600건.
"""
import json
import os
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL  # noqa: E402

API = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def get_token():
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("환경변수 GOOGLE_APPLICATION_CREDENTIALS 에 서비스 계정 JSON 경로를 지정하세요.")
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import Request
    except ImportError:
        sys.exit("google-auth 가 필요합니다:  pip install google-auth")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    creds.refresh(Request())
    return creds.token


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 가 없습니다. 먼저 `python build.py` 를 실행하세요.")
    tree = ET.parse(path)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text.strip() for loc in tree.findall(".//s:loc", ns)]


def normalize(args):
    out = []
    for a in args:
        a = a.strip()
        if a.startswith("http"):
            out.append(a)
        else:
            out.append(BASE_URL.rstrip("/") + "/" + a.lstrip("/"))
    return out


def notify(token, url, kind):
    payload = json.dumps({"url": url, "type": kind}).encode("utf-8")
    req = urllib.request.Request(
        API, data=payload, method="POST",
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return f"{e.code} {e.read().decode('utf-8', 'replace')[:200]}"
    except urllib.error.URLError as e:
        return f"ERR {e.reason}"


if __name__ == "__main__":
    args = sys.argv[1:]
    kind = "URL_UPDATED"
    if "--delete" in args:
        kind = "URL_DELETED"
        args = [a for a in args if a != "--delete"]
    urls = normalize(args) if args else sitemap_urls()
    token = get_token()
    print(f"Google Indexing API · {kind} · {len(urls)}개")
    ok = 0
    for u in urls:
        r = notify(token, u, kind)
        status = "✓" if r == 200 else "✗"
        if r == 200:
            ok += 1
        print(f"  {status} {u}  ({r})")
    print(f"\n완료: {ok}/{len(urls)} 성공")
