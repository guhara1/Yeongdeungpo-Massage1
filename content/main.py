# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# 방문형 사이트(오프라인 주소 없음)이므로 LocalBusiness 계열 스키마는 사용하지 않는다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "logo": "{BASE_URL}/assets/og-image.png",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "영등포구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 영등포구"
  }},
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "{PHONE}",
    "contactType": "reservations",
    "areaServed": "KR",
    "availableLanguage": "Korean"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "영등포구 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "inLanguage": "ko-KR",
  "breadcrumb": {{
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/"}}
    ]
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "영등포구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 여의동, 영등포본동, 당산동, 문래동, 신길동 등 아홉 개 대표 동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "여의도역이나 영등포역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "신길1동과 신길3동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "신길1·3·4·5·6·7동은 신길동 대표 페이지에서, 당산1·2동은 당산동, 양평1·2동은 양평동, 대림1·2·3동은 대림동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "테마별 관리는 어디에서 확인하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 영등포구 전지역</p>
    <h1>영등포구 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>여의도·영등포역·당산·문래·신길 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>9개</strong><span>대표 지역</span></li>
      <li><strong>16개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>영등포구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>영등포구 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 영등포구는 여의도 업무지구와 국회의사당 주변, 영등포역과 타임스퀘어 중심 상권, 문래동과 당산동의 주거·상업 생활권, 신길동과 대림동의 주거 생활권이 함께 있는 자치구입니다. 그래서 영등포구 사이트는 "전지역 가능"만 적기보다 대표 동과 역세권을 나누어 안내하는 구조가 정확합니다. 이 페이지는 영등포구 전체 구조를 설명하는 허브이며, 자세한 내용은 지역별·역세권별·테마별 안내에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차로 진행하며, 홈타이가 처음인 분도 어렵지 않게 예약하실 수 있도록 각 단계를 분명하게 안내합니다.</p>
</section>

<section id="zones">
<h2>여의도·영등포역·당산·문래 생활권 차이</h2>
<p>같은 영등포구라도 생활권마다 분위기와 방문 조건이 다릅니다. 여의도는 업무지구·국회·한강공원이 이어지는 영등포구에서 검색 의도가 가장 뚜렷한 권역이고, 영등포역·타임스퀘어 일대는 백화점과 상권이 밀집한 교통 중심지입니다. 문래동은 문래창작촌과 주거지가 섞인 독자적 생활권이며, 당산동·양평동은 한강변과 업무·주거가 함께 있는 권역입니다. 신길동과 대림동은 재개발과 주거 밀집이 특징입니다. 권역마다 시간대별 차량 이동 기준이 달라질 수 있으므로, 각 페이지의 방문 가능 지역과 추가 이동비 확인 안내를 함께 살펴보시는 것이 좋습니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 영등포구 아홉 개 대표 동을 기준으로 구성됩니다. 당산1·2동은 당산동, 양평1·2동은 양평동, 신길1·3·4·5·6·7동은 신길동, 대림1·2·3동은 대림동 페이지에서 통합 안내하며, 번호 동을 개별 페이지로 쪼개지 않습니다. 각 페이지에서는 생활권 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간을 동마다 고유하게 설명합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/yeongdeungpo-gu/yeongdeungpobon-dong/">영등포본동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/yeongdeungpo-dong/">영등포동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/yeoui-dong/">여의동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/dangsan-dong/">당산동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/dorim-dong/">도림동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/mullae-dong/">문래동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/yangpyeong-dong/">양평동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/singil-dong/">신길동</a></li>
<li><a href="/seoul/yeongdeungpo-gu/daerim-dong/">대림동</a></li>
</ul>
<p>영등포구 전체 구조가 궁금하시면 <a href="/seoul/yeongdeungpo-gu/">영등포구 지역별 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>영등포역·여의도역·당산역·문래역 역세권 안내</h2>
<p>역세권 안내는 영등포구를 지나는 1·2·5·7·9호선 주요 역을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표 동, 예약 가능 시간, 방문 전 준비사항을 설명하며, 환승역도 노선별로 나누지 않고 역명 기준 한 페이지만 운영합니다. 보라매역·대방역은 동작구와 경계가 닿아 인접 생활권으로 안내합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/yeongdeungpo-gu/station/yeongdeungpo-station/">영등포역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/yeongdeungpo-market-station/">영등포시장역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/singil-station/">신길역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/yeouido-station/">여의도역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/yeouinaru-station/">여의나루역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/national-assembly-station/">국회의사당역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/saetgang-station/">샛강역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/mullae-station/">문래역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/yeongdeungpo-gu-office-station/">영등포구청역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/dangsan-station/">당산역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/seonyudo-station/">선유도역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/yangpyeong-station/">양평역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/sinpung-station/">신풍역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/daerim-station/">대림역</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/boramae-nearby-area/">보라매역 인접</a></li>
<li><a href="/seoul/yeongdeungpo-gu/station/daebang-nearby-area/">대방역 인접</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 합니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="check">
<h2>영등포구 홈타이 예약 전 확인사항</h2>
<p>영등포구 홈타이 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다. 여의도와 영등포역처럼 접근성이 좋은 권역도 있지만, 신길동 일부 주거지나 대림동·양평동 일부는 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 알려주시면 도착이 정확해집니다. 준비사항 전체는 <a href="/guide/">이용가이드</a>, 예약 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="policy">
<h2>영등포구 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 지역명·역명만 바꿔 같은 내용을 반복하는 페이지를 만들지 않습니다. 번호 행정동은 대표 동으로 통합하고, 환승역은 역명 기준 한 페이지만 운영하며, 역과 테마를 조합한 검색용 페이지도 만들지 않습니다. 영등포본동과 영등포동은 이름이 비슷하지만 영등포역·시장 중심과 타임스퀘어·문래 인접 중심으로 본문 역할을 다르게 작성합니다. 신도림역은 구로구 성격이 강해 핵심 역세권으로 만들지 않고, 보라매역·대방역은 동작구 경계 인접 생활권으로 안내합니다.</p>
</section>

<section id="how">
<h2>영등포구 출장마사지 사이트 이용 방법</h2>
<p>예약은 다섯 단계로 진행됩니다. 희망 지역 또는 역 인근 위치를 확인하고, 희망 시간을 확인한 뒤, 코스와 인원을 정하고, 방문 가능 여부를 안내받은 다음 예약을 확정합니다. 저녁 시간대나 주말에는 문의가 몰릴 수 있어 한두 시간 이상 여유를 두고 예약하시기를 권장합니다. 거주 지역 기준이 편하면 <a href="/seoul/yeongdeungpo-gu/">지역별 안내</a>를, 역 기준이 익숙하면 <a href="/seoul/yeongdeungpo-gu/station/">역세권 안내</a>를, 관리 유형이 먼저 궁금하면 <a href="/themes/">테마별 안내</a>를 확인해 주세요.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>영등포구 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 여의동, 영등포본동, 당산동, 문래동, 신길동 등 아홉 개 대표 동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>여의도역이나 영등포역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>신길1동과 신길3동은 왜 따로 없나요?</h3>
<p>신길1·3·4·5·6·7동은 신길동 페이지에서, 당산1·2동은 당산동, 양평1·2동은 양평동, 대림1·2·3동은 대림동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>테마별 관리는 어디에서 확인하나요?</h3>
<p>스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>영등포구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "영등포구 출장마사지｜여의도·영등포역·당산·문래 홈타이 지역 안내",
    "desc": "영등포구 출장마사지·홈타이 예약 전 여의도, 영등포역, 당산, 문래, 신길 생활권을 확인하세요.",
    "h1": "영등포구 출장마사지 · 영등포구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
