def FOOT(l):
    a=l=='ar';t=T[l];p='' if a else ''
    L=[('about.html','عن بيبي جوي','About'),('contact.html','تواصل معنا','Contact'),('privacy.html','سياسة الخصوصية','Privacy'),('terms.html','الشروط والأحكام','Terms')]
    links=''.join(f'<li><a href="{h}">{x if a else y}</a></li>' for h,x,y in L)
    ret=''.join(f'<li><a href="#" rel="nofollow">{r[1] if a else r[0]}</a></li>' for r in RET)
    soc=''.join(f'<li><a href="#">{n}</a></li>' for n in ['Instagram','TikTok','X','YouTube','Facebook'])
    h=('الصفحات','اشتري من','تابعنا') if a else ('Pages','Buy at','Follow us')
    return f'''<footer><div class="wrap fgrid"><div><img src="{'' if a else '../'}img/logo.png" alt="BabyJoy" width="110" style="background:#fff;border-radius:12px;padding:6px 10px;margin-bottom:10px"><p>{'علامة تجارية للعناية بالطفل — نوجّهك لشراء منتجاتنا من شركائنا المعتمدين.' if a else 'A baby-care brand — we guide you to buy from our authorised retail partners.'}</p></div>
<div><h4>{h[0]}</h4><ul>{links}</ul></div><div><h4>{h[1]}</h4><ul>{ret}</ul></div><div><h4>{h[2]}</h4><ul>{soc}</ul></div></div>
<div class="wrap fbot">{t['foot']}<br><span class="small" style="color:#cfd6ea">{t['proto']}</span></div></footer>'''
SUB={'about':(('عن بيبي جوي','About BabyJoy'),('abt',)),'privacy':(('سياسة الخصوصية','Privacy Policy'),None),'terms':(('الشروط والأحكام','Terms & Conditions'),None),'contact':(('تواصل معنا','Contact us'),None)}
LEG={'ar':'⚠ نص قانوني افتراضي — يجب استبداله بنص معتمد من الفريق القانوني ومتوافق مع نظام حماية البيانات الشخصية (PDPL) في المملكة.','en':'⚠ Placeholder legal text — must be replaced with counsel-approved text compliant with Saudi PDPL.'}
PRIV={'ar':['البيانات التي نجمعها: الاسم، البريد، الجوال، ومحتوى رسالتك.','الغرض: الرد على استفسارك وتحسين خدماتنا.','المشاركة: لا نبيع بياناتك. قد نشاركها مع مزودي خدمات بموجب عقود.','حقوقك: الوصول والتصحيح والحذف عبر صفحة التواصل.','ملفات تعريف الارتباط والتحليلات: تُستخدم بعد موافقتك فقط.'],
'en':['Data we collect: name, email, mobile and message content.','Purpose: to respond to your enquiry and improve our services.','Sharing: we never sell your data; processors act under contract.','Your rights: access, correction and deletion via the contact page.','Cookies & analytics: used only after your consent.']}
TERMS={'ar':['هذا الموقع موقع تعريفي بالعلامة التجارية؛ لا تتم عمليات البيع عليه.','عمليات الشراء تتم لدى المتاجر الشريكة وتخضع لشروطها.','المعلومات المعروضة للإرشاد العام وقد تتغير.','جميع العلامات التجارية مملوكة لأصحابها.'],
'en':['This is a brand information site; no sales take place here.','Purchases happen at partner retailers under their own terms.','Information shown is general guidance and may change.','All trademarks belong to their respective owners.']}
def sub(l,k):
    a=l=='ar';h=page(l);title=SUB[k][0][0 if a else 1]
    start=h.index('<main>');end=h.index('</main>')+7
    if k=='contact':
        body=h[h.index('<section id="contact"'):h.index('</section></main>')+10]
    elif k=='about':
        body=f'<section><div class="wrap" style="max-width:820px"><h1>{title}</h1><p class="lead">{T[l]["abt"]}</p><img src="img/hero.jpg" alt="" style="border-radius:24px;margin:24px 0"><h2>{"رسالتنا" if a else "Our mission"}</h2><p>{"راحة الطفل وطمأنينة الأم في كل يوم. [نص افتراضي]" if a else "Comfort for babies and peace of mind for parents, every day. [Placeholder]"}</p></div></section>'
    else:
        items=(PRIV if k=='privacy' else TERMS)[l]
        body=f'<section><div class="wrap" style="max-width:820px"><h1>{title}</h1><p class="proto" style="border-radius:10px">{LEG[l]}</p><ol>{"".join(f"<li><p>{i}</p></li>" for i in items)}</ol><p class="small">{"آخر تحديث: —" if a else "Last updated: —"}</p></div></section>'
    h=h[:start]+'<main>'+body+'</main>'+h[end:]
    h=h.replace(f'<title>{T[l]["title"]}</title>',f'<title>{title} | {"بيبي جوي السعودية" if a else "BabyJoy Saudi Arabia"}</title>')
    h=h.replace('href="/"',f'href="/{k}.html"').replace('href="/en/"',f'href="/en/{k}.html"').replace(f'href="{T[l]["other"]}" hreflang',f'href="{T[l]["other"]}{k}.html" hreflang')
    h=h.replace('<a href="#"><img src','<a href="./"><img src').replace('<a href="#',f'<a href="./#').replace('href="./#" rel','href="#" rel')
    return h
import os
for l in ('ar','en'):
    for k in SUB:
        open(('' if l=='ar' else 'en/')+k+'.html','w').write(sub(l,k))
