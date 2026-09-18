# -*- coding: utf-8 -*-
from build_base import write, page

BODY = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="/">Home</a> / About</p>
    <div class="bearing"><div class="tick"></div><span>About Kinbound</span></div>
    <h1>Better care begins with the right connection.</h1>
    <p class="lede">Kinbound was built on a simple frustration with how home care usually works: agencies fill open shifts with whoever is available, and families are left hoping the fit happens to work out. We built Kinbound to do that work on purpose.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="bearing"><div class="tick"></div><span>Our mission</span></div>
        <h2>Peace of mind for families. A calling for caregivers.</h2>
        <p class="max-prose">To provide families with complete peace of mind through compassionate, high-quality home care, while empowering caregivers by connecting their personal career goals to a meaningful calling.</p>
        <p class="max-prose">That mission runs in two directions at once. A family only gets consistent, attentive care when the caregiver providing it feels valued, supported and genuinely suited to the role &mdash; not just scheduled into it.</p>
      </div>
      <div>
        <div class="bearing"><div class="tick"></div><span>Why Kinbound exists</span></div>
        <h2>We got tired of &ldquo;whoever&rsquo;s available.&rdquo;</h2>
        <p class="max-prose">Most home care in Omaha runs on staffing logistics: a shift opens, and whichever caregiver is free gets sent. Sometimes that works out. Often it means a revolving door of new faces, mismatched expectations, and a family left to manage the gap.</p>
        <p class="max-prose">Kinbound starts from the opposite direction &mdash; understanding the person who needs care first, then finding the caregiver whose background and temperament actually fit them.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Fit Over Filling&trade;</span></div>
      <h2>Our care philosophy, in practice.</h2>
      <p class="lede">Fit Over Filling isn&rsquo;t a slogan we put on a wall. It&rsquo;s the actual process behind every client we take on.</p>
    </div>
    <div class="grid-3">
      <div class="card">
        <h3>We ask before we assign.</h3>
        <p>Before a caregiver is ever suggested, we learn about the client&rsquo;s routines, personality, care needs and the kind of presence that would put them at ease &mdash; not just the hours we need covered.</p>
      </div>
      <div class="card">
        <h3>We match strengths to needs.</h3>
        <p>Caregivers bring different experience, pacing and personalities. We place people where those strengths are actually useful &mdash; with a client managing early memory loss, for instance, or one who simply wants a quiet, steady companion.</p>
      </div>
      <div class="card">
        <h3>We stay involved after the match.</h3>
        <p>Placement isn&rsquo;t the finish line. We check in, adjust when something isn&rsquo;t working, and treat consistency as something we actively protect, not something we hope holds.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Three pillars</span></div>
      <h2>What Kinbound is built on.</h2>
    </div>
    <div class="grid-3">
      <div class="pillar">
        <div class="bearing"><div class="tick"></div><span>Comfort &amp; Connection</span></div>
        <h3>Peace &amp; Belonging</h3>
        <p>Families gain real peace of mind when caregivers feel valued, supported and thoughtfully matched with the people they serve.</p>
      </div>
      <div class="pillar">
        <div class="bearing"><div class="tick"></div><span>Trust &amp; Placement</span></div>
        <h3>Stability &amp; Purpose</h3>
        <p>Consistent, reliable care comes from caregivers who are intentionally placed &mdash; not simply assigned to whatever shift is open.</p>
      </div>
      <div class="pillar">
        <div class="bearing"><div class="tick"></div><span>Quality &amp; Growth</span></div>
        <h3>Excellence &amp; Appreciation</h3>
        <p>Excellent client care is supported by a culture that recognizes caregiver professionalism, growth and the quality of their work.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Core values</span></div>
      <h2>What guides day-to-day decisions.</h2>
    </div>
    <div class="grid-3">
      <div class="card">
        <h3>Intentional Placement</h3>
        <p>Fit over filling. We don&rsquo;t blindly fill open slots &mdash; we match caregiver strengths, personality and experience with each family&rsquo;s actual needs.</p>
      </div>
      <div class="card">
        <h3>Recognized Excellence</h3>
        <p>High standards matter, and when a caregiver&rsquo;s performance is excellent, we make sure that&rsquo;s seen and appreciated &mdash; not assumed.</p>
      </div>
      <div class="card">
        <h3>Anchored Peace</h3>
        <p>Families should experience reliability, communication and safety, while the caregivers providing that care work in an environment that supports their own growth.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>See what this looks like for your family.</h2>
      <p>We&rsquo;ll ask a few questions about your situation and explain exactly how care would start.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-brass" href="/request-care/">Request Care</a>
      <a class="btn btn-outline on-dark" href="/careers/">Interested in caregiving work? &rsaquo;</a>
    </div>
  </div>
</section>
"""

write("about-kinbound/index.html", page(
    title="About Kinbound Home Care | Our Care Philosophy in Omaha, NE",
    description="Learn why Kinbound Home Care was built around intentional caregiver matching, not shift-filling, and the mission, pillars and values behind our Omaha home care.",
    path="/about-kinbound/",
    body=BODY,
))
