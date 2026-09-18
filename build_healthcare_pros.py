# -*- coding: utf-8 -*-
from build_base import write, page, PHONE_TEL, PHONE_DISPLAY, REFER_CLIENT_URL, EMAIL

BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="/">Home</a> / For Healthcare Professionals</p>
    <div class="bearing"><div class="tick"></div><span>For Healthcare Professionals</span></div>
    <h1>A referral partner for the non-medical gap after discharge.</h1>
    <p class="lede">For hospital case managers, social workers, discharge planners, rehabilitation professionals and senior-services organizations across the Omaha area: Kinbound provides the non-medical, in-home support that keeps a discharge plan from stalling out at the front door.</p>
    <a class="btn btn-brass" href="{REFER_CLIENT_URL}">Refer a Client</a>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="bearing"><div class="tick"></div><span>What we provide</span></div>
        <h2>Non-medical support, matched intentionally.</h2>
        <p class="max-prose">Kinbound provides personal care, companion care, homemaker services, dementia and memory support, and respite care for family caregivers &mdash; all non-medical. We're not a home health or skilled nursing agency, and we won't present ourselves as one to your patients or clients.</p>
        <p class="max-prose">What we do offer is intentional caregiver matching: rather than assigning whoever is available, we place a caregiver whose experience and approach genuinely fit the person's needs and personality, which matters for follow-through after discharge.</p>
        <a href="/personal-care-omaha-ne/">See all Kinbound services &rsaquo;</a>
      </div>
      <div>
        <div class="bearing"><div class="tick"></div><span>Where we serve</span></div>
        <h2>Omaha and the surrounding communities.</h2>
        <p class="max-prose">Our primary service area is Omaha, Nebraska, with coverage extending into Elkhorn, Papillion, La Vista, Bellevue, Ralston and Gretna.</p>
        <a href="/service-areas/">Full service area details &rsaquo;</a>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Referral process</span></div>
      <h2>What happens after you refer someone.</h2>
    </div>
    <div class="steps">
      <div class="step">
        <div class="step-num"></div>
        <div>
          <h3>You submit the referral.</h3>
          <p class="max-prose">Send us the relevant details through our referral workflow, or call us directly if the situation is time-sensitive.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num"></div>
        <div>
          <h3>We reach out to the family.</h3>
          <p class="max-prose">Our care team follows up with the patient or family to understand their needs, routine and preferences.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num"></div>
        <div>
          <h3>We match a caregiver.</h3>
          <p class="max-prose">Rather than assigning whoever is free, we place a caregiver whose background and approach fit the specific person.</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num"></div>
        <div>
          <h3>We keep you informed.</h3>
          <p class="max-prose">We can communicate with your team as care begins, so the referral doesn't disappear into a black box on your end.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="notice">
      <h4>Scope of care</h4>
      <p>Kinbound is a non-medical home care agency. We do not provide skilled nursing, medication administration, wound care, injections, two-person or mechanical-lift transfers, or medical transportation. We're glad to work alongside your patient's other providers for anything outside that scope.</p>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Ready to send a referral?</h2>
      <p>Use our referral workflow, or reach our team directly by phone or email.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-brass" href="{REFER_CLIENT_URL}">Refer a Client</a>
      <a class="btn btn-outline on-dark" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""

write("healthcare-professionals/index.html", page(
    title="Refer a Client | Healthcare Professionals | Kinbound",
    description="Kinbound partners with Omaha-area case managers, discharge planners and social workers to provide non-medical in-home care referrals.",
    path="/healthcare-professionals/",
    body=BODY,
))
