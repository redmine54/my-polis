// frontend/app.js

document.getElementById("run").addEventListener("click", async () => {
  const res = await fetch("/api/analysis/run", { method: "POST" });
  const data = await res.json();
  console.log("=== API Response ===",data);

  document.getElementById("clusters").textContent = JSON.stringify(data.clusters, null, 2);
  document.getElementById("consensus").textContent = JSON.stringify(data.consensus, null, 2);
});
