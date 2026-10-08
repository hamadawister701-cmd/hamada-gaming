from flask import Flask, request, render_template_string

app = Flask(__name__)
MY_NUMBER = "201141543557" # غير ده لرقمك

HTML = """
<!DOCTYPE html>
<html dir="rtl">
<head><title>Hamada Mahrous  </title>
<style>
body{background:#ff0148;color:white;font-family:Arial;text-align:center;padding:20px}
h1{color:#ff0040;text-shadow:0 0 20px #ff0148;font-size:50px}
.box{background:#1a1a1a;padding:30px;border-radius:20px;max-width:500px;margin:20px auto;border:2px solid #ff0040}
input,textarea{width:90%;padding:15px;margin:10px;border-radius:10px;border:none;font-size:18px}
button{background:#25D366;color:white;padding:15px 40px;border:none;border-radius:30px;font-size:22px;cursor:pointer;width:95%}
button:hover{background:#1da851}
.headset{font-size:100px}
#messages{margin-top:20px;text-align:right;background:#000;padding:15px;border-radius:10px}
.msg{border-bottom:1px solid #333;padding:10px}
</style>
</head>
<body>
<div class="headset">🎧</div>
<h1>HAMADA MAHROUS GAMING</h1>
<p>YOUR'E WELCOME TO MY PROJECT </p>

<div class="box">
<h2>ask them for any things</h2>
<form action="/send" method="post">
<input type="text" name="name" placeholder="اسمك ايه؟" required>
<textarea name="message" placeholder="اكتب رسالتك هنا..." rows="4" required></textarea>
<button type="submit">ابعت رسالة واتساب 📲</button>
</form>

<div id="messages">
<h3>الرسايل اللي اتبعتت:</h3>
{% for m in all_messages %}
<div class="msg"><b>{{ m.name }}:</b> {{ m.text }}</div>
{% endfor %}
</div>
</div>
</body>
</html>
"""

all_messages = []

@app.route("/")
def home():
    return render_template_string(HTML, all_messages=all_messages)

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    text = request.form["message"]
    all_messages.append({"name": name, "text": text})
    # ده بيحول الرسالة لواتساب بتاعك
    wa_text = f"رسالة جديدة من {name}: {text}"
    import urllib.parse
    wa_link = f"https://wa.me/{MY_NUMBER}?text={urllib.parse.quote(wa_text)}"
    return f'<script>window.open("{wa_link}", "_blank"); window.location.href="/";</script> رسالتك اتبعتت!'

if __name__ == "__main__":
    app.run(debug=True)