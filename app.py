from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!doctype html>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Opening App…</title>
<script>
  var t = Date.now();
  setTimeout(function(){
    if (Date.now() - t < 1500) location.replace("https://calendar.notion.so/");
  }, 1200);
  location.href = "cron://";
</script>
<body style="font-family:system-ui;padding:12px">
  正在開啟 Notion Calendar…
  <br><br>
  <br><a href="cron://">重新開啟 App</a>
  <br><a href="https://calendar.notion.so/">改用網頁</a>
</body>
"""

@app.route("/")
def home():
    return "✅ Flask 已啟動"

@app.route("/open")
def open_calendar():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
