// frontend/app.js
/*
document.getElementById("run").addEventListener("click", async () => {
  const res = await fetch("/api/analysis/run", { method: "POST" });
  const data = await res.json();
  console.log("=== API Response ===",data);

  document.getElementById("clusters").textContent = JSON.stringify(data.clusters, null, 2);
  document.getElementById("consensus").textContent = JSON.stringify(data.consensus, null, 2);
});
*/
// frontend/app.js

function toTable(obj) {
  if (!Array.isArray(obj) || obj.length === 0) {
    return "<p>データがありません</p>";
  }

  let html = "<table border='1' style='border-collapse: collapse;'>";

  // ヘッダー行
  html += "<tr>";
  for (const key of Object.keys(obj[0])) {
    html += `<th>${key}</th>`;
  }
  html += "</tr>";

  // データ行
  for (const row of obj) {
    html += "<tr>";
    for (const key of Object.keys(row)) {
      html += `<td>${row[key]}</td>`;
    }
    html += "</tr>";
  }

  html += "</table>";
  return html;
}

document.getElementById("run").addEventListener("click", async () => {
  const res = await fetch("/api/analysis/run", { method: "POST" });
  const data = await res.json();

  console.log("clusters:", data.clusters);
  console.log("consensus:", data.consensus);

  document.getElementById("clusters").innerHTML = toTable(data.clusters);
  document.getElementById("consensus").innerHTML = toTable(data.consensus);
});
