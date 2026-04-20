import streamlit as st
import textwrap

st.set_page_config(
    page_title="Floxia – Devis & Factures depuis WhatsApp en 3 min",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

INSTA = "https://www.instagram.com/floxia.pro/"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}

html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.block-container{
  background:#080808!important;
  font-family:'DM Sans',sans-serif!important;
  color:#F0EDE6!important;
}

#MainMenu,header,footer,
[data-testid="stSidebar"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stDeployButton{display:none!important;}

.block-container{padding:0!important;max-width:100%!important;}

@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
@keyframes pulseDot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(1.5)}}
@keyframes fadeIn{from{opacity:0;transform:translateY(32px)}to{opacity:1;transform:translateY(0)}}
@keyframes scanline{0%{top:-10%}100%{top:110%}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}

.reveal{opacity:1;transform:none;animation:fadeIn .65s cubic-bezier(.22,1,.36,1) both;}
.reveal.in{opacity:1;transform:translateY(0);}
.reveal-left{opacity:1;transform:none;animation:fadeIn .7s cubic-bezier(.22,1,.36,1) both;}
.reveal-left.in{opacity:1;transform:translateX(0);}
.reveal-right{opacity:1;transform:none;animation:fadeIn .7s cubic-bezier(.22,1,.36,1) both;}
.reveal-right.in{opacity:1;transform:translateX(0);}
.reveal-scale{opacity:1;transform:none;animation:fadeIn .75s cubic-bezier(.22,1,.36,1) both;}
.reveal-stagger > *{opacity:1;transform:none;animation:fadeIn .65s cubic-bezier(.22,1,.36,1) both;}
.reveal-stagger > *:nth-child(2){animation-delay:.05s;}
.reveal-stagger > *:nth-child(3){animation-delay:.10s;}
.reveal-stagger > *:nth-child(4){animation-delay:.15s;}
.reveal-stagger > *:nth-child(5){animation-delay:.20s;}
.reveal-stagger > *:nth-child(6){animation-delay:.25s;}

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

.mq-wrap{overflow:hidden;padding:.85rem 0;border-top:1px solid rgba(255,215,0,.06);border-bottom:1px solid rgba(255,215,0,.06);}
.mq-track{display:flex;gap:2.5rem;width:max-content;animation:marquee 32s linear infinite;}
.mq-item{font-size:.62rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:rgba(255,215,0,.3);display:flex;align-items:center;gap:.75rem;white-space:nowrap;}
.mq-dot{width:3px;height:3px;background:#FFD700;border-radius:50%;}

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
.robot-line.short{width:60%;}
.robot-line.gold{background:rgba(255,215,0,.35);width:80%;}
.robot-line.tiny{width:40%;}
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

.sec{padding:6.5rem 5vw;max-width:1280px;margin:0 auto;}
.sec-lbl{font-size:.6rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(255,215,0,.45);margin-bottom:.75rem;display:flex;align-items:center;gap:.55rem;}
.sec-lbl::before{content:'';width:18px;height:1px;background:rgba(255,215,0,.45);}
.sec-title{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,3rem);
  font-weight:800;letter-spacing:-.04em;line-height:1.08;margin-bottom:.85rem;color:#F0EDE6;}
.sec-sub{font-size:.93rem;color:rgba(240,237,230,.32);max-width:430px;line-height:1.88;font-weight:300;}
.div-line{height:1px;background:rgba(255,255,255,.04);}

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

div[data-testid="stSlider"]{padding:0 5vw;max-width:1280px;margin:0 auto;}
div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"]{background:#FFD700!important;border:none!important;box-shadow:0 0 0 4px rgba(255,215,0,.18)!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:nth-child(2){background:#FFD700!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:first-child{background:rgba(255,255,255,.07)!important;}
div[data-testid="stSlider"] label p{color:rgba(240,237,230,.4)!important;font-size:.6rem!important;letter-spacing:.2em!important;text-transform:uppercase!important;}

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
.pcheck{color:rgba(255,215,0,.65);}
.pcheck.bright{color:#FFD700;}
.pcta{display:block;text-align:center;padding:.72rem 1.2rem;border-radius:50px;font-weight:700;font-size:.82rem;text-decoration:none;transition:all .2s;}
.pcta-o{border:1px solid rgba(255,255,255,.12);color:rgba(240,237,230,.7);}
.pcta-o:hover{border-color:rgba(255,215,0,.5);color:#FFD700;}
.pcta-s{background:#FFD700;color:#080808;font-weight:800;}
.pcta-s:hover{box-shadow:0 8px 26px rgba(255,215,0,.38);transform:translateY(-1px);}
.pnote{font-size:.62rem;text-align:center;color:rgba(240,237,230,.22);margin-top:.75rem;}
.onglets-tag{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:1.2rem;}
.otag{font-size:.58rem;font-weight:600;background:rgba(255,255,255,.03);color:rgba(240,237,230,.4);
  padding:.18rem .52rem;border-radius:4px;border:1px solid rgba(255,255,255,.06);}

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

@media(max-width:768px){
  .nav-links{display:none;}
  .hero{padding:7rem 5vw 4rem;}
  .hero-title{font-size:clamp(2.4rem,11vw,4rem);}
  .hero-info{gap:1.2rem;}
  .hero-sep{display:none;}
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
"""

# ─── MARQUEE ITEMS ───────────────────────────────────────────────────────────
MARQUEE_ITEMS = [
    "Devis vocal en 3 min", "PV de reception auto", "Facture finale automatisee",
    "Scan tickets de caisse", "Avis Google Maps auto", "Relances intelligentes",
    "Planning salaries", "Rapports chantier PDF", "ERP 100% mobile",
] * 2

marquee_html = "".join(
    f'<div class="mq-item"><div class="mq-dot"></div>{t}</div>'
    for t in MARQUEE_ITEMS
)

# ─── HTML TOP ─────────────────────────────────────────────────────────────────
HTML_TOP = (
    '<nav class="nav">'
    '  <a class="nav-logo" href="#"><div class="bolt"></div>Floxia</a>'
    '  <div class="nav-links">'
    '    <a href="#services">Services</a>'
    '    <a href="#ecosystem">Ecosysteme</a>'
    '    <a href="#roi">ROI</a>'
    '    <a href="#tarifs">Tarifs</a>'
    '    <a href="' + INSTA + '" target="_blank" class="nav-cta">Demo</a>'
    '  </div>'
    '</nav>'

    '<section class="hero">'
    '  <div class="hero-grid"></div>'
    '  <div class="hero-scan"></div>'
    '  <div class="hero-orb"></div>'
    '  <div class="hero-badge"><div class="hero-badge-dot"></div>IA pour artisans et PME du batiment</div>'
    '  <h1 class="hero-title">Votre admin.<br><span class="outline">Automatisee.</span><br>Votre temps. Rendu.</h1>'
    '  <p class="hero-sub">Generez vos <strong>devis et factures depuis WhatsApp en 3 minutes</strong>.<br>Un vocal suffit — Floxia s\'occupe du reste.</p>'
    '  <div class="hero-info">'
    '    <div class="hero-info-item"><span class="hero-info-label">Temps libere</span><span class="hero-info-val">16h / mois</span></div>'
    '    <div class="hero-sep"></div>'
    '    <div class="hero-info-item"><span class="hero-info-label">Saisie admin</span><span class="hero-info-val">-80%</span></div>'
    '    <div class="hero-sep"></div>'
    '    <div class="hero-info-item"><span class="hero-info-label">Devis Facture</span><span class="hero-info-val">3 minutes</span></div>'
    '    <div class="hero-sep"></div>'
    '    <div class="hero-info-item"><span class="hero-info-label">Interface</span><span class="hero-info-val">WhatsApp + ERP</span></div>'
    '  </div>'
    '  <div class="hero-cta-row">'
    '    <a class="btn-y" href="' + INSTA + '" target="_blank">Reserver une demo</a>'
    '  </div>'
    '</section>'

    '<div class="mq-wrap"><div class="mq-track">'
    + marquee_html +
    '</div></div>'

    '<div class="robot-section">'
    '  <div class="robot-wrap">'
    '    <div class="reveal-left robot-visual">'
    '      <div style="position:relative;">'
    '        <div class="robot-body">'
    '          <div class="robot-head"><div class="robot-eye"></div><div class="robot-eye r"></div></div>'
    '          <div class="robot-screen">'
    '            <div class="robot-line gold"></div>'
    '            <div class="robot-line short"></div>'
    '            <div class="robot-line"></div>'
    '            <div class="robot-line tiny"></div>'
    '            <div class="robot-line gold short"></div>'
    '            <div class="robot-line"></div>'
    '          </div>'
    '          <div class="robot-badge">ERP IA</div>'
    '        </div>'
    '      </div>'
    '    </div>'
    '    <div class="reveal-right">'
    '      <div class="robot-tag">Votre robot ERP</div>'
    '      <h2 style="font-family:\'Syne\',sans-serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:800;color:#F0EDE6;margin-bottom:.6rem;">Un robot IA qui travaille<br>a votre place. 24h/24.</h2>'
    '      <p style="font-size:.88rem;color:rgba(240,237,230,.4);line-height:1.8;margin-bottom:1.8rem;">Floxia c\'est votre ERP intelligent connecte a WhatsApp. Il recoit vos messages vocaux, comprend ce que vous demandez, et execute : devis, PV, facture, relance, rapport. Sans que vous ayez rien a taper.</p>'
    '      <div class="robot-feat"><div class="robot-feat-icon">&#128172;</div><div><div class="robot-feat-title">Parlez, il genere</div><div class="robot-feat-desc">Un message vocal WhatsApp : devis PDF en 3 minutes, envoye automatiquement.</div></div></div>'
    '      <div class="robot-feat" style="margin-top:.75rem;"><div class="robot-feat-icon">&#128203;</div><div><div class="robot-feat-title">ERP complet sur votre telephone</div><div class="robot-feat-desc">Tableau de bord, chantiers, planning, salaries — tout en temps reel depuis votre mobile.</div></div></div>'
    '      <div class="robot-feat" style="margin-top:.75rem;"><div class="robot-feat-icon">&#129302;</div><div><div class="robot-feat-title">Il ne dort jamais</div><div class="robot-feat-desc">Relances J+3/J+7/J+14, avis Google, alertes retard — tout automatique.</div></div></div>'
    '    </div>'
    '  </div>'
    '</div>'
    '<div class="div-line"></div>'
)

# ─── SERVICES ────────────────────────────────────────────────────────────────
SERVICES_LIST = [
    ("&#128172;", "Devis - PV - Facture",
     "Un vocal WhatsApp suffit. Floxia genere le devis PDF, le client signe, le PV est cree, la facture finale se genere automatiquement.",
     "Cycle complet gere"),
    ("&#128248;", "Scan Tickets de Caisse",
     "Photographiez vos tickets sur WhatsApp. L'IA extrait fournisseur, articles, HT/TVA et alimente votre compta.",
     "Zero ressaisie"),
    ("&#11088;", "Avis Google Maps",
     "A chaque chantier termine, Floxia envoie un message WhatsApp au client pour inviter a laisser un avis Google.",
     "Reputation boostee"),
    ("&#128680;", "Alerte Probleme Chantier",
     "Un probleme ? Envoyez un vocal. Floxia redige l'e-mail pro au client : situation, causes, nouveau delai.",
     "Email en 30 sec"),
    ("&#128276;", "Relances Automatiques",
     "Floxia surveille vos devis non signes et relance en 3 temps : J+3, J+7, J+14.",
     "+30% de conversion"),
    ("&#128203;", "ERP Mobile Complet",
     "Devis, factures, PV, chantiers, planning, salaries, depenses — tout synchronise en temps reel.",
     "Tout en un endroit"),
    ("&#127897;", "Rapports Vocaux Chantier",
     "Dictez votre rapport en 2 min. Floxia le structure et l'envoie en PDF pro.",
     "Rapport en 2 min"),
    ("&#128176;", "Suivi Depenses et TVA",
     "Chaque ticket scanne alimente votre dashboard : depenses, TVA recuperable, export 1 clic.",
     "Compta simplifiee"),
    ("&#128101;", "Gestion Equipe et Salaries",
     "Heures, chantiers, planning temps reel. Synchronise avec Google Sheets.",
     "Equipe pilotee WA"),
]

services_cards = "".join(
    '<div class="scard">'
    f'<div class="cicon">{icon}</div>'
    f'<div class="ctitle">{title}</div>'
    f'<div class="cdesc">{desc}</div>'
    f'<span class="ctag">{tag}</span>'
    '</div>'
    for icon, title, desc, tag in SERVICES_LIST
)

SERVICES_HTML = (
    '<div id="services"></div>'
    '<div class="sec">'
    '  <div class="reveal">'
    '    <div class="sec-lbl">Ce que fait Floxia</div>'
    '    <h2 class="sec-title">Tout votre flux de travail,<br>automatise de A a Z.</h2>'
    '    <p class="sec-sub">Des automatisations concretes, operationnelles des aujourd\'hui.</p>'
    '  </div>'
    '  <div class="reveal-stagger cgrid">'
    + services_cards +
    '  </div>'
    '</div>'
    '<div class="div-line"></div>'
)

# ─── ECOSYSTEM ───────────────────────────────────────────────────────────────
ECO_FLUX = [
    ("Flux 1 - Cycle devis complet", [
        ("Vocal WA", ""), ("IA Floxia", "g"), ("Devis PDF", ""),
        ("Signature", ""), ("PV", ""), ("Facture", "e"),
    ]),
    ("Flux 2 - Avis Google Maps", [
        ("Chantier termine", ""), ("Floxia detecte", "g"),
        ("Message WA", ""), ("Avis Google", "e"),
    ]),
    ("Flux 3 - Ticket de caisse", [
        ("Photo WA", ""), ("OCR IA", "g"),
        ("Google Sheets", ""), ("Compta", "e"),
    ]),
    ("Flux 4 - Probleme chantier", [
        ("Vocal WA", ""), ("IA redaction", "g"), ("Email client", "e"),
    ]),
    ("Flux 5 - Relances devis", [
        ("Delai depasse", ""), ("Floxia detecte", "g"), ("SMS + Email", "e"),
    ]),
]

def flux_html(lbl, nodes):
    inner = ""
    for i, (txt, kind) in enumerate(nodes):
        inner += f'<span class="fn {kind}">{txt}</span>'
        if i < len(nodes) - 1:
            inner += '<span class="fa">&#8594;</span>'
    return (
        '<div class="fblock">'
        f'<div class="flbl">{lbl}</div>'
        '<div class="fwrap"><div class="frow">'
        + inner +
        '</div></div>'
        '</div>'
    )

steps_html = "".join(
    '<div style="display:flex;gap:1rem;margin-bottom:1.3rem;">'
    f'<div class="stepn">{n}</div>'
    '<div>'
    f'<div class="steptitle">{t}</div>'
    f'<div class="stepdesc">{d}</div>'
    '</div>'
    '</div>'
    for n, t, d in [
        ("1", "Une fois connecte", "WhatsApp Business, Gmail, Google Drive — on s\'occupe de tout."),
        ("2", "Parlez ou photographiez", "Vocal ou photo sur WhatsApp. Floxia agit instantanement."),
        ("3", "L\'IA travaille pour vous", "Devis envoye, PV genere, facture emise. Automatiquement."),
        ("4", "Pilotez depuis l\'ERP", "Tableau de bord temps reel sur mobile."),
    ]
)

flux_blocks = "".join(flux_html(l, n) for l, n in ECO_FLUX)

ECO_HTML = (
    '<div id="ecosystem"></div>'
    '<div class="eco-grid">'
    '  <div class="reveal-left">'
    '    <div class="sec-lbl">Comment ca marche</div>'
    '    <h2 class="sec-title">WhatsApp comme<br>centre de commandes.</h2>'
    '    <p class="sec-sub" style="margin-bottom:2.6rem;">Tout part de votre telephone. Aucun logiciel a apprendre.</p>'
    + steps_html +
    '  </div>'
    '  <div class="reveal-right">'
    + flux_blocks +
    '  </div>'
    '</div>'
    '<div class="div-line"></div>'
)

# ─── PROFILES ────────────────────────────────────────────────────────────────
PROFILES = [
    ("&#128295;", "Plombier-chauffagiste", "Ce que Floxia change pour un plombier",
     [
         "Devis vocal depuis la camionnette, envoye avant d'arriver chez le client suivant.",
         "Factures d'acompte + PV + facture finale generes sans ouvrir un ordinateur.",
         "Tickets fournisseur scannes direct depuis WhatsApp, compta a jour en temps reel.",
     ],
     "Temps libere", "~14h / mois"),
    ("&#9889;", "Electricien independant", "Ce que Floxia change pour un electricien",
     [
         "Devis signe plus vite : PDF envoye en 3 min, plus en 2 jours.",
         "Relances automatiques J+3/J+7/J+14 sur les devis non signes.",
         "Fini les e-mails le soir : Floxia redige les imprevus chantier depuis un vocal.",
     ],
     "Taux de signature", "+30% devis signes"),
    ("&#127912;", "Peintre / Carreleur", "Ce que Floxia change pour un peintre ou carreleur",
     [
         "Rapport photo de fin de chantier en 2 clics, envoye au client.",
         "Demande d'avis Google auto a la cloture de facture : reputation boostee.",
         "Planning equipe visible en temps reel, feuille de route sur WhatsApp.",
     ],
     "Admin supprimee", "-80% de saisie"),
]

def profile_card(av, metier, title, bullets, gl, gv):
    bl = "".join(
        f'<li><span class="profile-check">&#8594;</span><span>{b}</span></li>'
        for b in bullets
    )
    return (
        '<div class="profile-card">'
        '  <div class="profile-header">'
        f'    <div class="profile-avatar">{av}</div>'
        '    <div>'
        f'      <div class="profile-metier">{metier}</div>'
        '      <div class="profile-tag">Profil type</div>'
        '    </div>'
        '  </div>'
        f'  <div class="profile-title">{title}</div>'
        f'  <ul class="profile-bullets">{bl}</ul>'
        '  <div class="profile-gain">'
        f'    <span>{gl}</span>'
        f'    <span class="profile-gain-val">{gv}</span>'
        '  </div>'
        '</div>'
    )

profile_cards = "".join(profile_card(*p) for p in PROFILES)

PROFILES_HTML = (
    '<div class="proof-section">'
    '  <div class="reveal">'
    '    <div class="sec-lbl">Profils types</div>'
    '    <h2 class="sec-title">Ce que Floxia change<br>selon votre metier.</h2>'
    '    <p class="sec-sub">Pas de faux temoignages. Voici concretement les benefices que nous construisons avec chaque profil d\'artisan — bases sur les flux reels que Floxia automatise.</p>'
    '  </div>'
    '  <div class="reveal-scale proof-stat-row">'
    '    <div><div class="proof-stat-val">+30%</div><div class="proof-stat-lbl">de devis signes vises<br>grace aux relances automatiques</div></div>'
    '    <div><div class="proof-stat-val">16h</div><div class="proof-stat-lbl">liberees par mois<br>en cible sur cycle admin complet</div></div>'
    '    <div><div class="proof-stat-val">-80%</div><div class="proof-stat-lbl">de saisie administrative<br>des le premier mois d\'usage</div></div>'
    '  </div>'
    '  <div class="proof-disclaimer">Objectifs mesures sur les flux automatises — Floxia est en phase Beta 2026.</div>'
    '  <div class="reveal-stagger proof-grid" style="margin-top:2.5rem;">'
    + profile_cards +
    '  </div>'
    '</div>'
    '<div class="div-line"></div>'

    '<div id="roi"></div>'
    '<div class="sec" style="padding-bottom:2rem;">'
    '  <div class="reveal">'
    '    <div class="sec-lbl">Simulateur ROI</div>'
    '    <h2 class="sec-title">Calculez votre<br>temps libere.</h2>'
    '    <p class="sec-sub">Bougez le curseur — voyez ce que Floxia vous rapporte chaque mois.</p>'
    '  </div>'
    '</div>'
)

# ─── PRICING ─────────────────────────────────────────────────────────────────
feats_offre1 = "".join(
    f'<div class="pfeat"><span class="pcheck bright">&#10022;</span>{f}</div>'
    for f in [
        "Base de donnees Google Sheets dediee",
        "Creation automatique de Devis PDF",
        "Factures et Factures d'acompte auto",
        "PV de reception automatise",
        "Archivage structure Google Drive",
        "Envoi via API WhatsApp Business",
        "Signature electronique integree",
        "Conforme reforme facturation 2026",
    ]
)

onglets = "".join(
    f'<span class="otag">{o}</span>'
    for o in [
        "Vue generale", "Creer un devis", "Devis", "Facture et Paiements",
        "Export compta", "Chantier", "Planning", "Notifications",
        "Espace Clients", "Tous les dossiers", "Google Sheet",
        "Retards et Avenants", "RGPD",
    ]
)

feats_offre3 = "".join(
    f'<div class="pfeat"><span class="pcheck bright">&#10022;</span>{f}</div>'
    for f in [
        "Saisie vocale IA via WhatsApp",
        "Collecte photos fin de chantier",
        "Suivi heures collaborateurs",
        "Rentabilite reelle IA",
        "Scan tickets caisse vers compta auto",
        "Email pro depuis vocal",
        "Relances J+3 / J+7 / J+14",
        "Demande d'avis Google auto",
    ]
)

SCRIPT = """
<script>
(function(){
  function init(){
    var els=document.querySelectorAll('.reveal,.reveal-left,.reveal-right,.reveal-scale,.reveal-stagger');
    if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in');});return;}
    var obs=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){entry.target.classList.add('in');obs.unobserve(entry.target);}
      });
    },{threshold:0.15,rootMargin:'0px 0px -60px 0px'});
    els.forEach(function(e){obs.observe(e);});
  }
  if(document.readyState!=='loading') init();
  else document.addEventListener('DOMContentLoaded',init);
  setTimeout(init,500);
})();
</script>
"""

PRICING_HTML = (
    '<div class="div-line"></div>'
    '<div id="tarifs"></div>'
    '<div class="sec">'
    '  <div class="reveal">'
    '    <div class="sec-lbl">Tarifs</div>'
    '    <h2 class="sec-title">Un prix adapte<br>a votre activite.</h2>'
    '    <p class="sec-sub">Chaque tarif est personnalise selon votre volume de devis et vos besoins.</p>'
    '  </div>'
    '  <div class="reveal-stagger pgrid">'

    # OFFRE 1
    '    <div class="pcard">'
    '      <div class="pbadge">Offre 1</div>'
    '      <div class="pplan">Essentiel</div>'
    '      <div class="psub">Numerisation administrative · WhatsApp</div>'
    '      <div class="phighlight">Ideal pour demarrer : base de donnees, documents automatiques et conformite 2026.</div>'
    '      <div class="pprice-custom">Prix personnalise</div>'
    '      <div class="pprice-note">Calcule selon votre volume de devis.<br>Sans engagement.</div>'
    '      <div class="pfeats">'
    + feats_offre1 +
    '      </div>'
    '      <a class="pcta pcta-o" href="' + INSTA + '" target="_blank">Obtenir mon tarif</a>'
    '      <div class="pnote">Pour se lancer sans risque</div>'
    '    </div>'

    # OFFRE 2
    '    <div class="pcard feat">'
    '      <div class="pbadge">Le plus populaire · Offre 2</div>'
    '      <div class="pplan">L\'Artisan Autonome</div>'
    '      <div class="psub">Inclus Offre 1 · WhatsApp et ERP Web</div>'
    '      <div class="phighlight">Tout l\'Essentiel + votre ERP dedie pour piloter votre activite en autonomie complete.</div>'
    '      <div class="pprice-custom">Prix personnalise</div>'
    '      <div class="pprice-note">Sans engagement · resiliable a tout moment.</div>'
    '      <div class="pfeats">'
    '        <div class="pfeat incl"><span class="pcheck">&#11014;</span>Tout de l\'Offre Essentiel</div>'
    '        <div class="pfeat"><span class="pcheck bright">&#10022;</span>ERP dedie sur votre mobile</div>'
    '        <div class="pfeat"><span class="pcheck bright">&#10022;</span>Gestion des retards et avenants</div>'
    '      </div>'
    '      <div class="onglets-tag">'
    + onglets +
    '      </div>'
    '      <a class="pcta pcta-s" href="' + INSTA + '" target="_blank">Obtenir mon tarif</a>'
    '      <div class="pnote">Le meilleur rapport qualite/valeur</div>'
    '    </div>'

    # OFFRE 3
    '    <div class="pcard">'
    '      <div class="pbadge">Offre 3</div>'
    '      <div class="pplan">Premium</div>'
    '      <div class="psub">Inclus Offre 1 + 2 · Equipe et IA avancee</div>'
    '      <div class="phighlight">Gestion d\'equipe, IA vocale, rentabilite reelle — la puissance complete.</div>'
    '      <div class="pprice-custom">Prix personnalise</div>'
    '      <div class="pprice-note">Accompagnement dedie inclus.</div>'
    '      <div class="pfeats">'
    '        <div class="pfeat incl"><span class="pcheck">&#11014;</span>Tout de l\'Offre Artisan Autonome</div>'
    + feats_offre3 +
    '      </div>'
    '      <a class="pcta pcta-o" href="' + INSTA + '" target="_blank">Nous contacter</a>'
    '      <div class="pnote">Pour les equipes et PME</div>'
    '    </div>'

    '  </div>'
    '</div>'

    # CTA BAND
    '<div class="cta-band">'
    '  <div class="reveal-scale">'
    '    <h2>Pret a recuperer<br>votre temps ?</h2>'
    '    <a class="ibtn" href="' + INSTA + '" target="_blank">Reserver une demo — Instagram</a>'
    '    <div style="margin-top:1rem;font-size:.7rem;color:rgba(8,8,8,.45);">@floxia.pro · Reponse sous 24h</div>'
    '  </div>'
    '</div>'

    # FOOTER
    '<footer class="ft">'
    '  <div>'
    '    <div class="ft-logo"><div class="bolt" style="width:20px;height:20px;"></div>Floxia Service ERP</div>'
    '    <div class="ft-tag">L\'IA qui travaille a votre place.</div>'
    '  </div>'
    '  <div class="ft-links">'
    '    <a href="#">Mentions legales</a>'
    '    <a href="#">Confidentialite</a>'
    '    <a href="' + INSTA + '" target="_blank">Instagram</a>'
    '  </div>'
    '  <div class="ft-badge">Propulse par l\'IA</div>'
    '</footer>'
    + SCRIPT
)

# ═══ RENDER ═══════════════════════════════════════════════════════════════════
st.markdown(textwrap.dedent(CSS), unsafe_allow_html=True)
st.markdown(HTML_TOP, unsafe_allow_html=True)
st.markdown(SERVICES_HTML, unsafe_allow_html=True)
st.markdown(ECO_HTML, unsafe_allow_html=True)
st.markdown(PROFILES_HTML, unsafe_allow_html=True)

# ─── ROI SLIDER ───────────────────────────────────────────────────────────────
nb = st.slider("Nombre de devis par mois", 1, 80, 15, 1)

h_devis = round((45 + 12) * nb / 60, 1)
h = round(h_devis + 8 + 4 + round(18 * nb / 60, 1), 1)
cycle_h = round((60 - 3) * nb / 60, 1)
gain = round(h * 55)
abo = 49 if nb <= 10 else (99 if nb <= 30 else 149)
roi = round((gain / abo) * 100)

TASK_ITEMS = [
    ("Cycle devis - PV - facture finale", f"{cycle_h}h economisees / mois"),
    ("Taper des devis le soir", "45 min evitees / devis"),
    ("Ressaisir les tickets de caisse", "2h / semaine recuperees"),
    ("Rediger des e-mails clients", "30 min / incident"),
    ("Relancer les devis manuellement", "+30% de conversion"),
    ("Faire le planning a la main", "1h / semaine gagnee"),
    ("Exporter votre compta", "Export 1 clic"),
    ("Rediger les rapports chantier", "18 min / chantier"),
    ("Demander des avis Google", "Automatique"),
    ("Generer un PV de reception", "Auto apres signature"),
]

task_html = "".join(
    '<div class="task-item">'
    f'<div class="task-name">{name}</div>'
    f'<div class="task-gain">{g}</div>'
    '</div>'
    for name, g in TASK_ITEMS
)

roi_html = (
    '<div class="roi-grid-outer">'
    '  <div class="roi-box">'
    f'    <div class="roi-slbl">Resultats pour {nb} devis / mois</div>'
    '    <div class="roi-res">'
    '      <div class="roi-nums">'
    f'        <div><div class="roi-val">{h}h</div><div class="roi-lbl">temps libere</div></div>'
    f'        <div><div class="roi-val">{gain}&#8364;</div><div class="roi-lbl">valeur recuperee</div></div>'
    f'        <div><div class="roi-val">{roi}%</div><div class="roi-lbl">ROI estime</div></div>'
    '      </div>'
    '    </div>'
    '    <div style="margin-top:1rem;background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.09);border-radius:9px;padding:.85rem 1rem;">'
    '      <div style="font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,215,0,.55);margin-bottom:.55rem;">Cycle devis vers facture finale</div>'
    '      <div style="display:flex;gap:1.5rem;flex-wrap:wrap;">'
    f'        <div><div style="font-family:\'Syne\',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;">{cycle_h}h</div><div style="font-size:.62rem;color:rgba(240,237,230,.35);">economisees / mois</div></div>'
    '        <div><div style="font-family:\'Syne\',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;">3 min</div><div style="font-size:.62rem;color:rgba(240,237,230,.35);">au lieu de 60 min</div></div>'
    '        <div><div style="font-family:\'Syne\',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;">-95%</div><div style="font-size:.62rem;color:rgba(240,237,230,.35);">de temps admin</div></div>'
    '      </div>'
    '    </div>'
    '    <div style="font-size:.6rem;color:rgba(240,237,230,.2);margin-top:.75rem;">*55&#8364;/h artisan · estimation mensuelle.</div>'
    '  </div>'
    '  <div>'
    '    <div class="sec-lbl" style="margin-bottom:1rem;">Ce que vous ne faites plus</div>'
    + task_html +
    '  </div>'
    '</div>'
)

st.markdown(roi_html, unsafe_allow_html=True)
st.markdown(PRICING_HTML, unsafe_allow_html=True)
