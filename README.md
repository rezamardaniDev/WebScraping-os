# پروژه سیستم عامل
<h1>هدف پروژه</h1>
<p>
  هدف این برنامه استخراج قیمت گوشیهای موجود در سایت mobile.ir و نمایش آنها به صورت جدولی، همراه با 
گزارش گرانترین، ارزانترین و میانگین قیمت گوشیها میباشد. که در یک حالت سری و یک حالت چندنخی 
نوشته شده است تا مدت زمان انجام آنها با هم مقایسه شود
</p>
<hr>
<h1>کتابخانه های استفاده شده</h1>
<p>requests , beautifulsoup , pandas , threading , time</p>
<hr>
<h1>نحوه کارکرد پروژه</h1>
<p>
* در ابتدا، برای استخراج اطلاعات از سایت ir.mobile از کتابخانه requests و BeautifulSoup استفاده شده 
است.<br>
* سپس، با دسترسی به صفحات مختلف سایت، اطلاعات قیمت گوشیهای موجود در هر صفحه استخراج 
شده و به دو لیست تبدیل شده است.<br>
* لیست اول حاوی عنوان گوشیها بوده و در لیست دوم، قیمتهای مربوط به گوشیها قرار دارند.<br>
* در ادامه، این دو لیست به کمک تابع zip ترکیب شده و یک دیکشنری ساخته میشود که نام گوشی به عنوان 
کلید و قیمت آن به عنوان مقدار در آن ذخیره میشود.<br>
* سپس این دیکشنری به DataFrame pandas تبدیل شده و نمایش داده میشود.<br>
* با استفاده از توابع dataframe مربوط بهpandas ، گرانترین و ارزانترین گوشیها پیدا شده و به همراه 
میانگین قیمت گوشیها نمایش داده میشوند.<br>
* در نهایت، زمان اجرای برنامه نیز نمایش داده میشود.<br>
</p>
