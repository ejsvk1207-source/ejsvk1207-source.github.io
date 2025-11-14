import os

# =====================================
# 0. AdSense Auto Ads Code (빈칸 유지 가능)
# =====================================
ADSENSE_SNIPPET = """
"""

# =====================================
# 1. TEMPLATE / SCRIPT / STYLE
# =====================================

TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESCRIPTION}}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{{ADSENSE_SNIPPET}}
<link rel="stylesheet" href="../style.css">
</head>
<body>

<header>
  <h1>{{TITLE}}</h1>
  <p class="subtitle">{{COUNTRY}} · {{JOB}} · {{CURRENCY}}</p>
</header>

<main>
  <section class="intro">
    <p>{{DESCRIPTION}}</p>
    <p class="disclaimer">
      This tool gives a simplified estimate of take-home salary.
      Real tax systems are more complex and vary by region.
    </p>
  </section>

  <section class="calculator">
    <h2>Enter your salary</h2>
    <form id="salary-form">
      <label>
        Gross yearly salary ({{CURRENCY}}):
        <input type="number" id="grossYearly" required min="0" step="100">
      </label>

      <label>
        Optional yearly bonus ({{CURRENCY}}):
        <input type="number" id="bonusYearly" min="0" step="100">
      </label>

      <button type="submit">Calculate net salary</button>
    </form>

    <div id="result" class="result hidden">
      <h2>Estimated take-home pay</h2>
      <p>Yearly net: <span id="netYearly"></span> {{CURRENCY}}</p>
      <p>Monthly net: <span id="netMonthly"></span> {{CURRENCY}}</p>
      <p>Weekly net: <span id="netWeekly"></span> {{CURRENCY}}</p>
    </div>
  </section>

  <footer>
    <p>
      Part of the Global Salary Calculators project —
      <a href="../index.html">Back to index</a>
    </p>
  </footer>
</main>

<script>
  window.calculatorConfig = {
    "tax_rate": {{TAX_RATE}},
    "social_rate": {{SOCIAL_RATE}}
  };
</script>

<script src="../script.js"></script>

</body>
</html>
"""

SCRIPT_JS = """document.addEventListener("DOMContentLoaded", () => {
  const cfg = window.calculatorConfig;
  const form = document.getElementById("salary-form");
  const result = document.getElementById("result");
  const netY = document.getElementById("netYearly");
  const netM = document.getElementById("netMonthly");
  const netW = document.getElementById("netWeekly");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    let g = Number(document.getElementById("grossYearly").value);
    let b = Number(document.getElementById("bonusYearly").value || 0);
    if (!g) return alert("Enter valid salary.");

    let total = g + b;
    let rate = Math.min(cfg.tax_rate + cfg.social_rate, 0.8);

    let net = total * (1 - rate);
    netY.textContent = net.toLocaleString();
    netM.textContent = (net/12).toLocaleString();
    netW.textContent = (net/52).toLocaleString();

    result.classList.remove("hidden");
  });
});
"""

STYLE_CSS = """body {
  font-family: system-ui;
  background: #f6f6f6;
  margin: 0;
  padding: 0;
}
header {
  background: #fff;
  padding: 20px;
  border-bottom: 1px solid #ddd;
}
h1 { margin: 0 0 5px; }
.subtitle { color: #777; font-size: 0.9rem; }
main { max-width: 900px; margin: 20px auto; padding: 0 20px; }
section {
  background: #fff;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
}
.hidden { display: none; }
button {
  background: #0070f3;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  color: #fff;
  cursor: pointer;
}
button:hover { background: #0059d1; }
a { color: #0070f3; }
"""

# =====================================
# 2. COUNTRIES + 100 JOBS
# =====================================

COUNTRIES = [
    {"code": "us", "name": "United States", "currency": "USD", "tax_rate": 0.22, "social_rate": 0.076},
    {"code": "in", "name": "India", "currency": "INR", "tax_rate": 0.18, "social_rate": 0.03},
    {"code": "id", "name": "Indonesia", "currency": "IDR", "tax_rate": 0.08, "social_rate": 0.04},
    {"code": "br", "name": "Brazil", "currency": "BRL", "tax_rate": 0.17, "social_rate": 0.11},
    {"code": "ng", "name": "Nigeria", "currency": "NGN", "tax_rate": 0.10, "social_rate": 0.02},
    {"code": "mx", "name": "Mexico", "currency": "MXN", "tax_rate": 0.16, "social_rate": 0.06},
    {"code": "ph", "name": "Philippines", "currency": "PHP", "tax_rate": 0.12, "social_rate": 0.08},
    {"code": "bd", "name": "Bangladesh", "currency": "BDT", "tax_rate": 0.10, "social_rate": 0.03},
    {"code": "pk", "name": "Pakistan", "currency": "PKR", "tax_rate": 0.10, "social_rate": 0.03},
    {"code": "vn", "name": "Vietnam", "currency": "VND", "tax_rate": 0.10, "social_rate": 0.08},
    {"code": "uk", "name": "United Kingdom", "currency": "GBP", "tax_rate": 0.20, "social_rate": 0.12},
    {"code": "de", "name": "Germany", "currency": "EUR", "tax_rate": 0.22, "social_rate": 0.19},
    {"code": "fr", "name": "France", "currency": "EUR", "tax_rate": 0.22, "social_rate": 0.16},
    {"code": "ca", "name": "Canada", "currency": "CAD", "tax_rate": 0.20, "social_rate": 0.08},
    {"code": "au", "name": "Australia", "currency": "AUD", "tax_rate": 0.19, "social_rate": 0.095},
]

JOBS = [
    "Software Engineer","Teacher","Nurse","Doctor","Factory Worker","Call Center Agent",
    "Truck Driver","Taxi Driver","Retail Worker","Civil Servant","Data Analyst","Web Developer",
    "Accountant","Graphic Designer","Mechanical Engineer","Electrician","Plumber","Construction Worker",
    "Sales Manager","Marketing Manager","Project Manager","IT Support Specialist","Cybersecurity Analyst",
    "Pharmacist","Dentist","Lab Technician","Chef","Waiter","Hotel Manager","Flight Attendant",
    "Pilot","Bank Teller","Financial Analyst","Insurance Agent","Farmer","Fisherman","Warehouse Worker",
    "Delivery Driver","Barber","Hair Stylist","Makeup Artist","Painter","Photographer","Translator",
    "Interpreter","Writer","Editor","Journalist","Real Estate Agent","Architect","Civil Engineer",
    "Software Tester","Quality Assurance Specialist","UI/UX Designer","Content Creator","Social Media Manager",
    "SEO Specialist","Security Guard","Firefighter","Police Officer","Paramedic","Car Mechanic","Bus Driver",
    "Train Operator","Machine Operator","Miner","Oil Rig Worker","Teacher Assistant","Kindergarten Teacher",
    "University Professor","Research Assistant","Librarian","Veterinarian","Animal Care Worker","Scientist",
    "Chemist","Biologist","Physicist","Mathematician","Economist","Lawyer","Judge","Legal Assistant",
    "HR Manager","Recruiter","Business Consultant","Entrepreneur","Cafe Manager","Store Manager","Courier",
    "Logistics Coordinator","Network Engineer","Cloud Engineer","AI Engineer","ML Engineer","DevOps Engineer"
]

def slugify(text):
    return (
        text.lower()
        .replace(" ", "-")
        .replace("&", "and")
        .replace("/", "-")
        .replace(",", "")
        .replace(".", "")
    )

# =====================================
# 3. WRITE FILE UTILITY
# =====================================

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# =====================================
# 4. MAIN PAGE GENERATOR
# =====================================

def main():
    os.makedirs("docs", exist_ok=True)
    write("template.html", TEMPLATE_HTML)
    write("script.js", SCRIPT_JS)
    write("style.css", STYLE_CSS)

    calculators = []
    template = TEMPLATE_HTML.replace("{{ADSENSE_SNIPPET}}", ADSENSE_SNIPPET)

    # PAGE GENERATION
    for c in COUNTRIES:
        for j in JOBS:
            slug = f"{c['code']}-{slugify(j)}-salary-calculator"
            title = f"{c['name']} {j} Net Salary Calculator"
            desc = f"Calculate take-home pay for a {j} in {c['name']}."

            html = template.replace("{{TITLE}}", title)\
                .replace("{{DESCRIPTION}}", desc)\
                .replace("{{COUNTRY}}", c["name"])\
                .replace("{{JOB}}", j)\
                .replace("{{CURRENCY}}", c["currency"])\
                .replace("{{TAX_RATE}}", str(c["tax_rate"]))\
                .replace("{{SOCIAL_RATE}}", str(c["social_rate"]))

            write(f"docs/{slug}.html", html)

            calculators.append({"slug": slug, "country": c["name"], "job": j, "title": title})

    # INDEX
    calculators.sort(key=lambda x: (x["country"], x["job"]))
    index_html = "<html><body><h1>Global Salary Calculators</h1><ul>"
    for m in calculators:
        index_html += f'<li><a href="{m["slug"]}.html">{m["title"]}</a></li>'
    index_html += """
</ul>
<p><a href="privacy.html">Privacy Policy</a> | <a href="disclaimer.html">Disclaimer</a></p>
</body></html>
"""
    write("docs/index.html", index_html)

    # PRIVACY
    write("docs/privacy.html", "<html><body><h1>Privacy Policy</h1>This site uses AdSense.</body></html>")

    # DISCLAIMER
    write("docs/disclaimer.html", "<html><body><h1>Disclaimer</h1>Simplified salary estimation only.</body></html>")

    # SITEMAP
    SITE = "https://ejsvk1207-source.github.io/global-salary-calculators"
    sm = "<urlset>"
    for m in calculators:
        sm += f"<url><loc>{SITE}/{m['slug']}.html</loc></url>"
    sm += "</urlset>"
    write("docs/sitemap.xml", sm)

    # ROBOTS
    write("docs/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml")

    # README
    write("README.md", "# Global Salary Calculators\nAuto-generated salary pages.")

    print("DONE — All pages generated successfully!")

if __name__ == "__main__":
    main()
