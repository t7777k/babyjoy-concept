import json
D={'olive':{'tape':[['NB','0–5'],['S','4–8'],['M','6–11'],['L','9–14'],['XL','12–17']],'pants':[['M','6–11'],['L','9–14'],['XL','12–17'],['XXL','15–25']]},
'regular':{'tape':[['1','2–5'],['2','3–8'],['3','6–11'],['4','9–14'],['5','12–17']],'pants':[['3','6–11'],['4','TBC*'],['5','12–17'],['6','15–25']]}}
RET=[('Al-Dawaa','الدواء','al-dawaa-logo.png'),('Nahdi','النهدي','nahdi-logo.png'),('noon','نون','noon-logo-1.png'),('Amazon.sa','أمازون','amazon-logo.png'),('FirstCry','فيرست كراي','first-cry.png'),('Mumzworld','ممزورلد','mumzworld-min.png')]
T={
'ar':dict(dir='rtl',other='en/',otherlbl='English',p='',title='بيبي جوي السعودية | حفاضات بحماية من التسرب – اختبار ٤٥°',desc='اكتشفي حفاضات بيبي جوي: بريميوم زيتون، اللاصق والسروال. شاهدي اختبار الزاوية ٤٥° واعثري على المقاس المناسب لطفلك واشتري من متجرك المفضل.',
proto='نموذج تجريبي — بيانات المنتجات افتراضية ويجب التحقق منها مقابل ملف SKU الرئيسي',
nav=['الاختبار','المنتجات','اختر المقاس','نصائح','تواصل معنا'],
eb='اختبار الزاوية ٤٥°',h1='اختبار واحد... والفرق واضح.',sub='حماية من التسرب، حتى مع حركة طفلك.',lead='شاهد الفرق بين بيبي جوي وحفاض آخر، بنفس الزاوية وكمية السائل.',
filmh='بيبي جوي... قد التحدي',filml='الحفاض الذي تختاره الأمهات بثقة، في كل مرحلة.',cta='اعثري على المقاس المناسب',cta2='شاهدي المنتجات',bj='بيبي جوي',oth='حفاض آخر',ok='✓ بدون تسرب',bad='✗ تسرب',capt='٤٥° · نفس كمية السائل · نفس الزمن',play='تشغيل الفيديو',
cond='ظروف الاختبار',condt='[نص افتراضي] يُثبَّت كل حفاض على سطح مائل بزاوية ٤٥°، ويُسكب نفس حجم السائل بنفس المعدل، ثم يُقارن التسرب بصرياً بعد مدة محددة. يجب إرفاق المنهجية الموثقة ونتائج الاختبار المعتمدة قبل الإطلاق.',
ph='بيانات افتراضية',prodh='أربع عائلات، لكل طفل ما يناسبه',prodl='اختاري العائلة ثم المقاس. المواصفات أدناه تجريبية.',
fam=[('olive','olive-tape.webp','بريميوم زيتون – لاصق','بريميوم','لعناية فائقة بالبشرة الحساسة',['ملمس ناعم مع لمسة زيت الزيتون*','لاصق مرن قابل للتعديل','مؤشر رطوبة*']),
('olive','olive-pants.jpg','بريميوم زيتون – سروال','بريميوم','سهولة اللبس للطفل النشيط',['يُلبس كالملابس الداخلية','خصر مطاطي مريح','حماية من التسرب أثناء الحركة*']),
('regular','reg-tape.jpg','بيبي جوي المضغوط – لاصق','يومي','قيمة ممتازة للاستخدام اليومي',['تقنية الضغط لعبوة أصغر*','امتصاص سريع*','حواف مانعة للتسرب*']),
('regular','reg-pants.webp','بيبي جوي – سروال','يومي','للأطفال الذين يحبون الحركة',['سهل اللبس والخلع','مرونة كاملة','حماية ليلية*'])],
sz='المقاسات:',pick='اختاري مقاساً لعرض المواصفات',kg='كغ',pack='عدد الحبات: يحدد لاحقاً',buy='اشتري من:',
wipes='مناديل بيبي جوي المبللة',wipesl='لطيفة على البشرة لكل تغيير حفاض. (قسم مقترح — تفاصيل المنتجات تُضاف من الكتالوج الرسمي)',
fh='اعثري على المقاس المناسب في ٣ خطوات',fl='اختاري النوع وأدخلي وزن طفلك.',
f1='١. المجموعة',f2='٢. النوع',f3='٣. وزن الطفل (كغ)',ro=('olive','بريميوم زيتون'),rr=('regular','العادي / المضغوط'),tt='لاصق',tp='سروال',
cmp='مقارنة سريعة',cols=['','بريميوم زيتون لاصق','بريميوم زيتون سروال','مضغوط لاصق','سروال عادي'],
rows=[['الأنسب لـ','حديثو الولادة والبشرة الحساسة','الطفل النشيط','الاستخدام اليومي','التدريب والحركة'],['نطاق المقاسات*','NB–XL','M–XXL','1–5','3–6'],['طريقة اللبس','لاصق','سروال','لاصق','سروال'],['الفئة','بريميوم','بريميوم','قيمة','قيمة']],
note='* بيانات افتراضية. ملاحظة: يوجد تعارض في نطاق وزن السروال العادي مقاس ٤ بين مصادر مختلفة — تم إخفاؤه حتى التحقق.',
howh='كيف يعمل اختبار ٤٥°؟',how=[('التثبيت','يوضع الحفاضان جنباً إلى جنب على سطح مائل ٤٥°.'),('السكب','نفس كمية السائل وبنفس المعدل.'),('الانتظار','مدة زمنية موحدة للحفاضين.'),('النتيجة','مقارنة التسرب بوضوح أمام الكاميرا.')],
guideh='دليل الأم',guide=[('لاصق أم سروال؟','اللاصق مثالي لحديثي الولادة وتغيير الحفاض والطفل مستلقٍ. السروال أسهل للطفل الذي يزحف أو يمشي.'),('متى أغيّر المقاس؟','علامات حمراء على الفخذين، صعوبة إغلاق اللاصق، أو تكرار التسرب — قد تكون إشارة للانتقال للمقاس التالي.'),('نصائح لمنع التسرب','تأكدي من فرد الحواف الجانبية للخارج، وشد اللاصق بشكل متماثل، وتغيير الحفاض بانتظام.')],
faqh='أسئلة شائعة',faq=[('من أين أشتري بيبي جوي؟','من المتاجر الإلكترونية والصيدليات والهايبرماركت الكبرى في المملكة.'),('هل الحفاضات مناسبة للبشرة الحساسة؟','مجموعة بريميوم زيتون مصممة للعناية بالبشرة. [الادعاء يحتاج إلى توثيق]'),('ماذا لو كان طفلي بين مقاسين؟','اختاري المقاس الأكبر إذا اقترب الوزن من الحد الأعلى.')],
abh='عن بيبي جوي',abt='بيبي جوي علامة تجارية للعناية بالطفل تقدمها مجموعة UGHI بالشراكة مع يونيتشارم، وتهدف إلى منح الأمهات في المملكة حماية موثوقة وراحة يومية لأطفالهن. [نص مختصر — يُستبدل بالقصة المعتمدة]',
ch='تواصل معنا',name='الاسم',email='البريد الإلكتروني',mob='رقم الجوال',reason='سبب التواصل',reasons=['استفسار عن منتج','شكوى أو ملاحظة','شراكة / توزيع','أخرى'],msg='رسالتك',att='مرفق (اختياري)',
consent='أوافق على معالجة بياناتي للرد على استفساري وفقاً لسياسة الخصوصية.',send='إرسال',sent='شكراً! (نموذج تجريبي — لم يتم إرسال أي بيانات)',
foot='© ٢٠٢٦ بيبي جوي السعودية — نموذج تصميم تجريبي',priv='سياسة الخصوصية',terms='الشروط والأحكام'),
'en':dict(dir='ltr',other='../',otherlbl='العربية',p='../',title='BabyJoy Saudi Arabia | Leak-Protection Diapers – The 45° Test',desc='Discover BabyJoy diapers: Premium Olive, tape and pants. Watch the 45° test, find the right size for your baby and buy from your favourite retailer.',
proto='Concept prototype — product data is placeholder and must be verified against the master SKU file',
nav=['The test','Products','Size finder','Tips','Contact'],
eb='The 45° test',h1='One test. A clear difference.',sub='Leak protection, even when your baby moves.',lead='See the difference between BabyJoy and another diaper — same angle, same amount of liquid.',
filmh='BabyJoy. Up to the challenge.',filml='The diaper parents choose with confidence, at every stage.',cta='Find the right size',cta2='See products',bj='BabyJoy',oth='Other diaper',ok='✓ No leak',bad='✗ Leaked',capt='45° · same liquid · same time',play='Play video',
cond='Test conditions',condt='[Placeholder] Each diaper is fixed on a 45° inclined surface; the same volume of liquid is poured at the same rate, and leakage is compared visually after a set time. Documented methodology and verified results must be attached before launch.',
ph='Placeholder data',prodh='Four families, one for every baby',prodl='Choose a family, then a size. Specs below are placeholders.',
fam=[('olive','olive-tape.webp','Premium Olive – Tape','Premium','Extra care for sensitive skin',['Soft touch with olive oil*','Flexible, adjustable tapes','Wetness indicator*']),
('olive','olive-pants.jpg','Premium Olive – Pants','Premium','Easy on for active babies',['Pulls on like underwear','Comfy stretch waist','Leak protection on the move*']),
('regular','reg-tape.jpg','BabyJoy Compressed – Tape','Everyday','Great value for daily use',['Compressed, smaller pack*','Fast absorption*','Leak-guard edges*']),
('regular','reg-pants.webp','BabyJoy – Pants','Everyday','For babies who love to move',['Easy on and off','Full flexibility','Night protection*'])],
sz='Sizes:',pick='Select a size to see specs',kg='kg',pack='Pack count: TBC',buy='Buy at:',
wipes='BabyJoy Wet Wipes',wipesl='Gentle on skin for every change. (Proposed section — product details to come from the official catalogue)',
fh='Find the right size in 3 steps',fl='Choose a type and enter your baby\'s weight.',
f1='1. Range',f2='2. Type',f3='3. Baby weight (kg)',ro=('olive','Premium Olive'),rr=('regular','Regular / Compressed'),tt='Tape',tp='Pants',
cmp='Quick comparison',cols=['','Olive Tape','Olive Pants','Compressed Tape','Regular Pants'],
rows=[['Best for','Newborns & sensitive skin','Active babies','Everyday use','Training & movement'],['Size range*','NB–XL','M–XXL','1–5','3–6'],['Fit','Tape','Pants','Tape','Pants'],['Tier','Premium','Premium','Value','Value']],
note='* Placeholder data. Note: sources disagree on Regular Pants size 4 weight range — hidden until verified.',
howh='How does the 45° test work?',how=[('Set up','Both diapers side by side on a 45° incline.'),('Pour','Same amount of liquid, same rate.'),('Wait','Identical time for both.'),('Result','Leakage compared clearly on camera.')],
guideh='Parent guide',guide=[('Tape or pants?','Tape is ideal for newborns and lying-down changes. Pants are easier once your baby crawls or walks.'),('When to size up?','Red marks on thighs, tapes hard to close, or repeated leaks can signal it\'s time for the next size.'),('Leak-prevention tips','Pull the leg cuffs outward, fasten tapes evenly, and change regularly.')],
faqh='FAQ',faq=[('Where can I buy BabyJoy?','From major online stores, pharmacies and hypermarkets across the Kingdom.'),('Is it suitable for sensitive skin?','The Premium Olive range is designed with skin care in mind. [Claim needs substantiation]'),('What if my baby is between sizes?','Choose the larger size when weight is near the upper limit.')],
abh='About BabyJoy',abt='BabyJoy is a baby-care brand offered by UGHI in partnership with Unicharm, aiming to give parents in Saudi Arabia reliable protection and everyday comfort. [Short copy — replace with approved brand story]',
ch='Contact us',name='Name',email='Email',mob='Mobile number',reason='Reason',reasons=['Product question','Complaint or feedback','Partnership / distribution','Other'],msg='Your message',att='Attachment (optional)',
consent='I agree to the processing of my data to respond to my enquiry, per the Privacy Policy.',send='Send',sent='Thanks! (Prototype — no data was sent)',
foot='© 2026 BabyJoy Saudi Arabia — design concept prototype',priv='Privacy policy',terms='Terms'),
}
B='https://t7777k.github.io/babyjoy-concept'
ids=['test','products','finder','tips','contact']
def page(l):
    t=T[l];p=t['p'];a=l=='ar'
    ret=''.join(f'<a href="#" rel="nofollow" title="{r[1] if a else r[0]}"><img src="{p}img/{r[2]}" alt="{r[1] if a else r[0]}" loading="lazy"></a>' for r in RET)
    cards=''
    for i,(rg,img,nm,tier,tag,ben) in enumerate(t['fam']):
        typ='tape' if i in(0,2) else 'pants'
        btns=''.join(f'<button type="button" aria-pressed="false" data-spec="{t["sz"].rstrip(":")} {s}: {g} {t["kg"]} · {t["pack"]} ({t["ph"]})">{s}</button>' for s,g in D[rg][typ])
        fam=['f-olive','f-olive2','f-teal','f-blue'][i]
        cards+=f'''<article class="card pcard {fam} reveal"><div class="pimg"><img src="{p}img/{img}" alt="{nm}" loading="lazy" width="400" height="400"></div><span class="pill">{tier}</span><h3>{nm}</h3><p class="small">{tag}</p><ul class="ben">{''.join(f'<li>{b}</li>' for b in ben)}</ul><div class="small">{t['sz']}</div><div class="sizes" role="group" aria-label="{t['sz']}">{btns}</div><div class="spec" aria-live="polite">{t['pick']}</div><details><summary>{t['buy']}</summary><div class="retail">{ret}</div></details></article>'''
    th=''.join(f'<th scope="col">{c}</th>' for c in t['cols'])
    rows=''.join('<tr><th scope="row">'+r[0]+'</th>'+''.join(f'<td>{c}</td>' for c in r[1:])+'</tr>' for r in t['rows'])
    how=''.join(f'<div><h3>{h}</h3><p class="small">{x}</p></div>' for h,x in t['how'])
    guide=''.join(f'<article class="card"><h3>{h}</h3><p class="small">{x}</p></article>' for h,x in t['guide'])
    faq=''.join(f'<details><summary>{q}</summary><p>{x}</p></details>' for q,x in t['faq'])
    nav=''.join(f'<a href="#{i}">{n}</a>' for i,n in zip(ids,t['nav']))
    opts=''.join(f'<option>{r}</option>' for r in t['reasons'])
    return f'''<!doctype html><html lang="{l}" dir="{t['dir']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title><meta name="description" content="{t['desc']}"><meta name="robots" content="noindex,nofollow">
<link rel="alternate" hreflang="ar-SA" href="{B}/"><link rel="alternate" hreflang="en-SA" href="{B}/en/"><link rel="alternate" hreflang="x-default" href="{B}/"><link rel="canonical" href="{B}{'/' if a else '/en/'}">
<link rel="icon" href="{p}img/favicon.png"><link rel="stylesheet" href="{p}fonts/fonts.css"><link rel="stylesheet" href="{p}style.css"></head><body>
<div class="proto" role="note">⚠ {t['proto']}</div>
<header><div class="wrap nav"><a href="#"><img src="{p}img/logo.png" alt="BabyJoy" width="110" height="40"></a><nav aria-label="main">{nav}</nav><a class="lang" href="{t['other']}" hreflang="{'en' if a else 'ar'}">{t['otherlbl']}</a></div></header>
<main><section class="hero" id="test"><div class="wrap grid"><div class="reveal"><span class="eyebrow">{t['eb']}</span><h1>{t['h1']}</h1><p class="sub">{t['sub']}</p><p class="lead">{t['lead']}</p>
<div class="ctas"><a class="btn" href="#finder">{t['cta']}</a><a class="btn ghost" href="#products">{t['cta2']}</a></div>
<details class="cond"><summary>{t['cond']}</summary><p>{t['condt']}</p></details></div>
<div class="vidcol reveal"><figure class="video"><video id="v45" src="{p}img/test45.mp4" poster="{p}img/test45-poster.jpg" autoplay muted loop playsinline preload="metadata" aria-label="{t['capt']}"></video>
<figcaption><span class="chip ok">{t['bj']} {t['ok']}</span><span class="chip">{t['capt']}</span></figcaption><button class="mute" type="button" aria-label="{t['play']}">❚❚</button></figure>
<img class="slogan" src="{p}img/babyjoy-slogan-new-1.svg" alt="" aria-hidden="true"></div></div>
<div class="retailbar wrap reveal"><span>{t['buy']}</span><div class="retail">{ret}</div></div></section>
<section class="film"><video src="{p}img/hero.mp4" poster="{p}img/hero-poster.jpg" autoplay muted loop playsinline preload="none" aria-hidden="true"></video><div class="wrap filmtxt reveal"><h2>{t['filmh']}</h2><p>{t['filml']}</p></div></section>
<section id="products"><div class="wrap"><h2>{t['prodh']}</h2><p class="lead">{t['prodl']}</p><div class="cards">{cards}</div>
<article class="card wipes reveal"><div class="wicon" aria-hidden="true"><svg viewBox="0 0 48 48" width="40" height="40" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><rect x="8" y="14" width="32" height="24" rx="6"/><path d="M18 14c0-4 12-4 12 0M16 26h16"/></svg></div><div><h3>{t['wipes']}</h3><p class="small">{t['wipesl']}</p></div></article></div></section>
<section id="finder" class="alt"><div class="wrap"><form class="finder" id="finder-form" style="display:block" name="finder" onsubmit="return false"><h2>{t['fh']}</h2><p style="color:#cfd6ea">{t['fl']}</p>
<div class="steps"><div><label for="fr">{t['f1']}</label><select id="fr" name="range"><option value="{t['ro'][0]}">{t['ro'][1]}</option><option value="{t['rr'][0]}">{t['rr'][1]}</option></select></div>
<div><label for="ft">{t['f2']}</label><select id="ft" name="type"><option value="tape">{t['tt']}</option><option value="pants">{t['tp']}</option></select></div>
<div><label for="fw">{t['f3']}</label><input id="fw" name="weight" type="number" min="0" max="30" step="0.5" inputmode="decimal" value="7"></div></div>
<div class="result" id="fres" aria-live="polite"></div><p class="small" style="color:#cfd6ea;margin-top:14px">{t['buy']}</p><div class="retail">{ret}</div></form>
<h2 style="margin-top:48px">{t['cmp']}</h2><div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div><p class="small">{t['note']}</p></div></section>
<section><div class="wrap"><h2>{t['howh']}</h2><div class="how">{how}</div></div></section>
<section id="tips" class="alt"><div class="wrap"><div class="tipshead"><div><h2>{t['guideh']}</h2></div><!-- AI-generated CONCEPT imagery (Higgsfield) --><img class="photo" src="{p}img/concept-toddler.jpg" alt="" loading="lazy"></div><div class="cards">{guide}</div><h2 style="margin-top:48px">{t['faqh']}</h2><div class="faq">{faq}</div></div></section>
<section><div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:30px;align-items:center"><div><h2>{t['abh']}</h2><p class="lead">{t['abt']}</p></div><!-- AI-generated CONCEPT imagery (Higgsfield) — replace with licensed brand photography --><img class="photo" src="{p}img/concept-family.jpg" alt="" loading="lazy"></div></section>
<section id="contact" class="alt"><div class="wrap" style="max-width:760px"><h2>{t['ch']}</h2><form id="contact">
<div><label for="cn">{t['name']}</label><input id="cn" required autocomplete="name"></div><div><label for="ce">{t['email']}</label><input id="ce" type="email" required autocomplete="email" dir="ltr"></div>
<div><label for="cm">{t['mob']}</label><input id="cm" type="tel" placeholder="05XXXXXXXX" autocomplete="tel" dir="ltr"></div><div><label for="cr">{t['reason']}</label><select id="cr">{opts}</select></div>
<div class="full"><label for="cx">{t['msg']}</label><textarea id="cx" rows="4" required></textarea></div><div class="full"><label for="cf">{t['att']}</label><input id="cf" type="file"></div>
<div class="full small"><label style="font-weight:400;display:flex;gap:8px"><input type="checkbox" required style="width:auto"> {t['consent']} <a href="privacy.html">{t['priv']}</a></label></div>
<div class="full"><button class="btn">{t['send']}</button> <span class="ok small" hidden role="status">{t['sent']}</span></div></form></div></section></main>
{FOOT(l)}
<script src="{p}app.js"></script></body></html>'''
exec(open('pages.py').read())
open('index.html','w').write(page('ar'));open('en/index.html','w').write(page('en'))
