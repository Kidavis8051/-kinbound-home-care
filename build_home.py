# -*- coding: utf-8 -*-
from build_base import write, page, DOMAIN, PHONE_TEL, PHONE_DISPLAY, REQUEST_CARE_URL, REFER_CLIENT_URL

HERO_ART = """<svg viewBox="0 0 520 640" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Abstract illustration of two connected paths meeting, representing a caregiver and client matched with intention">
  <circle cx="260" cy="320" r="230" fill="none" stroke="rgba(247,244,238,0.18)" stroke-width="1"/>
  <circle cx="260" cy="320" r="170" fill="none" stroke="rgba(247,244,238,0.22)" stroke-width="1"/>
  <circle cx="190" cy="250" r="58" fill="none" stroke="#F7F4EE" stroke-width="2"/>
  <circle cx="330" cy="400" r="72" fill="none" stroke="#F7F4EE" stroke-width="2"/>
  <line x1="235" y1="288" x2="285" y2="352" stroke="#E9C892" stroke-width="2"/>
  <circle cx="235" cy="288" r="4" fill="#E9C892"/>
  <circle cx="285" cy="352" r="4" fill="#E9C892"/>
  <g stroke="#F7F4EE" stroke-width="1.2" opacity="0.75">
    <path d="M110 480 L150 470 L185 486 L222 466" fill="none"/>
  </g>
  <circle cx="110" cy="480" r="3" fill="#F7F4EE"/>
  <circle cx="150" cy="470" r="3" fill="#F7F4EE"/>
  <circle cx="185" cy="486" r="3" fill="#F7F4EE"/>
  <circle cx="222" cy="466" r="3" fill="#F7F4EE"/>
  <g transform="translate(392,150)" opacity="0.9">
    <line x1="0" y1="-16" x2="0" y2="16" stroke="#F7F4EE" stroke-width="1.4"/>
    <line x1="-16" y1="0" x2="16" y2="0" stroke="#F7F4EE" stroke-width="1.4"/>
    <circle cx="0" cy="0" r="22" fill="none" stroke="#F7F4EE" stroke-width="1"/>
  </g>
  <text x="34" y="588" fill="#F7F4EE" font-family="Newsreader, serif" font-size="17" opacity="0.85">N 41.2565&#176; &nbsp; W 95.9345&#176;</text>
  <text x="34" y="610" fill="#E9C892" font-family="Public Sans, sans-serif" font-size="12" letter-spacing="0.04em" opacity="0.9">OMAHA, NEBRASKA</text>
</svg>"""

BODY = f"""
<section class="hero">
  <div class="container">
    <div class="hero-copy">
      <div class="bearing"><div class="tick"></div><span>Non-medical home care &middot; Omaha, NE</span></div>
      <h1>Care should feel like the right fit.</h1>
      <p class="subhead">Personalized home care for Omaha-area seniors who want to stay comfortable, connected and supported in the place they call home.</p>
      <p>At Kinbound, we don&rsquo;t simply fill a shift. We take the time to understand your family&rsquo;s needs and thoughtfully connect you with a caregiver whose experience, strengths and personality genuinely fit &mdash; because that fit is what makes care feel steady instead of transactional.</p>
      <div class="hero-ctas">
        <a class="btn btn-brass" href="/request-care/">Request Care</a>
        <a class="btn btn-outline" href="{REFER_CLIENT_URL}">Refer a Client</a>
      </div>
      <div class="hero-services">
        <a href="/personal-care-omaha-ne/">Personal Care</a>
        <a href="/companion-care-omaha-ne/">Companion Care</a>
        <a href="/homemaker-services-omaha-ne/">Homemaker Services</a>
        <a href="/dementia-memory-care-omaha-ne/">Dementia Support</a>
      </div>
    </div>
    <div class="hero-art">{HERO_ART}</div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="trust-strip">
      <span>Locally owned &amp; operated in Omaha</span>
      <span>Caregivers matched by fit, not availability</span>
      <span>Personal Care &middot; Companion Care &middot; Homemaker &middot; Dementia Support &middot; Respite</span>
      <span>Serving families &amp; referring professionals across the metro</span>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>How we help</span></div>
      <h2>Support for the parts of the day that have gotten harder.</h2>
      <p class="lede">Most families don&rsquo;t call us because someone needs a hospital. They call because getting up, getting dressed, or getting through an evening alone has quietly become a struggle. Here&rsquo;s where we start.</p>
    </div>
    <div class="grid-2" style="row-gap:36px;">
      <div class="svc-card">
        <h3>Personal Care</h3>
        <p>Help with bathing, dressing, grooming and the daily routines that protect dignity and independence at home.</p>
        <a class="more" href="/personal-care-omaha-ne/">Explore Personal Care &rsaquo;</a>
      </div>
      <div class="svc-card">
        <h3>Companion Care</h3>
        <p>Conversation, presence and a familiar face &mdash; support that eases isolation and keeps days from feeling long.</p>
        <a class="more" href="/companion-care-omaha-ne/">Explore Companion Care &rsaquo;</a>
      </div>
      <div class="svc-card">
        <h3>Homemaker Services</h3>
        <p>Meal prep, light housekeeping and laundry, so a home stays safe, orderly and genuinely livable.</p>
        <a class="more" href="/homemaker-services-omaha-ne/">Explore Homemaker Services &rsaquo;</a>
      </div>
      <div class="svc-card">
        <h3>Dementia &amp; Memory Support</h3>
        <p>Structure, patience and cueing from caregivers trained to support memory loss with steadiness, not correction.</p>
        <a class="more" href="/dementia-memory-care-omaha-ne/">Explore Dementia Support &rsaquo;</a>
      </div>
    </div>
    <p style="margin-top:34px;"><a class="btn btn-outline btn-sm" href="/respite-care-omaha-ne/">We also provide Respite Care for family caregivers &rsaquo;</a></p>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="grid-2" style="align-items:center;">
      <div>
        <div class="bearing"><div class="tick"></div><span>Fit over filling</span></div>
        <h2>We match, we don&rsquo;t assign.</h2>
        <p>Most agencies staff by whoever is free. We ask different questions first: Does this caregiver have real experience with this condition? Will their pace and personality put this specific person at ease? Can they build a relationship that lasts longer than a shift?</p>
        <p>That intentional matching is the whole reason Kinbound exists &mdash; for families, it means fewer new faces and more consistency. For caregivers, it means being placed where their strengths are actually used.</p>
        <a class="btn btn-ink" href="/about-kinbound/">Read our care philosophy</a>
      </div>
      <div class="philosophy" style="border:none; padding:0;">
        <blockquote>&ldquo;Better care begins with the right connection.&rdquo;</blockquote>
        <cite>Kinbound&rsquo;s founding belief</cite>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Where we work</span></div>
      <h2>Serving Omaha and the communities around it.</h2>
      <p class="lede">Kinbound provides care throughout the Omaha metro, including Elkhorn, Papillion, La Vista, Bellevue, Ralston and Gretna.</p>
    </div>
    <div class="area-list">
      <a class="area-chip" href="/service-areas/#omaha">Omaha</a>
      <a class="area-chip" href="/service-areas/#elkhorn">Elkhorn</a>
      <a class="area-chip" href="/service-areas/#papillion">Papillion</a>
      <a class="area-chip" href="/service-areas/#la-vista">La Vista</a>
      <a class="area-chip" href="/service-areas/#bellevue">Bellevue</a>
      <a class="area-chip" href="/service-areas/#ralston">Ralston</a>
      <a class="area-chip" href="/service-areas/#gretna">Gretna</a>
    </div>
    <p style="margin-top:22px;"><a class="btn btn-outline btn-sm" href="/service-areas/">See full service area details &rsaquo;</a></p>
  </div>
</section>

<section class="section-deep">
  <div class="container">
    <div class="grid-2" style="align-items:center;">
      <div>
        <div class="bearing on-dark"><div class="tick"></div><span>For referring professionals</span></div>
        <h2>Discharge planning that doesn&rsquo;t stall at the door.</h2>
        <p>If you&rsquo;re a hospital case manager, social worker or discharge planner, we can typically respond to referrals quickly and keep you informed as care begins.</p>
        <a class="btn btn-brass" href="{REFER_CLIENT_URL}">Refer a Client</a>
        <a class="btn btn-outline on-dark" href="/healthcare-professionals/">For Healthcare Professionals &rsaquo;</a>
      </div>
      <div>
        <div class="bearing on-dark"><div class="tick"></div><span>For caregivers</span></div>
        <h2>Work that&rsquo;s matched to your strengths.</h2>
        <p>Kinbound places caregivers with clients based on real fit &mdash; not just an open slot &mdash; and recognizes the work you do.</p>
        <a class="btn btn-outline on-dark" href="/careers/">Join Kinbound &rsaquo;</a>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Not sure where to start? That&rsquo;s normal.</h2>
      <p>Tell us a little about your situation. We&rsquo;ll walk you through what home care with Kinbound actually looks like.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-brass" href="/request-care/">Request Care</a>
      <a class="btn btn-outline on-dark" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""

SCHEMA = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HomeHealthCareService",
  "name": "Kinbound Home Care",
  "url": "{DOMAIN}/",
  "telephone": "{PHONE_TEL}",
  "image": "{DOMAIN}/assets/img/og-default.jpg",
  "priceRange": "$$",
  "areaServed": [
    {{"@type": "City", "name": "Omaha, NE"}},
    {{"@type": "City", "name": "Elkhorn, NE"}},
    {{"@type": "City", "name": "Papillion, NE"}},
    {{"@type": "City", "name": "La Vista, NE"}},
    {{"@type": "City", "name": "Bellevue, NE"}},
    {{"@type": "City", "name": "Ralston, NE"}},
    {{"@type": "City", "name": "Gretna, NE"}}
  ],
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Omaha",
    "addressRegion": "NE",
    "addressCountry": "US"
  }},
  "description": "Kinbound Home Care provides non-medical personal care, companion care, homemaker services, dementia and memory support, and respite care for seniors throughout the Omaha, Nebraska area."
}}
</script>"""

write("index.html", page(
    title="Home Care in Omaha, NE | Kinbound Home Care",
    description="Kinbound Home Care provides personal care, companion care, homemaker services and dementia support for Omaha-area seniors, matched intentionally to the right caregiver.",
    path="/",
    body=BODY,
    schema=SCHEMA,
))
