import streamlit as st
import textwrap

st.set_page_config(
    page_title="Floxia - Devis & Factures depuis WhatsApp en 3 min",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CALENDLY = "https://calendly.com/afele1845/30min"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}

html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.block-container{
  background:#0F1923!important;
  font-family:'DM Sans',sans-serif!important;
  color:#E8EDF4!important;
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
  justify-content:space-between;padding:1rem 5vw;background:rgba(15,25,35,.95);backdrop-filter:blur(20px);
  border-bottom:1px solid rgba(255,255,255,.06);}
.nav-logo{display:flex;align-items:center;gap:.6rem;font-family:'Nunito',sans-serif;
  font-weight:900;font-size:1.15rem;letter-spacing:-.02em;color:#E8EDF4;text-decoration:none;}
.bolt{width:26px;height:26px;background:#F5C842;flex-shrink:0;
  clip-path:polygon(65% 0%,35% 45%,60% 45%,35% 100%,65% 55%,40% 55%);}
.nav-links{display:flex;gap:2.2rem;align-items:center;}
.nav-links a{font-size:.78rem;font-weight:600;color:rgba(232,237,244,.4);
  text-decoration:none;letter-spacing:.06em;text-transform:uppercase;cursor:pointer;transition:color .2s;}
.nav-links a:hover{color:#E8EDF4;}
.nav-cta{background:#F5C842!important;color:#1E2B45!important;padding:.46rem 1.2rem;
  border-radius:50px;font-size:.78rem;font-weight:800;text-decoration:none;transition:transform .15s,box-shadow .15s;}
.nav-cta:hover{transform:scale(1.05);box-shadow:0 4px 24px rgba(245,200,66,.45);}

.hero{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:8rem 6vw 6rem;position:relative;overflow:hidden;background:#0F1923;}
.hero-grid{position:absolute;inset:0;
  background-image:linear-gradient(rgba(245,200,66,.02) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(245,200,66,.02) 1px,transparent 1px);
  background-size:70px 70px;pointer-events:none;}
.hero-scan{position:absolute;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(245,200,66,.12),transparent);
  animation:scanline 5s linear infinite;pointer-events:none;}
.hero-orb{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:700px;height:700px;
  border-radius:50%;pointer-events:none;background:radial-gradient(circle,rgba(30,43,69,.5) 0%,transparent 60%);}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;font-size:.64rem;font-weight:800;
  letter-spacing:.22em;text-transform:uppercase;color:rgba(245,200,66,.65);margin-bottom:1.5rem;animation:fadeIn .7s ease .1s both;}
.hero-badge-dot{width:4px;height:4px;background:#F5C842;border-radius:50%;animation:pulseDot 2s infinite;}
.hero-title{font-family:'Nunito',sans-serif;font-weight:900;line-height:.96;letter-spacing:-.04em;
  color:#E8EDF4;font-size:clamp(2.8rem,8vw,7rem);margin-bottom:1.5rem;animation:fadeIn .7s ease .2s both;}
.hero-title .outline{-webkit-text-stroke:2px #F5C842;color:transparent;}
.hero-title .brand{color:#F5C842;}
.hero-sub{font-size:clamp(1rem,2.2vw,1.2rem);color:rgba(232,237,244,.5);font-weight:400;
  max-width:560px;margin:0 auto 2.2rem;line-height:1.7;animation:fadeIn .7s ease .35s both;}
.hero-sub strong{color:#F5C842;font-weight:700;}
.hero-info{display:flex;align-items:center;justify-content:center;gap:2.5rem;margin-bottom:2.5rem;flex-wrap:wrap;animation:fadeIn .7s ease .5s both;}
.hero-info-item{display:flex;flex-direction:column;gap:.18rem;align-items:center;}
.hero-info-label{font-size:.56rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(232,237,244,.25);}
.hero-info-val{font-family:'Nunito',sans-serif;font-size:.95rem;font-weight:800;color:#E8EDF4;}
.hero-sep{width:1px;height:36px;background:rgba(255,255,255,.1);}
.hero-cta-row{display:flex;gap:1rem;align-items:center;justify-content:center;flex-wrap:wrap;animation:fadeIn .7s ease .7s both;}
.btn-y{background:#F5C842;color:#1E2B45;padding:.82rem 2rem;border-radius:50px;font-weight:800;
  font-size:.88rem;text-decoration:none;display:inline-block;transition:transform .2s,box-shadow .2s;}
.btn-y:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(245,200,66,.42);}

.mq-wrap{overflow:hidden;padding:.85rem 0;border-top:1px solid rgba(245,200,66,.07);border-bottom:1px solid rgba(245,200,66,.07);background:#111D29;}
.mq-track{display:flex;gap:2.5rem;width:max-content;animation:marquee 32s linear infinite;}
.mq-item{font-size:.62rem;font-weight:800;letter-spacing:.18em;text-transform:uppercase;
  color:rgba(245,200,66,.4);display:flex;align-items:center;gap:.75rem;white-space:nowrap;}
.mq-dot{width:3px;height:3px;background:#F5C842;border-radius:50%;}

.robot-section{background:#0F1923;padding:5rem 5vw;max-width:1280px;margin:0 auto;}
.robot-wrap{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;}
.robot-visual{position:relative;display:flex;justify-content:center;}
.robot-body{width:220px;height:260px;background:linear-gradient(145deg,#1A2838,#131E2B);
  border:1px solid rgba(245,200,66,.15);border-radius:24px;position:relative;
  animation:floatY 3s ease-in-out infinite;box-shadow:0 0 60px rgba(30,43,69,.4);}
.robot-head{width:120px;height:80px;background:linear-gradient(145deg,#1A2838,#131E2B);
  border:1px solid rgba(245,200,66,.15);border-radius:16px;position:absolute;top:-50px;left:50%;
  transform:translateX(-50%);display:flex;align-items:center;justify-content:center;gap:12px;}
.robot-eye{width:18px;height:18px;background:#F5C842;border-radius:50%;box-shadow:0 0 12px rgba(245,200,66,.8);animation:pulseDot 1.8s infinite;}
.robot-eye.r{animation-delay:.4s;}
.robot-screen{width:160px;height:130px;background:rgba(245,200,66,.03);border:1px solid rgba(245,200,66,.08);
  border-radius:12px;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  display:flex;flex-direction:column;gap:6px;padding:12px;}
.robot-line{height:6px;background:rgba(245,200,66,.1);border-radius:3px;}
.robot-line.short{width:60%;}
.robot-line.gold{background:rgba(245,200,66,.35);width:80%;}
.robot-line.tiny{width:40%;}
.robot-badge{position:absolute;top:-8px;right:-8px;background:#F5C842;color:#1E2B45;
  font-family:'Nunito',sans-serif;font-weight:900;font-size:.55rem;letter-spacing:.05em;padding:.25rem .5rem;border-radius:50px;}
.robot-tag{font-size:.6rem;font-weight:800;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(245,200,66,.55);margin-bottom:.5rem;display:flex;align-items:center;gap:.55rem;}
.robot-tag::before{content:'';width:18px;height:1px;background:rgba(245,200,66,.45);}
.robot-feat{display:flex;align-items:flex-start;gap:.85rem;padding:.9rem;
  background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:12px;}
.robot-feat-icon{width:36px;height:36px;background:rgba(245,200,66,.07);border:1px solid rgba(245,200,66,.15);
  border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:.9rem;flex-shrink:0;}
.robot-feat-title{font-family:'Nunito',sans-serif;font-size:.88rem;font-weight:800;color:#E8EDF4;margin-bottom:.2rem;}
.robot-feat-desc{font-size:.75rem;color:rgba(232,237,244,.35);line-height:1.6;}

.sec{padding:6.5rem 5vw;max-width:1280px;margin:0 auto;}
.sec-lbl{font-size:.6rem;font-weight:800;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(245,200,66,.55);margin-bottom:.75rem;display:flex;align-items:center;gap:.55rem;}
.sec-lbl::before{content:'';width:18px;height:1px;background:rgba(245,200,66,.45);}
.sec-title{font-family:'Nunito',sans-serif;font-size:clamp(1.8rem,3.5vw,3rem);
  font-weight:900;letter-spacing:-.03em;line-height:1.08;margin-bottom:.85rem;color:#E8EDF4;}
.sec-sub{font-size:.93rem;color:rgba(232,237,244,.35);max-width:430px;line-height:1.88;font-weight:400;}
.div-line{height:1px;background:rgba(255,255,255,.05);}

.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:3.8rem;
  border:1px solid rgba(255,255,255,.06);border-radius:20px;overflow:hidden;background:rgba(255,255,255,.05);}
.scard{background:#0F1923;padding:2rem;transition:background .22s;}
.scard:hover{background:#141F2E;}
.cicon{width:40px;height:40px;background:rgba(245,200,66,.06);border:1px solid rgba(245,200,66,.12);
  border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:1.1rem;}
.ctitle{font-family:'Nunito',sans-serif;font-size:.95rem;font-weight:800;margin-bottom:.38rem;color:#E8EDF4;}
.cdesc{font-size:.78rem;color:rgba(232,237,244,.35);line-height:1.72;}
.ctag{display:inline-block;margin-top:.85rem;font-size:.6rem;font-weight:800;
  background:rgba(245,200,66,.05);color:rgba(245,200,66,.6);padding:.17rem .58rem;
  border-radius:50px;border:1px solid rgba(245,200,66,.12);}

.eco-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;max-width:1280px;margin:0 auto;padding:6.5rem 5vw;}
.fblock{margin-bottom:1.5rem;}
.flbl{font-size:.56rem;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:rgba(232,237,244,.2);margin-bottom:.45rem;}
.fwrap{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.06);border-radius:11px;padding:.95rem 1.1rem;}
.frow{display:flex;align-items:center;gap:.4rem;flex-wrap:wrap;}
.fn{display:inline-flex;align-items:center;background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.07);border-radius:6px;padding:.28rem .6rem;
  font-size:.7rem;font-weight:600;color:rgba(232,237,244,.5);white-space:nowrap;}
.fn.g{background:rgba(245,200,66,.06);border-color:rgba(245,200,66,.18);color:rgba(245,200,66,.8);}
.fn.e{background:#F5C842;color:#1E2B45;border-color:#F5C842;font-weight:800;}
.fa{color:rgba(255,255,255,.15);font-size:.72rem;}
.stepn{width:38px;height:38px;border-radius:50%;background:rgba(245,200,66,.07);
  border:1px solid rgba(245,200,66,.15);color:rgba(245,200,66,.8);font-family:'Nunito',sans-serif;
  font-weight:900;font-size:.9rem;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.steptitle{font-family:'Nunito',sans-serif;font-weight:800;font-size:.9rem;margin-bottom:.16rem;color:#E8EDF4;}
.stepdesc{font-size:.78rem;color:rgba(232,237,244,.32);line-height:1.65;}

.proof-section{background:#0F1923;padding:6rem 5vw;max-width:1280px;margin:0 auto;}
.proof-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:3rem;}
.profile-card{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.06);
  border-radius:18px;padding:1.8rem;transition:border-color .2s,transform .2s;}
.profile-card:hover{border-color:rgba(245,200,66,.2);transform:translateY(-3px);}
.profile-header{display:flex;align-items:center;gap:.85rem;margin-bottom:1.3rem;padding-bottom:1rem;border-bottom:1px solid rgba(255,255,255,.06);}
.profile-avatar{width:44px;height:44px;border-radius:12px;background:rgba(245,200,66,.09);
  border:1px solid rgba(245,200,66,.2);display:flex;align-items:center;justify-content:center;font-size:1.3rem;}
.profile-metier{font-family:'Nunito',sans-serif;font-size:1rem;font-weight:900;color:#E8EDF4;}
.profile-tag{font-size:.6rem;color:rgba(245,200,66,.6);margin-top:.15rem;letter-spacing:.08em;text-transform:uppercase;font-weight:700;}
.profile-title{font-family:'Nunito',sans-serif;font-size:.85rem;font-weight:800;color:rgba(245,200,66,.8);margin-bottom:.9rem;}
.profile-bullets{list-style:none;display:flex;flex-direction:column;gap:.65rem;}
.profile-bullets li{display:flex;align-items:flex-start;gap:.6rem;font-size:.78rem;color:rgba(232,237,244,.55);line-height:1.55;}
.profile-check{color:#F5C842;font-weight:800;flex-shrink:0;margin-top:1px;}
.profile-gain{margin-top:1.2rem;padding-top:1rem;border-top:1px solid rgba(255,255,255,.06);
  display:flex;align-items:center;gap:.6rem;font-size:.72rem;color:rgba(245,200,66,.7);font-weight:700;}
.profile-gain-val{font-family:'Nunito',sans-serif;font-size:1.15rem;font-weight:900;color:#F5C842;margin-left:auto;}
.proof-stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;
  margin-top:3rem;padding:2rem;background:rgba(245,200,66,.02);border:1px solid rgba(245,200,66,.08);border-radius:16px;}
.proof-stat-val{font-family:'Nunito',sans-serif;font-size:2rem;font-weight:900;color:#F5C842;letter-spacing:-.03em;}
.proof-stat-lbl{font-size:.65rem;color:rgba(232,237,244,.32);margin-top:.25rem;line-height:1.5;}
.proof-disclaimer{margin-top:1.2rem;text-align:center;font-size:.64rem;color:rgba(232,237,244,.2);font-style:italic;}

.roi-grid-outer{display:grid;grid-template-columns:1fr 1fr;gap:4rem;max-width:1280px;margin:0 auto;padding:0 5vw 2rem;}
.roi-box{background:rgba(255,255,255,.025);border:1px solid rgba(245,200,66,.09);border-radius:18px;padding:2.2rem;}
.roi-slbl{font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(232,237,244,.4);margin-bottom:.65rem;font-weight:700;}
.roi-res{background:rgba(245,200,66,.04);border:1px solid rgba(245,200,66,.1);border-radius:11px;padding:1.3rem 1.5rem;margin-top:1.5rem;}
.roi-nums{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;}
.roi-val{font-family:'Nunito',sans-serif;font-size:1.7rem;font-weight:900;color:#F5C842;letter-spacing:-.03em;}
.roi-lbl{font-size:.62rem;color:rgba(232,237,244,.35);margin-top:.2rem;}
.task-item{display:flex;justify-content:space-between;align-items:center;
  padding:.6rem .85rem;background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:7px;margin-bottom:.45rem;}
.task-name{font-size:.76rem;color:rgba(232,237,244,.35);text-decoration:line-through;}
.task-gain{font-size:.63rem;font-weight:800;color:rgba(245,200,66,.8);background:rgba(245,200,66,.05);
  border:1px solid rgba(245,200,66,.12);padding:.13rem .5rem;border-radius:50px;white-space:nowrap;}

.roi-cta-band{max-width:1280px;margin:0 auto;padding:0 5vw 6.5rem;}
.roi-cta-box{background:rgba(245,200,66,.04);border:1px solid rgba(245,200,66,.15);border-radius:18px;
  padding:2rem 2.5rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1.5rem;}
.roi-cta-label{font-size:.58rem;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
  color:rgba(245,200,66,.55);margin-bottom:.5rem;}
.roi-cta-text{font-family:'Nunito',sans-serif;font-size:1.1rem;font-weight:900;color:#E8EDF4;line-height:1.45;}
.roi-cta-text span{color:#F5C842;}
.roi-cta-sub{font-size:.75rem;color:rgba(232,237,244,.32);margin-top:.4rem;}
.roi-cta-btn{background:#F5C842;color:#1E2B45;padding:.82rem 2rem;border-radius:50px;font-weight:800;
  font-size:.88rem;text-decoration:none;display:inline-block;white-space:nowrap;
  transition:transform .2s,box-shadow .2s;}
.roi-cta-btn:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(245,200,66,.42);}

div[data-testid="stSlider"]{padding:0 5vw;max-width:1280px;margin:0 auto;}
div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"]{background:#F5C842!important;border:none!important;box-shadow:0 0 0 4px rgba(245,200,66,.2)!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:nth-child(2){background:#F5C842!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:first-child{background:rgba(255,255,255,.08)!important;}
div[data-testid="stSlider"] label p{color:rgba(232,237,244,.4)!important;font-size:.6rem!important;letter-spacing:.2em!important;text-transform:uppercase!important;}

/* =============================================
   COMPARATIF — desktop : tableau normal
   mobile    : cartes empilees (plus robuste
               que overflow-x dans Streamlit)
   ============================================= */
.cmp-section{max-width:1280px;margin:0 auto;padding:6.5rem 5vw;}
.cmp-table-wrap{margin-top:3rem;border:1px solid rgba(255,255,255,.06);border-radius:20px;overflow:hidden;}
.cmp-table{width:100%;border-collapse:collapse;}
.cmp-table th{padding:1.1rem 1.4rem;font-size:.62rem;font-weight:800;letter-spacing:.16em;
  text-transform:uppercase;color:rgba(232,237,244,.32);background:#111D29;text-align:left;}
.cmp-table th.floxia-col{color:#F5C842;background:rgba(245,200,66,.04);}
.cmp-table td{padding:.9rem 1.4rem;font-size:.8rem;border-top:1px solid rgba(255,255,255,.05);
  color:rgba(232,237,244,.5);background:#0F1923;vertical-align:middle;}
.cmp-table td.floxia-col{background:rgba(245,200,66,.03);color:rgba(232,237,244,.9);}
.cmp-table tr:hover td{background:#141F2E;}
.cmp-table tr:hover td.floxia-col{background:rgba(245,200,66,.05);}
.cmp-row-label{font-size:.78rem;color:rgba(232,237,244,.5);font-weight:500;}
.cmp-yes{color:#F5C842;font-weight:800;}
.cmp-no{color:rgba(232,237,244,.2);}
.cmp-partial{color:rgba(232,237,244,.4);font-style:italic;font-size:.76rem;}
.cmp-floxia-badge{display:inline-flex;align-items:center;gap:.45rem;font-family:'Nunito',sans-serif;
  font-weight:900;font-size:.92rem;color:#E8EDF4;}
.cmp-floxia-dot{width:8px;height:8px;background:#F5C842;border-radius:50%;}
.cmp-note{margin-top:1.2rem;font-size:.62rem;color:rgba(232,237,244,.2);font-style:italic;text-align:center;}

/* Cartes mobiles comparatif — toutes colonnes */
.cmp-mobile-cards{display:none;flex-direction:column;gap:.7rem;margin-top:2rem;}
.cmp-mcard{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.06);border-radius:12px;padding:1rem 1.1rem;}
.cmp-mcard-feat{font-size:.78rem;color:#E8EDF4;font-weight:700;margin-bottom:.7rem;line-height:1.4;}
.cmp-mcard-cols{display:grid;grid-template-columns:repeat(5,1fr);gap:.3rem;}
.cmp-mcard-col{display:flex;flex-direction:column;align-items:center;gap:.25rem;}
.cmp-mcard-col-lbl{font-size:.46rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:rgba(232,237,244,.25);text-align:center;line-height:1.3;}
.cmp-mcard-col-lbl.floxia{color:rgba(245,200,66,.55);}
.cmp-mcard-yes{font-size:.65rem;font-weight:800;color:#F5C842;}
.cmp-mcard-partial{font-size:.65rem;font-weight:600;color:rgba(232,237,244,.4);font-style:italic;}
.cmp-mcard-no{font-size:.75rem;color:rgba(232,237,244,.18);}
.cmp-mobile-note{display:none;margin-top:1rem;text-align:center;font-size:.65rem;color:rgba(232,237,244,.25);font-style:italic;}

.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:3.5rem;
  border:1px solid rgba(255,255,255,.06);border-radius:20px;overflow:hidden;background:rgba(255,255,255,.05);}
.pcard{background:#0F1923;padding:2.2rem;display:flex;flex-direction:column;}
.pcard.feat{background:rgba(245,200,66,.02);}
.pbadge{display:inline-flex;font-size:.58rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
  background:rgba(245,200,66,.07);color:rgba(245,200,66,.8);padding:.18rem .65rem;border-radius:50px;
  margin-bottom:.9rem;border:1px solid rgba(245,200,66,.18);align-self:flex-start;}
.pplan{font-family:'Nunito',sans-serif;font-weight:900;font-size:1.4rem;margin-bottom:.25rem;color:#E8EDF4;}
.psub{font-size:.78rem;color:rgba(232,237,244,.4);margin-bottom:1.3rem;font-weight:400;}
.phighlight{background:rgba(245,200,66,.05);border:1px solid rgba(245,200,66,.12);
  border-radius:9px;padding:.65rem .85rem;margin-bottom:1.3rem;font-size:.76rem;color:rgba(245,200,66,.8);font-style:italic;}
.pprice-custom{font-family:'Nunito',sans-serif;font-size:1rem;font-weight:900;color:#E8EDF4;margin-bottom:.2rem;}
.pprice-note{font-size:.7rem;color:rgba(232,237,244,.3);margin-bottom:1.5rem;}
.pfeats{display:flex;flex-direction:column;gap:.52rem;margin-bottom:1.7rem;flex-grow:1;}
.pfeat{display:flex;align-items:flex-start;gap:.52rem;font-size:.78rem;color:rgba(232,237,244,.55);}
.pfeat.incl{color:rgba(232,237,244,.3);font-style:italic;}
.pcheck{color:rgba(245,200,66,.65);}
.pcheck.bright{color:#F5C842;}
.pcta{display:block;text-align:center;padding:.72rem 1.2rem;border-radius:50px;font-weight:800;font-size:.82rem;text-decoration:none;transition:all .2s;}
.pcta-o{border:1px solid rgba(255,255,255,.14);color:rgba(232,237,244,.7);}
.pcta-o:hover{border-color:rgba(245,200,66,.6);color:#F5C842;}
.pcta-s{background:#F5C842;color:#1E2B45;font-weight:900;}
.pcta-s:hover{box-shadow:0 8px 26px rgba(245,200,66,.4);transform:translateY(-1px);}
.pnote{font-size:.62rem;text-align:center;color:rgba(232,237,244,.22);margin-top:.75rem;}
.onglets-tag{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:1.2rem;}
.otag{font-size:.58rem;font-weight:600;background:rgba(255,255,255,.04);color:rgba(232,237,244,.4);
  padding:.18rem .52rem;border-radius:4px;border:1px solid rgba(255,255,255,.07);}

.cta-band{background:#F5C842;padding:6rem 5vw;text-align:center;}
.cta-band h2{font-family:'Nunito',sans-serif;font-size:clamp(2.2rem,5vw,4rem);font-weight:900;color:#1E2B45;margin-bottom:2.5rem;}
.ibtn{display:inline-flex;align-items:center;gap:.7rem;background:#1E2B45;color:#F5C842;font-weight:800;
  font-size:.92rem;padding:.92rem 2.3rem;border-radius:50px;text-decoration:none;transition:transform .2s,box-shadow .2s;}
.ibtn:hover{transform:translateY(-2px);box-shadow:0 10px 34px rgba(0,0,0,.3);}
.ft{padding:2rem 5vw;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1.2rem;background:#0A1520;border-top:1px solid rgba(255,255,255,.05);}
.ft-logo{font-family:'Nunito',sans-serif;font-weight:900;font-size:.95rem;display:flex;align-items:center;gap:.45rem;color:#E8EDF4;}
.ft-tag{font-size:.68rem;color:rgba(232,237,244,.3);margin-top:.2rem;}
.ft-links{display:flex;gap:1.8rem;}
.ft-links a{font-size:.7rem;color:rgba(232,237,244,.35);text-decoration:none;}
.ft-links a:hover{color:#F5C842;}
.ft-badge{font-size:.62rem;background:rgba(245,200,66,.06);color:rgba(245,200,66,.65);
  padding:.35rem .75rem;border-radius:50px;font-weight:800;border:1px solid rgba(245,200,66,.14);}

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
  .sec,.robot-section,.proof-section,.cmp-section{padding:4rem 5vw;}
  .ft{flex-direction:column;align-items:flex-start;}
  .roi-cta-box{flex-direction:column;align-items:flex-start;}

  /* Comparatif mobile : on cache le tableau, on affiche les cartes */
  .cmp-table-wrap{display:none!important;}
  .cmp-mobile-cards{display:flex!important;}
  .cmp-mobile-note{display:block;}
}
@media(min-width:769px){
  .cmp-mobile-cards{display:none!important;}
}
@media(min-width:768px) and (max-width:1024px){
  .cgrid,.pgrid,.proof-grid{grid-template-columns:repeat(2,1fr);}
}
</style>
"""

# Marquee
MARQUEE_ITEMS = [
    "Devis vocal en 3 min", "PV de reception auto", "Facture finale automatisee",
    "Scan tickets de caisse", "Avis Google Maps auto", "Relances intelligentes",
    "Planning salaries", "Rapports chantier PDF", "ERP 100% mobile",
] * 2

marquee_html = "".join(
    '<div class="mq-item"><div class="mq-dot"></div>' + t + '</div>'
    for t in MARQUEE_ITEMS
)

HTML_TOP = (
    '<nav class="nav">'
    '<a class="nav-logo" href="#"><div class="bolt"></div>Floxia</a>'
    '<div class="nav-links">'
    '<a href="#services">Services</a>'
    '<a href="#ecosystem">Ecosysteme</a>'
    '<a href="#comparatif">Comparatif</a>'
    '<a href="#roi">ROI</a>'
    '<a href="#tarifs">Tarifs</a>'
    '<a href="' + CALENDLY + '" target="_blank" class="nav-cta">Reserver une demo</a>'
    '</div>'
    '</nav>'

    '<section class="hero">'
    '<div class="hero-grid"></div>'
    '<div class="hero-scan"></div>'
    '<div class="hero-orb"></div>'
    '<div class="hero-badge"><div class="hero-badge-dot"></div>IA pour artisans et PME du batiment</div>'
    '<h1 class="hero-title"><span class="brand">Floxia</span> Automatisee.<br>Votre temps. Rendu.</h1>'
    '<p class="hero-sub">Generez vos <strong>devis et factures depuis WhatsApp en 3 minutes</strong>.<br>Un vocal suffit — Floxia s\'occupe du reste.</p>'
    '<div class="hero-info">'
    '<div class="hero-info-item"><span class="hero-info-label">Temps libere</span><span class="hero-info-val">16h / mois</span></div>'
    '<div class="hero-sep"></div>'
    '<div class="hero-info-item"><span class="hero-info-label">Saisie admin</span><span class="hero-info-val">-80%</span></div>'
    '<div class="hero-sep"></div>'
    '<div class="hero-info-item"><span class="hero-info-label">Devis vers Facture</span><span class="hero-info-val">3 minutes</span></div>'
    '<div class="hero-sep"></div>'
    '<div class="hero-info-item"><span class="hero-info-label">Interface</span><span class="hero-info-val">WhatsApp + ERP</span></div>'
    '</div>'
    '<div class="hero-cta-row">'
    '<a class="btn-y" href="' + CALENDLY + '" target="_blank">Reserver une demo — 30 min</a>'
    '</div>'
    '</section>'

    '<div class="mq-wrap"><div class="mq-track">'
    + marquee_html +
    '</div></div>'

    '<div class="robot-section">'
    '<div class="robot-wrap">'
    '<div class="reveal-left robot-visual">'
    '<div style="position:relative;">'
    '<div class="robot-body">'
    '<div class="robot-head"><div class="robot-eye"></div><div class="robot-eye r"></div></div>'
    '<div class="robot-screen">'
    '<div class="robot-line gold"></div>'
    '<div class="robot-line short"></div>'
    '<div class="robot-line"></div>'
    '<div class="robot-line tiny"></div>'
    '<div class="robot-line gold short"></div>'
    '<div class="robot-line"></div>'
    '</div>'
    '<div class="robot-badge">ERP IA</div>'
    '</div>'
    '</div>'
    '</div>'
    '<div class="reveal-right">'
    '<div class="robot-tag">Votre robot ERP</div>'
    '<h2 style="font-family:\'Nunito\',sans-serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:900;color:#E8EDF4;margin-bottom:.6rem;">Un robot IA qui travaille<br>a votre place. 24h/24.</h2>'
    '<p style="font-size:.88rem;color:rgba(232,237,244,.4);line-height:1.8;margin-bottom:1.8rem;">Floxia c\'est votre ERP intelligent connecte a WhatsApp. Il recoit vos messages vocaux, comprend ce que vous demandez, et execute : devis, PV, facture, relance, rapport. Sans que vous ayez rien a taper.</p>'
    '<div class="robot-feat"><div class="robot-feat-icon">&#128172;</div><div><div class="robot-feat-title">Parlez, il genere</div><div class="robot-feat-desc">Un message vocal WhatsApp : devis PDF en 3 minutes, envoye automatiquement.</div></div></div>'
    '<div class="robot-feat" style="margin-top:.75rem;"><div class="robot-feat-icon">&#128203;</div><div><div class="robot-feat-title">ERP complet sur votre telephone</div><div class="robot-feat-desc">Tableau de bord, chantiers, planning, salaries — tout en temps reel depuis votre mobile.</div></div></div>'
    '<div class="robot-feat" style="margin-top:.75rem;"><div class="robot-feat-icon">&#129302;</div><div><div class="robot-feat-title">Il ne dort jamais</div><div class="robot-feat-desc">Relances J+3/J+7/J+14, avis Google, alertes retard — tout automatique.</div></div></div>'
    '</div>'
    '</div>'
    '</div>'
    '<div class="div-line"></div>'
)

# Services
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
    '<div class="cicon">' + icon + '</div>'
    '<div class="ctitle">' + title + '</div>'
    '<div class="cdesc">' + desc + '</div>'
    '<span class="ctag">' + tag + '</span>'
    '</div>'
    for icon, title, desc, tag in SERVICES_LIST
)

SERVICES_HTML = (
    '<div id="services"></div>'
    '<div class="sec">'
    '<div class="reveal">'
    '<div class="sec-lbl">Ce que fait Floxia</div>'
    '<h2 class="sec-title">Tout votre flux de travail,<br>automatise de A a Z.</h2>'
    '<p class="sec-sub">Des automatisations concretes, operationnelles des aujourd\'hui.</p>'
    '</div>'
    '<div class="reveal-stagger cgrid">'
    + services_cards +
    '</div>'
    '</div>'
    '<div class="div-line"></div>'
)

# Ecosystem
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
        inner += '<span class="fn ' + kind + '">' + txt + '</span>'
        if i < len(nodes) - 1:
            inner += '<span class="fa">&#8594;</span>'
    return (
        '<div class="fblock">'
        '<div class="flbl">' + lbl + '</div>'
        '<div class="fwrap"><div class="frow">' + inner + '</div></div>'
        '</div>'
    )

steps_html = "".join(
    '<div style="display:flex;gap:1rem;margin-bottom:1.3rem;">'
    '<div class="stepn">' + n + '</div>'
    '<div>'
    '<div class="steptitle">' + t + '</div>'
    '<div class="stepdesc">' + d + '</div>'
    '</div>'
    '</div>'
    for n, t, d in [
        ("1", "Une fois connecte",        "WhatsApp Business, Gmail, Google Drive et l'ERP — on s'occupe de tout."),
        ("2", "Parlez ou photographiez",  "Vocal ou photo sur WhatsApp. Floxia agit instantanement."),
        ("3", "L'IA travaille pour vous", "Devis envoye, PV genere, facture emise. Automatiquement."),
        ("4", "Pilotez depuis l'ERP",     "Tableau de bord temps reel sur mobile, et plus encore."),
    ]
)

ECO_HTML = (
    '<div id="ecosystem"></div>'
    '<div class="eco-grid">'
    '<div class="reveal-left">'
    '<div class="sec-lbl">Comment ca marche</div>'
    '<h2 class="sec-title">WhatsApp ou l\'ERP comme<br>centre de commandes.</h2>'
    '<p class="sec-sub" style="margin-bottom:2.6rem;">Tout part de votre telephone. Aucun logiciel a apprendre.</p>'
    + steps_html +
    '</div>'
    '<div class="reveal-right">'
    + "".join(flux_html(l, n) for l, n in ECO_FLUX) +
    '</div>'
    '</div>'
    '<div class="div-line"></div>'
)

# Profiles
PROFILES = [
    ("&#128295;", "Plombier-chauffagiste", "Ce que Floxia change pour un plombier",
     ["Devis vocal depuis la camionnette, envoye avant d'arriver chez le client suivant.",
      "Factures d'acompte + PV + facture finale generes sans ouvrir un ordinateur.",
      "Tickets fournisseur scannes direct depuis WhatsApp, compta a jour en temps reel."],
     "Temps libere", "~14h / mois"),
    ("&#9889;", "Electricien independant", "Ce que Floxia change pour un electricien",
     ["Devis signe plus vite : PDF envoye en 3 min, plus en 2 jours.",
      "Relances automatiques J+3/J+7/J+14 sur les devis non signes.",
      "Fini les e-mails le soir : Floxia redige les imprevus chantier depuis un vocal."],
     "Taux de signature", "+30% devis signes"),
    ("&#127912;", "Peintre / Carreleur", "Ce que Floxia change pour un peintre ou carreleur",
     ["Rapport photo de fin de chantier en 2 clics, envoye au client.",
      "Demande d'avis Google auto a la cloture de facture : reputation boostee.",
      "Planning equipe visible en temps reel, feuille de route sur WhatsApp."],
     "Admin supprimee", "-80% de saisie"),
]

def profile_card(av, metier, title, bullets, gl, gv):
    bl = "".join(
        '<li><span class="profile-check">&#8594;</span><span>' + b + '</span></li>'
        for b in bullets
    )
    return (
        '<div class="profile-card">'
        '<div class="profile-header">'
        '<div class="profile-avatar">' + av + '</div>'
        '<div><div class="profile-metier">' + metier + '</div>'
        '<div class="profile-tag">Profil type</div></div>'
        '</div>'
        '<div class="profile-title">' + title + '</div>'
        '<ul class="profile-bullets">' + bl + '</ul>'
        '<div class="profile-gain">'
        '<span>' + gl + '</span>'
        '<span class="profile-gain-val">' + gv + '</span>'
        '</div>'
        '</div>'
    )

PROFILES_HTML = (
    '<div class="proof-section">'
    '<div class="reveal">'
    '<div class="sec-lbl">Profils types</div>'
    '<h2 class="sec-title">Ce que Floxia change<br>selon votre metier.</h2>'
    '<p class="sec-sub">Pas de faux temoignages. Voici concretement les benefices construits avec chaque profil — bases sur les flux reels que Floxia automatise.</p>'
    '</div>'
    '<div class="reveal-scale proof-stat-row">'
    '<div><div class="proof-stat-val">+30%</div><div class="proof-stat-lbl">de devis signes vises<br>grace aux relances automatiques</div></div>'
    '<div><div class="proof-stat-val">16h</div><div class="proof-stat-lbl">liberees par mois<br>en cible sur cycle admin complet</div></div>'
    '<div><div class="proof-stat-val">-80%</div><div class="proof-stat-lbl">de saisie administrative<br>des le premier mois d\'usage</div></div>'
    '</div>'
    '<div class="proof-disclaimer">Objectifs mesures sur les flux automatises — Floxia est en phase Beta 2026.</div>'
    '<div class="reveal-stagger proof-grid" style="margin-top:2.5rem;">'
    + "".join(profile_card(*p) for p in PROFILES) +
    '</div>'
    '</div>'
    '<div class="div-line"></div>'
    '<div id="roi"></div>'
    '<div class="sec" style="padding-bottom:2rem;">'
    '<div class="reveal">'
    '<div class="sec-lbl">Simulateur ROI</div>'
    '<h2 class="sec-title">Calculez votre<br>temps libere.</h2>'
    '<p class="sec-sub">Bougez le curseur — voyez ce que Floxia vous rapporte chaque mois.</p>'
    '</div>'
    '</div>'
)

# ==============================
# Comparatif
# ==============================
COMP_ROWS = [
    ("Devis depuis WhatsApp vocal",           "Oui — natif",  "Non",      "Non",      "Non",      "Non"),
    ("Cycle devis complet en 3 min automatise", "Oui",         "Non",     "Partiel",   "Non",     "Non"),
    ("PV de reception automatique",            "Oui",          "Non",      "Oui",      "Non",     "Non"),
    ("Facture finale auto apres PV",           "Oui",          "Oui",      "Oui",      "Oui",     "Non"),
    ("Scan tickets de caisse via WA",          "Oui",          "Non",      "Non",      "Non",     "Non"),
    ("Relances auto J+3 / J+7 / J+14",        "Oui",          "Non",      "Partiel",  "Non",      "Non"),
    ("Demande d'avis Google auto",             "Oui",          "Non",      "Non",      "Non",     "Non"),
    ("Email pro depuis message vocal",         "Oui",          "Non",      "Non",      "Non",     "Non"),
    ("ERP tres flexible (WA + web + mobile)",  "Oui",          "Non",      "Partiel",  "Partiel", "Non"),
    ("Gestion equipe et planning",             "Oui",          "Non",      "Oui",      "Oui",     "Partiel"),
    ("App mobile chantier terrain",            "Oui",          "Non",      "Oui",      "Oui",     "Non"),
    ("Suivi heures equipe smartphone",         "Oui",          "Non",      "Oui",      "Oui",     "Non"),
    ("IA vocale / traitement NLP",             "Oui",          "Non",      "Non",      "Non",     "Non"),
    ("Automatisations sans action manuelle",   "Oui",          "Non",      "Non",      "Non",     "Non"),
    ("Conformite facturation 2026",            "Oui",          "Oui",      "Oui",      "Oui",     "Non"),
    ("Sans abonnement logiciel lourd",         "Oui",          "Non",      "Non",      "Non",     "Oui"),
    ("Interface unique WA + ERP",              "Oui",          "Non",      "Non",      "Non",     "Non"),
]

def cmp_td(val, is_floxia=False):
    col_class = ' class="floxia-col"' if is_floxia else ''
    if val.startswith("Oui"):
        inner = '<span class="cmp-yes">&#10003; ' + val + '</span>'
    elif val == "Non":
        inner = '<span class="cmp-no">&#215;</span>'
    else:
        inner = '<span class="cmp-partial">' + val + '</span>'
    return '<td' + col_class + '>' + inner + '</td>'

cmp_rows_html = "".join(
    '<tr>'
    '<td class="cmp-row-label">' + row[0] + '</td>'
    + cmp_td(row[1], is_floxia=True)
    + cmp_td(row[2])
    + cmp_td(row[3])
    + cmp_td(row[4])
    + cmp_td(row[5])
    + '</tr>'
    for row in COMP_ROWS
)

# Cartes mobiles : fonctionnalite + statut Floxia uniquement
def cmp_mobile_card(row):
    cols_data = [
        ("Floxia", row[1], True),
        ("Batiprix", row[2], False),
        ("Onaya", row[3], False),
        ("EBP/sage", row[4], False),
        ("Excel", row[5], False),
    ]
    cols_html = ""
    for lbl, val, is_floxia in cols_data:
        lbl_class = ' floxia' if is_floxia else ''
        if val.startswith("Oui"):
            badge = '<span class="cmp-mcard-yes">✓</span>'
        elif val == "Non":
            badge = '<span class="cmp-mcard-no">×</span>'
        else:
            badge = '<span class="cmp-mcard-partial">~</span>'
        cols_html += (
            '<div class="cmp-mcard-col">'
            '<div class="cmp-mcard-col-lbl' + lbl_class + '">' + lbl + '</div>'
            + badge +
            '</div>'
        )
    return (
        '<div class="cmp-mcard">'
        '<div class="cmp-mcard-feat">' + row[0] + '</div>'
        '<div class="cmp-mcard-cols">' + cols_html + '</div>'
        '</div>'
    )

mobile_cards_html = "".join(cmp_mobile_card(row) for row in COMP_ROWS)

COMPARATIF_HTML = (
    '<div class="div-line"></div>'
    '<div id="comparatif"></div>'
    '<div class="cmp-section">'
    '<div class="reveal">'
    '<div class="sec-lbl">Comparatif</div>'
    '<h2 class="sec-title">Floxia vs les autres<br>solutions du marche.</h2>'
    '<p class="sec-sub">Les ERP du batiment existants sont puissants — mais aucun ne parle WhatsApp. Floxia comble ce que les autres ont laisse de cote.</p>'
    '</div>'

    # Tableau desktop
    '<div class="reveal-scale cmp-table-wrap">'
    '<table class="cmp-table">'
    '<thead><tr>'
    '<th style="width:28%;">Fonctionnalite</th>'
    '<th class="floxia-col"><div class="cmp-floxia-badge"><div class="cmp-floxia-dot"></div>Floxia</div></th>'
    '<th>Batiprix / Obat</th>'
    '<th>Onaya / Batigest</th>'
    '<th>EBP / Sage</th>'
    '<th>Excel manuel</th>'
    '</tr></thead>'
    '<tbody>' + cmp_rows_html + '</tbody>'
    '</table>'
    '</div>'

    # Cartes mobiles (cachees sur desktop via CSS)
    '<div class="cmp-mobile-cards">'
    '<div style="font-size:.62rem;font-weight:800;letter-spacing:.18em;text-transform:uppercase;'
    'color:rgba(245,200,66,.55);margin-bottom:.75rem;display:flex;align-items:center;gap:.5rem;">'
    '<span style="width:14px;height:1px;background:rgba(245,200,66,.4);display:inline-block;"></span>'
    'Floxia — toutes les fonctionnalites'
    '</div>'
    + mobile_cards_html +
    '</div>'

    '<div class="cmp-mobile-note">Comparatif base sur les fonctionnalites publiquement documentees·</div>'
    '</div>'
    '<div class="div-line"></div>'
)

# Pricing
feats_offre1 = "".join(
    '<div class="pfeat"><span class="pcheck bright">&#10022;</span>' + f + '</div>'
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
    '<span class="otag">' + o + '</span>'
    for o in [
        "Vue generale", "Creer un devis", "Devis", "Facture et Paiements",
        "Export compta", "Chantier", "Planning", "Notifications",
        "Espace Clients", "Tous les dossiers", "Google Sheet",
        "Retards et Avenants", "RGPD",
    ]
)

feats_offre3 = "".join(
    '<div class="pfeat"><span class="pcheck bright">&#10022;</span>' + f + '</div>'
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

SCRIPT = (
    '<script>'
    '(function(){'
    'function init(){'
    'var els=document.querySelectorAll(".reveal,.reveal-left,.reveal-right,.reveal-scale,.reveal-stagger");'
    'if(!("IntersectionObserver" in window)){els.forEach(function(e){e.classList.add("in");});return;}'
    'var obs=new IntersectionObserver(function(entries){'
    'entries.forEach(function(entry){'
    'if(entry.isIntersecting){entry.target.classList.add("in");obs.unobserve(entry.target);}'
    '});'
    '},{threshold:0.15,rootMargin:"0px 0px -60px 0px"});'
    'els.forEach(function(e){obs.observe(e);});'
    '}'
    'if(document.readyState!=="loading") init();'
    'else document.addEventListener("DOMContentLoaded",init);'
    'setTimeout(init,500);'
    '})();'
    '</script>'
)

PRICING_HTML = (
    '<div class="div-line"></div>'
    '<div id="tarifs"></div>'
    '<div class="sec">'
    '<div class="reveal">'
    '<div class="sec-lbl">Tarifs</div>'
    '<h2 class="sec-title">Un prix adapte<br>a votre activite.</h2>'
    '<p class="sec-sub">Chaque tarif est personnalise selon votre volume de devis et vos besoins.</p>'
    '</div>'
    '<div class="reveal-stagger pgrid">'

    '<div class="pcard">'
    '<div class="pbadge">Offre 1</div>'
    '<div class="pplan">Essentiel</div>'
    '<div class="psub">Numerisation administrative · WhatsApp</div>'
    '<div class="phighlight">Ideal pour demarrer : base de donnees, documents automatiques et conformite 2026.</div>'
    '<div class="pprice-custom">Prix personnalise</div>'
    '<div class="pprice-note">Calcule selon votre volume de devis.<br>Sans engagement.</div>'
    '<div class="pfeats">' + feats_offre1 + '</div>'
    '<a class="pcta pcta-o" href="' + CALENDLY + '" target="_blank">Obtenir mon tarif</a>'
    '<div class="pnote">Pour se lancer sans risque</div>'
    '</div>'

    '<div class="pcard feat">'
    '<div class="pbadge">Le plus populaire · Offre 2</div>'
    '<div class="pplan">L\'Artisan Autonome</div>'
    '<div class="psub">Inclus Offre 1 · WhatsApp et ERP Web</div>'
    '<div class="phighlight">Tout l\'Essentiel + votre ERP dedie pour piloter votre activite en autonomie complete.</div>'
    '<div class="pprice-custom">Prix personnalise</div>'
    '<div class="pprice-note">Sans engagement · resiliable a tout moment.</div>'
    '<div class="pfeats">'
    '<div class="pfeat incl"><span class="pcheck">&#11014;</span>Tout de l\'Offre Essentiel</div>'
    '<div class="pfeat"><span class="pcheck bright">&#10022;</span>ERP dedie sur votre mobile</div>'
    '<div class="pfeat"><span class="pcheck bright">&#10022;</span>Gestion des retards et avenants</div>'
    '</div>'
    '<div class="onglets-tag">' + onglets + '</div>'
    '<a class="pcta pcta-s" href="' + CALENDLY + '" target="_blank">Obtenir mon tarif</a>'
    '<div class="pnote">Le meilleur rapport qualite/valeur</div>'
    '</div>'

    '<div class="pcard">'
    '<div class="pbadge">Offre 3</div>'
    '<div class="pplan">Premium</div>'
    '<div class="psub">Inclus Offre 1 + 2 · Equipe et IA avancee</div>'
    '<div class="phighlight">Gestion d\'equipe, IA vocale, rentabilite reelle — la puissance complete.</div>'
    '<div class="pprice-custom">Prix personnalise</div>'
    '<div class="pprice-note">Accompagnement dedie inclus.</div>'
    '<div class="pfeats">'
    '<div class="pfeat incl"><span class="pcheck">&#11014;</span>Tout de l\'Offre Artisan Autonome</div>'
    + feats_offre3 +
    '</div>'
    '<a class="pcta pcta-o" href="' + CALENDLY + '" target="_blank">Nous contacter</a>'
    '<div class="pnote">Pour les equipes et PME</div>'
    '</div>'

    '</div>'
    '</div>'

    '<div class="cta-band">'
    '<div class="reveal-scale">'
    '<h2>Pret a recuperer<br>votre temps ?</h2>'
    '<a class="ibtn" href="' + CALENDLY + '" target="_blank">Reserver une demo — 30 min</a>'
    '<div style="margin-top:1rem;font-size:.7rem;color:rgba(30,43,69,.55);">Reponse sous 24h · Sans engagement</div>'
    '</div>'
    '</div>'

    '<footer class="ft">'
    '<div>'
    '<div class="ft-logo"><div class="bolt" style="width:20px;height:20px;"></div>Floxia Service ERP</div>'
    '<div class="ft-tag">L\'IA qui travaille a votre place.</div>'
    '</div>'
    '<div class="ft-links">'
    '<a href="#">Mentions legales</a>'
    '<a href="#">Confidentialite</a>'
    '<a href="' + CALENDLY + '" target="_blank">Reserver une demo</a>'
    '</div>'
    '<div class="ft-badge">Propulse par l\'IA</div>'
    '</footer>'
    + SCRIPT
)

# === RENDER ===
st.markdown(textwrap.dedent(CSS), unsafe_allow_html=True)
st.markdown(HTML_TOP, unsafe_allow_html=True)
st.markdown(SERVICES_HTML, unsafe_allow_html=True)
st.markdown(ECO_HTML, unsafe_allow_html=True)
st.markdown(PROFILES_HTML, unsafe_allow_html=True)

# ROI Slider
nb = st.slider("Nombre de devis par mois", 1, 80, 15, 1)

h_devis = round((45 + 12) * nb / 60, 1)
h       = round(h_devis + 8 + 4 + round(18 * nb / 60, 1), 1)
cycle_h = round((60 - 3) * nb / 60, 1)
gain    = round(h * 55)
abo     = 49 if nb <= 10 else (99 if nb <= 30 else 149)
roi     = round((gain / abo) * 100)

offre_label = "Essentiel" if nb <= 10 else ("Artisan Autonome" if nb <= 30 else "Premium")

TASK_ITEMS = [
    ("Cycle devis - PV - facture finale", str(cycle_h) + "h economisees / mois"),
    ("Taper des devis le soir",           "45 min evitees / devis"),
    ("Ressaisir les tickets de caisse",   "2h / semaine recuperees"),
    ("Rediger des e-mails clients",       "30 min / incident"),
    ("Relancer les devis manuellement",   "+30% de conversion"),
    ("Faire le planning a la main",       "1h / semaine gagnee"),
    ("Exporter votre compta",             "Export 1 clic"),
    ("Rediger les rapports chantier",     "18 min / chantier"),
    ("Demander des avis Google",          "Automatique"),
    ("Generer un PV de reception",        "Auto apres signature"),
]

task_html = "".join(
    '<div class="task-item">'
    '<div class="task-name">' + name + '</div>'
    '<div class="task-gain">' + g + '</div>'
    '</div>'
    for name, g in TASK_ITEMS
)

roi_html = (
    '<div class="roi-grid-outer">'
    '<div class="roi-box">'
    '<div class="roi-slbl">Resultats pour ' + str(nb) + ' devis / mois</div>'
    '<div class="roi-res">'
    '<div class="roi-nums">'
    '<div><div class="roi-val">' + str(h) + 'h</div><div class="roi-lbl">temps libere</div></div>'
    '<div><div class="roi-val">' + str(gain) + '&#8364;</div><div class="roi-lbl">valeur recuperee</div></div>'
    '<div><div class="roi-val">' + str(roi) + '%</div><div class="roi-lbl">ROI estime</div></div>'
    '</div>'
    '</div>'
    '<div style="margin-top:1rem;background:rgba(245,200,66,.04);border:1px solid rgba(245,200,66,.1);border-radius:9px;padding:.85rem 1rem;">'
    '<div style="font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(245,200,66,.6);margin-bottom:.55rem;">Cycle devis vers facture finale</div>'
    '<div style="display:flex;gap:1.5rem;flex-wrap:wrap;">'
    '<div><div style="font-family:\'Nunito\',sans-serif;font-size:1.3rem;font-weight:900;color:#F5C842;">' + str(cycle_h) + 'h</div><div style="font-size:.62rem;color:rgba(232,237,244,.35);">economisees / mois</div></div>'
    '<div><div style="font-family:\'Nunito\',sans-serif;font-size:1.3rem;font-weight:900;color:#F5C842;">3 min</div><div style="font-size:.62rem;color:rgba(232,237,244,.35);">au lieu de 60 min</div></div>'
    '<div><div style="font-family:\'Nunito\',sans-serif;font-size:1.3rem;font-weight:900;color:#F5C842;">-95%</div><div style="font-size:.62rem;color:rgba(232,237,244,.35);">de temps admin</div></div>'
    '</div>'
    '</div>'
    '<div style="font-size:.6rem;color:rgba(232,237,244,.2);margin-top:.75rem;">*55&#8364;/h artisan · estimation mensuelle.</div>'
    '</div>'
    '<div>'
    '<div class="sec-lbl" style="margin-bottom:1rem;">Ce que vous ne faites plus</div>'
    + task_html +
    '</div>'
    '</div>'
)

roi_cta_html = (
    '<div class="roi-cta-band">'
    '<div class="roi-cta-box">'
    '<div>'
    '<div class="roi-cta-label">Votre estimation personnalisee</div>'
    '<div class="roi-cta-text">'
    'Pour <span>' + str(nb) + ' devis/mois</span> — offre conseillee : <span>' + offre_label + '</span><br>'
    'Valeur recuperee estimee : <span>' + str(gain) + '&#8364; / mois</span> · ROI <span>' + str(roi) + '%</span>'
    '</div>'
    '<div class="roi-cta-sub">Tarif personnalise selon votre volume · sans engagement · reponse sous 24h</div>'
    '</div>'
    '<a class="roi-cta-btn" href="' + CALENDLY + '" target="_blank">Reserver ma demo 30 min &#8594;</a>'
    '</div>'
    '</div>'
)

st.markdown(roi_html, unsafe_allow_html=True)
st.markdown(roi_cta_html, unsafe_allow_html=True)
st.markdown(COMPARATIF_HTML, unsafe_allow_html=True)
st.markdown(PRICING_HTML, unsafe_allow_html=True)
