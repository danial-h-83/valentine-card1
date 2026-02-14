import os

PROJECT_NAME = "valentine_card"
IMAGES_FOLDER = os.path.join(PROJECT_NAME, "images")

HTML_CONTENT = """<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>برای شهرزادِ من</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;500&display=swap');

body{
  margin:0;
  min-height:100vh;
  display:flex;
  justify-content:center;
  align-items:center;
  direction:rtl;
  font-family:sans-serif;
  position:relative;
  overflow:hidden;
}

/* تصویر بوسه کلیمت – نرم و رمانتیک */
body::before{
  content:"";
  position:absolute;
  inset:0;
  background: url('klimt.jpg') center/cover no-repeat;
  filter: blur(14px) brightness(0.7) saturate(1.1);
  transform: scale(1.15);
  z-index:-2;
}

/* لایه گرم عاشقانه (طلایی-صورتی) */
body::after{
  content:"";
  position:absolute;
  inset:0;
  background:
    linear-gradient(
      135deg,
      rgba(240,190,200,0.45),
      rgba(210,170,120,0.45)
    );
  z-index:-1;
}


.card {
    width: 90%;
    max-width: 380px;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(6px);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    color: #fff;
    cursor: pointer;
    transition: transform 0.6s;
}

.card.open {
    transform: scale(1.03);
}

h1 {
    font-weight: 500;
}

.text {
    display: none;
    margin-top: 15px;
    font-size: 15px;
    line-height: 1.9;
}

.card.open .text {
    display: block;
}

.hearts {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

.heart {
    width: 90px;
    height: 90px;
    background-size: cover;
    background-position: center;
    clip-path: path("M45 80 C20 60 0 40 0 22 C0 10 10 0 22 0 C32 0 40 8 45 15 C50 8 58 0 68 0 C80 0 90 10 90 22 C90 40 70 60 45 80 Z");
}
</style>
</head>

<body>

<div class="card" onclick="this.classList.toggle('open')">
    <h1>برای شهرزاد 🤍</h1>

    <div class="text">
        <p>
        شهرزادِ من،<br>
        حتی فاصله هم بلد نیست<br>
        عشق من به تو رو کم‌رنگ کنه.<br>
        تو مثل این نقاشی،<br>
        طلایی، عمیق و موندگاری…<br>
        و من هر روز<br>
        بیشتر از دیروز<br>
        دوستت دارم.
        </p>

        <div class="hearts">
            <div class="heart" style="background-image:url('images/pic1.jpg')"></div>
            <div class="heart" style="background-image:url('images/pic2.jpg')"></div>
            <div class="heart" style="background-image:url('images/pic3.jpg')"></div>
        </div>
    </div>

    <p style="margin-top:10px;font-size:13px;">(لمس کن 🌹)</p>
</div>

</body>
</html>
"""

def main():
    # ساخت پوشه اصلی
    if not os.path.exists(PROJECT_NAME):
        os.mkdir(PROJECT_NAME)

    # ساخت پوشه تصاویر
    if not os.path.exists(IMAGES_FOLDER):
        os.mkdir(IMAGES_FOLDER)

    # ساخت فایل HTML
    html_path = os.path.join(PROJECT_NAME, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    print("✅ کارت ولنتاین با موفقیت ساخته شد!")
    print("📁 مسیر پروژه:", PROJECT_NAME)
    print("🖼️ حالا 3 عکس با نام‌های زیر داخل پوشه images قرار بده:")
    print("   - pic1.jpg")
    print("   - pic2.jpg")
    print("   - pic3.jpg")
    print("🌐 بعدش می‌تونی index.html رو باز کنی یا آپلودش کنی و لینک بفرستی ❤️")

if __name__ == "__main__":
    main()
