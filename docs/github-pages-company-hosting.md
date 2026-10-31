# GitHub Pages and company websites

Reviewed against the official GitHub documentation on **2026-10-31**.
This is a practical reading of the published rules, not legal advice or
approval from GitHub. Recheck the sources before a production launch.

## Short answer for this website

A static page describing a company, its services, references and contact details
is not an online shop or SaaS application. However, **the absence of a checkout
does not by itself establish that GitHub allows the site**.

GitHub explicitly supports websites about an organization or project, but its
Pages terms also prohibit using Pages as free hosting to run an online business.
The published documents do not give an unqualified exemption for every
service-company brochure/contact website. A consulting company's main customer-facing
marketing site falls close enough to that boundary that this guide cannot
confirm permission solely because sales happen by phone or email.

**Recommendation:** ask [GitHub Support](https://support.github.com/) for written
clarification describing the actual site before relying on Pages as the
company's permanent public host. Without that clarification, use the existing
[STRATO deployment](deploy_starto.md) or another host whose terms expressly
cover company websites. The workflows here provide technical deployment
capability, not a determination that a particular use is permitted.

## What the official sources establish

| Question | Published guidance and implication |
|---|---|
| Can Pages present an organization? | [What is GitHub Pages?][about] describes hosting a website about yourself, your organization or a project. The [Pages terms][terms] describe its primary purpose as showcasing personal and organizational projects. This supports informational/project showcases, but does not override the business-use restriction. |
| Is an online shop or commercial SaaS allowed? | The [Pages terms][terms] and [usage limits][limits] exclude free hosting for online business, e-commerce and sites primarily facilitating commercial transactions or providing commercial SaaS. Do not deploy a shop, checkout, payment flow or commercial SaaS through these workflows. |
| Does "company services + contact, no shop" guarantee approval? | No explicit blanket approval for this exact case appears in the cited rules. A project/organization showcase and a company's operational sales/lead-generation website are not necessarily the same use. Describe the real purpose and contact mechanisms to Support rather than treating "no checkout" as a loophole. |
| Is a custom domain technically supported? | Yes. [Custom-domain documentation][domains] supports owned apex domains and subdomains. This is a URL/DNS feature, not a commercial-hosting exemption. The same Pages usage rules apply on `github.io` and on a custom domain. |
| Does a paid GitHub plan settle business-use eligibility? | The cited Pages terms do not state a blanket commercial-hosting exception for paid plans. Plan/visibility access to Pages is a separate issue from whether the site's use complies. |
| Is there a short-term test/PoC exception? | The cited rules do not provide a general duration-based exemption. An otherwise prohibited business site does not become permitted just because it is temporary, unadvertised or marked `noindex`. |
| Are educational copies of websites treated separately? | The [educational-exercise guidance][limits] allows learning copies under stated conditions: write the code yourself, collect no user data and prominently disclose that the copy is an unaffiliated educational exercise. This is not a blanket exception for a real company's staging or production site. Do not make a false non-affiliation claim for a company-authorized rebuild. |

## Applying that distinction to ABC Abel Bau-Consulting

The current rebuild is static and contains services, project references,
seminar information, company/contact details and legal pages. No shop, checkout,
payment collection, customer account system or commercial SaaS has been added.
Contact links, including email or phone links, do not implement a transaction
on the site, but that alone does not determine the website's primary purpose.

For a Support request, describe:

- That this is a construction-consulting company's informational website.
- That it lists services and references and provides contact information.
- That there are no orders, bookings, payments, accounts or SaaS features on
  the site, if that remains true at the time of the request.
- Whether it is the official ongoing company website or an authorized,
  temporary technical preview of a replacement website.
- The intended URL, including whether it uses a custom domain.
- Whether inquiry/lead generation is a primary goal, rather than describing
  a marketing site as purely educational.

Keep GitHub's answer with the project's deployment records and reassess if
features or the site's purpose change. Do not add a checkout or commercial
service flow on the assumption that an earlier informational-site answer
still applies.

## Testing and PoC deployments

For development with no public-hosting decision, use
[local preview](../README.md#build-and-view-locally) or the downloadable
[`deploy_local` export](deploy_local.md). A local test does not publish to Pages.

If GitHub confirms the intended public preview is acceptable:

1. Use [`deploy_gh_pages`](deploy_gh_pages.md) for a default-domain test or
   [`deploy_gh_custom`](deploy_gh_custom.md) for a dedicated test hostname.
2. Keep the existing `noindex` defaults and clearly label the preview as a
   non-production preview where appropriate. Neither measure grants hosting
   permission or prevents public access.
3. Do not collect customer or sensitive data through a test site. Pages is not
   intended for sensitive transactions. GitHub itself logs visitor IP addresses
   for security, according to [its Pages overview][about]; "static" does not
   mean no provider-side processing or remove privacy-notice obligations.
4. Check image/content rights and have the company review the inherited legal
   pages; the rebuild's historical privacy text is not a hosting-compliance
   assessment.
5. After testing, run the workflow's confirmed `delete` operation, verify Pages
   is disabled and remove/update custom-domain DNS records. Deletion does not
   erase GitHub's logs or immediately purge all external caches.

Temporary hosting should therefore be a controlled deployment lifecycle,
**not a workaround for the usage restrictions**. If Support has not clarified
the company-site use, keep the PoC local or use suitable business hosting.

## Official sources

1. [GitHub Terms for Additional Products and Features, Pages section][terms].
   The version fetched for this review states an effective date of
   August 27, 2026. This is the primary Pages-specific contractual source.
2. [GitHub Pages limits, usage restrictions and educational exercises][limits].
3. [What is GitHub Pages?][about], including organization sites, supported site
   types, custom-domain hosting and visitor IP logging.
4. [About custom domains and GitHub Pages][domains], including domain
   verification and takeover risks when a site is disabled.
5. [GitHub Support portal](https://support.github.com/) for classification of
   the intended use; the Pages terms explicitly direct uncertain users there.

[terms]: https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#pages
[limits]: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
[about]: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
[domains]: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages
