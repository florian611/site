import streamlit as st

st.set_page_config(
    page_title="Floxia Service – Automatisation IA",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.block-container{
    background:#F7F5F0!important;font-family:'DM Sans',sans-serif!important;color:#1E1E1E!important;}
#MainMenu,header,footer,[data-testid="stSidebar"],[data-testid="stToolbar"],
[data-testid="stDecoration"],[data-testid="stStatusWidget"],.stDeployButton,.css-ch5dnh{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}

.nav{position:fixed;top:0;left:0;right:0;z-index:9999;display:flex;align-items:center;
    justify-content:space-between;padding:1rem 5vw;background:rgba(247,245,240,0.93);
    backdrop-filter:blur(14px);border-bottom:1px solid rgba(30,30,30,0.07);}
.nav-logo{display:flex;align-items:center;gap:.55rem;font-family:'Syne',sans-serif;
    font-weight:800;font-size:1.25rem;letter-spacing:-.03em;color:#1E1E1E;text-decoration:none;}
.nav-bolt{width:26px;height:26px;background:#FFD700;flex-shrink:0;
    clip-path:polygon(65% 0%,35% 45%,60% 45%,35% 100%,65% 55%,40% 55%);}
.nav-links{display:flex;gap:2rem;align-items:center;}
.nav-links a{font-size:.87rem;font-weight:500;color:#1E1E1E;text-decoration:none;
    opacity:.6;transition:opacity .2s;}
.nav-links a:hover{opacity:1;}
.nav-cta{background:#1E1E1E;color:#FFD700!important;padding:.55rem 1.3rem;border-radius:50px;
    font-size:.87rem;font-weight:600;text-decoration:none;opacity:1!important;
    transition:background .2s,transform .15s;white-space:nowrap;}
.nav-cta:hover{background:#FFD700!important;color:#1E1E1E!important;transform:scale(1.03);}

.hero{min-height:100vh;display:flex;flex-direction:column;align-items:center;
    justify-content:center;text-align:center;padding:8rem 5vw 5rem;
    position:relative;overflow:hidden;}
.hero::before{content:'';position:absolute;top:-8%;left:50%;transform:translateX(-50%);
    width:750px;height:750px;
    background:radial-gradient(circle,rgba(255,215,0,.11) 0%,transparent 70%);pointer-events:none;}
.hero-badge{display:inline-flex;align-items:center;gap:.45rem;
    background:rgba(255,215,0,.13);border:1px solid rgba(255,215,0,.38);
    color:#9A7A00;font-size:.76rem;font-weight:600;letter-spacing:.09em;
    text-transform:uppercase;padding:.35rem 1rem;border-radius:50px;margin-bottom:2rem;}
.hero-badge-dot{width:6px;height:6px;background:#FFD700;border-radius:50%;animation:pdot 2s infinite;}
@keyframes pdot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.45;transform:scale(1.35)}}
.hero-title{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,5vw,4.4rem);
    font-weight:800;line-height:1.07;letter-spacing:-.04em;color:#1E1E1E;
    max-width:860px;margin-bottom:1.5rem;}
.gold{color:#FFD700;}
.hero-sub{font-size:clamp(.95rem,1.5vw,1.15rem);font-weight:300;
    color:rgba(30,30,30,.58);max-width:540px;line-height:1.75;margin-bottom:2.8rem;}
.cta-group{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;}
.btn-primary{background:#FFD700;color:#1E1E1E;padding:.9rem 2.2rem;border-radius:50px;
    font-weight:700;font-size:.97rem;border:none;text-decoration:none;cursor:pointer;
    font-family:'DM Sans',sans-serif;box-shadow:0 4px 24px rgba(255,215,0,.32);
    transition:transform .2s,box-shadow .2s;display:inline-block;}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 34px rgba(255,215,0,.45);}
.btn-secondary{background:transparent;color:#1E1E1E;padding:.9rem 2.2rem;border-radius:50px;
    font-weight:500;font-size:.97rem;border:1.5px solid rgba(30,30,30,.2);
    text-decoration:none;cursor:pointer;font-family:'DM Sans',sans-serif;
    display:inline-block;transition:border-color .2s,background .2s;}
.btn-secondary:hover{border-color:#1E1E1E;background:rgba(30,30,30,.04);}
.hero-stats{display:flex;gap:3.5rem;justify-content:center;flex-wrap:wrap;
    margin-top:4rem;padding-top:3rem;border-top:1px solid rgba(30,30,30,.08);}
.stat-num{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;color:#1E1E1E;}
.stat-label{font-size:.8rem;color:rgba(30,30,30,.48);margin-top:.2rem;}

.section{padding:6rem 5vw;max-width:1200px;margin:0 auto;}
.section-label{font-size:.74rem;font-weight:600;letter-spacing:.13em;text-transform:uppercase;
    color:#9A7A00;margin-bottom:.7rem;}
.section-title{font-family:'Syne',sans-serif;font-size:clamp(1.75rem,3vw,2.75rem);
    font-weight:800;letter-spacing:-.035em;line-height:1.13;margin-bottom:.9rem;}
.section-sub{font-size:1rem;color:rgba(30,30,30,.54);max-width:480px;line-height:1.72;}

.cards-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:1.4rem;margin-top:3rem;}
.service-card{background:#fff;border:1px solid rgba(30,30,30,.07);border-radius:20px;
    padding:2rem;transition:transform .25s,border-color .25s,box-shadow .25s;
    position:relative;overflow:hidden;}
.service-card:hover{transform:translateY(-5px);border-color:rgba(255,215,0,.38);
    box-shadow:0 12px 40px rgba(255,215,0,.1);}
.service-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;
    background:#FFD700;transform:scaleX(0);transform-origin:left;transition:transform .3s;}
.service-card:hover::before{transform:scaleX(1);}
.card-icon{width:48px;height:48px;background:rgba(255,215,0,.12);border-radius:12px;
    display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1.2rem;}
.card-title{font-family:'Syne',sans-serif;font-size:1.02rem;font-weight:700;margin-bottom:.55rem;}
.card-desc{font-size:.87rem;color:rgba(30,30,30,.54);line-height:1.62;}
.card-tag{display:inline-block;margin-top:1rem;font-size:.7rem;font-weight:600;
    letter-spacing:.04em;background:rgba(255,215,0,.12);color:#9A7A00;
    padding:.25rem .7rem;border-radius:50px;}

.roi-wrapper{background:#1E1E1E;border-radius:24px;padding:2.8rem;color:#F7F5F0;
    position:relative;overflow:hidden;}
.roi-wrapper::after{content:'';position:absolute;bottom:-50px;right:-50px;width:240px;height:240px;
    background:radial-gradient(circle,rgba(255,215,0,.13) 0%,transparent 70%);}
.roi-slider-label{font-size:.78rem;letter-spacing:.07em;text-transform:uppercase;
    color:rgba(247,245,240,.42);margin-bottom:1rem;}
.roi-result{background:rgba(255,215,0,.09);border:1px solid rgba(255,215,0,.22);
    border-radius:16px;padding:1.5rem 2rem;margin-top:2rem;}
.roi-result-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;}
.roi-metric-val{font-family:'Syne',sans-serif;font-size:1.9rem;font-weight:800;color:#FFD700;}
.roi-metric-lbl{font-size:.76rem;color:rgba(247,245,240,.45);margin-top:.25rem;}

.flow-wrapper{background:#fff;border:1px solid rgba(30,30,30,.07);
    border-radius:16px;padding:1.4rem 1.6rem;margin-bottom:1rem;}
.flow-row{display:flex;align-items:center;gap:.7rem;flex-wrap:wrap;}
.flow-node{display:flex;align-items:center;gap:.4rem;background:#F7F5F0;
    border:1px solid rgba(30,30,30,.09);border-radius:10px;padding:.5rem .85rem;
    font-size:.8rem;font-weight:600;color:#1E1E1E;white-space:nowrap;}
.flow-node.gd{background:rgba(255,215,0,.12);border-color:rgba(255,215,0,.35);color:#7A5E00;}
.flow-node.dk{background:#1E1E1E;color:#FFD700;border-color:#1E1E1E;}
.flow-arrow{font-size:.95rem;color:rgba(30,30,30,.3);flex-shrink:0;}
.flow-label{font-size:.68rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
    color:rgba(30,30,30,.35);margin-bottom:.35rem;}

.dark-band{background:#1E1E1E;padding:5.5rem 5vw;text-align:center;}
.dark-band h2{font-family:'Syne',sans-serif;font-size:clamp(1.75rem,3.5vw,3rem);
    font-weight:800;letter-spacing:-.035em;color:#F7F5F0;margin-bottom:.9rem;}
.dark-band p{color:rgba(247,245,240,.42);font-size:.97rem;margin-bottom:2.5rem;}
.insta-btn{display:inline-flex;align-items:center;gap:.75rem;
    background:linear-gradient(135deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);
    color:#fff;font-family:'DM Sans',sans-serif;font-weight:700;font-size:1rem;
    padding:.95rem 2.4rem;border-radius:50px;text-decoration:none;
    box-shadow:0 6px 28px rgba(220,39,67,.32);transition:transform .2s,box-shadow .2s;}
.insta-btn:hover{transform:translateY(-2px);box-shadow:0 10px 36px rgba(220,39,67,.48);}

.footer{padding:2.8rem 5vw;display:flex;align-items:center;justify-content:space-between;
    flex-wrap:wrap;gap:1.5rem;border-top:1px solid rgba(30,30,30,.08);}
.footer-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:1.05rem;
    letter-spacing:-.03em;display:flex;align-items:center;gap:.5rem;}
.footer-tagline{font-size:.8rem;color:rgba(30,30,30,.38);margin-top:.35rem;}
.footer-links{display:flex;gap:2rem;}
.footer-links a{font-size:.8rem;color:rgba(30,30,30,.48);text-decoration:none;}
.footer-links a:hover{color:#1E1E1E;}
.footer-badge{font-size:.72rem;background:rgba(255,215,0,.12);color:#9A7A00;
    padding:.28rem .75rem;border-radius:50px;font-weight:600;}
.divider{height:1px;background:rgba(30,30,30,.07);max-width:1200px;margin:0 auto;}

/* PRICING SECTION */
.pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
    gap:1.4rem;margin-top:3rem;}
.pricing-card{background:#fff;border:1px solid rgba(30,30,30,.07);border-radius:20px;
    padding:2rem;position:relative;overflow:hidden;transition:transform .25s,box-shadow .25s;}
.pricing-card.featured{background:#1E1E1E;color:#F7F5F0;border-color:#1E1E1E;}
.pricing-card:hover{transform:translateY(-5px);box-shadow:0 12px 40px rgba(255,215,0,.12);}
.pricing-badge{display:inline-block;font-size:.68rem;font-weight:700;letter-spacing:.07em;
    text-transform:uppercase;background:rgba(255,215,0,.15);color:#9A7A00;
    padding:.25rem .7rem;border-radius:50px;margin-bottom:1rem;}
.pricing-card.featured .pricing-badge{background:rgba(255,215,0,.2);color:#FFD700;}
.pricing-plan{font-family:'Syne',sans-serif;font-weight:800;font-size:1.1rem;margin-bottom:.5rem;}
.pricing-price{font-family:'Syne',sans-serif;font-size:2.8rem;font-weight:800;
    letter-spacing:-.04em;line-height:1;color:#1E1E1E;margin:.7rem 0 .3rem;}
.pricing-card.featured .pricing-price{color:#FFD700;}
.pricing-per{font-size:.78rem;color:rgba(30,30,30,.42);margin-bottom:1.5rem;}
.pricing-card.featured .pricing-per{color:rgba(247,245,240,.38);}
.pricing-features{display:flex;flex-direction:column;gap:.6rem;margin-bottom:1.8rem;}
.pricing-feature{display:flex;align-items:flex-start;gap:.6rem;font-size:.84rem;
    color:rgba(30,30,30,.65);line-height:1.45;}
.pricing-card.featured .pricing-feature{color:rgba(247,245,240,.65);}
.pricing-feature-check{color:#FFD700;font-size:.9rem;flex-shrink:0;margin-top:.05rem;}
.pricing-cta{display:block;text-align:center;padding:.75rem 1.5rem;border-radius:50px;
    font-weight:700;font-size:.9rem;text-decoration:none;transition:all .2s;}
.pricing-cta-outline{border:1.5px solid rgba(30,30,30,.2);color:#1E1E1E;}
.pricing-cta-outline:hover{background:#1E1E1E;color:#FFD700;}
.pricing-cta-solid{background:#FFD700;color:#1E1E1E;border:none;
    box-shadow:0 4px 20px rgba(255,215,0,.3);}
.pricing-cta-solid:hover{box-shadow:0 8px 28px rgba(255,215,0,.5);transform:translateY(-1px);}
.pricing-note{font-size:.72rem;text-align:center;color:rgba(30,30,30,.35);margin-top:1rem;}
.pricing-card.featured .pricing-note{color:rgba(247,245,240,.28);}
.pricing-devis-highlight{background:rgba(255,215,0,.08);border:1px solid rgba(255,215,0,.25);
    border-radius:12px;padding:.9rem 1.1rem;margin-bottom:1.2rem;font-size:.82rem;
    color:#7A5E00;line-height:1.5;}
.pricing-card.featured .pricing-devis-highlight{background:rgba(255,215,0,.1);
    border-color:rgba(255,215,0,.3);color:#FFD700;}

div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"]{
    background:#FFD700!important;border:none!important;
    box-shadow:0 0 0 4px rgba(255,215,0,.22)!important;}
div[data-testid="stSlider"] [data-baseweb="slider"]>div:first-child>div:nth-child(2){
    background:#FFD700!important;}
div[data-testid="stButton"]>button{
    background:#FFD700!important;color:#1E1E1E!important;border:none!important;
    border-radius:50px!important;font-weight:700!important;font-size:.95rem!important;
    padding:.7rem 2rem!important;font-family:'DM Sans',sans-serif!important;
    box-shadow:0 4px 20px rgba(255,215,0,.28)!important;
    transition:transform .15s,box-shadow .15s!important;}
div[data-testid="stButton"]>button:hover{
    transform:translateY(-2px)!important;
    box-shadow:0 8px 28px rgba(255,215,0,.44)!important;}
</style>
""", unsafe_allow_html=True)

# ── NAVBAR ─────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav">
  <a class="nav-logo" href="#">
    <div class="nav-bolt"></div>Floxia Service
  </a>
  <div class="nav-links">
    <a href="#services">Services</a>
    <a href="#ecosystem">Écosystème</a>
    <a href="#simulateur">ROI</a>
    <a href="#tarifs">Tarifs</a>
    <a href="https://www.instagram.com/floxia.pro/" target="_blank" class="nav-cta">Réserver une démo →</a>
  </div>
</nav>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="hero">
  <div class="hero-badge">
    <div class="hero-badge-dot"></div>
    IA pour artisans &amp; PME du bâtiment
  </div>
  <h1 class="hero-title">
    Arrêtez de subir<br>votre paperasse.<br><span class="gold">Automatisez-la.</span>
  </h1>
  <p class="hero-sub">
    Floxia connecte WhatsApp, l'IA et votre ERP pour automatiser
    devis, factures, relances, tickets de caisse et rapports chantier —
    tout depuis votre téléphone, sans aucune saisie manuelle.
  </p>
  <div class="cta-group">
    <a class="btn-primary" href="https://www.instagram.com/floxia.pro/" target="_blank">
      ⚡ Réserver une démo gratuite
    </a>
    <a class="btn-secondary" href="#services">Découvrir les services</a>
  </div>
  <div class="hero-stats">
    <div>
      <div class="stat-num">16<span class="gold">h</span></div>
      <div class="stat-label">gagnées / mois en moyenne</div>
    </div>
    <div>
      <div class="stat-num"><span class="gold">−</span>80<span class="gold">%</span></div>
      <div class="stat-label">de saisie administrative</div>
    </div>
    <div>
      <div class="stat-num">3<span class="gold">min</span></div>
      <div class="stat-label">du devis à la facture finale</div>
    </div>
    <div>
      <div class="stat-num">100<span class="gold">%</span></div>
      <div class="stat-label">sur WhatsApp &amp; mobile</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── SERVICES ───────────────────────────────────────────────────────────────────
st.markdown("""
<div id="services">
<div class="section">
  <div class="section-label">Ce que fait Floxia</div>
  <h2 class="section-title">Tout votre flux de travail,<br>automatisé de A à Z.</h2>
  <p class="section-sub">Des automatisations concrètes, opérationnelles dès aujourd'hui, sans installation ni compétence technique.</p>
  <div class="cards-grid">

    <div class="service-card">
      <div class="card-icon">💬</div>
      <div class="card-title">Devis → Facture Finale</div>
      <div class="card-desc">Envoyez un vocal depuis votre téléphone. Floxia génère le devis PDF, le client signe, et le cycle complet se clôture automatiquement en facture finale — sans jamais toucher un ordinateur.</div>
      <span class="card-tag">⚡ Cycle complet géré</span>
    </div>

    <div class="service-card">
      <div class="card-icon">📸</div>
      <div class="card-title">Scan Tickets de Caisse</div>
      <div class="card-desc">Photographiez vos tickets directement sur WhatsApp. L'IA extrait fournisseur, articles, montants HT/TVA et les stocke automatiquement dans votre comptabilité. Plus jamais une boîte à chaussures.</div>
      <span class="card-tag">⚡ Zéro ressaisie</span>
    </div>

    <div class="service-card">
      <div class="card-icon">⭐</div>
      <div class="card-title">Avis Google Maps</div>
      <div class="card-desc">À chaque chantier terminé, Floxia envoie automatiquement un message WhatsApp à votre client pour l'inviter à laisser un avis Google. Plus d'avis, meilleure réputation, plus de clients.</div>
      <span class="card-tag">⚡ Réputation boostée</span>
    </div>

    <div class="service-card">
      <div class="card-icon">🚨</div>
      <div class="card-title">Alerte Problème Chantier</div>
      <div class="card-desc">Un problème sur le chantier ? Envoyez un vocal WhatsApp. Floxia rédige automatiquement un e-mail professionnel au client expliquant la situation, les causes et le nouveau délai prévu.</div>
      <span class="card-tag">⚡ Email client en 30 sec</span>
    </div>

    <div class="service-card">
      <div class="card-icon">🔔</div>
      <div class="card-title">Relances Automatiques</div>
      <div class="card-desc">Floxia surveille vos devis non signés et relance automatiquement vos clients par SMS et e-mail au bon moment, avec le bon message. Plus jamais un devis oublié.</div>
      <span class="card-tag">⚡ +30 % de conversion</span>
    </div>

    <div class="service-card">
      <div class="card-icon">📋</div>
      <div class="card-title">ERP Mobile Complet</div>
      <div class="card-desc">Devis, factures, chantiers, planning, salariés, dépenses — tout dans une interface web accessible depuis votre téléphone, synchronisée en temps réel avec Google Sheets.</div>
      <span class="card-tag">⚡ Tout en un seul endroit</span>
    </div>

    <div class="service-card">
      <div class="card-icon">🎙️</div>
      <div class="card-title">Rapports Vocaux Chantier</div>
      <div class="card-desc">Dictez votre rapport de fin de journée en 2 minutes. Floxia le structure, le met en page et l'envoie directement au client sous forme de compte-rendu professionnel.</div>
      <span class="card-tag">⚡ Rapport en 2 min</span>
    </div>

    <div class="service-card">
      <div class="card-icon">💰</div>
      <div class="card-title">Suivi Dépenses &amp; TVA</div>
      <div class="card-desc">Chaque ticket scanné alimente votre tableau de bord financier : dépenses par catégorie, TVA récupérable, résultat net estimé et export comptable mensuel en un clic.</div>
      <span class="card-tag">⚡ Compta simplifiée</span>
    </div>

  </div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── ÉCOSYSTÈME / FLUX ──────────────────────────────────────────────────────────
st.markdown('<div id="ecosystem"></div>', unsafe_allow_html=True)

eco_l, eco_r = st.columns([1, 1], gap="large")

with eco_l:
    st.markdown("""
    <div class="section" style="padding-right:0;">
      <div class="section-label">Comment ça marche</div>
      <h2 class="section-title">WhatsApp comme<br>centre de commandes.</h2>
      <p class="section-sub">Tout part de votre téléphone. Floxia fait le reste — aucun logiciel à apprendre, aucune connexion sur un ordinateur.</p>

      <div style="margin-top:2.5rem;display:flex;flex-direction:column;gap:1rem;">
        <div style="display:flex;align-items:flex-start;gap:1rem;">
          <div style="width:44px;height:44px;border-radius:50%;background:#1E1E1E;
              color:#FFD700;font-family:'Syne',sans-serif;font-weight:800;font-size:1rem;
              display:flex;align-items:center;justify-content:center;flex-shrink:0;">1</div>
          <div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;font-size:.95rem;margin-bottom:.3rem;">Une fois connecté</div>
            <div style="font-size:.83rem;color:rgba(30,30,30,.5);line-height:1.6;">WhatsApp Business, Gmail, Google Drive — tout est prêt, on s'en occupe.</div>
          </div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:1rem;">
          <div style="width:44px;height:44px;border-radius:50%;background:#1E1E1E;
              color:#FFD700;font-family:'Syne',sans-serif;font-weight:800;font-size:1rem;
              display:flex;align-items:center;justify-content:center;flex-shrink:0;">2</div>
          <div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;font-size:.95rem;margin-bottom:.3rem;">Parlez ou photographiez</div>
            <div style="font-size:.83rem;color:rgba(30,30,30,.5);line-height:1.6;">Vocal ou photo sur WhatsApp. Floxia comprend et agit instantanément.</div>
          </div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:1rem;">
          <div style="width:44px;height:44px;border-radius:50%;background:#1E1E1E;
              color:#FFD700;font-family:'Syne',sans-serif;font-weight:800;font-size:1rem;
              display:flex;align-items:center;justify-content:center;flex-shrink:0;">3</div>
          <div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;font-size:.95rem;margin-bottom:.3rem;">L'IA travaille pour vous</div>
            <div style="font-size:.83rem;color:rgba(30,30,30,.5);line-height:1.6;">Devis envoyé, ticket enregistré, email rédigé, rapport structuré. Automatiquement.</div>
          </div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:1rem;">
          <div style="width:44px;height:44px;border-radius:50%;background:#1E1E1E;
              color:#FFD700;font-family:'Syne',sans-serif;font-weight:800;font-size:1rem;
              display:flex;align-items:center;justify-content:center;flex-shrink:0;">4</div>
          <div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;font-size:.95rem;margin-bottom:.3rem;">Pilotez depuis l'ERP</div>
            <div style="font-size:.83rem;color:rgba(30,30,30,.5);line-height:1.6;">Tableau de bord temps réel : CA, planning, salariés, dépenses, facturation.</div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with eco_r:
    st.markdown("""
    <div style="padding:4rem 1rem 4rem 2rem;">

      <div class="flow-label">Flux 1 — Cycle Devis complet</div>
      <div class="flow-wrapper">
        <div class="flow-row">
          <div class="flow-node">🎙️ Vocal WhatsApp</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node gd">⚡ IA Floxia</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node">📄 Devis PDF</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node">✍️ Signature</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node dk">🧾 Facture finale</div>
        </div>
      </div>

      <div class="flow-label">Flux 2 — Avis Google Maps</div>
      <div class="flow-wrapper">
        <div class="flow-row">
          <div class="flow-node">✅ Chantier terminé</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node gd">⚡ Floxia détecte</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node">💬 Message WhatsApp</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node dk">⭐ Avis Google</div>
        </div>
      </div>

      <div class="flow-label">Flux 3 — Ticket de caisse</div>
      <div class="flow-wrapper">
        <div class="flow-row">
          <div class="flow-node">📸 Photo WhatsApp</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node gd">⚡ OCR IA</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node">📊 Google Sheets</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node dk">✅ Compta</div>
        </div>
      </div>

      <div class="flow-label">Flux 4 — Problème chantier</div>
      <div class="flow-wrapper">
        <div class="flow-row">
          <div class="flow-node">🚨 Vocal WhatsApp</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node gd">⚡ IA rédaction</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node dk">📧 Email client</div>
        </div>
      </div>

      <div class="flow-label">Flux 5 — Relances devis</div>
      <div class="flow-wrapper">
        <div class="flow-row">
          <div class="flow-node">⏰ Délai dépassé</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node gd">⚡ Floxia détecte</div>
          <div class="flow-arrow">→</div>
          <div class="flow-node dk">💬 SMS + Email</div>
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── ROI SIMULATOR ──────────────────────────────────────────────────────────────
st.markdown('<div id="simulateur"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section" style="padding-bottom:1rem;">
  <div class="section-label">Simulateur ROI</div>
  <h2 class="section-title">Calculez votre temps libéré.</h2>
  <p class="section-sub">Bougez le curseur — voyez ce que Floxia vous rapporte chaque mois.</p>
</div>
""", unsafe_allow_html=True)

roi_l, roi_r = st.columns([1, 1], gap="large")

with roi_l:
    st.markdown('<div class="roi-wrapper"><div class="roi-slider-label">Nombre de devis par mois</div>', unsafe_allow_html=True)
    nb_devis = st.slider("", min_value=1, max_value=80, value=15, step=1,
                         key="roi_slider", label_visibility="collapsed")
    heures_gagnees = round(((64 - 3) * nb_devis + nb_devis * 12) / 60, 1)
    gain_euros     = round(heures_gagnees * 55)

    # Pricing based on nb_devis
    if nb_devis <= 10:
        abonnement = 49
        plan_label = "Starter"
    elif nb_devis <= 30:
        abonnement = 99
        plan_label = "Pro"
    else:
        abonnement = 149
        plan_label = "Expert"

    roi_pourcent   = round((gain_euros / abonnement) * 100)
    st.markdown(f"""
    <div class="roi-result">
      <div style="font-size:.75rem;color:rgba(247,245,240,.42);text-transform:uppercase;
                  letter-spacing:.07em;margin-bottom:1.2rem;">Résultats pour {nb_devis} devis/mois</div>
      <div class="roi-result-grid">
        <div><div class="roi-metric-val">{heures_gagnees}h</div><div class="roi-metric-lbl">temps libéré</div></div>
        <div><div class="roi-metric-val">{gain_euros}€</div><div class="roi-metric-lbl">valeur récupérée</div></div>
        <div><div class="roi-metric-val">{roi_pourcent}%</div><div class="roi-metric-lbl">ROI mensuel</div></div>
      </div>
    </div>
    <div style="font-size:.72rem;color:rgba(247,245,240,.22);margin-top:1rem;">
      *Basé sur 55€/h artisan · Plan {plan_label} à {abonnement}€/mois pour {nb_devis} devis.
    </div></div>
    """, unsafe_allow_html=True)

with roi_r:
    ITEMS = [
        ("Taper des devis le soir", "45 min évitées / devis"),
        ("Ressaisir les tickets de caisse", "2h / semaine récupérées"),
        ("Rédiger des e-mails clients complexes", "30 min / incident"),
        ("Relancer les devis manuellement", "+30% de conversion offert"),
        ("Faire le planning à la main", "1h / semaine gagnée"),
        ("Exporter votre compta en fin de mois", "Export 1 clic"),
        ("Rédiger les rapports chantier", "2 min au lieu de 20"),
        ("Demander des avis Google manuellement", "Automatique à chaque chantier"),
    ]
    st.markdown('<div style="padding:1.5rem 0;"><div class="section-label" style="margin-bottom:1rem;">Ce que vous ne faites plus</div><div style="display:flex;flex-direction:column;gap:.75rem;">', unsafe_allow_html=True)
    for task, gain in ITEMS:
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:center;
                    padding:.8rem 1.1rem;background:#fff;
                    border:1px solid rgba(30,30,30,.07);border-radius:12px;">
          <div style="font-size:.85rem;color:rgba(30,30,30,.52);text-decoration:line-through;">{task}</div>
          <div style="font-size:.75rem;font-weight:600;color:#9A7A00;background:rgba(255,215,0,.12);
                      padding:.2rem .6rem;border-radius:50px;white-space:nowrap;margin-left:.75rem;">{gain}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('<div class="divider" style="margin-top:3rem;"></div>', unsafe_allow_html=True)

# ── TARIFS ─────────────────────────────────────────────────────────────────────
st.markdown('<div id="tarifs"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Tarifs</div>
  <h2 class="section-title">Un prix qui s'adapte<br>à votre activité.</h2>
  <p class="section-sub">Payez selon le nombre de devis générés chaque mois. Plus vous travaillez, plus Floxia vous fait économiser.</p>

  <div class="pricing-grid">

    <div class="pricing-card">
      <div class="pricing-badge">Starter</div>
      <div class="pricing-plan">Pour démarrer</div>
      <div class="pricing-devis-highlight">
        ⚡ Jusqu'à <strong>10 devis / mois</strong>
      </div>
      <div class="pricing-price">49€</div>
      <div class="pricing-per">par mois · sans engagement</div>
      <div class="pricing-features">
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Devis WhatsApp vocal</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Cycle devis → facture finale</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Scan tickets de caisse</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Relances automatiques</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Avis Google Maps auto</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>ERP mobile (Google Sheets)</div>
      </div>
      <a class="pricing-cta pricing-cta-outline" href="https://www.instagram.com/floxia.pro/" target="_blank">Démarrer →</a>
      <div class="pricing-note">Idéal pour les artisans solo</div>
    </div>

    <div class="pricing-card featured">
      <div class="pricing-badge">⚡ Le plus populaire — Pro</div>
      <div class="pricing-plan">Pour les actifs</div>
      <div class="pricing-devis-highlight">
        ⚡ Jusqu'à <strong>30 devis / mois</strong>
      </div>
      <div class="pricing-price">99€</div>
      <div class="pricing-per">par mois · sans engagement</div>
      <div class="pricing-features">
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Tout du plan Starter</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Alertes problème chantier</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Rapports vocaux PDF</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Planning & salariés</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Suivi dépenses & TVA</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Support prioritaire WhatsApp</div>
      </div>
      <a class="pricing-cta pricing-cta-solid" href="https://www.instagram.com/floxia.pro/" target="_blank">Choisir Pro →</a>
      <div class="pricing-note">Le meilleur rapport qualité / valeur</div>
    </div>

    <div class="pricing-card">
      <div class="pricing-badge">Expert</div>
      <div class="pricing-plan">Pour les équipes</div>
      <div class="pricing-devis-highlight">
        ⚡ <strong>Devis illimités</strong>
      </div>
      <div class="pricing-price">149€</div>
      <div class="pricing-per">par mois · sans engagement</div>
      <div class="pricing-features">
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Tout du plan Pro</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Devis illimités</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Multi-utilisateurs (équipe)</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Tableaux de bord avancés</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Intégrations sur mesure</div>
        <div class="pricing-feature"><span class="pricing-feature-check">✦</span>Accompagnement dédié</div>
      </div>
      <a class="pricing-cta pricing-cta-outline" href="https://www.instagram.com/floxia.pro/" target="_blank">Nous contacter →</a>
      <div class="pricing-note">Pour les PME et équipes terrain</div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── CTA FINAL ─────────────────────────────────────────────────────────────────
st.markdown("""
<div id="contact" class="dark-band">
  <h2>Prêt à récupérer<br><span class="gold">votre temps ?</span></h2>
  <div style="display:flex;flex-direction:column;align-items:center;gap:1rem;">
    <a class="insta-btn" href="https://www.instagram.com/floxia.pro/" target="_blank">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
        <rect x="2" y="2" width="20" height="20" rx="5" stroke="white" stroke-width="1.8"/>
        <circle cx="12" cy="12" r="4.5" stroke="white" stroke-width="1.8"/>
        <circle cx="17.5" cy="6.5" r="1" fill="white"/>
      </svg>
      Réserver une démo — m'envoyer un message sur Instagram
    </a>
    <div style="font-size:.78rem;color:rgba(247,245,240,.28);">@floxia.pro · Réponse sous 24h</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="footer">
  <div>
    <div class="footer-logo">
      <div class="nav-bolt" style="width:20px;height:20px;"></div>
      Floxia Service
    </div>
    <div class="footer-tagline">Floxia répond à tous vos besoins.</div>
  </div>
  <div class="footer-links">
    <a href="#">Mentions légales</a>
    <a href="#">Confidentialité</a>
    <a href="https://www.instagram.com/floxia.pro/" target="_blank">📸 Instagram</a>
  </div>
  <div class="footer-badge">⚡ Propulsé par l'IA</div>
</footer>
""", unsafe_allow_html=True)
