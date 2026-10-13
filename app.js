const L=document.documentElement.lang,ar=L==='ar';
// PLACEHOLDER size data — must be verified against master SKU file
const D={olive:{tape:[['NB','0–5'],['S','4–8'],['M','6–11'],['L','9–14'],['XL','12–17']],pants:[['M','6–11'],['L','9–14'],['XL','12–17'],['XXL','15–25']]},
regular:{tape:[['1','2–5'],['2','3–8'],['3','6–11'],['4','9–14'],['5','12–17']],pants:[['3','6–11'],['4','TBC*'],['5','12–17'],['6','15–25']]}};
const f=document.getElementById('finder-form');
if(f){const go=()=>{const r=f.range.value,t=f.type.value,w=parseFloat(f.weight.value),out=document.getElementById('fres');
 if(!w){out.innerHTML=ar?'أدخل وزن طفلك لعرض المقاس المقترح.':'Enter your baby\'s weight to see a suggested size.';return}
 const hit=D[r][t].filter(([s,g])=>{const m=g.match(/([\d.]+)–([\d.]+)/);return m&&w>=+m[1]&&w<=+m[2]});
 const name={olive:ar?'بريميوم زيتون':'Premium Olive',regular:ar?'العادي':'Regular'}[r]+' '+(t==='tape'?(ar?'لاصق':'Tape'):(ar?'سروال':'Pants'));
 out.innerHTML=hit.length?`${ar?'المقاس المقترح':'Suggested size'}: <strong>${name} — ${hit.map(h=>h[0]).join(ar?' أو ':' or ')}</strong><br><span class="small" style="color:#cfd6ea">${ar?'بيانات تجريبية — يجب التحقق منها':'Placeholder data — to be verified'}${hit.length>1?(ar?' · عند التداخل اختر المقاس الأكبر إذا اقترب الطفل من الحد الأعلى':' · If between sizes, size up when near the upper limit'):''}</span>`:(ar?'لا يوجد مقاس مطابق في البيانات التجريبية لهذا الوزن.':'No matching size in placeholder data for this weight.');};
 f.addEventListener('input',go);f.addEventListener('submit',e=>{e.preventDefault();go()});go();}
document.querySelectorAll('.sizes').forEach(g=>g.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
 g.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));g.nextElementSibling.textContent=b.dataset.spec}));
document.querySelectorAll('.play').forEach(p=>p.addEventListener('click',()=>{p.textContent='⏸';p.setAttribute('aria-label','paused placeholder')}));
const c=document.getElementById('contact');if(c)c.addEventListener('submit',e=>{e.preventDefault();c.querySelector('.ok').hidden=false});
