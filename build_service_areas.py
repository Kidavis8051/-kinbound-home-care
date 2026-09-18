# -*- coding: utf-8 -*-
from build_base import write, page, DOMAIN, PHONE_TEL, PHONE_DISPLAY

AREAS = [
    ("omaha", "Omaha", "Our primary service area, including neighborhoods throughout the metro."),
    ("elkhorn", "Elkhorn", "Care for families in Elkhorn and the surrounding western Omaha area."),
    ("papillion", "Papillion", "Serving Papillion and nearby Sarpy County communities."),
    ("la-vista", "La Vista", "In-home care for families throughout La Vista."),
    ("bellevue", "Bellevue", "Care coverage across Bellevue and the surrounding area."),
    ("ralston", "Ralston", "Serving Ralston and the neighboring central-metro area."),
    ("gretna", "Gretna", "Care for families in Gretna and nearby western Sarpy County."),
]

area_sections = "\n".join(f"""
<div class="card" id="{slug}">
  <h3>{name}</h3>
  <p>{desc}</p>
</div>""" for slug, name, desc in AREAS)

BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="/">Home</a> / Service Areas</p>
    <div class="bearing"><div class="tick"></div><span>Service Areas</span></div>
    <h1>Where Kinbound provides care.</h1>
    <p class="lede">Kinbound's primary service area is Omaha, Nebraska, with care also available in the communities immediately around it. If you're not sure whether we cover your address, the fastest way to find out is to ask us directly.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-3" style="row-gap:26px;">
      {area_sections}
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Looking ahead</span></div>
      <h2>Expanding carefully, not everywhere at once.</h2>
      <p class="max-prose">Over time, we expect to grow further into the wider Douglas and Sarpy County area. We'd rather confirm we can actually deliver dependable, well-matched care in a community before advertising service there &mdash; so if your address falls just outside our current areas, reach out. We may already be able to help, or can tell you honestly if we're not there yet.</p>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Not sure if we cover your area?</h2>
      <p>Give us a call or send a request &mdash; we'll tell you plainly whether Kinbound serves your address.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-brass" href="/request-care/">Request Care</a>
      <a class="btn btn-outline on-dark" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""

write("service-areas/index.html", page(
    title="Service Areas | Home Care Near Omaha, NE | Kinbound",
    description="Kinbound Home Care serves Omaha, Nebraska and nearby communities including Elkhorn, Papillion, La Vista, Bellevue, Ralston and Gretna.",
    path="/service-areas/",
    body=BODY,
))
