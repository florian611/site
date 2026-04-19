import streamlit as st

st.set_page_config(
    page_title="Floxia Service ERP – Automatisation IA",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── TOUT en un seul st.markdown() ──────────────────────────────────────────────
# Streamlit ne peut pas mélanger st.columns() avec du HTML complexe.
# Solution : 100% HTML natif, zéro composant Streamlit sauf le slider ROI.

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.block-container{
  background:#080808!important;font-family:'DM Sans',sans-serif!important;color:#F0EDE6!important;}
#MainMenu,header,footer,[data-testid="stSidebar"],[data-testid="stToolbar"],
[data-testid="stDecoration"],[data-testid="stStatusWidget"],.stDeployButton{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}

@keyframes fadeUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.5);opacity:.4}}
@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
@keyframes glow{0%,100%{box-shadow:0 0 0 0 rgba(255,215,0,0)}50%{box-shadow:0 0 40px 6px rgba(255,215,0,.12)}}
.a1{animation:fadeUp .8s cubic-bezier(.16,1,.3,1) .05s both}
.a2{animation:fadeUp .8s cubic-bezier(.16,1,.3,1) .2s both}
.a3{animation:fadeUp .8s cubic-bezier(.16,1,.3,1) .35s both}
.a4{animation:fadeUp .8s cubic-bezier(.16,1,.3,1) .5s both}
.a5{animation:fadeUp .8s cubic-bezier(.16,1,.3,1) .65s both}

.nav{position:fixed;top:0;left:0;right:0;z-index:9999;display:flex;align-items:center;
  justify-content:space-between;padding:.85rem 5vw;
  background:rgba(8,8,8,.92);backdrop-filter:blur(24px);
  border-bottom:1px solid rgba(255,255,255,.05);}
.nav-logo{display:flex;align-items:center;gap:.55rem;font-family:'Syne',sans-serif;
  font-weight:800;font-size:1.15rem;letter-spacing:-.03em;color:#F0EDE6;text-decoration:none;}
.bolt{width:28px;height:28px;background:#FFD700;flex-shrink:0;
  clip-path:polygon(65% 0%,35% 45%,60% 45%,35% 100%,65% 55%,40% 55%);}
.nav-links{display:flex;gap:2rem;align-items:center;}
.nav-links a{font-size:.85rem;font-weight:500;color:#F0EDE6;text-decoration:none;opacity:.4;transition:opacity .2s;}
.nav-links a:hover{opacity:1;}
.nav-cta{background:#FFD700;color:#080808!important;padding:.5rem 1.3rem;border-radius:50px;
  font-size:.84rem;font-weight:700;text-decoration:none;opacity:1!important;transition:transform .15s,box-shadow .15s;}
.nav-cta:hover{transform:scale(1.05);box-shadow:0 4px 24px rgba(255,215,0,.4);}

.hero{min-height:100vh;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;padding:9rem 5vw 6rem;
  position:relative;overflow:hidden;background:#080808;}
.hero-orb{position:absolute;top:-15%;left:50%;transform:translateX(-50%);
  width:1000px;height:1000px;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle,rgba(255,215,0,.06) 0%,rgba(255,215,0,.02) 35%,transparent 65%);}
.hero-ring-a{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:750px;height:750px;border-radius:50%;border:1px solid rgba(255,215,0,.05);pointer-events:none;}
.hero-ring-b{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:520px;height:520px;border-radius:50%;border:1px solid rgba(255,215,0,.08);pointer-events:none;}
.hero>*{position:relative;z-index:1;}

.badge{display:inline-flex;align-items:center;gap:.5rem;
  background:rgba(255,215,0,.07);border:1px solid rgba(255,215,0,.18);
  color:#C8A600;font-size:.7rem;font-weight:700;letter-spacing:.13em;
  text-transform:uppercase;padding:.35rem 1rem;border-radius:50px;margin-bottom:2.2rem;}
.badge-dot{width:5px;height:5px;background:#FFD700;border-radius:50%;animation:pulse 2s infinite;}
.hero-title{font-family:'Syne',sans-serif;font-size:clamp(3rem,7vw,5.8rem);
  font-weight:800;line-height:1.01;letter-spacing:-.05em;color:#F0EDE6;max-width:950px;margin-bottom:1.6rem;}
.outline{-webkit-text-stroke:2px #FFD700;color:transparent;}
.hero-sub{font-size:clamp(.93rem,1.4vw,1.1rem);font-weight:300;color:rgba(240,237,230,.42);
  max-width:500px;line-height:1.82;margin-bottom:3rem;letter-spacing:.01em;}

.cta-row{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:5rem;}
.btn-y{background:#FFD700;color:#080808;padding:.9rem 2.4rem;border-radius:50px;font-weight:700;
  font-size:.95rem;border:none;text-decoration:none;display:inline-block;letter-spacing:.01em;
  transition:transform .2s,box-shadow .2s;animation:glow 3s ease-in-out infinite;}
.btn-y:hover{transform:translateY(-3px);box-shadow:0 14px 40px rgba(255,215,0,.42);}
.btn-g{background:rgba(255,255,255,.04);color:#F0EDE6;padding:.9rem 2.4rem;border-radius:50px;
  font-weight:500;font-size:.95rem;border:1px solid rgba(255,255,255,.1);
  text-decoration:none;display:inline-block;transition:border-color .2s,background .2s;}
.btn-g:hover{border-color:rgba(255,255,255,.28);background:rgba(255,255,255,.07);}

.stats-bar{display:flex;border:1px solid rgba(255,255,255,.07);border-radius:20px;
  overflow:hidden;background:rgba(255,255,255,.02);}
.stat-item{padding:1.4rem 2.5rem;border-right:1px solid rgba(255,255,255,.06);text-align:center;flex:1;}
.stat-item:last-child{border-right:none;}
.stat-n{font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:#FFD700;line-height:1;}
.stat-l{font-size:.71rem;color:rgba(240,237,230,.33);margin-top:.38rem;letter-spacing:.03em;}

.mq-wrap{overflow:hidden;padding:1.1rem 0;background:rgba(255,215,0,.04);
  border-top:1px solid rgba(255,215,0,.09);border-bottom:1px solid rgba(255,215,0,.09);}
.mq-track{display:flex;gap:3rem;width:max-content;animation:marquee 28s linear infinite;white-space:nowrap;}
.mq-item{font-size:.72rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;
  color:rgba(255,215,0,.48);display:flex;align-items:center;gap:.9rem;}
.mq-dot{width:3px;height:3px;background:#FFD700;border-radius:50%;opacity:.5;}

.sec{padding:7rem 5vw;max-width:1280px;margin:0 auto;}
.sec-lbl{font-size:.69rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:#C8A600;margin-bottom:.9rem;display:flex;align-items:center;gap:.6rem;}
.sec-lbl::before{content:'';width:18px;height:1px;background:#C8A600;}
.sec-title{font-family:'Syne',sans-serif;font-size:clamp(1.9rem,3.5vw,3.1rem);
  font-weight:800;letter-spacing:-.04em;line-height:1.1;margin-bottom:1rem;color:#F0EDE6;}
.sec-sub{font-size:.96rem;color:rgba(240,237,230,.38);max-width:450px;line-height:1.82;font-weight:300;}

.cgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;margin-top:4rem;
  border:1px solid rgba(255,255,255,.05);border-radius:24px;overflow:hidden;
  background:rgba(255,255,255,.05);}
@media(max-width:1100px){.cgrid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.cgrid{grid-template-columns:1fr;}}
.scard{background:#080808;padding:2.2rem;transition:background .3s;position:relative;overflow:hidden;}
.scard:hover{background:#0F0F0F;}
.scard::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,#FFD700,transparent);
  transform:scaleX(0);transform-origin:center;transition:transform .45s;}
.scard:hover::after{transform:scaleX(1);}
.cicon{width:44px;height:44px;background:rgba(255,215,0,.07);border:1px solid rgba(255,215,0,.14);
  border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;margin-bottom:1.4rem;}
.ctitle{font-family:'Syne',sans-serif;font-size:.98rem;font-weight:700;margin-bottom:.5rem;color:#F0EDE6;letter-spacing:-.01em;}
.cdesc{font-size:.84rem;color:rgba(240,237,230,.38);line-height:1.7;}
.ctag{display:inline-block;margin-top:1.1rem;font-size:.67rem;font-weight:700;letter-spacing:.06em;
  background:rgba(255,215,0,.06);color:#C8A600;padding:.22rem .72rem;border-radius:50px;border:1px solid rgba(255,215,0,.14);}

.div-line{height:1px;background:rgba(255,255,255,.04);}

/* ÉCOSYSTÈME — 2 colonnes HTML pur */
.eco-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;max-width:1280px;margin:0 auto;padding:7rem 5vw;}
@media(max-width:768px){.eco-grid{grid-template-columns:1fr;}}

.flow-sec{padding:0;}
.fblock{margin-bottom:1.8rem;}
.flbl{font-size:.63rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:rgba(240,237,230,.22);margin-bottom:.6rem;}
.fwrap{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.06);
  border-radius:13px;padding:1.1rem 1.3rem;transition:border-color .3s;}
.fwrap:hover{border-color:rgba(255,215,0,.16);}
.frow{display:flex;align-items:center;gap:.55rem;flex-wrap:wrap;}
.fn{display:inline-flex;align-items:center;background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.07);border-radius:8px;padding:.38rem .78rem;
  font-size:.77rem;font-weight:600;color:rgba(240,237,230,.65);white-space:nowrap;}
.fn.g{background:rgba(255,215,0,.07);border-color:rgba(255,215,0,.2);color:#C8A600;}
.fn.e{background:#FFD700;color:#080808;border-color:#FFD700;font-weight:700;}
.fa{color:rgba(255,255,255,.18);font-size:.82rem;flex-shrink:0;}

.stepn{width:42px;height:42px;border-radius:50%;background:rgba(255,215,0,.07);
  border:1px solid rgba(255,215,0,.18);color:#FFD700;font-family:'Syne',sans-serif;
  font-weight:800;font-size:.92rem;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.steptitle{font-family:'Syne',sans-serif;font-weight:700;font-size:.93rem;margin-bottom:.22rem;color:#F0EDE6;}
.stepdesc{font-size:.81rem;color:rgba(240,237,230,.35);line-height:1.68;}

/* ROI — 2 colonnes HTML pur */
.roi-grid-outer{display:grid;grid-template-columns:1fr 1fr;gap:4rem;max-width:1280px;margin:0 auto;padding:0 5vw 7rem;}
@media(max-width:768px){.roi-grid-outer{grid-template-columns:1fr;}}
.roi-box{background:rgba(255,255,255,.03);border:1px solid rgba(255,215,0,.1);
  border-radius:22px;padding:2.6rem;position:relative;overflow:hidden;}
.roi-slbl{font-size:.68rem;letter-spacing:.13em;text-transform:uppercase;color:rgba(240,237,230,.3);margin-bottom:.8rem;}
.roi-res{background:rgba(255,215,0,.05);border:1px solid rgba(255,215,0,.13);
  border-radius:14px;padding:1.5rem 1.8rem;margin-top:1.8rem;}
.roi-nums{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;}
.roi-val{font-family:'Syne',sans-serif;font-size:1.95rem;font-weight:800;color:#FFD700;letter-spacing:-.03em;}
.roi-lbl{font-size:.7rem;color:rgba(240,237,230,.3);margin-top:.28rem;letter-spacing:.03em;}
.roi-note{font-size:.66rem;color:rgba(240,237,230,.16);margin-top:.9rem;}

.task-item{display:flex;justify-content:space-between;align-items:center;
  padding:.72rem .95rem;background:rgba(255,255,255,.025);
  border:1px solid rgba(255,255,255,.055);border-radius:9px;margin-bottom:.6rem;}
.task-name{font-size:.8rem;color:rgba(240,237,230,.27);text-decoration:line-through;}
.task-gain{font-size:.7rem;font-weight:700;color:#C8A600;background:rgba(255,215,0,.06);
  border:1px solid rgba(255,215,0,.13);padding:.16rem .58rem;border-radius:50px;white-space:nowrap;margin-left:.7rem;}

/* TARIFS — 3 colonnes HTML pur */
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.1rem;margin-top:3.5rem;}
@media(max-width:900px){.pgrid{grid-template-columns:1fr;}}
.pcard{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.07);
  border-radius:20px;padding:2.1rem;transition:transform .25s,border-color .25s;}
.pcard:hover{transform:translateY(-4px);border-color:rgba(255,215,0,.18);}
.pcard.feat{background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.22);}
.pcard.feat:hover{border-color:rgba(255,215,0,.42);}
.pbadge{display:inline-block;font-size:.65rem;font-weight:700;letter-spacing:.1em;
  text-transform:uppercase;background:rgba(255,215,0,.09);color:#C8A600;
  padding:.22rem .72rem;border-radius:50px;margin-bottom:.9rem;border:1px solid rgba(255,215,0,.18);}
.pplan{font-family:'Syne',sans-serif;font-weight:700;font-size:.98rem;margin-bottom:.45rem;color:#F0EDE6;}
.phighlight{background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.13);
  border-radius:10px;padding:.75rem .95rem;margin-bottom:1.1rem;font-size:.81rem;color:#C8A600;line-height:1.5;}
.pprice{font-family:'Syne',sans-serif;font-size:2.9rem;font-weight:800;
  letter-spacing:-.05em;line-height:1;color:#F0EDE6;margin:.65rem 0 .28rem;}
.pcard.feat .pprice{color:#FFD700;}
.pper{font-size:.74rem;color:rgba(240,237,230,.28);margin-bottom:1.5rem;}
.pfeats{display:flex;flex-direction:column;gap:.6rem;margin-bottom:1.8rem;}
.pfeat{display:flex;align-items:flex-start;gap:.6rem;font-size:.83rem;color:rgba(240,237,230,.5);line-height:1.5;}
.pcheck{color:#FFD700;font-size:.78rem;flex-shrink:0;margin-top:.1rem;}
.pcta{display:block;text-align:center;padding:.78rem 1.4rem;border-radius:50px;
  font-weight:700;font-size:.87rem;text-decoration:none;transition:all .2s;letter-spacing:.02em;}
.pcta-o{border:1px solid rgba(255,255,255,.12);color:#F0EDE6;}
.pcta-o:hover{border-color:rgba(255,215,0,.38);color:#FFD700;}
.pcta-s{background:#FFD700;color:#080808;border:none;font-weight:800;}
.pcta-s:hover{box-shadow:0 8px 32px rgba(255,215,0,.42);transform:translateY(-1px);}
.pnote{font-size:.68rem;text-align:center;color:rgba(240,237,230,.18);margin-top:.85rem;}

.cta-band{background:#FFD700;padding:6rem 5vw;text-align:center;}
.cta-band h2{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,4.5vw,3.8rem);
  font-weight:800;letter-spacing:-.04em;color:#080808;margin-bottom:2.8rem;line-height:1.08;}
.ibtn{display:inline-flex;align-items:center;gap:.75rem;background:#080808;color:#FFD700;
  font-family:'DM Sans',sans-serif;font-weight:700;font-size:1rem;
  padding:1rem 2.6rem;border-radius:50px;text-decoration:none;transition:transform .2s,box-shadow .2s;}
.ibtn:hover{transform:translateY(-3px);box-shadow:0 12px 40px rgba(0,0,0,.35);}

.ft{padding:2.4rem 5vw;display:flex;align-items:center;justify-content:space-between;
  flex-wrap:wrap;gap:1.5rem;background:#080808;border-top:1px solid rgba(255,255,255,.04);}
.ft-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:.98rem;
  letter-spacing:-.03em;display:flex;align-items:center;gap:.5rem;color:#F0EDE6;}
.ft-tag{font-size:.74rem;color:rgba(240,237,230,.22);margin-top:.28rem;}
.ft-links{display:flex;gap:2rem;}
.ft-links a{font-size:.76rem;color:rgba(240,237,230,.28);text-decoration:none;}
.ft-links a:hover{color:#FFD700;}
.ft-badge{font-size:.68rem;background:rgba(255,215,0,.07);color:#C8A600;
  padding:.25rem .75rem;border-radius:50px;font-weight:700;border:1px solid rgba(255,215,0,.14);}
</style>

<!-- NAV -->
<nav class="nav">
  <a class="nav-logo" href="#"><div class="bolt"></div>Floxia Service ERP</a>
  <div class="nav-links">
    <a href="#services">Services</a>
    <a href="#ecosystem">&#201;cosyst&#232;me</a>
    <a href="#roi">ROI</a>
    <a href="#tarifs">Tarifs</a>
    <a href="https://www.instagram.com/floxia.pro/" target="_blank" class="nav-cta">D&#233;mo gratuite &#8594;</a>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-orb"></div>
  <div class="hero-ring-a"></div>
  <div class="hero-ring-b"></div>
  <div class="badge a1"><div class="badge-dot"></div>IA pour artisans &amp; PME du b&#226;timent</div>
  <h1 class="hero-title a2">Votre admin.<br><span class="outline">Automatis&#233;e.</span><br>Votre temps. Rendu.</h1>
  <p class="hero-sub a3">Floxia connecte WhatsApp, l'IA et votre ERP pour g&#233;rer devis, PV de r&#233;ception, factures, relances et rapports chantier &#8212; depuis votre t&#233;l&#233;phone.</p>
  <div class="cta-row a4">
    <a class="btn-y" href="https://www.instagram.com/floxia.pro/" target="_blank">&#x26A1; R&#233;server une d&#233;mo gratuite</a>
    <a class="btn-g" href="#services">D&#233;couvrir les services</a>
  </div>
  <div class="stats-bar a5">
    <div class="stat-item"><div class="stat-n">16h</div><div class="stat-l">gagn&#233;es / mois</div></div>
    <div class="stat-item"><div class="stat-n">&#8722;80%</div><div class="stat-l">de saisie admin</div></div>
    <div class="stat-item"><div class="stat-n">3min</div><div class="stat-l">devis &#8594; facture finale</div></div>
    <div class="stat-item"><div class="stat-n">100%</div><div class="stat-l">sur WhatsApp</div></div>
  </div>
</section>

<!-- MARQUEE -->
<div class="mq-wrap"><div class="mq-track">
  <div class="mq-item"><div class="mq-dot"></div>Devis vocal en 3&#160;min</div>
  <div class="mq-item"><div class="mq-dot"></div>PV de r&#233;ception auto</div>
  <div class="mq-item"><div class="mq-dot"></div>Facture finale automatis&#233;e</div>
  <div class="mq-item"><div class="mq-dot"></div>Scan tickets de caisse</div>
  <div class="mq-item"><div class="mq-dot"></div>Avis Google Maps auto</div>
  <div class="mq-item"><div class="mq-dot"></div>Relances intelligentes</div>
  <div class="mq-item"><div class="mq-dot"></div>Planning salari&#233;s</div>
  <div class="mq-item"><div class="mq-dot"></div>Rapports chantier PDF</div>
  <div class="mq-item"><div class="mq-dot"></div>ERP 100% mobile</div>
  <div class="mq-item"><div class="mq-dot"></div>Devis vocal en 3&#160;min</div>
  <div class="mq-item"><div class="mq-dot"></div>PV de r&#233;ception auto</div>
  <div class="mq-item"><div class="mq-dot"></div>Facture finale automatis&#233;e</div>
  <div class="mq-item"><div class="mq-dot"></div>Scan tickets de caisse</div>
  <div class="mq-item"><div class="mq-dot"></div>Avis Google Maps auto</div>
  <div class="mq-item"><div class="mq-dot"></div>Relances intelligentes</div>
  <div class="mq-item"><div class="mq-dot"></div>Planning salari&#233;s</div>
  <div class="mq-item"><div class="mq-dot"></div>Rapports chantier PDF</div>
  <div class="mq-item"><div class="mq-dot"></div>ERP 100% mobile</div>
</div></div>

<!-- SERVICES -->
<div id="services" style="background:#080808;">
<div class="sec">
  <div class="sec-lbl">Ce que fait Floxia Service ERP</div>
  <h2 class="sec-title">Tout votre flux de travail,<br>automatis&#233; de A &#224; Z.</h2>
  <p class="sec-sub">Des automatisations concr&#232;tes, op&#233;rationnelles d&#232;s aujourd'hui.</p>
  <div class="cgrid">
    <div class="scard"><div class="cicon">&#x1F4AC;</div><div class="ctitle">Devis &#8594; PV &#8594; Facture</div><div class="cdesc">Un vocal WhatsApp suffit. Floxia g&#233;n&#232;re le devis PDF, le client signe, vous &#233;mettez le PV de r&#233;ception, et la facture finale se cr&#233;e automatiquement.</div><span class="ctag">&#x26A1; Cycle complet g&#233;r&#233;</span></div>
    <div class="scard"><div class="cicon">&#x1F4F8;</div><div class="ctitle">Scan Tickets de Caisse</div><div class="cdesc">Photographiez vos tickets sur WhatsApp. L'IA extrait fournisseur, articles, montants HT/TVA et alimente votre comptabilit&#233; instantan&#233;ment.</div><span class="ctag">&#x26A1; Z&#233;ro ressaisie</span></div>
    <div class="scard"><div class="cicon">&#x2B50;</div><div class="ctitle">Avis Google Maps</div><div class="cdesc">&#192; chaque chantier termin&#233;, Floxia envoie un message WhatsApp au client pour l'inviter &#224; laisser un avis Google. Plus d'avis, meilleure r&#233;putation.</div><span class="ctag">&#x26A1; R&#233;putation boost&#233;e</span></div>
    <div class="scard"><div class="cicon">&#x1F6A8;</div><div class="ctitle">Alerte Probl&#232;me Chantier</div><div class="cdesc">Un probl&#232;me sur le chantier&#160;? Envoyez un vocal. Floxia r&#233;dige l'e-mail professionnel au client&#160;: situation, causes, nouveau d&#233;lai.</div><span class="ctag">&#x26A1; Email client en 30&#160;sec</span></div>
    <div class="scard"><div class="cicon">&#x1F514;</div><div class="ctitle">Relances Automatiques</div><div class="cdesc">Floxia surveille vos devis non sign&#233;s et relance automatiquement par SMS et e-mail au bon moment. Plus jamais un devis oubli&#233;.</div><span class="ctag">&#x26A1; +30&#160;% de conversion</span></div>
    <div class="scard"><div class="cicon">&#x1F4CB;</div><div class="ctitle">ERP Mobile Complet</div><div class="cdesc">Devis, factures, PV, chantiers, planning, salari&#233;s, d&#233;penses &#8212; tout synchronis&#233; en temps r&#233;el avec Google Sheets, accessible depuis n'importe quel &#233;cran.</div><span class="ctag">&#x26A1; Tout en un seul endroit</span></div>
    <div class="scard"><div class="cicon">&#x1F399;</div><div class="ctitle">Rapports Vocaux Chantier</div><div class="cdesc">Dictez votre rapport de fin de journ&#233;e en 2&#160;minutes. Floxia le structure et l'envoie au client sous forme de compte-rendu professionnel.</div><span class="ctag">&#x26A1; Rapport en 2&#160;min</span></div>
    <div class="scard"><div class="cicon">&#x1F4B0;</div><div class="ctitle">Suivi D&#233;penses &amp; TVA</div><div class="cdesc">Chaque ticket scann&#233; alimente votre tableau de bord&#160;: d&#233;penses par cat&#233;gorie, TVA r&#233;cup&#233;rable, r&#233;sultat net et export comptable en 1&#160;clic.</div><span class="ctag">&#x26A1; Compta simplifi&#233;e</span></div>
  </div>
</div>
</div>

<div class="div-line"></div>

<!-- ÉCOSYSTÈME -->
<div id="ecosystem" style="background:#080808;">
<div class="eco-grid">
  <div>
    <div class="sec-lbl">Comment &#231;a marche</div>
    <h2 class="sec-title">WhatsApp comme<br>centre de commandes.</h2>
    <p class="sec-sub" style="margin-bottom:2.8rem;">Tout part de votre t&#233;l&#233;phone. Aucun logiciel &#224; apprendre. Floxia fait le reste.</p>
    <div style="display:flex;flex-direction:column;gap:1.5rem;">
      <div style="display:flex;align-items:flex-start;gap:1.1rem;">
        <div class="stepn">1</div>
        <div><div class="steptitle">Une fois connect&#233;</div><div class="stepdesc">WhatsApp Business, Gmail, Google Drive &#8212; tout est pr&#234;t, on s'en occupe.</div></div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:1.1rem;">
        <div class="stepn">2</div>
        <div><div class="steptitle">Parlez ou photographiez</div><div class="stepdesc">Vocal ou photo sur WhatsApp. Floxia comprend et agit instantan&#233;ment.</div></div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:1.1rem;">
        <div class="stepn">3</div>
        <div><div class="steptitle">L'IA travaille pour vous</div><div class="stepdesc">Devis envoy&#233;, PV g&#233;n&#233;r&#233;, facture &#233;mise, ticket enregistr&#233;. Automatiquement.</div></div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:1.1rem;">
        <div class="stepn">4</div>
        <div><div class="steptitle">Pilotez depuis l'ERP</div><div class="stepdesc">Tableau de bord temps r&#233;el&#160;: CA, planning, salari&#233;s, d&#233;penses, facturation.</div></div>
      </div>
    </div>
  </div>
  <div class="flow-sec">
    <div class="fblock">
      <div class="flbl">Flux 1 &#8212; Cycle devis complet</div>
      <div class="fwrap"><div class="frow">
        <div class="fn">&#x1F399; Vocal WA</div><div class="fa">&#8594;</div>
        <div class="fn g">&#x26A1; IA Floxia</div><div class="fa">&#8594;</div>
        <div class="fn">&#x1F4C4; Devis PDF</div><div class="fa">&#8594;</div>
        <div class="fn">&#x270D; Signature</div><div class="fa">&#8594;</div>
        <div class="fn">&#x1F4CB; PV R&#233;ception</div><div class="fa">&#8594;</div>
        <div class="fn e">&#x1F9FE; Facture finale</div>
      </div></div>
    </div>
    <div class="fblock">
      <div class="flbl">Flux 2 &#8212; Avis Google Maps</div>
      <div class="fwrap"><div class="frow">
        <div class="fn">&#x2705; Chantier termin&#233;</div><div class="fa">&#8594;</div>
        <div class="fn g">&#x26A1; Floxia d&#233;tecte</div><div class="fa">&#8594;</div>
        <div class="fn">&#x1F4AC; Message WA</div><div class="fa">&#8594;</div>
        <div class="fn e">&#x2B50; Avis Google</div>
      </div></div>
    </div>
    <div class="fblock">
      <div class="flbl">Flux 3 &#8212; Ticket de caisse</div>
      <div class="fwrap"><div class="frow">
        <div class="fn">&#x1F4F8; Photo WA</div><div class="fa">&#8594;</div>
        <div class="fn g">&#x26A1; OCR IA</div><div class="fa">&#8594;</div>
        <div class="fn">&#x1F4CA; Google Sheets</div><div class="fa">&#8594;</div>
        <div class="fn e">&#x2705; Compta</div>
      </div></div>
    </div>
    <div class="fblock">
      <div class="flbl">Flux 4 &#8212; Probl&#232;me chantier</div>
      <div class="fwrap"><div class="frow">
        <div class="fn">&#x1F6A8; Vocal WA</div><div class="fa">&#8594;</div>
        <div class="fn g">&#x26A1; IA r&#233;daction</div><div class="fa">&#8594;</div>
        <div class="fn e">&#x1F4E7; Email client</div>
      </div></div>
    </div>
    <div class="fblock">
      <div class="flbl">Flux 5 &#8212; Relances devis</div>
      <div class="fwrap"><div class="frow">
        <div class="fn">&#x23F0; D&#233;lai d&#233;pass&#233;</div><div class="fa">&#8594;</div>
        <div class="fn g">&#x26A1; Floxia d&#233;tecte</div><div class="fa">&#8594;</div>
        <div class="fn e">&#x1F4AC; SMS + Email</div>
      </div></div>
    </div>
  </div>
</div>
</div>

<div class="div-line"></div>

<!-- ROI HEADER -->
<div id="roi" style="background:#080808;">
<div class="sec" style="padding-bottom:2rem;">
  <div class="sec-lbl">Simulateur ROI</div>
  <h2 class="sec-title">Calculez votre<br>temps lib&#233;r&#233;.</h2>
  <p class="sec-sub">Bougez le curseur &#8212; voyez ce que Floxia vous rapporte chaque mois.</p>
</div>
</div>
""", unsafe_allow_html=True)

# ── SLIDER ROI — seul composant Streamlit ────────────────────────────────────
st.markdown("""
<style>
div[data-testid="stSlider"]{padding:0 5vw;max-width:1280px;margin:0 auto;}
div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"]{
  background:#FFD700!important;border:none!important;box-shadow:0 0 0 4px rgba(255,215,0,.2)!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:nth-child(2){background:#FFD700!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:first-child{background:rgba(255,255,255,.08)!important;}
div[data-testid="stSlider"] label{color:rgba(240,237,230,.3)!important;font-size:.68rem!important;letter-spacing:.13em!important;text-transform:uppercase!important;}
</style>
""", unsafe_allow_html=True)

nb_devis = st.slider("Nombre de devis par mois", min_value=1, max_value=80, value=15, step=1)

h = round(((64 - 3) * nb_devis + nb_devis * 12) / 60, 1)
g = round(h * 55)
if nb_devis <= 10: abo, plan = 49, "Starter"
elif nb_devis <= 30: abo, plan = 99, "Pro"
else: abo, plan = 149, "Expert"
roi = round((g / abo) * 100)

st.markdown(f"""
<div style="background:#080808;">
<div class="roi-grid-outer">
  <div class="roi-box">
    <div class="roi-slbl">R&#233;sultats pour {nb_devis} devis / mois</div>
    <div class="roi-res">
      <div class="roi-nums">
        <div><div class="roi-val">{h}h</div><div class="roi-lbl">temps lib&#233;r&#233;</div></div>
        <div><div class="roi-val">{g}&#8364;</div><div class="roi-lbl">valeur r&#233;cup&#233;r&#233;e</div></div>
        <div><div class="roi-val">{roi}%</div><div class="roi-lbl">ROI mensuel</div></div>
      </div>
    </div>
    <div class="roi-note">*55&#8364;/h artisan &#183; Plan {plan} &#224; {abo}&#8364;/mois pour {nb_devis} devis.</div>
  </div>
  <div>
    <div class="sec-lbl" style="margin-bottom:1.2rem;">Ce que vous ne faites plus</div>
    <div class="task-item"><div class="task-name">Taper des devis le soir</div><div class="task-gain">45&#160;min &#233;vit&#233;es / devis</div></div>
    <div class="task-item"><div class="task-name">Ressaisir les tickets de caisse</div><div class="task-gain">2h / semaine r&#233;cup&#233;r&#233;es</div></div>
    <div class="task-item"><div class="task-name">R&#233;diger des e-mails clients</div><div class="task-gain">30&#160;min / incident</div></div>
    <div class="task-item"><div class="task-name">Relancer les devis manuellement</div><div class="task-gain">+30% de conversion</div></div>
    <div class="task-item"><div class="task-name">Faire le planning &#224; la main</div><div class="task-gain">1h / semaine gagn&#233;e</div></div>
    <div class="task-item"><div class="task-name">Exporter votre compta</div><div class="task-gain">Export 1&#160;clic</div></div>
    <div class="task-item"><div class="task-name">R&#233;diger les rapports chantier</div><div class="task-gain">2&#160;min au lieu de 20</div></div>
    <div class="task-item"><div class="task-name">Demander des avis Google</div><div class="task-gain">Automatique &#224; chaque chantier</div></div>
    <div class="task-item"><div class="task-name">G&#233;n&#233;rer un PV de r&#233;ception</div><div class="task-gain">Auto apr&#232;s signature</div></div>
  </div>
</div>
</div>

<div class="div-line"></div>

<!-- TARIFS -->
<div id="tarifs" style="background:#080808;">
<div class="sec">
  <div class="sec-lbl">Tarifs</div>
  <h2 class="sec-title">Un prix qui s'adapte<br>&#224; votre activit&#233;.</h2>
  <p class="sec-sub">Payez selon vos devis g&#233;n&#233;r&#233;s. Plus vous travaillez, plus Floxia vous fait &#233;conomiser.</p>
  <div class="pgrid">
    <div class="pcard">
      <div class="pbadge">Starter</div>
      <div class="pplan">Pour d&#233;marrer</div>
      <div class="phighlight">&#x26A1; Jusqu'&#224; <strong style="color:#FFD700;">10 devis / mois</strong></div>
      <div class="pprice">49&#8364;</div>
      <div class="pper">par mois &#183; sans engagement</div>
      <div class="pfeats">
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Devis WhatsApp vocal</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Cycle devis &#8594; PV &#8594; facture</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Scan tickets de caisse</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Relances automatiques</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Avis Google Maps auto</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>ERP mobile (Google Sheets)</div>
      </div>
      <a class="pcta pcta-o" href="https://www.instagram.com/floxia.pro/" target="_blank">D&#233;marrer &#8594;</a>
      <div class="pnote">Id&#233;al pour les artisans solo</div>
    </div>
    <div class="pcard feat">
      <div class="pbadge">&#x26A1; Le plus populaire &#8212; Pro</div>
      <div class="pplan">Pour les actifs</div>
      <div class="phighlight">&#x26A1; Jusqu'&#224; <strong style="color:#FFD700;">30 devis / mois</strong></div>
      <div class="pprice">99&#8364;</div>
      <div class="pper">par mois &#183; sans engagement</div>
      <div class="pfeats">
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Tout du plan Starter</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Alertes probl&#232;me chantier</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Rapports vocaux PDF</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Planning &amp; salari&#233;s</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Suivi d&#233;penses &amp; TVA</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Support prioritaire WhatsApp</div>
      </div>
      <a class="pcta pcta-s" href="https://www.instagram.com/floxia.pro/" target="_blank">Choisir Pro &#8594;</a>
      <div class="pnote">Le meilleur rapport qualit&#233; / valeur</div>
    </div>
    <div class="pcard">
      <div class="pbadge">Expert</div>
      <div class="pplan">Pour les &#233;quipes</div>
      <div class="phighlight">&#x26A1; <strong style="color:#FFD700;">Devis illimit&#233;s</strong></div>
      <div class="pprice">149&#8364;</div>
      <div class="pper">par mois &#183; sans engagement</div>
      <div class="pfeats">
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Tout du plan Pro</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Devis illimit&#233;s</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Multi-utilisateurs (&#233;quipe)</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Tableaux de bord avanc&#233;s</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Int&#233;grations sur mesure</div>
        <div class="pfeat"><span class="pcheck">&#x2736;</span>Accompagnement d&#233;di&#233;</div>
      </div>
      <a class="pcta pcta-o" href="https://www.instagram.com/floxia.pro/" target="_blank">Nous contacter &#8594;</a>
      <div class="pnote">Pour les PME et &#233;quipes terrain</div>
    </div>
  </div>
</div>
</div>

<!-- CTA FINAL -->
<div id="contact" class="cta-band">
  <h2>Pr&#234;t &#224; r&#233;cup&#233;rer<br>votre temps&#160;?</h2>
  <a class="ibtn" href="https://www.instagram.com/floxia.pro/" target="_blank">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
      <rect x="2" y="2" width="20" height="20" rx="5" stroke="#FFD700" stroke-width="1.8"/>
      <circle cx="12" cy="12" r="4.5" stroke="#FFD700" stroke-width="1.8"/>
      <circle cx="17.5" cy="6.5" r="1" fill="#FFD700"/>
    </svg>
    R&#233;server une d&#233;mo &#8212; Instagram
  </a>
  <div style="margin-top:1.1rem;font-size:.74rem;color:rgba(8,8,8,.4);font-weight:500;">
    @floxia.pro &#183; R&#233;ponse sous 24h
  </div>
</div>

<!-- FOOTER -->
<footer class="ft">
  <div>
    <div class="ft-logo"><div class="bolt" style="width:20px;height:20px;"></div>Floxia Service ERP</div>
    <div class="ft-tag">L'IA qui travaille &#224; votre place.</div>
  </div>
  <div class="ft-links">
    <a href="#">Mentions l&#233;gales</a>
    <a href="#">Confidentialit&#233;</a>
    <a href="https://www.instagram.com/floxia.pro/" target="_blank">Instagram</a>
  </div>
  <div class="ft-badge">&#x26A1; Propuls&#233; par l'IA</div>
</footer>
""", unsafe_allow_html=True)
