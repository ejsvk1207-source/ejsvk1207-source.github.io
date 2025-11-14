document.addEventListener("DOMContentLoaded", () => {
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
