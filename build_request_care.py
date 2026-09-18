# -*- coding: utf-8 -*-
from build_base import write, page, PHONE_TEL, PHONE_DISPLAY, REQUEST_CARE_URL

BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="/">Home</a> / Request Care</p>
    <div class="bearing"><div class="tick"></div><span>Request Care</span></div>
    <h1>Let's figure out what your family actually needs.</h1>
    <p class="lede">Requesting care starts a conversation, not a commitment. Start your request below, and our care team will reach out to talk through next steps.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="bearing"><div class="tick"></div><span>What happens next</span></div>
        <h2>From request to care, step by step.</h2>
        <div class="steps" style="margin-top:1.6rem;">
          <div class="step">
            <div class="step-num"></div>
            <div>
              <h3>You start your request.</h3>
              <p class="max-prose">Use the secure request form below, or call us directly &mdash; whichever is easier.</p>
            </div>
          </div>
          <div class="step">
            <div class="step-num"></div>
            <div>
              <h3>We talk through your situation.</h3>
              <p class="max-prose">A member of our care team will ask about your loved one's routine, needs and personality, so we understand what "the right fit" actually means for your family.</p>
            </div>
          </div>
          <div class="step">
            <div class="step-num"></div>
            <div>
              <h3>We match a caregiver.</h3>
              <p class="max-prose">We select a caregiver based on that conversation &mdash; not just who happens to be available.</p>
            </div>
          </div>
          <div class="step">
            <div class="step-num"></div>
            <div>
              <h3>Care begins.</h3>
              <p class="max-prose">We confirm scheduling and stay involved after care starts, so we can adjust quickly if anything isn't working.</p>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div class="card">
          <h3>Ready to start?</h3>
          <p>Starting your request takes you to our secure intake system, where you can share details about your family's situation directly with our care team.</p>
          <a class="btn btn-brass" href="{REQUEST_CARE_URL}" style="margin-top:6px;">Start Your Request</a>
        </div>
        <p class="text-sm" style="margin-top:16px;">Prefer to talk it through first? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="notice">
      <h4>Before you request care</h4>
      <p>Kinbound provides non-medical home care only. If your loved one needs skilled nursing, medication management, wound care or medical transportation, let us know &mdash; we can talk through what non-medical support we can still provide alongside those services.</p>
    </div>
  </div>
</section>
"""

write("request-care/index.html", page(
    title="Request Care | Kinbound Home Care in Omaha, NE",
    description="Request non-medical home care from Kinbound in Omaha, NE. Start your request and our care team will reach out to talk through next steps.",
    path="/request-care/",
    body=BODY,
))
