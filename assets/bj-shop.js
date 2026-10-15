/* BabyJoy Shop Now picker (verified variant links/counts from BJV) */
(function(){
var V=window.BJV;if(!V)return;
var L=document.documentElement.lang.indexOf('ar')===0?'ar':'en',T=V.tx[L],P=V.prefix;
function el(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e}
function unit(c,t){return t==='pants'?T.pants_u:(c&&c.indexOf('wipes')===0?T.wipes_u:T.tape_u)}
function Picker(root){
  var st={c:root.dataset.c||'olive',t:root.dataset.t||'tape',s:root.dataset.s||'',fixed:root.dataset.fixed||''};
  var wipe=st.c.indexOf('wipes')===0;
  root.classList.add('bjp');root.innerHTML='';
  var ctr=el('div','bjp-ctrl');root.appendChild(ctr);
  var cards=el('div','bjp-cards');root.appendChild(cards);
  function seg(opts,cur,on,lbl){var g=el('div','bjp-seg');g.setAttribute('role','group');g.setAttribute('aria-label',lbl);
    opts.forEach(function(o){var b=el('button',null,o[1]);b.type='button';b.setAttribute('aria-pressed',o[0]===cur?'true':'false');if(o[2])b.disabled=true;b.onclick=function(){on(o[0])};g.appendChild(b)});return g}
  function sizes(){return ((V.sizes[st.c]||{})[st.t])||[]}
  function render(){
    ctr.innerHTML='';
    if(!wipe){
      if(st.fixed!=='line'){
        ctr.appendChild(seg([['olive',T.olive],['comp',T.comp],['s8',T.s8]],st.c,function(v){st.c=v;if(!sizes().length)st.t=st.t==='tape'?'pants':'tape';st.s='';render()},T.coll));
        var ty=[['tape',T.tape,!(V.sizes[st.c].tape||[]).length],['pants',T.pantsl,!(V.sizes[st.c].pants||[]).length]];
        ctr.appendChild(seg(ty,st.t,function(v){st.t=v;st.s='';render()},T.type));
      }
      var ss=sizes();if(!ss.some(function(x){return x[0]===st.s}))st.s=(ss[Math.min(2,ss.length-1)]||[''])[0];
      var sg=el('div','bjp-sizes');sg.setAttribute('role','group');sg.setAttribute('aria-label',T.size);
      ss.forEach(function(x){var b=el('button',null,'<b>'+x[0]+'</b>'+(x[1]?'<small><bdi dir="ltr">'+x[1]+'</bdi> '+T.kg+'</small>':''));b.type='button';b.setAttribute('aria-pressed',x[0]===st.s?'true':'false');b.onclick=function(){st.s=x[0];render();root.dispatchEvent(new CustomEvent('bjp:size',{detail:st.s}))};sg.appendChild(b)});
      if(st.fixed!=='line'){var lab=el('div','bjp-lbl',T.size);ctr.appendChild(lab);ctr.appendChild(sg)}
    }
    var key=wipe?st.c:st.c+'|'+st.t+'|'+st.s,vv=V.v[key]||{};
    cards.innerHTML='';
    V.ret[L].forEach(function(r){
      var c=el('div','bjp-card'),packs=vv[r.k]||[];
      c.appendChild(el('div','bjp-logo','<img src="'+P+r.logo+'" alt="'+r.n+'" loading="lazy">'));
      if(packs.length){
        var ul=el('div','bjp-packs');
        packs.slice(0,4).forEach(function(p){var a=el('a','bjp-pack','<span>'+p[0]+' '+unit(st.c,st.t)+'</span><b>'+T.shop+'</b>');a.href=p[1];a.target='_blank';a.rel='nofollow noopener';ul.appendChild(a)});
        c.appendChild(ul);
      }else{
        var a=el('a','bjp-pack bjp-gen','<span>'+T.all+'</span><b>'+T.shop+'</b>');a.href=r.url;a.target='_blank';a.rel='nofollow noopener';c.appendChild(a);
      }
      cards.appendChild(c);
    });
  }
  root._bjp={set:function(o){for(var k in o)st[k]=o[k];wipe=st.c.indexOf('wipes')===0;render()}};
  render();
}
document.querySelectorAll('[data-bjp]').forEach(Picker);
/* product page: keep picker in sync with the size buttons */
document.querySelectorAll('.bjx-sizes button').forEach(function(b){b.addEventListener('click',function(){var p=document.querySelector('[data-bjp]');if(p&&p._bjp)p._bjp.set({s:b.dataset.s})})});
/* drawer */
var d=document.getElementById('bjp-drawer');
if(d){var pk=d.querySelector('[data-bjp]'),last=null;
  function op(c,t){last=document.activeElement;pk._bjp.set({c:c,t:t,s:''});d.hidden=false;requestAnimationFrame(function(){d.classList.add('on')});document.body.style.overflow='hidden';d.querySelector('.bjp-x').focus()}
  function cl(){d.classList.remove('on');document.body.style.overflow='';setTimeout(function(){d.hidden=true},220);if(last)last.focus()}
  document.querySelectorAll('[data-bjp-open]').forEach(function(b){b.addEventListener('click',function(){var a=b.dataset.bjpOpen.split('|');op(a[0],a[1])})});
  d.addEventListener('click',function(e){if(e.target.closest('[data-close]'))cl()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!d.hidden)cl()});
}
})();
