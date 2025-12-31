from flask import Flask, render_template, request

app = Flask(__name__)

def farming_answer(question):
    q = question.lower()

    if "fertilizer" in q or "မြေဩဇာ" in q:
        return "Myanmar: မြေဩဇာကို သီးနှံအလိုက် သုံးပါ။\nEnglish: Use fertilizer based on crop type."
    elif "pest" in q or "ပိုး" in q:
        return "Myanmar: ပိုးမွှားတွေ့ရင် အချိန်မီ ကာကွယ်ပါ။\nEnglish: Control pests early."
    elif "water" in q or "ရေ" in q:
        return "Myanmar: ရေလောင်းတက်တာကို ထိန်းညှိပါ။\nEnglish: Proper irrigation is important."
    elif "seed" in q or "မျိုးစေ့" in q:
        return "Myanmar: အရည်အသွေးကောင်းတဲ့ မျိုးစေ့ကို အသုံးပြုပါ။\nEnglish: Use high-quality seeds."
    else:
        return "Myanmar: အချက်အလက်မရှိသေးပါ။\nEnglish: No information available."

@app.route("/", methods=["GET","POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = farming_answer(question)
    return render_template("index.html", answer=answer)

if name == "__main__":
    app.run(host="0.0.0.0", port=10000)