# -*- coding: utf-8 -*-
from build_base import write, page, PHONE_TEL, PHONE_DISPLAY, JOIN_TEAM_URL

BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="/">Home</a> / Careers</p>
    <div class="bearing"><div class="tick"></div><span>Careers at Kinbound</span></div>
    <h1>Caregiving work, placed with the same intention we ask of it.</h1>
    <p class="lede">Kinbound was built around the idea that better care starts with the right connection &mdash; and that applies to how we treat our caregivers, not only how we place them with clients.</p>
    <a class="btn btn-brass" href="{JOIN_TEAM_URL}">Join Kinbound</a>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="bearing"><div class="tick"></div><span>Fit over filling, for you too</span></div>
        <h2>We place you where your strengths matter.</h2>
        <p class="max-prose">A lot of agencies hand caregivers whatever shift is open, regardless of whether it's a good match. Kinbound works the other way: we learn what you're genuinely good at &mdash; dementia care, personal care, companionship, a certain kind of steady presence &mdash; and place you with clients where that actually gets used.</p>
        <p class="max-prose">That's better for the client, and it's better for you: work that fits is work you can sustain.</p>
      </div>
      <div>
        <div class="bearing"><div class="tick"></div><span>Recognized excellence</span></div>
        <h2>Good work gets noticed.</h2>
        <p class="max-prose">Caregiving is demanding, often invisible work. Part of our culture is making sure excellent performance is actually seen and appreciated, not just expected.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Our three pillars</span></div>
      <h2>What we try to build for our caregivers.</h2>
    </div>
    <div class="grid-3">
      <div class="pillar">
        <h3>Peace &amp; Belonging</h3>
        <p>Caregivers who feel valued and appropriately matched are able to build real, lasting relationships with the people they care for.</p>
      </div>
      <div class="pillar">
        <h3>Stability &amp; Purpose</h3>
        <p>Intentional placement, not last-minute shift-filling, so the work you do feels connected to a purpose rather than a schedule.</p>
      </div>
      <div class="pillar">
        <h3>Excellence &amp; Growth</h3>
        <p>A culture that supports your growth and recognizes the quality of the care you provide.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>What you'd be doing</span></div>
      <h2>The kind of work Kinbound places caregivers into.</h2>
      <p class="lede">Depending on your background and interests, that might include personal care, companion care, homemaker support, dementia and memory care, or respite relief for family caregivers.</p>
    </div>
    <div class="area-list">
      <a class="area-chip" href="/personal-care-omaha-ne/">Personal Care</a>
      <a class="area-chip" href="/companion-care-omaha-ne/">Companion Care</a>
      <a class="area-chip" href="/homemaker-services-omaha-ne/">Homemaker Services</a>
      <a class="area-chip" href="/dementia-memory-care-omaha-ne/">Dementia &amp; Memory Support</a>
      <a class="area-chip" href="/respite-care-omaha-ne/">Respite Care</a>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Interested in caregiving work that fits you?</h2>
      <p>Reach out and tell us about your experience &mdash; we'll talk through where you might fit at Kinbound.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-brass" href="{JOIN_TEAM_URL}">Join Kinbound</a>
      <a class="btn btn-outline on-dark" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""

write("careers/index.html", page(
    title="Caregiver Careers in Omaha, NE | Join Kinbound Home Care",
    description="Kinbound hires caregivers in the Omaha, NE area and places them intentionally based on fit, not just an open shift. Learn about caregiving careers here.",
    path="/careers/",
    body=BODY,
))
