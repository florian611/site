import streamlit as st

st.set_page_config(
    page_title=\"Floxia – Devis & Factures depuis WhatsApp en 3 min\",
    page_icon=\"⚡\",
    layout=\"wide\",
    initial_sidebar_state=\"collapsed\",
)

INSTA = \"https://www.instagram.com/floxia.pro/\"

CSS = \"\"\"
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body,[data-testid=\"stAppViewContainer\"],[data-testid=\"stMain\"],.main,.block-container{
  background:#080808!important;font-family:'DM Sans',sans-serif!important;color:#F0EDE6!important;}
#MainMenu,header,footer,[data-testid=\"stSidebar\"],[data-testid=\"stToolbar\"],
[data-testid=\"stDecoration\"],[data-testid=\"stStatusWidget\"],.stDeployButton{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}

@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
@keyframes pulseDot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(1.5)}}
@keyframes fadeIn{from{opacity:0;transform:translateY(32px)}to{opacity:1;transform:translateY(0)}}
@keyframes scanline{0%{top:-10%}100%{top:110%}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}

/* SCROLL REVEAL */
.reveal{opacity:0;transform:translateY(40px);transition:opacity .9s cubic-bezier(.22,1,.36,1),transform .9s cubic-bezier(.22,1,.36,1);}
.reveal.in{opacity:1;transform:translateY(0);}
.reveal-left{opacity:0;transform:translateX(-40px);transition:opacity .9s cubic-bezier(.22,1,.36,1),transform .9s cubic-bezier(.22,1,.36,1);}
.reveal-left.in{opacity:1;transform:translateX(0);}
.reveal-right{opacity:0;transform:translateX(40px);transition:opacity .9s cubic-bezier(.22,1,.36,1),transform .9s cubic-bezier(.22,1,.36,1);}
.reveal-right.in{opacity:1;transform:translateX(0);}
.reveal-scale{opacity:0;transform:scale(.92);transition:opacity .9s cubic-bezier(.22,1,.36,1),transform .9s cubic-bezier(.22,1,.36,1);}
.reveal-scale.in{opacity:1;transform:scale(1);}
.reveal-stagger > *{opacity:0;transform:translateY(30px);transition:opacity .7s cubic-bezier(.22,1,.36,1),transform .7s cubic-bezier(.22,1,.36,1);}
.reveal-stagger.in > *{opacity:1;transform:translateY(0);}
.reveal-stagger.in > *:nth-child(1){transition-delay:.05s}
.reveal-stagger.in > *:nth-child(2){transition-delay:.12s}
.reveal-stagger.in > *:nth-child(3){transition-delay:.19s}
.reveal-stagger.in > *:nth-child(4){transition-delay:.26s}
.reveal-stagger.in > *:nth-child(5){transition-delay:.33s}
.reveal-stagger.in > *:nth-child(6){transition-delay:.40s}
.reveal-stagger.in > *:nth-child(7){transition-delay:.47s}
.reveal-stagger.in > *:nth-child(8){transition-delay:.54s}
.reveal-stagger.in > *:nth-child(9){transition-delay:.61s}

/* NAV */
.nav{position:fixed;top:0;left:0;right:0;z-index:9999;display:flex;align-items:center;
  justify-content:space-between;padding:1rem 5vw;background:rgba(8,8,8,.92);backdrop-filter:blur(20px);
  border-bottom:1px solid rgba(255,255,255,.04);}
.nav-logo{display:flex;align-items:center;gap:.6rem;font-family:'Syne',sans-serif;
  font-weight:900;font-size:1.1rem;letter-spacing:-.04em;color:#F0EDE6;text-decoration:none;}
.bolt{width:26px;height:26px;background:#FFD700;flex-shrink:0;
  clip-path:polygon(65% 0%,35% 45%,60% 45%,35% 100%,65% 55%,40% 55%);}
.nav-links{display:flex;gap:2.2rem;align-items:center;}
.nav-links a{font-size:.78rem;font-weight:500;color:rgba(240,237,230,.38);
  text-decoration:none;letter-spacing:.06em;text-transform:uppercase;cursor:pointer;transition:color .2s;}
.nav-links a:hover{color:#F0EDE6;}
.nav-cta{background:#FFD700!important;color:#080808!important;padding:.46rem 1.2rem;
  border-radius:50px;font-size:.78rem;font-weight:700;text-decoration:none;transition:transform .15s,box-shadow .15s;}
.nav-cta:hover{transform:scale(1.05);box-shadow:0 4px 24px rgba(255,215,0,.45);}

/* HERO */
.hero{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:8rem 6vw 6rem;position:relative;overflow:hidden;background:#080808;}
.hero-grid{position:absolute;inset:0;
  background-image:linear-gradient(rgba(255,215,0,.025) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,215,0,.025) 1px,transparent 1px);
  background-size:70px 70px;pointer-events:none;}
.hero-scan{position:absolute;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,215,0,.12),transparent);
  animation:scanline 5s linear infinite;pointer-events:none;}
.hero-orb{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:700px;height:700px;
  border-radius:50%;pointer-events:none;background:radial-gradient(circle,rgba(255,215,0,.07) 0%,transparent 60%);}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;font-size:.64rem;font-weight:700;
  letter-spacing:.22em;text-transform:uppercase;color:rgba(255,215,0,.55);margin-bottom:1.5rem;animation:fadeIn .7s ease .1s both;}
.hero-badge-dot{width:4px;height:4px;background:#FFD700;border-radius:50%;animation:pulseDot 2s infinite;}
.hero-title{font-family:'Syne',sans-serif;font-weight:900;line-height:.92;letter-spacing:-.06em;
  color:#F0EDE6;font-size:clamp(2.8rem,8vw,7.5rem);margin-bottom:1.5rem;animation:fadeIn .7s ease .2s both;}
.hero-title .outline{-webkit-text-stroke:2px #FFD700;color:transparent;}
.hero-sub{font-size:clamp(1rem,2.2vw,1.25rem);color:rgba(240,237,230,.52);font-weight:300;
  max-width:560px;margin:0 auto 2.2rem;line-height:1.7;animation:fadeIn .7s ease .35s both;}
.hero-sub strong{color:#FFD700;font-weight:600;}
.hero-info{display:flex;align-items:center;justify-content:center;gap:2.5rem;margin-bottom:2.5rem;flex-wrap:wrap;animation:fadeIn .7s ease .5s both;}
.hero-info-item{display:flex;flex-direction:column;gap:.18rem;align-items:center;}
.hero-info-label{font-size:.56rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(240,237,230,.22);}
.hero-info-val{font-family:'Syne',sans-serif;font-size:.9rem;font-weight:700;color:#F0EDE6;}
.hero-sep{width:1px;height:36px;background:rgba(255,255,255,.08);}
.hero-cta-row{display:flex;gap:1rem;align-items:center;justify-content:center;flex-wrap:wrap;animation:fadeIn .7s ease .7s both;}
.btn-y{background:#FFD700;color:#080808;padding:.82rem 2rem;border-radius:50px;font-weight:700;
  font-size:.88rem;text-decoration:none;display:inline-block;transition:transform .2s,box-shadow .2s;}
.btn-y:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(255,215,0,.42);}

/* MARQUEE */
.mq-wrap{overflow:hidden;padding:.85rem 0;border-top:1px solid rgba(255,215,0,.06);border-bottom:1px solid rgba(255,215,0,.06);}
.mq-track{display:flex;gap:2.5rem;width:max-content;animation:marquee 32s linear infinite;}
.mq-item{font-size:.62rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:rgba(255,215,0,.3);display:flex;align-items:center;gap:.75rem;white-space:nowrap;}
.mq-dot{width:3px;height:3px;background:#FFD700;border-radius:50%;}

/* ROBOT */
.robot-section{background:#080808;padding:5rem 5vw;max-width:1280px;margin:0 auto;}
.robot-wrap{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;}
.robot-visual{position:relative;display:flex;justify-content:center;}
.robot-body{width:220px;height:260px;background:linear-gradient(145deg,#111,#0a0a0a);
  border:1px solid rgba(255,215,0,.15);border-radius:24px;position:relative;
  animation:floatY 3s ease-in-out infinite;box-shadow:0 0 60px rgba(255,215,0,.06);}
.robot-head{width:120px;height:80px;background:linear-gradient(145deg,#111,#0a0a0a);
  border:1px solid rgba(255,215,0,.15);border-radius:16px;position:absolute;top:-50px;left:50%;
  transform:translateX(-50%);display:flex;align-items:center;justify-content:center;gap:12px;}
.robot-eye{width:18px;height:18px;background:#FFD700;border-radius:50%;box-shadow:0 0 12px rgba(255,215,0,.8);animation:pulseDot 1.8s infinite;}
.robot-eye.r{animation-delay:.4s;}
.robot-screen{width:160px;height:130px;background:rgba(255,215,0,.03);border:1px solid rgba(255,215,0,.08);
  border-radius:12px;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  display:flex;flex-direction:column;gap:6px;padding:12px;}
.robot-line{height:6px;background:rgba(255,215,0,.12);border-radius:3px;}
.robot-line.short{width:60%;}.robot-line.gold{background:rgba(255,215,0,.35);width:80%;}.robot-line.tiny{width:40%;}
.robot-badge{position:absolute;top:-8px;right:-8px;background:#FFD700;color:#080808;
  font-family:'Syne',sans-serif;font-weight:800;font-size:.55rem;letter-spacing:.05em;padding:.25rem .5rem;border-radius:50px;}
.robot-tag{font-size:.6rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(255,215,0,.45);margin-bottom:.5rem;display:flex;align-items:center;gap:.55rem;}
.robot-tag::before{content:'';width:18px;height:1px;background:rgba(255,215,0,.45);}
.robot-feat{display:flex;align-items:flex-start;gap:.85rem;padding:.9rem;
  background:rgba(255,255,255,.015);border:1px solid rgba(255,255,255,.04);border-radius:12px;}
.robot-feat-icon{width:36px;height:36px;background:rgba(255,215,0,.06);border:1px solid rgba(255,215,0,.12);
  border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:.9rem;flex-shrink:0;}
.robot-feat-title{font-family:'Syne',sans-serif;font-size:.82rem;font-weight:700;color:#F0EDE6;margin-bottom:.2rem;}
.robot-feat-desc{font-size:.73rem;color:rgba(240,237,230,.3);line-height:1.6;}

/* SECTIONS */
.sec{padding:6.5rem 5vw;max-width:1280px;margin:0 auto;}
.sec-lbl{font-size:.6rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(255,215,0,.45);margin-bottom:.75rem;display:flex;align-items:center;gap:.55rem;}
.sec-lbl::before{content:'';width:18px;height:1px;background:rgba(255,215,0,.45);}
.sec-title{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,3rem);
  font-weight:800;letter-spacing:-.04em;line-height:1.08;margin-bottom:.85rem;color:#F0EDE6;}
.sec-sub{font-size:.93rem;color:rgba(240,237,230,.32);max-width:430px;line-height:1.88;font-weight:300;}
.div-line{height:1px;background:rgba(255,255,255,.04);}

/* SERVICES */
.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:3.8rem;
  border:1px solid rgba(255,255,255,.045);border-radius:20px;overflow:hidden;background:rgba(255,255,255,.04);}
.scard{background:#080808;padding:2rem;transition:background .22s;}
.scard:hover{background:#0c0c0c;}
.cicon{width:40px;height:40px;background:rgba(255,215,0,.05);border:1px solid rgba(255,215,0,.1);
  border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:1.1rem;}
.ctitle{font-family:'Syne',sans-serif;font-size:.9rem;font-weight:700;margin-bottom:.38rem;color:#F0EDE6;}
.cdesc{font-size:.78rem;color:rgba(240,237,230,.32);line-height:1.72;}
.ctag{display:inline-block;margin-top:.85rem;font-size:.6rem;font-weight:700;
  background:rgba(255,215,0,.04);color:rgba(255,215,0,.5);padding:.17rem .58rem;
  border-radius:50px;border:1px solid rgba(255,215,0,.1);}

/* ECOSYSTEM */
.eco-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;max-width:1280px;margin:0 auto;padding:6.5rem 5vw;}
.fblock{margin-bottom:1.5rem;}
.flbl{font-size:.56rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:rgba(240,237,230,.15);margin-bottom:.45rem;}
.fwrap{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.045);border-radius:11px;padding:.95rem 1.1rem;}
.frow{display:flex;align-items:center;gap:.4rem;flex-wrap:wrap;}
.fn{display:inline-flex;align-items:center;background:rgba(255,255,255,.03);
  border:1px solid rgba(255,255,255,.055);border-radius:6px;padding:.28rem .6rem;
  font-size:.7rem;font-weight:600;color:rgba(240,237,230,.5);white-space:nowrap;}
.fn.g{background:rgba(255,215,0,.05);border-color:rgba(255,215,0,.15);color:rgba(255,215,0,.75);}
.fn.e{background:#FFD700;color:#080808;border-color:#FFD700;font-weight:700;}
.fa{color:rgba(255,255,255,.12);font-size:.72rem;}
.stepn{width:38px;height:38px;border-radius:50%;background:rgba(255,215,0,.05);
  border:1px solid rgba(255,215,0,.13);color:rgba(255,215,0,.75);font-family:'Syne',sans-serif;
  font-weight:800;font-size:.86rem;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.steptitle{font-family:'Syne',sans-serif;font-weight:700;font-size:.86rem;margin-bottom:.16rem;color:#F0EDE6;}
.stepdesc{font-size:.76rem;color:rgba(240,237,230,.28);line-height:1.65;}

/* PROFILS TYPES */
.proof-section{background:#080808;padding:6rem 5vw;max-width:1280px;margin:0 auto;}
.proof-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:3rem;}
.profile-card{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);
  border-radius:18px;padding:1.8rem;transition:border-color .2s,transform .2s;}
.profile-card:hover{border-color:rgba(255,215,0,.15);transform:translateY(-3px);}
.profile-header{display:flex;align-items:center;gap:.85rem;margin-bottom:1.3rem;padding-bottom:1rem;border-bottom:1px solid rgba(255,255,255,.05);}
.profile-avatar{width:44px;height:44px;border-radius:12px;background:rgba(255,215,0,.08);
  border:1px solid rgba(255,215,0,.18);display:flex;align-items:center;justify-content:center;font-size:1.3rem;}
.profile-metier{font-family:'Syne',sans-serif;font-size:.95rem;font-weight:800;color:#F0EDE6;}
.profile-tag{font-size:.6rem;color:rgba(255,215,0,.55);margin-top:.15rem;letter-spacing:.08em;text-transform:uppercase;font-weight:600;}
.profile-title{font-family:'Syne',sans-serif;font-size:.82rem;font-weight:700;color:rgba(255,215,0,.75);margin-bottom:.9rem;}
.profile-bullets{list-style:none;display:flex;flex-direction:column;gap:.65rem;}
.profile-bullets li{display:flex;align-items:flex-start;gap:.6rem;font-size:.78rem;color:rgba(240,237,230,.55);line-height:1.55;}
.profile-check{color:#FFD700;font-weight:800;flex-shrink:0;margin-top:1px;}
.profile-gain{margin-top:1.2rem;padding-top:1rem;border-top:1px solid rgba(255,255,255,.05);
  display:flex;align-items:center;gap:.6rem;font-size:.72rem;color:rgba(255,215,0,.7);font-weight:600;}
.profile-gain-val{font-family:'Syne',sans-serif;font-size:1.15rem;font-weight:900;color:#FFD700;margin-left:auto;}
.proof-stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;
  margin-top:3rem;padding:2rem;background:rgba(255,215,0,.02);border:1px solid rgba(255,215,0,.07);border-radius:16px;}
.proof-stat-val{font-family:'Syne',sans-serif;font-size:2rem;font-weight:900;color:#FFD700;letter-spacing:-.04em;}
.proof-stat-lbl{font-size:.65rem;color:rgba(240,237,230,.3);margin-top:.25rem;line-height:1.5;}
.proof-disclaimer{margin-top:1.2rem;text-align:center;font-size:.64rem;color:rgba(240,237,230,.18);font-style:italic;}

/* ROI */
.roi-grid-outer{display:grid;grid-template-columns:1fr 1fr;gap:4rem;max-width:1280px;margin:0 auto;padding:0 5vw 6.5rem;}
.roi-box{background:rgba(255,255,255,.02);border:1px solid rgba(255,215,0,.08);border-radius:18px;padding:2.2rem;}
.roi-slbl{font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(240,237,230,.4);margin-bottom:.65rem;font-weight:700;}
.roi-res{background:rgba(255,215,0,.035);border:1px solid rgba(255,215,0,.09);border-radius:11px;padding:1.3rem 1.5rem;margin-top:1.5rem;}
.roi-nums{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;}
.roi-val{font-family:'Syne',sans-serif;font-size:1.7rem;font-weight:800;color:#FFD700;letter-spacing:-.03em;}
.roi-lbl{font-size:.62rem;color:rgba(240,237,230,.35);margin-top:.2rem;}
.task-item{display:flex;justify-content:space-between;align-items:center;
  padding:.6rem .85rem;background:rgba(255,255,255,.015);border:1px solid rgba(255,255,255,.04);border-radius:7px;margin-bottom:.45rem;}
.task-name{font-size:.76rem;color:rgba(240,237,230,.35);text-decoration:line-through;}
.task-gain{font-size:.63rem;font-weight:700;color:rgba(255,215,0,.75);background:rgba(255,215,0,.04);
  border:1px solid rgba(255,215,0,.1);padding:.13rem .5rem;border-radius:50px;white-space:nowrap;}

/* Streamlit slider customisation */
div[data-testid=\"stSlider\"]{padding:0 5vw;max-width:1280px;margin:0 auto;}
div[data-testid=\"stSlider\"] [data-baseweb=\"slider\"] div[role=\"slider\"]{background:#FFD700!important;border:none!important;box-shadow:0 0 0 4px rgba(255,215,0,.18)!important;}
div[data-testid=\"stSlider\"] [data-baseweb=\"slider\"]>div:first-child>div:nth-child(2){background:#FFD700!important;}
div[data-testid=\"stSlider\"] [data-baseweb=\"slider\"]>div:first-child>div:first-child{background:rgba(255,255,255,.07)!important;}
div[data-testid=\"stSlider\"] label p{color:rgba(240,237,230,.4)!important;font-size:.6rem!important;letter-spacing:.2em!important;text-transform:uppercase!important;}

/* PRICING */
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:3.5rem;
  border:1px solid rgba(255,255,255,.045);border-radius:20px;overflow:hidden;background:rgba(255,255,255,.04);}
.pcard{background:#080808;padding:2.2rem;display:flex;flex-direction:column;}
.pcard.feat{background:rgba(255,215,0,.02);}
.pbadge{display:inline-flex;font-size:.58rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  background:rgba(255,215,0,.06);color:rgba(255,215,0,.75);padding:.18rem .65rem;border-radius:50px;
  margin-bottom:.9rem;border:1px solid rgba(255,215,0,.15);align-self:flex-start;}
.pplan{font-family:'Syne',sans-serif;font-weight:800;font-size:1.4rem;margin-bottom:.25rem;color:#F0EDE6;}
.psub{font-size:.78rem;color:rgba(240,237,230,.4);margin-bottom:1.3rem;font-weight:300;}
.phighlight{background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.1);
  border-radius:9px;padding:.65rem .85rem;margin-bottom:1.3rem;font-size:.76rem;color:rgba(255,215,0,.75);font-style:italic;}
.pprice-custom{font-family:'Syne',sans-serif;font-size:1rem;font-weight:800;color:#F0EDE6;margin-bottom:.2rem;}
.pprice-note{font-size:.7rem;color:rgba(240,237,230,.3);margin-bottom:1.5rem;}
.pfeats{display:flex;flex-direction:column;gap:.52rem;margin-bottom:1.7rem;flex-grow:1;}
.pfeat{display:flex;align-items:flex-start;gap:.52rem;font-size:.78rem;color:rgba(240,237,230,.55);}
.pfeat.incl{color:rgba(240,237,230,.3);font-style:italic;}
.pcheck{color:rgba(255,215,0,.65);}.pcheck.bright{color:#FFD700;}
.pcta{display:block;text-align:center;padding:.72rem 1.2rem;border-radius:50px;font-weight:700;font-size:.82rem;text-decoration:none;transition:all .2s;}
.pcta-o{border:1px solid rgba(255,255,255,.12);color:rgba(240,237,230,.7);}
.pcta-o:hover{border-color:rgba(255,215,0,.5);color:#FFD700;}
.pcta-s{background:#FFD700;color:#080808;font-weight:800;}
.pcta-s:hover{box-shadow:0 8px 26px rgba(255,215,0,.38);transform:translateY(-1px);}
.pnote{font-size:.62rem;text-align:center;color:rgba(240,237,230,.22);margin-top:.75rem;}
.onglets-tag{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:1.2rem;}
.otag{font-size:.58rem;font-weight:600;background:rgba(255,255,255,.03);color:rgba(240,237,230,.4);
  padding:.18rem .52rem;border-radius:4px;border:1px solid rgba(255,255,255,.06);}

/* CTA + FOOTER */
.cta-band{background:#FFD700;padding:6rem 5vw;text-align:center;}
.cta-band h2{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,5vw,4rem);font-weight:900;color:#080808;margin-bottom:2.5rem;}
.ibtn{display:inline-flex;align-items:center;gap:.7rem;background:#080808;color:#FFD700;font-weight:700;
  font-size:.92rem;padding:.92rem 2.3rem;border-radius:50px;text-decoration:none;transition:transform .2s,box-shadow .2s;}
.ibtn:hover{transform:translateY(-2px);box-shadow:0 10px 34px rgba(0,0,0,.28);}
.ft{padding:2rem 5vw;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1.2rem;background:#080808;border-top:1px solid rgba(255,255,255,.04);}
.ft-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:.92rem;display:flex;align-items:center;gap:.45rem;color:#F0EDE6;}
.ft-tag{font-size:.68rem;color:rgba(240,237,230,.28);margin-top:.2rem;}
.ft-links{display:flex;gap:1.8rem;}
.ft-links a{font-size:.7rem;color:rgba(240,237,230,.35);text-decoration:none;}
.ft-links a:hover{color:#FFD700;}
.ft-badge{font-size:.62rem;background:rgba(255,215,0,.05);color:rgba(255,215,0,.65);
  padding:.35rem .75rem;border-radius:50px;font-weight:700;border:1px solid rgba(255,215,0,.12);}

/* MOBILE */
@media(max-width:768px){
  .nav-links{display:none;}
  .hero{padding:7rem 5vw 4rem;}
  .hero-title{font-size:clamp(2.4rem,11vw,4rem);}
  .hero-info{gap:1.2rem;}.hero-sep{display:none;}
  .robot-wrap{grid-template-columns:1fr;gap:2.5rem;}
  .cgrid,.pgrid,.proof-grid{grid-template-columns:1fr;border-radius:14px;}
  .eco-grid,.roi-grid-outer{grid-template-columns:1fr;gap:2rem;padding:4rem 5vw;}
  .proof-stat-row{grid-template-columns:1fr;text-align:center;}
  .sec,.robot-section,.proof-section{padding:4rem 5vw;}
  .ft{flex-direction:column;align-items:flex-start;}
}
@media(min-width:768px) and (max-width:1024px){
  .cgrid,.pgrid,.proof-grid{grid-template-columns:repeat(2,1fr);}
}
</style>
\"\"\"

HTML_TOP = f\"\"\"
<nav class=\"nav\">
  <a class=\"nav-logo\" href=\"#\"><div class=\"bolt\"></div>Floxia</a>
  <div class=\"nav-links\">
    <a href=\"#services\">Services</a>
    <a href=\"#ecosystem\">Écosystème</a>
    <a href=\"#roi\">ROI</a>
    <a href=\"#tarifs\">Tarifs</a>
    <a href=\"{INSTA}\" target=\"_blank\" class=\"nav-cta\">Démo →</a>
  </div>
</nav>

<section class=\"hero\">
  <div class=\"hero-grid\"></div><div class=\"hero-scan\"></div><div class=\"hero-orb\"></div>
  <div class=\"hero-badge\"><div class=\"hero-badge-dot\"></div>IA pour artisans & PME du bâtiment</div>
  <h1 class=\"hero-title\">Votre admin.<br><span class=\"outline\">Automatisée.</span><br>Votre temps. Rendu.</h1>
  <p class=\"hero-sub\">Générez vos <strong>devis et factures depuis WhatsApp en 3 minutes</strong>.<br>Un vocal suffit — Floxia s'occupe du reste.</p>
  <div class=\"hero-info\">
    <div class=\"hero-info-item\"><span class=\"hero-info-label\">Temps libéré</span><span class=\"hero-info-val\">16h / mois</span></div>
    <div class=\"hero-sep\"></div>
    <div class=\"hero-info-item\"><span class=\"hero-info-label\">Saisie admin</span><span class=\"hero-info-val\">−80%</span></div>
    <div class=\"hero-sep\"></div>
    <div class=\"hero-info-item\"><span class=\"hero-info-label\">Devis → Facture</span><span class=\"hero-info-val\">3 minutes</span></div>
    <div class=\"hero-sep\"></div>
    <div class=\"hero-info-item\"><span class=\"hero-info-label\">Interface</span><span class=\"hero-info-val\">WhatsApp + ERP</span></div>
  </div>
  <div class=\"hero-cta-row\">
    <a class=\"btn-y\" href=\"{INSTA}\" target=\"_blank\">⚡ Réserver une démo</a>
  </div>
</section>

<div class=\"mq-wrap\"><div class=\"mq-track\">
\"\"\" + \"\".join([f'<div class=\"mq-item\"><div class=\"mq-dot\"></div>{t}</div>' for t in [
    \"Devis vocal en 3 min\",\"PV de réception auto\",\"Facture finale automatisée\",\"Scan tickets de caisse\",
    \"Avis Google Maps auto\",\"Relances intelligentes\",\"Planning salariés\",\"Rapports chantier PDF\",\"ERP 100% mobile\"
]*2]) + \"\"\"
</div></div>

<div class=\"robot-section\">
  <div class=\"robot-wrap\">
    <div class=\"reveal-left robot-visual\">
      <div style=\"position:relative;\">
        <div class=\"robot-body\">
          <div class=\"robot-head\"><div class=\"robot-eye\"></div><div class=\"robot-eye r\"></div></div>
          <div class=\"robot-screen\">
            <div class=\"robot-line gold\"></div><div class=\"robot-line short\"></div>
            <div class=\"robot-line\"></div><div class=\"robot-line tiny\"></div>
            <div class=\"robot-line gold short\"></div><div class=\"robot-line\"></div>
          </div>
          <div class=\"robot-badge\">ERP IA</div>
        </div>
      </div>
    </div>
    <div class=\"reveal-right\">
      <div class=\"robot-tag\">Votre robot ERP</div>
      <h2 style=\"font-family:'Syne',sans-serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:800;color:#F0EDE6;margin-bottom:.6rem;\">Un robot IA qui travaille<br>à votre place. 24h/24.</h2>
      <p style=\"font-size:.88rem;color:rgba(240,237,230,.4);line-height:1.8;margin-bottom:1.8rem;\">Floxia c'est votre ERP intelligent connecté à WhatsApp. Il reçoit vos messages vocaux, comprend ce que vous demandez, et exécute : devis, PV, facture, relance, rapport. Sans que vous ayez rien à taper.</p>
      <div class=\"robot-feat\"><div class=\"robot-feat-icon\">💬</div><div><div class=\"robot-feat-title\">Parlez, il génère</div><div class=\"robot-feat-desc\">Un message vocal WhatsApp → devis PDF en 3 minutes, envoyé automatiquement.</div></div></div>
      <div class=\"robot-feat\" style=\"margin-top:.75rem;\"><div class=\"robot-feat-icon\">📋</div><div><div class=\"robot-feat-title\">ERP complet sur votre téléphone</div><div class=\"robot-feat-desc\">Tableau de bord, chantiers, planning, salariés — tout en temps réel depuis votre mobile.</div></div></div>
      <div class=\"robot-feat\" style=\"margin-top:.75rem;\"><div class=\"robot-feat-icon\">🤖</div><div><div class=\"robot-feat-title\">Il ne dort jamais</div><div class=\"robot-feat-desc\">Relances J+3/J+7/J+14, avis Google, alertes retard — tout automatique.</div></div></div>
    </div>
  </div>
</div>
<div class=\"div-line\"></div>
\"\"\"

SERVICES_LIST = [
    (\"💬\",\"Devis → PV → Facture\",\"Un vocal WhatsApp suffit. Floxia génère le devis PDF, le client signe, le PV est créé, la facture finale se génère automatiquement.\",\"⚡ Cycle complet géré\"),
    (\"📸\",\"Scan Tickets de Caisse\",\"Photographiez vos tickets sur WhatsApp. L'IA extrait fournisseur, articles, HT/TVA et alimente votre compta.\",\"⚡ Zéro ressaisie\"),
    (\"⭐\",\"Avis Google Maps\",\"À chaque chantier terminé, Floxia envoie un message WhatsApp au client pour inviter à laisser un avis Google.\",\"⚡ Réputation boostée\"),
    (\"🚨\",\"Alerte Problème Chantier\",\"Un problème ? Envoyez un vocal. Floxia rédige l'e-mail pro au client : situation, causes, nouveau délai.\",\"⚡ Email en 30 sec\"),
    (\"🔔\",\"Relances Automatiques\",\"Floxia surveille vos devis non signés et relance en 3 temps : J+3, J+7, J+14.\",\"⚡ +30% de conversion\"),
    (\"📋\",\"ERP Mobile Complet\",\"Devis, factures, PV, chantiers, planning, salariés, dépenses — tout synchronisé en temps réel.\",\"⚡ Tout en un endroit\"),
    (\"🎙\",\"Rapports Vocaux Chantier\",\"Dictez votre rapport en 2 min. Floxia le structure et l'envoie en PDF pro.\",\"⚡ Rapport en 2 min\"),
    (\"💰\",\"Suivi Dépenses & TVA\",\"Chaque ticket scanné alimente votre dashboard : dépenses, TVA récupérable, export 1 clic.\",\"⚡ Compta simplifiée\"),
    (\"👥\",\"Gestion Équipe & Salariés\",\"Heures, chantiers, planning temps réel. Synchronisé avec Google Sheets.\",\"⚡ Équipe pilotée WA\"),
]

SERVICES_HTML = f\"\"\"
<div id=\"services\"></div>
<div class=\"sec\">
  <div class=\"reveal\">
    <div class=\"sec-lbl\">Ce que fait Floxia</div>
    <h2 class=\"sec-title\">Tout votre flux de travail,<br>automatisé de A à Z.</h2>
    <p class=\"sec-sub\">Des automatisations concrètes, opérationnelles dès aujourd'hui.</p>
  </div>
  <div class=\"reveal-stagger cgrid\">
\"\"\" + \"\".join([f'<div class=\"scard\"><div class=\"cicon\">{i}</div><div class=\"ctitle\">{t}</div><div class=\"cdesc\">{d}</div><span class=\"ctag\">{tg}</span></div>' for i,t,d,tg in SERVICES_LIST]) + \"\"\"
  </div>
</div>
<div class=\"div-line\"></div>
\"\"\"

ECO_FLUX = [
    (\"Flux 1 — Cycle devis complet\",[(\"🎙 Vocal WA\",\"\"),(\"⚡ IA Floxia\",\"g\"),(\"📄 Devis PDF\",\"\"),(\"✍ Signature\",\"\"),(\"📋 PV\",\"\"),(\"🧾 Facture\",\"e\")]),
    (\"Flux 2 — Avis Google Maps\",[(\"✅ Chantier terminé\",\"\"),(\"⚡ Floxia détecte\",\"g\"),(\"💬 Message WA\",\"\"),(\"⭐ Avis Google\",\"e\")]),
    (\"Flux 3 — Ticket de caisse\",[(\"📸 Photo WA\",\"\"),(\"⚡ OCR IA\",\"g\"),(\"📊 Google Sheets\",\"\"),(\"✅ Compta\",\"e\")]),
    (\"Flux 4 — Problème chantier\",[(\"🚨 Vocal WA\",\"\"),(\"⚡ IA rédaction\",\"g\"),(\"📧 Email client\",\"e\")]),
    (\"Flux 5 — Relances devis\",[(\"⏰ Délai dépassé\",\"\"),(\"⚡ Floxia détecte\",\"g\"),(\"💬 SMS + Email\",\"e\")]),
]
def flux_html(lbl, nodes):
    inner = \"\"
    for i,(txt,kind) in enumerate(nodes):
        inner += f'<span class=\"fn {kind}\">{txt}</span>'
        if i < len(nodes)-1: inner += '<span class=\"fa\">→</span>'
    return f'<div class=\"fblock\"><div class=\"flbl\">{lbl}</div><div class=\"fwrap\"><div class=\"frow\">{inner}</div></div></div>'

ECO_HTML = f\"\"\"
<div id=\"ecosystem\"></div>
<div class=\"eco-grid\">
  <div class=\"reveal-left\">
    <div class=\"sec-lbl\">Comment ça marche</div>
    <h2 class=\"sec-title\">WhatsApp comme<br>centre de commandes.</h2>
    <p class=\"sec-sub\" style=\"margin-bottom:2.6rem;\">Tout part de votre téléphone. Aucun logiciel à apprendre.</p>
\"\"\" + \"\".join([f'<div style=\"display:flex;gap:1rem;margin-bottom:1.3rem;\"><div class=\"stepn\">{n}</div><div><div class=\"steptitle\">{t}</div><div class=\"stepdesc\">{d}</div></div></div>' for n,t,d in [
    (\"1\",\"Une fois connecté\",\"WhatsApp Business, Gmail, Google Drive — on s'occupe de tout.\"),
    (\"2\",\"Parlez ou photographiez\",\"Vocal ou photo sur WhatsApp. Floxia agit instantanément.\"),
    (\"3\",\"L'IA travaille pour vous\",\"Devis envoyé, PV généré, facture émise. Automatiquement.\"),
    (\"4\",\"Pilotez depuis l'ERP\",\"Tableau de bord temps réel sur mobile.\"),
]]) + \"\"\"
  </div>
  <div class=\"reveal-right\">
\"\"\" + \"\".join([flux_html(l,n) for l,n in ECO_FLUX]) + \"\"\"
  </div>
</div>
<div class=\"div-line\"></div>
\"\"\"

PROFILES = [
    (\"🔧\",\"Plombier-chauffagiste\",\"Ce que Floxia change pour un plombier\",
     [\"Devis vocal depuis la camionnette, envoyé avant d'arriver chez le client suivant.\",
      \"Factures d'acompte + PV + facture finale générés sans ouvrir un ordinateur.\",
      \"Tickets fournisseur scannés direct depuis WhatsApp, compta à jour en temps réel.\"],
     \"Temps libéré\",\"~14h / mois\"),
    (\"⚡\",\"Électricien indépendant\",\"Ce que Floxia change pour un électricien\",
     [\"Devis signé plus vite : PDF envoyé en 3 min, plus en 2 jours.\",
      \"Relances automatiques J+3/J+7/J+14 sur les devis non signés.\",
      \"Fini les e-mails le soir : Floxia rédige les imprévus chantier depuis un vocal.\"],
     \"Taux de signature\",\"+30% devis signés\"),
    (\"🎨\",\"Peintre / Carreleur\",\"Ce que Floxia change pour un peintre ou carreleur\",
     [\"Rapport photo de fin de chantier en 2 clics, envoyé au client.\",
      \"Demande d'avis Google auto à la clôture de facture → réputation boostée.\",
      \"Planning équipe visible en temps réel, feuille de route sur WhatsApp.\"],
     \"Admin supprimée\",\"−80% de saisie\"),
]

def profile_card(av,metier,title,bullets,gl,gv):
    bl = \"\".join([f'<li><span class=\"profile-check\">→</span><span>{b}</span></li>' for b in bullets])
    return f\"\"\"<div class=\"profile-card\">
      <div class=\"profile-header\">
        <div class=\"profile-avatar\">{av}</div>
        <div><div class=\"profile-metier\">{metier}</div><div class=\"profile-tag\">Profil type</div></div>
      </div>
      <div class=\"profile-title\">{title}</div>
      <ul class=\"profile-bullets\">{bl}</ul>
      <div class=\"profile-gain\"><span>{gl}</span><span class=\"profile-gain-val\">{gv}</span></div>
    </div>\"\"\"

PROFILES_HTML = f\"\"\"
<div class=\"proof-section\">
  <div class=\"reveal\">
    <div class=\"sec-lbl\">Profils types</div>
    <h2 class=\"sec-title\">Ce que Floxia change<br>selon votre métier.</h2>
    <p class=\"sec-sub\">Pas de faux témoignages. Voici concrètement les bénéfices que nous construisons avec chaque profil d'artisan — basés sur les flux réels que Floxia automatise.</p>
  </div>
  <div class=\"reveal-scale proof-stat-row\">
    <div><div class=\"proof-stat-val\">+30%</div><div class=\"proof-stat-lbl\">de devis signés visés<br>grâce aux relances automatiques</div></div>
    <div><div class=\"proof-stat-val\">16h</div><div class=\"proof-stat-lbl\">libérées par mois<br>en cible sur cycle admin complet</div></div>
    <div><div class=\"proof-stat-val\">−80%</div><div class=\"proof-stat-lbl\">de saisie administrative<br>dès le premier mois d'usage</div></div>
  </div>
  <div class=\"proof-disclaimer\">Objectifs mesurés sur les flux automatisés — Floxia est en phase Beta 2026.</div>
  <div class=\"reveal-stagger proof-grid\" style=\"margin-top:2.5rem;\">
    {\"\".join([profile_card(*p) for p in PROFILES])}
  </div>
</div>
<div class=\"div-line\"></div>

<div id=\"roi\"></div>
<div class=\"sec\" style=\"padding-bottom:2rem;\">
  <div class=\"reveal\">
    <div class=\"sec-lbl\">Simulateur ROI</div>
    <h2 class=\"sec-title\">Calculez votre<br>temps libéré.</h2>
    <p class=\"sec-sub\">Bougez le curseur — voyez ce que Floxia vous rapporte chaque mois.</p>
  </div>
</div>
\"\"\"

PRICING_HTML = f\"\"\"
<div class=\"div-line\"></div>
<div id=\"tarifs\"></div>
<div class=\"sec\">
  <div class=\"reveal\">
    <div class=\"sec-lbl\">Tarifs</div>
    <h2 class=\"sec-title\">Un prix adapté<br>à votre activité.</h2>
    <p class=\"sec-sub\">Chaque tarif est personnalisé selon votre volume de devis et vos besoins.</p>
  </div>
  <div class=\"reveal-stagger pgrid\">
    <div class=\"pcard\">
      <div class=\"pbadge\">Offre 1</div>
      <div class=\"pplan\">Essentiel</div>
      <div class=\"psub\">Numérisation administrative · WhatsApp</div>
      <div class=\"phighlight\">Idéal pour démarrer : base de données, documents automatiques et conformité 2026.</div>
      <div class=\"pprice-custom\">Prix personnalisé</div>
      <div class=\"pprice-note\">Calculé selon votre volume de devis.<br>Sans engagement.</div>
      <div class=\"pfeats\">
\"\"\" + \"\".join([f'<div class=\"pfeat\"><span class=\"pcheck bright\">✦</span>{f}</div>' for f in [
    \"Base de données Google Sheets dédiée\",\"Création automatique de Devis PDF\",
    \"Factures & Factures d'acompte auto\",\"PV de réception automatisé\",
    \"Archivage structuré Google Drive\",\"Envoi via API WhatsApp Business\",
    \"Signature électronique intégrée\",\"Conforme réforme facturation 2026\"
]]) + f\"\"\"
      </div>
      <a class=\"pcta pcta-o\" href=\"{INSTA}\" target=\"_blank\">Obtenir mon tarif →</a>
      <div class=\"pnote\">Pour se lancer sans risque</div>
    </div>

    <div class=\"pcard feat\">
      <div class=\"pbadge\">⚡ Le plus populaire · Offre 2</div>
      <div class=\"pplan\">L'Artisan Autonome</div>
      <div class=\"psub\">Inclus Offre 1 · WhatsApp & ERP Web</div>
      <div class=\"phighlight\">Tout l'Essentiel + votre ERP dédié pour piloter votre activité en autonomie complète.</div>
      <div class=\"pprice-custom\">Prix personnalisé</div>
      <div class=\"pprice-note\">Sans engagement · résiliable à tout moment.</div>
      <div class=\"pfeats\">
        <div class=\"pfeat incl\"><span class=\"pcheck\">⬆</span>Tout de l'Offre Essentiel</div>
        <div class=\"pfeat\"><span class=\"pcheck bright\">✦</span>ERP dédié sur votre mobile</div>
        <div class=\"pfeat\"><span class=\"pcheck bright\">✦</span>Gestion des retards & avenants</div>
      </div>
      <div class=\"onglets-tag\">
\"\"\" + \"\".join([f'<span class=\"otag\">{o}</span>' for o in [
    \"Vue générale\",\"Créer un devis\",\"Devis\",\"Facture & Paiements\",\"Export compta\",\"Chantier\",\"Planning\",\"Notifications\",\"Espace Clients\",\"Tous les dossiers\",\"Google Sheet\",\"Retards & Avenants\",\"RGPD\"
]]) + f\"\"\"
      </div>
      <a class=\"pcta pcta-s\" href=\"{INSTA}\" target=\"_blank\">Obtenir mon tarif →</a>
      <div class=\"pnote\">Le meilleur rapport qualité/valeur</div>
    </div>

    <div class=\"pcard\">
      <div class=\"pbadge\">Offre 3</div>
      <div class=\"pplan\">Premium</div>
      <div class=\"psub\">Inclus Offre 1 + 2 · Équipe & IA avancée</div>
      <div class=\"phighlight\">Gestion d'équipe, IA vocale, rentabilité réelle — la puissance complète.</div>
      <div class=\"pprice-custom\">Prix personnalisé</div>
      <div class=\"pprice-note\">Accompagnement dédié inclus.</div>
      <div class=\"pfeats\">
        <div class=\"pfeat incl\"><span class=\"pcheck\">⬆</span>Tout de l'Offre Artisan Autonome</div>
\"\"\" + \"\".join([f'<div class=\"pfeat\"><span class=\"pcheck bright\">✦</span>{f}</div>' for f in [
    \"Saisie vocale IA via WhatsApp\",\"Collecte photos fin de chantier\",\"Suivi heures collaborateurs\",
    \"Rentabilité réelle IA\",\"Scan tickets caisse → compta auto\",\"Email pro depuis vocal\",
    \"Relances J+3 / J+7 / J+14\",\"Demande d'avis Google auto\"
]]) + f\"\"\"
      </div>
      <a class=\"pcta pcta-o\" href=\"{INSTA}\" target=\"_blank\">Nous contacter →</a>
      <div class=\"pnote\">Pour les équipes & PME</div>
    </div>
  </div>
</div>

<div class=\"cta-band\">
  <div class=\"reveal-scale\">
    <h2>Prêt à récupérer<br>votre temps ?</h2>
    <a class=\"ibtn\" href=\"{INSTA}\" target=\"_blank\">⚡ Réserver une démo — Instagram</a>
    <div style=\"margin-top:1rem;font-size:.7rem;color:rgba(8,8,8,.45);\">@floxia.pro · Réponse sous 24h</div>
  </div>
</div>

<footer class=\"ft\">
  <div>
    <div class=\"ft-logo\"><div class=\"bolt\" style=\"width:20px;height:20px;\"></div>Floxia Service ERP</div>
    <div class=\"ft-tag\">L'IA qui travaille à votre place.</div>
  </div>
  <div class=\"ft-links\">
    <a href=\"#\">Mentions légales</a><a href=\"#\">Confidentialité</a>
    <a href=\"{INSTA}\" target=\"_blank\">Instagram</a>
  </div>
  <div class=\"ft-badge\">⚡ Propulsé par l'IA</div>
</footer>

<script>
(function(){{
  function init(){{
    var els = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .reveal-stagger');
    if(!('IntersectionObserver' in window)){{ els.forEach(function(e){{ e.classList.add('in'); }}); return; }}
    var obs = new IntersectionObserver(function(entries){{
      entries.forEach(function(entry){{
        if(entry.isIntersecting){{ entry.target.classList.add('in'); obs.unobserve(entry.target); }}
      }});
    }}, {{ threshold: 0.15, rootMargin: '0px 0px -60px 0px' }});
    els.forEach(function(e){{ obs.observe(e); }});
  }}
  if(document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
  setTimeout(init, 500);
}})();
</script>
\"\"\"

# ═══ RENDER ═══
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(HTML_TOP, unsafe_allow_html=True)
st.markdown(SERVICES_HTML, unsafe_allow_html=True)
st.markdown(ECO_HTML, unsafe_allow_html=True)
st.markdown(PROFILES_HTML, unsafe_allow_html=True)

# ═══ ROI SLIDER (interactif Streamlit) ═══
nb = st.slider(\"Nombre de devis par mois\", 1, 80, 15, 1)

h_devis = round((45+12)*nb/60, 1)
h = round(h_devis + 8 + 4 + round(18*nb/60,1), 1)
cycle_h = round((60-3)*nb/60, 1)
gain = round(h * 55)
abo = 49 if nb<=10 else (99 if nb<=30 else 149)
roi = round((gain/abo)*100)

st.markdown(f\"\"\"
<div class=\"roi-grid-outer\">
  <div class=\"roi-box\">
    <div class=\"roi-slbl\">Résultats pour {nb} devis / mois</div>
    <div class=\"roi-res\">
      <div class=\"roi-nums\">
        <div><div class=\"roi-val\">{h}h</div><div class=\"roi-lbl\">temps libéré</div></div>
        <div><div class=\"roi-val\">{gain}€</div><div class=\"roi-lbl\">valeur récupérée</div></div>
        <div><div class=\"roi-val\">{roi}%</div><div class=\"roi-lbl\">ROI estimé</div></div>
      </div>
    </div>
    <div style=\"margin-top:1rem;background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.09);border-radius:9px;padding:.85rem 1rem;\">
      <div style=\"font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,215,0,.55);margin-bottom:.55rem;\">⚡ Cycle devis → facture finale</div>
      <div style=\"display:flex;gap:1.5rem;flex-wrap:wrap;\">
        <div><div style=\"font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;\">{cycle_h}h</div><div style=\"font-size:.62rem;color:rgba(240,237,230,.35);\">économisées / mois</div></div>
        <div><div style=\"font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;\">3 min</div><div style=\"font-size:.62rem;color:rgba(240,237,230,.35);\">au lieu de 60 min</div></div>
        <div><div style=\"font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;\">−95%</div><div style=\"font-size:.62rem;color:rgba(240,237,230,.35);\">de temps admin</div></div>
      </div>
    </div>
    <div style=\"font-size:.6rem;color:rgba(240,237,230,.2);margin-top:.75rem;\">*55€/h artisan · estimation mensuelle.</div>
  </div>
  <div>
    <div class=\"sec-lbl\" style=\"margin-bottom:1rem;\">Ce que vous ne faites plus</div>
\"\"\" + \"\".join([f'<div class=\"task-item\"><div class=\"task-name\">{n}</div><div class=\"task-gain\">{g}</div></div>' for n,g in [
    (\"Cycle devis → PV → facture finale\", f\"{cycle_h}h économisées / mois\"),
    (\"Taper des devis le soir\", \"45 min évitées / devis\"),
    (\"Ressaisir les tickets de caisse\", \"2h / semaine récupérées\"),
    (\"Rédiger des e-mails clients\", \"30 min / incident\"),
    (\"Relancer les devis manuellement\", \"+30% de conversion\"),
    (\"Faire le planning à la main\", \"1h / semaine gagnée\"),
    (\"Exporter votre compta\", \"Export 1 clic\"),
    (\"Rédiger les rapports chantier\", \"18 min / chantier\"),
    (\"Demander des avis Google\", \"Automatique\"),
    (\"Générer un PV de réception\", \"Auto après signature\"),
]]) + \"\"\"
  </div>
</div>
\"\"\", unsafe_allow_html=True)
