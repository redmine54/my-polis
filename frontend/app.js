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

  // スクロール可能なコンテナ（最大10行分の高さ）
  let html = `
    <div style="max-height: 250px; overflow-y: auto; border: 1px solid #ccc;">
      <table border='1' style='border-collapse: collapse; width: 100%;'>
  `;

  // ヘッダー行
  html += "<tr>";
  for (const key of Object.keys(obj[0])) {
    html += `<th style="background:#f0f0f0; position: sticky; top: 0;">${key}</th>`;
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

  html += `
      </table>
    </div>
  `;
  return html;
}

document.getElementById("run").addEventListener("click", async () => {
  const res = await fetch("/api/analysis/run", { method: "POST" });
  const data = await res.json();

  //console.log("clusters:", data.clusters);
  //console.log("consensus:", data.consensus);

  document.getElementById("clusters").innerHTML = toTable(data.clusters);
  document.getElementById("consensus").innerHTML = toTable(data.consensus);
});
