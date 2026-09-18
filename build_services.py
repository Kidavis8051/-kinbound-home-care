# -*- coding: utf-8 -*-
from build_base import write, page, DOMAIN, PHONE_TEL, PHONE_DISPLAY

NON_MEDICAL_NOTICE = """
<div class="notice">
  <h4>What Kinbound does not provide</h4>
  <p>Kinbound is a non-medical home care agency. We do not provide skilled nursing, medication administration, injections, wound care, two-person or mechanical-lift transfers, or medical transportation. If your family situation includes those needs, we're happy to talk through what non-medical support can still cover, and what to ask a home health or skilled nursing provider about the rest.</p>
</div>
"""

def related_links(exclude_href):
    all_links = [
        ("Personal Care", "/personal-care-omaha-ne/"),
        ("Companion Care", "/companion-care-omaha-ne/"),
        ("Homemaker Services", "/homemaker-services-omaha-ne/"),
        ("Dementia &amp; Memory Support", "/dementia-memory-care-omaha-ne/"),
        ("Respite Care", "/respite-care-omaha-ne/"),
    ]
    items = "\n".join(
        f'<a class="area-chip" href="{href}">{label}</a>'
        for label, href in all_links if href != exclude_href
    )
    return f'<div class="area-list">{items}</div>'


def service_schema(name, description, path):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{name}",
  "name": "{name} | Kinbound Home Care",
  "description": "{description}",
  "areaServed": {{"@type": "City", "name": "Omaha, NE"}},
  "provider": {{
    "@type": "LocalBusiness",
    "name": "Kinbound Home Care",
    "telephone": "{PHONE_TEL}",
    "url": "{DOMAIN}/"
  }},
  "url": "{DOMAIN}{path}"
}}
</script>"""


def build_page(cfg):
    includes_html = "\n".join(f"<li>{i}</li>" for i in cfg["includes"])
    who_html = "\n".join(f"<li>{i}</li>" for i in cfg["who_for"])

    boundaries_block = ""
    if cfg.get("boundaries"):
        b_html = "\n".join(f"<li>{i}</li>" for i in cfg["boundaries"])
        boundaries_block = f"""
<section class="section-alt">
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="bearing"><div class="tick"></div><span>Where non-medical care draws the line</span></div>
        <h2>{cfg['boundaries_head']}</h2>
        <p class="max-prose">{cfg['boundaries_lede']}</p>
        <ul class="not-list">{b_html}</ul>
      </div>
      <div>{NON_MEDICAL_NOTICE}</div>
    </div>
  </div>
</section>"""

    extra = cfg.get("extra_html", "")

    body = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="/">Home</a> / {cfg['breadcrumb']}</p>
    <div class="bearing"><div class="tick"></div><span>{cfg['eyebrow']}</span></div>
    <h1>{cfg['h1']}</h1>
    <p class="lede">{cfg['lede']}</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="bearing"><div class="tick"></div><span>What's included</span></div>
        <h2>{cfg['includes_head']}</h2>
        <p class="max-prose">{cfg['includes_intro']}</p>
        <ul class="check-list">{includes_html}</ul>
      </div>
      <div>
        <div class="bearing"><div class="tick"></div><span>Who this is for</span></div>
        <h2>{cfg['who_head']}</h2>
        <p class="max-prose">{cfg['who_intro']}</p>
        <ul class="check-list">{who_html}</ul>
      </div>
    </div>
  </div>
</section>
{boundaries_block}
{extra}
<section>
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Matched, not assigned</span></div>
      <h2>How we choose the right caregiver.</h2>
      <p class="lede">Before we place anyone, our care team talks through your loved one's routines, needs and personality, then matches a caregiver whose experience and approach genuinely fit &mdash; our Fit Over Filling&trade; approach.</p>
      <p><a href="/about-kinbound/">More about our care philosophy &rsaquo;</a></p>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <div class="bearing"><div class="tick"></div><span>Related support</span></div>
      <h2>Other ways Kinbound can help.</h2>
    </div>
    {related_links(cfg['path'])}
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>{cfg['cta_head']}</h2>
      <p>{cfg['cta_body']}</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-brass" href="/request-care/">Request Care</a>
      <a class="btn btn-outline on-dark" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""
    return body


SERVICES = [
    dict(
        path="/personal-care-omaha-ne/",
        file="personal-care-omaha-ne/index.html",
        title="Personal Care Services in Omaha, NE | Kinbound Home Care",
        description="Kinbound provides non-medical personal care in Omaha, NE, including bathing, dressing, grooming and mobility assistance, matched to a caregiver who genuinely fits.",
        breadcrumb="Personal Care",
        eyebrow="Personal Care &middot; Omaha, NE",
        h1="Personal care that protects dignity, not just routine.",
        lede="Bathing, dressing and daily hygiene can quietly become the hardest part of the day. Kinbound provides hands-on, non-medical personal care that helps your loved one stay clean, comfortable and steady on their feet &mdash; without losing their independence in the process.",
        includes_head="Day-to-day help, handled with respect.",
        includes_intro="Personal care covers the physical, routine parts of the day that become harder with age, illness or mobility changes. Every task is approached at the client's pace, with privacy and dignity as the starting point, not an afterthought.",
        includes=[
            "Bathing and shower assistance",
            "Grooming and personal hygiene",
            "Dressing and help choosing appropriate clothing",
            "Toileting and incontinence assistance",
            "Routine mobility assistance, including help moving safely around the home",
            "Support with other appropriate non-medical activities of daily living",
        ],
        who_head="For families noticing the small signs first.",
        who_intro="Personal care usually starts small: skipped showers, the same outfit for days, or a fall that almost happened. It's a fit if any of this sounds familiar.",
        who_for=[
            "A parent who's begun avoiding the shower or bath",
            "Someone who needs a steady hand getting dressed or standing up",
            "A family member managing incontinence who wants privacy and patience, not rush",
            "An adult child who lives too far away to help with daily routines in person",
        ],
        boundaries_head="Personal care is hands-on. It isn't clinical.",
        boundaries_lede="Our caregivers provide non-medical assistance with daily living. They do not perform the clinical tasks below.",
        boundaries=[
            "Medication administration or injections",
            "Wound care or dressing changes",
            "Two-person or mechanical (Hoyer) lift transfers",
            "Skilled nursing assessments or procedures",
        ],
        cta_head="Let's talk through what your parent actually needs.",
        cta_body="A conversation with our care team costs nothing and helps you understand what personal care with Kinbound would look like day to day.",
    ),
    dict(
        path="/companion-care-omaha-ne/",
        file="companion-care-omaha-ne/index.html",
        title="Companion Care in Omaha, NE | Kinbound Home Care",
        description="Kinbound's companion care in Omaha, NE offers conversation, social engagement and a safe presence for seniors aging at home.",
        breadcrumb="Companion Care",
        eyebrow="Companion Care &middot; Omaha, NE",
        h1="Someone to talk to, and someone watching out.",
        lede="Isolation is one of the quietest risks of aging at home. Companion care gives your loved one regular, genuine company &mdash; and gives your family a consistent set of eyes on how they're really doing.",
        includes_head="More than a check-in.",
        includes_intro="Companion care is built around presence: a caregiver who shows up consistently, knows the person they're with, and makes the day feel less alone.",
        includes=[
            "Conversation and genuine companionship",
            "Support attending social activities and staying engaged",
            "General supervision for safety throughout the day",
            "Help maintaining daily routines and structure",
            "Accompaniment for hobbies, walks and errands around the home",
            "A consistent, familiar presence that helps reduce isolation",
        ],
        who_head="For seniors who are safe, but alone too often.",
        who_intro="Companion care fits families where the bigger worry isn't a medical need &mdash; it's the hours spent alone.",
        who_for=[
            "A parent living alone since a spouse passed away",
            "Someone whose family lives out of town and can't check in daily",
            "A senior who's become withdrawn or stopped doing things they used to enjoy",
            "Families who want a trusted presence in the home for safety, without full personal care",
        ],
        boundaries=None,
        cta_head="Give your loved one a familiar face to look forward to.",
        cta_body="Tell us about their routine and personality, and we'll match a caregiver who genuinely fits.",
    ),
    dict(
        path="/homemaker-services-omaha-ne/",
        file="homemaker-services-omaha-ne/index.html",
        title="Homemaker Services in Omaha, NE | Kinbound Home Care",
        description="Kinbound's homemaker services in Omaha, NE include meal preparation, light housekeeping and laundry, helping seniors keep a safe, livable home.",
        breadcrumb="Homemaker Services",
        eyebrow="Homemaker Services &middot; Omaha, NE",
        h1="A home that stays safe, orderly and livable.",
        lede="When household tasks pile up, a home can quietly become harder to live in safely. Homemaker services keep the day-to-day running &mdash; meals prepared, laundry done, floors clear &mdash; so your loved one can stay in the home they know.",
        includes_head="The household work that keeps a home livable.",
        includes_intro="Homemaker services focus on the home itself: the tasks that, left undone, turn into safety hazards or a loss of independence.",
        includes=[
            "Meal preparation, including planning around dietary preferences",
            "Light housekeeping and tidying",
            "Laundry and linen changes",
            "Household organization",
            "Other appropriate household support as needs come up",
        ],
        who_head="For homes where the basics have become a struggle.",
        who_intro="Homemaker services are often paired with personal or companion care, but they can also stand alone.",
        who_for=[
            "A parent who's stopped cooking regular meals",
            "A home where laundry and clutter have started piling up",
            "Someone recovering from a fall or illness who needs help catching back up at home",
            "Families who want the home itself kept safe between visits",
        ],
        boundaries=None,
        cta_head="A tidy, well-stocked home starts with the right support.",
        cta_body="We'll talk through your loved one's routine and household needs, then match a caregiver who fits.",
    ),
    dict(
        path="/dementia-memory-care-omaha-ne/",
        file="dementia-memory-care-omaha-ne/index.html",
        title="Dementia & Memory Care Support Omaha, NE | Kinbound",
        description="Kinbound provides non-medical dementia and memory support in Omaha, NE, with routine, cueing and safety supervision from caregivers matched to fit your loved one.",
        breadcrumb="Dementia & Memory Support",
        eyebrow="Dementia &amp; Memory Support &middot; Omaha, NE",
        h1="Steadiness for the days memory loss makes harder.",
        lede="Dementia changes the shape of a day: routines matter more, unfamiliar faces are harder, and small moments of confusion need patience instead of correction. Kinbound's dementia and memory support is built around that reality, not around it.",
        includes_head="Structure and presence, not correction.",
        includes_intro="Our approach centers on routine, gentle redirection and a caregiver who becomes a familiar, steady presence &mdash; because for someone living with memory loss, consistency itself is a form of care.",
        includes=[
            "Consistent daily routine and structure",
            "Companionship suited to the person's current stage and pace",
            "Cueing and gentle redirection during moments of confusion",
            "Personal-care assistance, including bathing, dressing and hygiene",
            "Safety supervision throughout the day",
            "Support and respite for the family caregiver",
        ],
        who_head="For families navigating memory loss at home.",
        who_intro="Dementia and memory support fits a wide range of situations, from early forgetfulness to more advanced care needs.",
        who_for=[
            "A parent recently diagnosed with dementia or Alzheimer's disease",
            "A family caregiver who is exhausted and needs reliable relief",
            "Someone who wanders, becomes confused, or has had a safety scare at home",
            "A household adjusting routines to support a loved one's changing needs",
        ],
        boundaries_head="Memory support, within non-medical care.",
        boundaries_lede="Our caregivers provide non-medical dementia support. They do not manage the clinical side of a dementia diagnosis.",
        boundaries=[
            "Medication management or administration",
            "Behavioral or psychiatric medical treatment",
            "Clinical dementia diagnosis or staging",
            "Skilled nursing care",
        ],
        extra_html="""
<section class="section-alt">
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="bearing"><div class="tick"></div><span>Our approach</span></div>
        <h2>Why fit matters even more with memory loss.</h2>
        <p class="max-prose">A new face can be genuinely disorienting for someone living with dementia. That's part of why intentional matching is so central to how we approach memory support &mdash; a caregiver who understands the person's history, habits and pace can prevent a lot of the agitation that comes from feeling unfamiliar or rushed.</p>
        <p class="max-prose">We also try to keep that caregiver consistent over time. Continuity itself is calming; it's one less unfamiliar thing in a day that can already feel confusing.</p>
      </div>
      <div>
        <div class="bearing"><div class="tick"></div><span>Supporting the family</span></div>
        <h2>You need support here too.</h2>
        <p class="max-prose">Caring for a loved one with dementia is exhausting in ways that are hard to explain to people who haven't lived it. Part of our role is giving you real, scheduled relief &mdash; not just coverage for emergencies.</p>
        <p><a href="/respite-care-omaha-ne/">Learn more about respite care for family caregivers &rsaquo;</a></p>
      </div>
    </div>
  </div>
</section>""",
        cta_head="Let's talk about where your family is right now.",
        cta_body="Every dementia journey looks different. Tell us where yours stands, and we'll explain how Kinbound can help.",
    ),
    dict(
        path="/respite-care-omaha-ne/",
        file="respite-care-omaha-ne/index.html",
        title="Respite Care in Omaha, NE | Family Caregiver Relief | Kinbound",
        description="Kinbound's respite care gives Omaha-area family caregivers scheduled relief and peace of mind, with non-medical in-home support for their loved one.",
        breadcrumb="Respite Care",
        eyebrow="Respite Care &middot; Omaha, NE",
        h1="Relief for the person who's been holding it all together.",
        lede="If you're the one providing care for a parent or spouse, respite care gives you real, scheduled time away &mdash; knowing your loved one is in steady, familiar hands.",
        includes_head="Time away, without the worry.",
        includes_intro="Respite care covers your loved one's day-to-day non-medical needs while you step away, whether for a few hours, a regular weekly break, or a longer stretch.",
        includes=[
            "Companionship and supervision while you're away",
            "Personal care and daily routine support in your absence",
            "Meal preparation and light household help",
            "Consistent presence, so your loved one isn't navigating a new caregiver during your time off",
            "Flexible scheduling built around your own routine, not just theirs",
        ],
        who_head="For the family caregiver running on empty.",
        who_intro="Respite care exists for you as much as for the person receiving care.",
        who_for=[
            "An adult child providing daily care for a parent, with no regular break",
            "A spouse caring for a partner with dementia or a chronic condition",
            "A family caregiver who needs to travel, work, or simply rest",
            "Someone who feels guilty asking for help, but is close to burnout",
        ],
        boundaries=None,
        cta_head="You're allowed to need a break.",
        cta_body="Tell us your loved one's routine and the kind of relief you need, and we'll match a caregiver who can step in reliably.",
    ),
]


def build_all():
    for cfg in SERVICES:
        body = build_page(cfg)
        schema = service_schema(cfg["breadcrumb"], cfg["description"], cfg["path"])
        write(cfg["file"], page(
            title=cfg["title"],
            description=cfg["description"],
            path=cfg["path"],
            body=body,
            schema=schema,
        ))


if __name__ == "__main__":
    build_all()
