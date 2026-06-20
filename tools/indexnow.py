#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex 등 IndexNow 참여 검색엔진.

사용법:
  # 1) 사이트 전체(sitemap.xml 기준) 일괄 통보
  python tools/indexnow.py

  # 2) 특정 URL만 통보 (글 새로 올렸을 때)
  python tools/indexnow.py https://yeongdeungpo-massage1.pages.dev/magazine/새글/

  # 3) 경로만 넘겨도 됨 (도메인 자동 부착)
  python tools/indexnow.py /magazine/새글/  /seoul/yeongdeungpo-gu/yeoui-dong/

주의:
  - 통보 전에 배포가 끝나 있어야 합니다. IndexNow가 https://<도메인>/<키>.txt 를
    조회해 소유권을 확인하기 때문입니다. (키 파일은 build.py가 루트에 발행)
  - 표준 라이브러리만 사용합니다(requests 불필요).
"""
import json
import os
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

HOST = BASE_URL.split("://", 1)[-1].strip("/")
ENDPOINT = "https://api.indexnow.org/indexnow"


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
        if a.startswith("http://") or a.startswith("https://"):
            out.append(a)
        else:
            out.append(BASE_URL.rstrip("/") + "/" + a.lstrip("/"))
    return out


def submit(urls):
    if not urls:
        print("통보할 URL이 없습니다.")
        return
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.status
            body = resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        code = e.code
        body = e.read().decode("utf-8", "replace")
    except urllib.error.URLError as e:
        sys.exit(f"네트워크 오류: {e.reason}")

    print(f"IndexNow 응답: HTTP {code}")
    if body.strip():
        print(body.strip())
    # 200/202 = 정상 접수
    if code in (200, 202):
        print(f"✓ {len(urls)}개 URL 통보 완료 (Bing·Naver·Yandex 등에 전파됩니다).")
    else:
        print("⚠ 접수에 실패했을 수 있습니다. 키 파일 접근 가능 여부와 도메인을 확인하세요.")
        print(f"  키 파일: {BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt")


if __name__ == "__main__":
    args = sys.argv[1:]
    urls = normalize(args) if args else sitemap_urls()
    print(f"호스트: {HOST}  |  URL {len(urls)}개")
    submit(urls)
