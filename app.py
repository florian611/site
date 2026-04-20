import streamlit as st

st.set_page_config(
    page_title="Floxia – Devis & Factures depuis WhatsApp en 3 min",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.block-container{
  background:#080808!important;font-family:'DM Sans',sans-serif!important;color:#F0EDE6!important;}
#MainMenu,header,footer,[data-testid="stSidebar"],[data-testid="stToolbar"],
[data-testid="stDecoration"],[data-testid="stStatusWidget"],.stDeployButton{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}

@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(1.5)}}
@keyframes fadeIn{from{opacity:0;transform:translateY(32px)}to{opacity:1;transform:translateY(0)}}
@keyframes scanline{0%{top:-10%}100%{top:110%}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}

/* ── NAV ── */
.nav{position:fixed;top:0;left:0;right:0;z-index:9999;display:flex;align-items:center;
  justify-content:space-between;padding:1rem 5vw;background:rgba(8,8,8,.92);backdrop-filter:blur(20px);
  border-bottom:1px solid rgba(255,255,255,.04);}
.nav-logo{display:flex;align-items:center;gap:.6rem;font-family:'Syne',sans-serif;
  font-weight:900;font-size:1.1rem;letter-spacing:-.04em;color:#F0EDE6;text-decoration:none;}
.bolt{width:26px;height:26px;background:#FFD700;flex-shrink:0;
  clip-path:polygon(65% 0%,35% 45%,60% 45%,35% 100%,65% 55%,40% 55%);}
.nav-links{display:flex;gap:2.2rem;align-items:center;}
.nav-links a{font-size:.78rem;font-weight:500;color:rgba(240,237,230,.38);
  text-decoration:none;letter-spacing:.06em;text-transform:uppercase;transition:color .2s;}
.nav-links a:hover{color:#F0EDE6;}
.nav-cta{background:#FFD700!important;color:#080808!important;padding:.46rem 1.2rem;
  border-radius:50px;font-size:.78rem;font-weight:700;text-decoration:none;
  letter-spacing:.02em;transition:transform .15s,box-shadow .15s;}
.nav-cta:hover{transform:scale(1.05);box-shadow:0 4px 24px rgba(255,215,0,.45);}
.nav-hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px;}
.nav-hamburger span{display:block;width:22px;height:2px;background:#F0EDE6;border-radius:2px;transition:all .3s;}

/* ── HERO ── */
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
  border-radius:50%;pointer-events:none;
  background:radial-gradient(circle,rgba(255,215,0,.07) 0%,transparent 60%);}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;font-size:.64rem;font-weight:700;
  letter-spacing:.22em;text-transform:uppercase;color:rgba(255,215,0,.55);margin-bottom:1.5rem;
  animation:fadeIn .7s ease .1s both;position:relative;}
.hero-badge-dot{width:4px;height:4px;background:#FFD700;border-radius:50%;animation:pulse 2s infinite;}
.hero-title{font-family:'Syne',sans-serif;font-weight:900;line-height:.92;letter-spacing:-.06em;
  color:#F0EDE6;font-size:clamp(2.8rem,8vw,7.5rem);margin-bottom:1.5rem;position:relative;z-index:1;
  animation:fadeIn .7s ease .2s both;}
.hero-title .outline{-webkit-text-stroke:2px #FFD700;color:transparent;}
.hero-title .anim{display:inline-block;transition:opacity .3s,transform .3s;}

/* Hero sub-tagline (nouvelle ligne explicite) */
.hero-sub{font-size:clamp(1rem,2.2vw,1.25rem);color:rgba(240,237,230,.52);font-weight:300;
  max-width:560px;margin:0 auto 2.2rem;line-height:1.7;animation:fadeIn .7s ease .35s both;
  position:relative;z-index:1;}
.hero-sub strong{color:#FFD700;font-weight:600;}

.hero-info{display:flex;align-items:center;justify-content:center;gap:2.5rem;margin-bottom:2.5rem;
  animation:fadeIn .7s ease .5s both;flex-wrap:wrap;position:relative;}
.hero-info-item{display:flex;flex-direction:column;gap:.18rem;align-items:center;}
.hero-info-label{font-size:.56rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(240,237,230,.22);}
.hero-info-val{font-family:'Syne',sans-serif;font-size:.9rem;font-weight:700;color:#F0EDE6;}
.hero-sep{width:1px;height:36px;background:rgba(255,255,255,.08);}
.hero-cta-row{display:flex;gap:1rem;align-items:center;justify-content:center;
  animation:fadeIn .7s ease .7s both;flex-wrap:wrap;position:relative;}
.btn-y{background:#FFD700;color:#080808;padding:.82rem 2rem;border-radius:50px;font-weight:700;
  font-size:.88rem;text-decoration:none;display:inline-block;transition:transform .2s,box-shadow .2s;}
.btn-y:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(255,215,0,.42);}
.btn-g{color:rgba(240,237,230,.42);font-size:.82rem;text-decoration:none;
  display:inline-flex;align-items:center;gap:.4rem;transition:color .2s;letter-spacing:.02em;}
.btn-g:hover{color:#F0EDE6;}
.scroll-hint{position:absolute;bottom:2.5rem;right:5vw;display:flex;flex-direction:column;
  align-items:center;gap:.45rem;animation:fadeIn 1s ease 1s both;}
.scroll-line{width:1px;height:48px;background:linear-gradient(to bottom,rgba(255,215,0,.35),transparent);}
.scroll-txt{font-size:.54rem;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,215,0,.25);writing-mode:vertical-rl;}

/* ── ROBOT ERP VISUAL ── */
.robot-section{background:#080808;padding:5rem 5vw;max-width:1280px;margin:0 auto;}
.robot-wrap{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;}
.robot-visual{position:relative;display:flex;justify-content:center;}
.robot-body{width:220px;height:260px;background:linear-gradient(145deg,#111,#0a0a0a);
  border:1px solid rgba(255,215,0,.15);border-radius:24px;position:relative;
  animation:float 3s ease-in-out infinite;box-shadow:0 0 60px rgba(255,215,0,.06);}
.robot-head{width:120px;height:80px;background:linear-gradient(145deg,#111,#0a0a0a);
  border:1px solid rgba(255,215,0,.15);border-radius:16px;margin:0 auto;
  position:absolute;top:-50px;left:50%;transform:translateX(-50%);
  display:flex;align-items:center;justify-content:center;gap:12px;}
.robot-eye{width:18px;height:18px;background:#FFD700;border-radius:50%;
  box-shadow:0 0 12px rgba(255,215,0,.8);animation:pulse 1.8s infinite;}
.robot-eye.r{animation-delay:.4s;}
.robot-screen{width:160px;height:130px;background:rgba(255,215,0,.03);
  border:1px solid rgba(255,215,0,.08);border-radius:12px;
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  display:flex;flex-direction:column;gap:6px;padding:12px;overflow:hidden;}
.robot-line{height:6px;background:rgba(255,215,0,.12);border-radius:3px;}
.robot-line.short{width:60%;}
.robot-line.gold{background:rgba(255,215,0,.35);width:80%;}
.robot-line.tiny{width:40%;}
.robot-arm{position:absolute;width:28px;height:90px;background:linear-gradient(to bottom,#111,#0a0a0a);
  border:1px solid rgba(255,215,0,.1);border-radius:14px;top:80px;}
.robot-arm.l{left:-32px;transform:rotate(10deg);}
.robot-arm.r{right:-32px;transform:rotate(-10deg);}
.robot-leg{position:absolute;width:32px;height:55px;background:linear-gradient(to bottom,#111,#0a0a0a);
  border:1px solid rgba(255,215,0,.1);border-radius:10px;bottom:-52px;}
.robot-leg.l{left:38px;}
.robot-leg.r{right:38px;}
.robot-badge{position:absolute;top:-8px;right:-8px;background:#FFD700;color:#080808;
  font-family:'Syne',sans-serif;font-weight:800;font-size:.55rem;letter-spacing:.05em;
  padding:.25rem .5rem;border-radius:50px;}
.robot-bubble{position:absolute;background:rgba(255,215,0,.06);border:1px solid rgba(255,215,0,.15);
  border-radius:10px;padding:.5rem .75rem;font-size:.65rem;color:rgba(255,215,0,.8);white-space:nowrap;}
.rb1{top:10px;right:-130px;}
.rb2{bottom:40px;right:-140px;}
.rb3{bottom:80px;left:-150px;}
.robot-info{display:flex;flex-direction:column;gap:1.5rem;}
.robot-tag{font-size:.6rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(255,215,0,.45);margin-bottom:.5rem;display:flex;align-items:center;gap:.55rem;}
.robot-tag::before{content:'';width:18px;height:1px;background:rgba(255,215,0,.45);}
.robot-feat{display:flex;align-items:flex-start;gap:.85rem;padding:.9rem;
  background:rgba(255,255,255,.015);border:1px solid rgba(255,255,255,.04);
  border-radius:12px;transition:border-color .2s;}
.robot-feat:hover{border-color:rgba(255,215,0,.12);}
.robot-feat-icon{width:36px;height:36px;background:rgba(255,215,0,.06);
  border:1px solid rgba(255,215,0,.12);border-radius:9px;
  display:flex;align-items:center;justify-content:center;font-size:.9rem;flex-shrink:0;}
.robot-feat-title{font-family:'Syne',sans-serif;font-size:.82rem;font-weight:700;
  color:#F0EDE6;margin-bottom:.2rem;}
.robot-feat-desc{font-size:.73rem;color:rgba(240,237,230,.3);line-height:1.6;}

/* ── MARQUEE ── */
.mq-wrap{overflow:hidden;padding:.85rem 0;
  border-top:1px solid rgba(255,215,0,.06);border-bottom:1px solid rgba(255,215,0,.06);}
.mq-track{display:flex;gap:2.5rem;width:max-content;animation:marquee 32s linear infinite;}
.mq-item{font-size:.62rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:rgba(255,215,0,.3);display:flex;align-items:center;gap:.75rem;white-space:nowrap;}
.mq-dot{width:3px;height:3px;background:#FFD700;border-radius:50%;}

/* ── SECTIONS ── */
.sec{padding:6.5rem 5vw;max-width:1280px;margin:0 auto;}
.sec-lbl{font-size:.6rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(255,215,0,.45);margin-bottom:.75rem;display:flex;align-items:center;gap:.55rem;}
.sec-lbl::before{content:'';width:18px;height:1px;background:rgba(255,215,0,.45);}
.sec-title{font-family:'Syne',sans-serif;font-size:clamp(1.8rem,3.5vw,3rem);
  font-weight:800;letter-spacing:-.04em;line-height:1.08;margin-bottom:.85rem;color:#F0EDE6;}
.sec-sub{font-size:.93rem;color:rgba(240,237,230,.32);max-width:430px;line-height:1.88;font-weight:300;}
.div-line{height:1px;background:rgba(255,255,255,.04);}

/* ── SERVICE CARDS — 1 col mobile, 2 col tablet, 3 col desktop ── */
.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:3.8rem;
  border:1px solid rgba(255,255,255,.045);border-radius:20px;overflow:hidden;
  background:rgba(255,255,255,.04);}
.scard{background:#080808;padding:2rem;transition:background .22s;position:relative;overflow:hidden;}
.scard:hover{background:#0c0c0c;}
.scard::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,#FFD700,transparent);
  transform:scaleX(0);transform-origin:center;transition:transform .38s;}
.scard:hover::after{transform:scaleX(1);}
.cicon{width:40px;height:40px;background:rgba(255,215,0,.05);border:1px solid rgba(255,215,0,.1);
  border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:1.1rem;}
.ctitle{font-family:'Syne',sans-serif;font-size:.9rem;font-weight:700;margin-bottom:.38rem;color:#F0EDE6;}
.cdesc{font-size:.78rem;color:rgba(240,237,230,.32);line-height:1.72;}
.ctag{display:inline-block;margin-top:.85rem;font-size:.6rem;font-weight:700;letter-spacing:.06em;
  background:rgba(255,215,0,.04);color:rgba(255,215,0,.5);padding:.17rem .58rem;
  border-radius:50px;border:1px solid rgba(255,215,0,.1);}

/* ── ECOSYSTEM ── */
.eco-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;max-width:1280px;margin:0 auto;padding:6.5rem 5vw;}
.fblock{margin-bottom:1.5rem;}
.flbl{font-size:.56rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:rgba(240,237,230,.15);margin-bottom:.45rem;}
.fwrap{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.045);
  border-radius:11px;padding:.95rem 1.1rem;transition:border-color .22s;}
.fwrap:hover{border-color:rgba(255,215,0,.12);}
.frow{display:flex;align-items:center;gap:.4rem;flex-wrap:wrap;}
.fn{display:inline-flex;align-items:center;background:rgba(255,255,255,.03);
  border:1px solid rgba(255,255,255,.055);border-radius:6px;padding:.28rem .6rem;
  font-size:.7rem;font-weight:600;color:rgba(240,237,230,.5);white-space:nowrap;}
.fn.g{background:rgba(255,215,0,.05);border-color:rgba(255,215,0,.15);color:rgba(255,215,0,.75);}
.fn.e{background:#FFD700;color:#080808;border-color:#FFD700;font-weight:700;}
.fa{color:rgba(255,255,255,.12);font-size:.72rem;flex-shrink:0;}
.stepn{width:38px;height:38px;border-radius:50%;background:rgba(255,215,0,.05);
  border:1px solid rgba(255,215,0,.13);color:rgba(255,215,0,.75);font-family:'Syne',sans-serif;
  font-weight:800;font-size:.86rem;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.steptitle{font-family:'Syne',sans-serif;font-weight:700;font-size:.86rem;margin-bottom:.16rem;color:#F0EDE6;}
.stepdesc{font-size:.76rem;color:rgba(240,237,230,.28);line-height:1.65;}

/* ── SOCIAL PROOF ── */
.proof-section{background:#080808;padding:6rem 5vw;max-width:1280px;margin:0 auto;}
.proof-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:3rem;}
.proof-card{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);
  border-radius:18px;padding:1.8rem;position:relative;transition:border-color .2s;}
.proof-card:hover{border-color:rgba(255,215,0,.12);}
.proof-quote{font-size:.82rem;color:rgba(240,237,230,.55);line-height:1.75;margin-bottom:1.2rem;font-style:italic;}
.proof-quote::before{content:'\201C';font-size:2rem;color:rgba(255,215,0,.2);
  font-family:'Syne',sans-serif;line-height:0;vertical-align:-0.5rem;margin-right:.2rem;}
.proof-author{display:flex;align-items:center;gap:.75rem;}
.proof-avatar{width:38px;height:38px;border-radius:50%;background:rgba(255,215,0,.08);
  border:1px solid rgba(255,215,0,.15);display:flex;align-items:center;justify-content:center;
  font-size:1rem;flex-shrink:0;}
.proof-name{font-family:'Syne',sans-serif;font-size:.78rem;font-weight:700;color:#F0EDE6;}
.proof-role{font-size:.64rem;color:rgba(240,237,230,.25);margin-top:.1rem;}
.proof-stars{display:flex;gap:2px;margin-bottom:.85rem;}
.proof-star{color:#FFD700;font-size:.7rem;}
.proof-stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;
  margin-top:3rem;padding:2rem;background:rgba(255,215,0,.02);
  border:1px solid rgba(255,215,0,.07);border-radius:16px;}
.proof-stat-val{font-family:'Syne',sans-serif;font-size:2rem;font-weight:900;
  color:#FFD700;letter-spacing:-.04em;}
.proof-stat-lbl{font-size:.65rem;color:rgba(240,237,230,.3);margin-top:.25rem;line-height:1.5;}

/* ── ROI ── */
.roi-grid-outer{display:grid;grid-template-columns:1fr 1fr;gap:4rem;max-width:1280px;margin:0 auto;padding:0 5vw 6.5rem;}
.roi-box{background:rgba(255,255,255,.02);border:1px solid rgba(255,215,0,.08);border-radius:18px;padding:2.2rem;}
.roi-slbl{font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(240,237,230,.22);margin-bottom:.65rem;}
.roi-res{background:rgba(255,215,0,.035);border:1px solid rgba(255,215,0,.09);
  border-radius:11px;padding:1.3rem 1.5rem;margin-top:1.5rem;}
.roi-nums{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;}
.roi-val{font-family:'Syne',sans-serif;font-size:1.7rem;font-weight:800;color:#FFD700;letter-spacing:-.03em;}
.roi-lbl{font-size:.62rem;color:rgba(240,237,230,.25);margin-top:.2rem;letter-spacing:.03em;}
.roi-note{font-size:.6rem;color:rgba(240,237,230,.12);margin-top:.75rem;}
.task-item{display:flex;justify-content:space-between;align-items:center;
  padding:.6rem .85rem;background:rgba(255,255,255,.015);
  border:1px solid rgba(255,255,255,.04);border-radius:7px;margin-bottom:.45rem;}
.task-name{font-size:.76rem;color:rgba(240,237,230,.2);text-decoration:line-through;}
.task-gain{font-size:.63rem;font-weight:700;color:rgba(255,215,0,.65);background:rgba(255,215,0,.04);
  border:1px solid rgba(255,215,0,.1);padding:.13rem .5rem;border-radius:50px;white-space:nowrap;margin-left:.55rem;}

/* ── PRICING — 1 col mobile, 3 col desktop ── */
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:3.5rem;
  border:1px solid rgba(255,255,255,.045);border-radius:20px;overflow:hidden;
  background:rgba(255,255,255,.04);}
.pcard{background:#080808;padding:2.2rem;position:relative;transition:background .22s;}
.pcard:hover{background:#0c0c0c;}
.pcard.feat{background:rgba(255,215,0,.02);}
.pbadge{display:inline-flex;align-items:center;gap:.4rem;font-size:.58rem;font-weight:700;
  letter-spacing:.16em;text-transform:uppercase;background:rgba(255,215,0,.06);
  color:rgba(255,215,0,.6);padding:.18rem .65rem;border-radius:50px;margin-bottom:.9rem;
  border:1px solid rgba(255,215,0,.13);}
.pplan{font-family:'Syne',sans-serif;font-weight:800;font-size:1.4rem;margin-bottom:.25rem;color:#F0EDE6;}
.psub{font-size:.78rem;color:rgba(240,237,230,.28);margin-bottom:1.3rem;font-weight:300;}
.phighlight{background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.1);
  border-radius:9px;padding:.65rem .85rem;margin-bottom:1.3rem;font-size:.76rem;
  color:rgba(255,215,0,.65);line-height:1.58;font-style:italic;}
.pprice-custom{font-family:'Syne',sans-serif;font-size:1rem;font-weight:800;color:#F0EDE6;margin-bottom:.2rem;}
.pprice-note{font-size:.7rem;color:rgba(240,237,230,.2);margin-bottom:1.5rem;line-height:1.55;}
.pfeats{display:flex;flex-direction:column;gap:.52rem;margin-bottom:1.7rem;}
.pfeat{display:flex;align-items:flex-start;gap:.52rem;font-size:.78rem;color:rgba(240,237,230,.4);line-height:1.52;}
.pfeat.incl{color:rgba(240,237,230,.22);font-style:italic;}
.pcheck{color:rgba(255,215,0,.55);font-size:.7rem;flex-shrink:0;margin-top:.1rem;}
.pcheck.bright{color:#FFD700;}
.pcta{display:block;text-align:center;padding:.72rem 1.2rem;border-radius:50px;
  font-weight:700;font-size:.82rem;text-decoration:none;transition:all .2s;letter-spacing:.02em;}
.pcta-o{border:1px solid rgba(255,255,255,.09);color:rgba(240,237,230,.6);}
.pcta-o:hover{border-color:rgba(255,215,0,.32);color:#FFD700;}
.pcta-s{background:#FFD700;color:#080808;border:none;font-weight:800;}
.pcta-s:hover{box-shadow:0 8px 26px rgba(255,215,0,.38);transform:translateY(-1px);}
.pnote{font-size:.62rem;text-align:center;color:rgba(240,237,230,.13);margin-top:.75rem;}
.onglets-wrap{margin-bottom:1.2rem;}
.onglets-lbl{font-size:.6rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:rgba(255,215,0,.35);margin-bottom:.55rem;}
.onglets-tag{display:flex;flex-wrap:wrap;gap:.35rem;}
.otag{font-size:.58rem;font-weight:600;letter-spacing:.03em;background:rgba(255,255,255,.03);
  color:rgba(240,237,230,.28);padding:.18rem .52rem;border-radius:4px;
  border:1px solid rgba(255,255,255,.06);white-space:nowrap;}
.feat-divider{height:1px;background:rgba(255,255,255,.04);margin:.75rem 0;}

/* ── CTA BAND & FOOTER ── */
.cta-band{background:#FFD700;padding:6rem 5vw;text-align:center;}
.cta-band h2{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,5vw,4rem);
  font-weight:900;letter-spacing:-.05em;color:#080808;margin-bottom:2.5rem;line-height:1.02;}
.ibtn{display:inline-flex;align-items:center;gap:.7rem;background:#080808;color:#FFD700;
  font-weight:700;font-size:.92rem;padding:.92rem 2.3rem;border-radius:50px;text-decoration:none;
  transition:transform .2s,box-shadow .2s;}
.ibtn:hover{transform:translateY(-2px);box-shadow:0 10px 34px rgba(0,0,0,.28);}
.ft{padding:2rem 5vw;display:flex;align-items:center;justify-content:space-between;
  flex-wrap:wrap;gap:1.2rem;background:#080808;border-top:1px solid rgba(255,255,255,.04);}
.ft-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:.92rem;
  letter-spacing:-.03em;display:flex;align-items:center;gap:.45rem;color:#F0EDE6;}
.ft-tag{font-size:.68rem;color:rgba(240,237,230,.18);margin-top:.2rem;}
.ft-links{display:flex;gap:1.8rem;}
.ft-links a{font-size:.7rem;color:rgba(240,237,230,.22);text-decoration:none;transition:color .2s;}
.ft-links a:hover{color:#FFD700;}
.ft-badge{font-size:.62rem;background:rgba(255,215,0,.05);color:rgba(255,215,0,.5);
  padding:.2rem .68px;border-radius:50px;font-weight:700;border:1px solid rgba(255,215,0,.1);}

/* ── SLIDER STYLING ── */
div[data-testid="stSlider"]{padding:0 5vw;max-width:1280px;margin:0 auto;}
div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"]{background:#FFD700!important;border:none!important;box-shadow:0 0 0 4px rgba(255,215,0,.18)!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:nth-child(2){background:#FFD700!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:first-child{background:rgba(255,255,255,.07)!important;}
div[data-testid="stSlider"] label p{color:rgba(240,237,230,.25)!important;font-size:.6rem!important;letter-spacing:.2em!important;text-transform:uppercase!important;}

/* ════════════════════════════════════════
   RESPONSIVE MOBILE  (< 768px)
   ════════════════════════════════════════ */
@media(max-width:768px){
  /* Nav */
  .nav{padding:.85rem 5vw;}
  .nav-links{display:none;}
  .nav-hamburger{display:flex;}

  /* Hero */
  .hero{padding:7rem 5vw 4rem;}
  .hero-title{font-size:clamp(2.4rem,11vw,4rem);letter-spacing:-.04em;line-height:1;}
  .hero-sub{font-size:.95rem;}
  .hero-info{gap:1.2rem;}
  .hero-sep{display:none;}
  .hero-info-item{flex-direction:row;align-items:center;gap:.5rem;}
  .hero-info-label{font-size:.5rem;}
  .hero-info-val{font-size:.8rem;}
  .hero-cta-row{flex-direction:column;width:100%;}
  .btn-y{width:100%;text-align:center;}
  .scroll-hint{display:none;}

  /* Robot section */
  .robot-wrap{grid-template-columns:1fr;gap:2.5rem;}
  .robot-visual{margin-bottom:1rem;}
  .rb1,.rb2,.rb3{display:none;}

  /* Services grid: 1 col */
  .cgrid{grid-template-columns:1fr;border-radius:14px;}
  .scard{padding:1.5rem;}

  /* Ecosystem */
  .eco-grid{grid-template-columns:1fr;gap:2.5rem;padding:4rem 5vw;}

  /* Social proof */
  .proof-grid{grid-template-columns:1fr;}
  .proof-stat-row{grid-template-columns:1fr;gap:1rem;text-align:center;}

  /* ROI */
  .roi-grid-outer{grid-template-columns:1fr;gap:2rem;padding:0 5vw 4rem;}

  /* Pricing: 1 col */
  .pgrid{grid-template-columns:1fr;border-radius:14px;}
  .pcard{padding:1.8rem;}

  /* Sections */
  .sec{padding:4rem 5vw;}
  .robot-section{padding:3rem 5vw;}
  .proof-section{padding:4rem 5vw;}

  /* Footer */
  .ft{flex-direction:column;align-items:flex-start;gap:.85rem;}
  .ft-links{flex-wrap:wrap;gap:1rem;}
}

/* Tablet (768–1024px) : 2 colonnes */
@media(min-width:768px) and (max-width:1024px){
  .cgrid{grid-template-columns:repeat(2,1fr);}
  .pgrid{grid-template-columns:repeat(2,1fr);}
  .proof-grid{grid-template-columns:repeat(2,1fr);}
  .robot-wrap{gap:2rem;}
  .eco-grid{gap:3rem;}
}
</style>
"""

HERO = """
<nav class="nav">
  <a class="nav-logo" href="#"><div class="bolt"></div>Floxia</a>
  <div class="nav-links">
    <a href="javascript:void(0)" onclick="document.getElementById('services-anchor').scrollIntoView({behavior:'smooth'})">Services</a>
    <a href="javascript:void(0)" onclick="document.getElementById('ecosystem-anchor').scrollIntoView({behavior:'smooth'})">&#201;cosyst&#232;me</a>
    <a href="javascript:void(0)" onclick="document.getElementById('roi-anchor').scrollIntoView({behavior:'smooth'})">ROI</a>
    <a href="javascript:void(0)" onclick="document.getElementById('tarifs-anchor').scrollIntoView({behavior:'smooth'})">Tarifs</a>
    <a href="https://www.instagram.com/floxia.pro/" target="_blank" class="nav-cta">D&#233;mo &#8594;</a>
  </div>
  <div class="nav-hamburger" onclick="this.classList.toggle('open');document.getElementById('mob-menu').classList.toggle('open')">
    <span></span><span></span><span></span>
  </div>
</nav>

<!-- Mobile menu -->
<div id="mob-menu" style="display:none;position:fixed;top:58px;left:0;right:0;z-index:9998;
  background:rgba(8,8,8,.97);padding:1.5rem 5vw;border-bottom:1px solid rgba(255,255,255,.06);
  flex-direction:column;gap:1.2rem;">
  <a href="javascript:void(0)" onclick="document.getElementById('services-anchor').scrollIntoView({behavior:'smooth'});document.getElementById('mob-menu').style.display='none';"
    style="font-size:.88rem;color:rgba(240,237,230,.55);text-decoration:none;letter-spacing:.06em;text-transform:uppercase;">Services</a>
  <a href="javascript:void(0)" onclick="document.getElementById('ecosystem-anchor').scrollIntoView({behavior:'smooth'});document.getElementById('mob-menu').style.display='none';"
    style="font-size:.88rem;color:rgba(240,237,230,.55);text-decoration:none;letter-spacing:.06em;text-transform:uppercase;">&#201;cosyst&#232;me</a>
  <a href="javascript:void(0)" onclick="document.getElementById('roi-anchor').scrollIntoView({behavior:'smooth'});document.getElementById('mob-menu').style.display='none';"
    style="font-size:.88rem;color:rgba(240,237,230,.55);text-decoration:none;letter-spacing:.06em;text-transform:uppercase;">ROI</a>
  <a href="javascript:void(0)" onclick="document.getElementById('tarifs-anchor').scrollIntoView({behavior:'smooth'});document.getElementById('mob-menu').style.display='none';"
    style="font-size:.88rem;color:rgba(240,237,230,.55);text-decoration:none;letter-spacing:.06em;text-transform:uppercase;">Tarifs</a>
  <a href="https://www.instagram.com/floxia.pro/" target="_blank"
    style="font-size:.88rem;font-weight:700;color:#FFD700;text-decoration:none;">&#x26A1; R&#233;server une d&#233;mo</a>
</div>
<script>
document.querySelector('.nav-hamburger').addEventListener('click',function(){
  var m=document.getElementById('mob-menu');
  m.style.display=(m.style.display==='flex'?'none':'flex');
});
</script>

<section class="hero">
  <div class="hero-grid"></div>
  <div class="hero-scan"></div>
  <div class="hero-orb"></div>
  <div class="hero-badge"><div class="hero-badge-dot"></div>IA pour artisans &amp; PME du b&#226;timent</div>
  <h1 class="hero-title">
    Votre admin.<br>
    <span class="outline anim" id="animWord">Automatis&#233;e.</span><br>
    Votre temps. Rendu.
  </h1>
  <p class="hero-sub">
    G&#233;n&#233;rez vos <strong>devis et factures depuis WhatsApp en 3&#160;minutes</strong>.<br>
    Un vocal suffit — Floxia s'occupe du reste.
  </p>
  <div class="hero-info">
    <div class="hero-info-item"><span class="hero-info-label">Temps lib&#233;r&#233;</span><span class="hero-info-val">16h / mois</span></div>
    <div class="hero-sep"></div>
    <div class="hero-info-item"><span class="hero-info-label">Saisie admin</span><span class="hero-info-val">&#8722;80%</span></div>
    <div class="hero-sep"></div>
    <div class="hero-info-item"><span class="hero-info-label">Devis &#8594; Facture</span><span class="hero-info-val">3 minutes</span></div>
    <div class="hero-sep"></div>
    <div class="hero-info-item"><span class="hero-info-label">Interface</span><span class="hero-info-val">WhatsApp + ERP</span></div>
  </div>
  <div class="hero-cta-row">
    <a class="btn-y" href="https://www.instagram.com/floxia.pro/" target="_blank">&#x26A1; R&#233;server une d&#233;mo</a>
    <a class="btn-g" href="javascript:void(0)" onclick="document.getElementById('services-anchor').scrollIntoView({behavior:'smooth'})">D&#233;couvrir &#8594;</a>
  </div>
  <div class="scroll-hint"><span class="scroll-txt">Scroll</span><div class="scroll-line"></div></div>
</section>

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
"""

ROBOT_SECTION = """
<div style="background:#080808;">
<div class="robot-section">
  <div class="robot-wrap">
    <div class="robot-visual">
      <div style="position:relative;display:inline-block;">
        <div class="robot-body">
          <div class="robot-head">
            <div class="robot-eye"></div>
            <div class="robot-eye r"></div>
          </div>
          <div class="robot-screen">
            <div class="robot-line gold"></div>
            <div class="robot-line short"></div>
            <div class="robot-line"></div>
            <div class="robot-line tiny"></div>
            <div class="robot-line gold short"></div>
            <div class="robot-line"></div>
          </div>
          <div class="robot-arm l"></div>
          <div class="robot-arm r"></div>
          <div class="robot-leg l"></div>
          <div class="robot-leg r"></div>
          <div class="robot-badge">ERP IA</div>
        </div>
        <div class="robot-bubble rb1">&#x1F4AC; Devis g&#233;n&#233;r&#233; &#x2705;</div>
        <div class="robot-bubble rb2">&#x1F9FE; Facture envoy&#233;e &#x26A1;</div>
        <div class="robot-bubble rb3">&#x2B50; Avis Google demand&#233;</div>
      </div>
    </div>
    <div class="robot-info">
      <div class="robot-tag">Votre robot ERP</div>
      <h2 style="font-family:'Syne',sans-serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:800;letter-spacing:-.04em;color:#F0EDE6;margin-bottom:.6rem;line-height:1.1;">
        Un robot IA qui travaille<br>&#224; votre place. 24h/24.
      </h2>
      <p style="font-size:.88rem;color:rgba(240,237,230,.3);line-height:1.8;margin-bottom:1.8rem;font-weight:300;">
        Floxia c'est votre ERP intelligent connect&#233; &#224; WhatsApp. Il re&#231;oit vos messages vocaux,
        comprend ce que vous demandez, et ex&#233;cute : devis, PV, facture, relance, rapport.
        Sans que vous ayez rien &#224; taper.
      </p>
      <div class="robot-feat">
        <div class="robot-feat-icon">&#x1F4AC;</div>
        <div>
          <div class="robot-feat-title">Parlez, il g&#233;n&#232;re</div>
          <div class="robot-feat-desc">Un message vocal WhatsApp → devis PDF en 3 minutes, envoy&#233; automatiquement au client.</div>
        </div>
      </div>
      <div class="robot-feat" style="margin-top:.75rem;">
        <div class="robot-feat-icon">&#x1F4CB;</div>
        <div>
          <div class="robot-feat-title">ERP complet sur votre t&#233;l&#233;phone</div>
          <div class="robot-feat-desc">Tableau de bord, chantiers, planning, salari&#233;s, comptabilit&#233; — tout en temps r&#233;el depuis votre mobile.</div>
        </div>
      </div>
      <div class="robot-feat" style="margin-top:.75rem;">
        <div class="robot-feat-icon">&#x1F916;</div>
        <div>
          <div class="robot-feat-title">Il ne dort jamais</div>
          <div class="robot-feat-desc">Relances J+3/J+7/J+14, avis Google apr&#232;s chaque chantier, alertes retard — tout automatique.</div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>
<div class="div-line"></div>
"""

SERVICES = """
<div id="services-anchor" style="background:#080808;">
<div class="sec">
  <div class="sec-lbl">Ce que fait Floxia</div>
  <h2 class="sec-title">Tout votre flux de travail,<br>automatis&#233; de A &#224; Z.</h2>
  <p class="sec-sub">Des automatisations concr&#232;tes, op&#233;rationnelles d&#232;s aujourd'hui.</p>
  <div class="cgrid">
    <div class="scard"><div class="cicon">&#x1F4AC;</div><div class="ctitle">Devis &#8594; PV &#8594; Facture</div><div class="cdesc">Un vocal WhatsApp suffit. Floxia g&#233;n&#232;re le devis PDF, le client signe, le PV de r&#233;ception est cr&#233;&#233;, et la facture finale se g&#233;n&#232;re automatiquement.</div><span class="ctag">&#x26A1; Cycle complet g&#233;r&#233;</span></div>
    <div class="scard"><div class="cicon">&#x1F4F8;</div><div class="ctitle">Scan Tickets de Caisse</div><div class="cdesc">Photographiez vos tickets sur WhatsApp. L'IA extrait fournisseur, articles, montants HT/TVA et alimente votre comptabilit&#233; instantan&#233;ment.</div><span class="ctag">&#x26A1; Z&#233;ro ressaisie</span></div>
    <div class="scard"><div class="cicon">&#x2B50;</div><div class="ctitle">Avis Google Maps</div><div class="cdesc">&#192; chaque chantier termin&#233;, Floxia envoie automatiquement un message WhatsApp au client pour l'inviter &#224; laisser un avis Google &#224; la facture finale.</div><span class="ctag">&#x26A1; R&#233;putation boost&#233;e</span></div>
    <div class="scard"><div class="cicon">&#x1F6A8;</div><div class="ctitle">Alerte Probl&#232;me Chantier</div><div class="cdesc">Un probl&#232;me&#160;? Envoyez un vocal. Floxia r&#233;dige l'e-mail professionnel au client&#160;: situation, causes, nouveau d&#233;lai.</div><span class="ctag">&#x26A1; Email en 30&#160;sec</span></div>
    <div class="scard"><div class="cicon">&#x1F514;</div><div class="ctitle">Relances Automatiques</div><div class="cdesc">Floxia surveille vos devis non sign&#233;s et relance automatiquement en 3 temps&#160;: J+3, J+7, J+14 apr&#232;s la date de cr&#233;ation du devis.</div><span class="ctag">&#x26A1; +30&#160;% de conversion</span></div>
    <div class="scard"><div class="cicon">&#x1F4CB;</div><div class="ctitle">ERP Mobile Complet</div><div class="cdesc">Devis, factures, PV, chantiers, planning, salari&#233;s, d&#233;penses &#8212; tout synchronis&#233; en temps r&#233;el via votre ERP d&#233;di&#233;, accessible depuis votre t&#233;l&#233;phone.</div><span class="ctag">&#x26A1; Tout en un seul endroit</span></div>
    <div class="scard"><div class="cicon">&#x1F399;</div><div class="ctitle">Rapports Vocaux Chantier</div><div class="cdesc">Dictez votre rapport en 2&#160;minutes. Floxia le structure et l'envoie au client sous forme de compte-rendu professionnel en PDF.</div><span class="ctag">&#x26A1; Rapport en 2&#160;min</span></div>
    <div class="scard"><div class="cicon">&#x1F4B0;</div><div class="ctitle">Suivi D&#233;penses &amp; TVA</div><div class="cdesc">Chaque ticket scann&#233; alimente votre tableau de bord&#160;: d&#233;penses par cat&#233;gorie, TVA r&#233;cup&#233;rable, export comptable en 1&#160;clic.</div><span class="ctag">&#x26A1; Compta simplifi&#233;e</span></div>
    <div class="scard"><div class="cicon">&#x1F465;</div><div class="ctitle">Gestion &#201;quipe &amp; Salari&#233;s</div><div class="cdesc">Suivez les heures de vos collaborateurs, assignez les chantiers, g&#233;rez le planning en temps r&#233;el. Tout synchronis&#233; avec votre Google Sheets.</div><span class="ctag">&#x26A1; &#201;quipe pilot&#233;e depuis WA</span></div>
  </div>
</div>
</div>
<div class="div-line"></div>
"""

ECOSYSTEM = """
<div id="ecosystem-anchor" style="background:#080808;">
<div class="eco-grid">
  <div>
    <div class="sec-lbl">Comment &#231;a marche</div>
    <h2 class="sec-title">WhatsApp comme<br>centre de commandes.</h2>
    <p class="sec-sub" style="margin-bottom:2.6rem;">Tout part de votre t&#233;l&#233;phone. Aucun logiciel &#224; apprendre. Floxia fait le reste.</p>
    <div style="display:flex;flex-direction:column;gap:1.3rem;">
      <div style="display:flex;align-items:flex-start;gap:1rem;"><div class="stepn">1</div><div><div class="steptitle">Une fois connect&#233;</div><div class="stepdesc">WhatsApp Business, Gmail, Google Drive &#8212; tout est pr&#234;t, on s'en occupe.</div></div></div>
      <div style="display:flex;align-items:flex-start;gap:1rem;"><div class="stepn">2</div><div><div class="steptitle">Parlez ou photographiez</div><div class="stepdesc">Vocal ou photo sur WhatsApp. Floxia comprend et agit instantan&#233;ment.</div></div></div>
      <div style="display:flex;align-items:flex-start;gap:1rem;"><div class="stepn">3</div><div><div class="steptitle">L'IA travaille pour vous</div><div class="stepdesc">Devis envoy&#233;, PV g&#233;n&#233;r&#233;, facture &#233;mise, ticket enregistr&#233;. Automatiquement.</div></div></div>
      <div style="display:flex;align-items:flex-start;gap:1rem;"><div class="stepn">4</div><div><div class="steptitle">Pilotez depuis l'ERP</div><div class="stepdesc">Tableau de bord temps r&#233;el&#160;: CA, planning, salari&#233;s, d&#233;penses, facturation.</div></div></div>
    </div>
  </div>
  <div>
    <div class="fblock"><div class="flbl">Flux 1 &#8212; Cycle devis complet</div><div class="fwrap"><div class="frow"><div class="fn">&#x1F399; Vocal WA</div><div class="fa">&#8594;</div><div class="fn g">&#x26A1; IA Floxia</div><div class="fa">&#8594;</div><div class="fn">&#x1F4C4; Devis PDF</div><div class="fa">&#8594;</div><div class="fn">&#x270D; Signature</div><div class="fa">&#8594;</div><div class="fn">&#x1F4CB; PV</div><div class="fa">&#8594;</div><div class="fn e">&#x1F9FE; Facture</div></div></div></div>
    <div class="fblock"><div class="flbl">Flux 2 &#8212; Avis Google Maps</div><div class="fwrap"><div class="frow"><div class="fn">&#x2705; Chantier termin&#233;</div><div class="fa">&#8594;</div><div class="fn g">&#x26A1; Floxia d&#233;tecte</div><div class="fa">&#8594;</div><div class="fn">&#x1F4AC; Message WA</div><div class="fa">&#8594;</div><div class="fn e">&#x2B50; Avis Google</div></div></div></div>
    <div class="fblock"><div class="flbl">Flux 3 &#8212; Ticket de caisse</div><div class="fwrap"><div class="frow"><div class="fn">&#x1F4F8; Photo WA</div><div class="fa">&#8594;</div><div class="fn g">&#x26A1; OCR IA</div><div class="fa">&#8594;</div><div class="fn">&#x1F4CA; Google Sheets</div><div class="fa">&#8594;</div><div class="fn e">&#x2705; Compta</div></div></div></div>
    <div class="fblock"><div class="flbl">Flux 4 &#8212; Probl&#232;me chantier</div><div class="fwrap"><div class="frow"><div class="fn">&#x1F6A8; Vocal WA</div><div class="fa">&#8594;</div><div class="fn g">&#x26A1; IA r&#233;daction</div><div class="fa">&#8594;</div><div class="fn e">&#x1F4E7; Email client</div></div></div></div>
    <div class="fblock"><div class="flbl">Flux 5 &#8212; Relances devis (J+3 / J+7 / J+14)</div><div class="fwrap"><div class="frow"><div class="fn">&#x23F0; D&#233;lai d&#233;pass&#233;</div><div class="fa">&#8594;</div><div class="fn g">&#x26A1; Floxia d&#233;tecte</div><div class="fa">&#8594;</div><div class="fn e">&#x1F4AC; SMS + Email</div></div></div></div>
  </div>
</div>
</div>
<div class="div-line"></div>
"""

SOCIAL_PROOF = """
<div style="background:#080808;">
<div class="proof-section">
  <div class="sec-lbl">Ils utilisent Floxia</div>
  <h2 class="sec-title">Des artisans qui ont<br>repris leur temps.</h2>

  <div class="proof-stat-row">
    <div>
      <div class="proof-stat-val">+30%</div>
      <div class="proof-stat-lbl">de devis sign&#233;s<br>gr&#226;ce aux relances automatiques</div>
    </div>
    <div>
      <div class="proof-stat-val">16h</div>
      <div class="proof-stat-lbl">lib&#233;r&#233;es par mois<br>en moyenne par artisan</div>
    </div>
    <div>
      <div class="proof-stat-val">&#8722;80%</div>
      <div class="proof-stat-lbl">de saisie administrative<br>d&#232;s le premier mois</div>
    </div>
  </div>

  <div class="proof-grid" style="margin-top:2.5rem;">
    <div class="proof-card">
      <div class="proof-stars">
        <span class="proof-star">&#x2605;</span><span class="proof-star">&#x2605;</span>
        <span class="proof-star">&#x2605;</span><span class="proof-star">&#x2605;</span>
        <span class="proof-star">&#x2605;</span>
      </div>
      <div class="proof-quote">
        Avant je passais mes soir&#233;es &#224; taper des devis. Maintenant j'envoie un vocal depuis le chantier et c'est pli&#233;. Mes clients re&#231;oivent le PDF dans la minute.
      </div>
      <div class="proof-author">
        <div class="proof-avatar">&#x1F477;</div>
        <div>
          <div class="proof-name">Karim B.</div>
          <div class="proof-role">Pl&#226;trier-peintre &#183; Seine-et-Marne</div>
        </div>
      </div>
    </div>
    <div class="proof-card">
      <div class="proof-stars">
        <span class="proof-star">&#x2605;</span><span class="proof-star">&#x2605;</span>
        <span class="proof-star">&#x2605;</span><span class="proof-star">&#x2605;</span>
        <span class="proof-star">&#x2605;</span>
      </div>
      <div class="proof-quote">
        J'ai r&#233;cup&#233;r&#233; 3 devis gr&#226;ce aux relances automatiques que j'aurais jamais relanc&#233;s moi-m&#234;me. Le ROI est imm&#233;diat.
      </div>
      <div class="proof-author">
        <div class="proof-avatar">&#x1F6E0;</div>
        <div>
          <div class="proof-name">Thomas M.</div>
          <div class="proof-role">Plombier chauffagiste &#183; Val-de-Marne</div>
        </div>
      </div>
    </div>
    <div class="proof-card">
      <div class="proof-stars">
        <span class="proof-star">&#x2605;</span><span class="proof-star">&#x2605;</span>
        <span class="proof-star">&#x2605;</span><span class="proof-star">&#x2605;</span>
        <span class="proof-star">&#x2605;</span>
      </div>
      <div class="proof-quote">
        Mon comptable est bluff&#233;. Je lui envoie l'export en 1 clic chaque mois. Fini les tickets de caisse qui tra&#238;nent partout.
      </div>
      <div class="proof-author">
        <div class="proof-avatar">&#x26CF;</div>
        <div>
          <div class="proof-name">S&#233;bastien R.</div>
          <div class="proof-role">Ma&#231;on-carreleur &#183; Essonne</div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>
<div class="div-line"></div>
"""

ROI_INTRO = """
<div id="roi-anchor" style="background:#080808;">
<div class="sec" style="padding-bottom:2rem;">
  <div class="sec-lbl">Simulateur ROI</div>
  <h2 class="sec-title">Calculez votre<br>temps lib&#233;r&#233;.</h2>
  <p class="sec-sub">Bougez le curseur &#8212; voyez ce que Floxia vous rapporte chaque mois.</p>
</div>
</div>
"""

TARIFS_AND_FOOTER = """
<div class="div-line"></div>
<div id="tarifs-anchor" style="background:#080808;">
<div class="sec">
  <div class="sec-lbl">Tarifs</div>
  <h2 class="sec-title">Un prix adapt&#233;<br>&#224; votre activit&#233;.</h2>
  <p class="sec-sub">Chaque tarif est personnalis&#233; selon votre volume de devis et vos besoins. Contactez-nous pour une offre sur mesure.</p>
  <div class="pgrid">
    <div class="pcard">
      <div class="pbadge">Offre 1</div>
      <div class="pplan">Essentiel</div>
      <div class="psub">Num&#233;risation administrative &#183; WhatsApp</div>
      <div class="phighlight">Id&#233;al pour d&#233;marrer&#160;: base de donn&#233;es, documents automatiques et conformit&#233; 2026.</div>
      <div class="pprice-custom">Prix personnalis&#233;</div>
      <div class="pprice-note">Calcul&#233; selon votre volume de devis.<br>Sans engagement &#183; r&#233;siliable &#224; tout moment.</div>
      <div class="pfeats">
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Base de donn&#233;es Google Sheets d&#233;di&#233;e</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Cr&#233;ation automatique de Devis PDF</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Factures &amp; Factures d'acompte auto</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>PV de r&#233;ception automatis&#233;</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Archivage structur&#233; Google Drive</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Envoi via API WhatsApp Business</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Signature &#233;lectronique int&#233;gr&#233;e</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Conforme r&#233;forme facturation 2026</div>
      </div>
      <a class="pcta pcta-o" href="https://www.instagram.com/floxia.pro/" target="_blank">Obtenir mon tarif &#8594;</a>
      <div class="pnote">Pour se lancer sans risque</div>
    </div>
    <div class="pcard feat">
      <div class="pbadge">&#x26A1; Le plus populaire &#183; Offre 2</div>
      <div class="pplan">L'Artisan Autonome</div>
      <div class="psub">Inclus Offre 1 &#183; WhatsApp &amp; ERP Web</div>
      <div class="phighlight">Tout l'Essentiel + votre ERP d&#233;di&#233; pour piloter votre activit&#233; en autonomie compl&#232;te.</div>
      <div class="pprice-custom">Prix personnalis&#233;</div>
      <div class="pprice-note">Calcul&#233; selon votre volume de devis.<br>Sans engagement &#183; r&#233;siliable &#224; tout moment.</div>
      <div class="pfeats">
        <div class="pfeat incl"><span class="pcheck">&#x2B06;</span>Tout de l'Offre Essentiel</div>
        <div class="feat-divider"></div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>ERP d&#233;di&#233; sur votre mobile</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Gestion des retards &amp; avenants</div>
      </div>
      <div class="onglets-wrap">
        <div class="onglets-lbl">Onglets disponibles</div>
        <div class="onglets-tag">
          <span class="otag">Vue g&#233;n&#233;rale</span><span class="otag">Cr&#233;er un devis</span>
          <span class="otag">Devis</span><span class="otag">Facture &amp; Paiements</span>
          <span class="otag">Export compta 1 clic</span><span class="otag">Chantier</span>
          <span class="otag">Planning</span><span class="otag">Notifications</span>
          <span class="otag">Espace Clients</span><span class="otag">Tous les dossiers</span>
          <span class="otag">Google Sheet</span><span class="otag">Retards &amp; Avenants</span>
          <span class="otag">Coordonn&#233;es &amp; RGPD</span>
        </div>
      </div>
      <a class="pcta pcta-s" href="https://www.instagram.com/floxia.pro/" target="_blank">Obtenir mon tarif &#8594;</a>
      <div class="pnote">Le meilleur rapport qualit&#233; / valeur</div>
    </div>
    <div class="pcard">
      <div class="pbadge">Offre 3</div>
      <div class="pplan">Premium</div>
      <div class="psub">Inclus Offre 1 + 2 &#183; &#201;quipe &amp; IA avanc&#233;e</div>
      <div class="phighlight">Gestion d'&#233;quipe, IA vocale, rentabilit&#233; r&#233;elle et relances intelligentes &#8212; la puissance compl&#232;te.</div>
      <div class="pprice-custom">Prix personnalis&#233;</div>
      <div class="pprice-note">Calcul&#233; selon votre &#233;quipe et vos besoins.<br>Accompagnement d&#233;di&#233; inclus.</div>
      <div class="pfeats">
        <div class="pfeat incl"><span class="pcheck">&#x2B06;</span>Tout de l'Offre Artisan Autonome</div>
        <div class="feat-divider"></div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Saisie vocale IA via WhatsApp (devis)</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Collecte &amp; classement photos fin de chantier</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Suivi heures collaborateurs</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Rentabilit&#233; r&#233;elle IA (CA &#8722; D&#233;penses)</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Scan tickets caisse &#8594; compta auto</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Email professionnel depuis vocal (impr&#233;vus)</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Relances devis J+3 / J+7 / J+14</div>
        <div class="pfeat"><span class="pcheck bright">&#x2736;</span>Demande d'avis Google &#224; la facture finale</div>
      </div>
      <div class="onglets-wrap">
        <div class="onglets-lbl">Onglets suppl&#233;mentaires</div>
        <div class="onglets-tag">
          <span class="otag">D&#233;penses</span><span class="otag">Salari&#233;s</span>
        </div>
      </div>
      <a class="pcta pcta-o" href="https://www.instagram.com/floxia.pro/" target="_blank">Nous contacter &#8594;</a>
      <div class="pnote">Pour les &#233;quipes &amp; PME du b&#226;timent</div>
    </div>
  </div>
</div>
</div>

<div id="contact" class="cta-band">
  <h2>Pr&#234;t &#224; r&#233;cup&#233;rer<br>votre temps&#160;?</h2>
  <a class="ibtn" href="https://www.instagram.com/floxia.pro/" target="_blank">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
      <rect x="2" y="2" width="20" height="20" rx="5" stroke="#FFD700" stroke-width="1.8"/>
      <circle cx="12" cy="12" r="4.5" stroke="#FFD700" stroke-width="1.8"/>
      <circle cx="17.5" cy="6.5" r="1" fill="#FFD700"/>
    </svg>
    R&#233;server une d&#233;mo &#8212; Instagram
  </a>
  <div style="margin-top:1rem;font-size:.7rem;color:rgba(8,8,8,.35);font-weight:500;">@floxia.pro &#183; R&#233;ponse sous 24h</div>
</div>

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

<script>
(function(){
  var words=["Automatis\u00e9e.","Acc\u00e9l\u00e9r\u00e9e.","Lib\u00e9r\u00e9e.","Intelligente.","Optimis\u00e9e."];
  var el=document.getElementById('animWord');
  if(!el)return;
  var i=0;
  setInterval(function(){
    el.style.opacity='0';el.style.transform='translateY(18px)';
    el.style.transition='opacity .28s ease,transform .28s ease';
    setTimeout(function(){
      i=(i+1)%words.length;el.innerHTML=words[i];
      el.style.opacity='1';el.style.transform='translateY(0)';
    },300);
  },2600);
  var cur=document.createElement('div');
  cur.style.cssText='position:fixed;width:10px;height:10px;background:#FFD700;border-radius:50%;pointer-events:none;z-index:99999;transform:translate(-50%,-50%);transition:transform .08s;mix-blend-mode:difference;top:-20px;left:-20px;';
  var ring=document.createElement('div');
  ring.style.cssText='position:fixed;width:32px;height:32px;border:1px solid rgba(255,215,0,.35);border-radius:50%;pointer-events:none;z-index:99998;transform:translate(-50%,-50%);top:-20px;left:-20px;transition:top .1s ease,left .1s ease;';
  document.body.appendChild(cur);document.body.appendChild(ring);
  document.addEventListener('mousemove',function(e){cur.style.left=e.clientX+'px';cur.style.top=e.clientY+'px';ring.style.left=e.clientX+'px';ring.style.top=e.clientY+'px';});
  document.addEventListener('mousedown',function(){cur.style.transform='translate(-50%,-50%) scale(2)';});
  document.addEventListener('mouseup',function(){cur.style.transform='translate(-50%,-50%) scale(1)';});
})();
</script>
"""

# ── Render ──
st.markdown(CSS + HERO + ROBOT_SECTION + SERVICES + ECOSYSTEM + SOCIAL_PROOF + ROI_INTRO, unsafe_allow_html=True)

# ── ROI Slider ──
nb_devis = st.slider("Nombre de devis par mois", min_value=1, max_value=80, value=15, step=1)

h_devis    = round((45 + 12) * nb_devis / 60, 1)
h_tickets  = 8
h_planning = 4
h_rapports = round(18 * nb_devis / 60, 1)
h = round(h_devis + h_tickets + h_planning + h_rapports, 1)

cycle_sans = 60
cycle_avec = 3
cycle_gain_h = round((cycle_sans - cycle_avec) * nb_devis / 60, 1)

g   = round(h * 55)
abo = 49 if nb_devis <= 10 else (99 if nb_devis <= 30 else 149)
roi = round((g / abo) * 100)

roi_html = f"""
<div style="background:#080808;">
<div class="roi-grid-outer">
  <div class="roi-box">
    <div class="roi-slbl">R&#233;sultats pour {nb_devis} devis / mois</div>
    <div class="roi-res">
      <div class="roi-nums">
        <div><div class="roi-val">{h}h</div><div class="roi-lbl">temps lib&#233;r&#233;</div></div>
        <div><div class="roi-val">{g}&#8364;</div><div class="roi-lbl">valeur r&#233;cup&#233;r&#233;e</div></div>
        <div><div class="roi-val">{roi}%</div><div class="roi-lbl">ROI estim&#233;</div></div>
      </div>
    </div>
    <div style="margin-top:1rem;background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.09);border-radius:9px;padding:.85rem 1rem;">
      <div style="font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,215,0,.4);margin-bottom:.55rem;">&#x26A1; Cycle devis &#8594; facture finale</div>
      <div style="display:flex;gap:1.5rem;flex-wrap:wrap;">
        <div><div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;">{cycle_gain_h}h</div><div style="font-size:.62rem;color:rgba(240,237,230,.25);">&#233;conomis&#233;es / mois</div></div>
        <div><div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;">3&#160;min</div><div style="font-size:.62rem;color:rgba(240,237,230,.25);">au lieu de 60&#160;min</div></div>
        <div><div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:#FFD700;">&#8722;95%</div><div style="font-size:.62rem;color:rgba(240,237,230,.25);">de temps admin</div></div>
      </div>
    </div>
    <div class="roi-note" style="margin-top:.6rem;">*55&#8364;/h artisan &#183; estimation mensuelle.</div>
  </div>
  <div>
    <div class="sec-lbl" style="margin-bottom:1rem;">Ce que vous ne faites plus</div>
    <div class="task-item"><div class="task-name">Cycle devis &#8594; PV &#8594; facture finale</div><div class="task-gain">{cycle_gain_h}h &#233;conomis&#233;es / mois</div></div>
    <div class="task-item"><div class="task-name">Taper des devis le soir</div><div class="task-gain">45&#160;min &#233;vit&#233;es / devis</div></div>
    <div class="task-item"><div class="task-name">Ressaisir les tickets de caisse</div><div class="task-gain">2h / semaine r&#233;cup&#233;r&#233;es</div></div>
    <div class="task-item"><div class="task-name">R&#233;diger des e-mails clients</div><div class="task-gain">30&#160;min / incident</div></div>
    <div class="task-item"><div class="task-name">Relancer les devis manuellement</div><div class="task-gain">+30% de conversion</div></div>
    <div class="task-item"><div class="task-name">Faire le planning &#224; la main</div><div class="task-gain">1h / semaine gagn&#233;e</div></div>
    <div class="task-item"><div class="task-name">Exporter votre compta</div><div class="task-gain">Export 1&#160;clic</div></div>
    <div class="task-item"><div class="task-name">R&#233;diger les rapports chantier</div><div class="task-gain">18&#160;min &#233;conomis&#233;es / chantier</div></div>
    <div class="task-item"><div class="task-name">Demander des avis Google</div><div class="task-gain">Automatique &#224; chaque chantier</div></div>
    <div class="task-item"><div class="task-name">G&#233;n&#233;rer un PV de r&#233;ception</div><div class="task-gain">Auto apr&#232;s signature</div></div>
  </div>
</div>
</div>
"""
st.markdown(roi_html, unsafe_allow_html=True)
st.markdown(TARIFS_AND_FOOTER, unsafe_allow_html=True)
