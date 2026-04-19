import streamlit as st
import anthropic
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Floxia Service – Automatisation IA",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ===== RESET & BASE ===== */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"],
[data-testid="stMain"], .main, .block-container {
    background: #F7F5F0 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #1E1E1E !important;
}

/* Hide ALL Streamlit chrome */
#MainMenu, header, footer,
[data-testid="stSidebar"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stDeployButton, .css-ch5dnh { display: none !important; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ===== NAVBAR ===== */
.nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1rem 5vw;
    background: rgba(247,245,240,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(30,30,30,0.07);
}
.nav-logo {
    display: flex; align-items: center; gap: 0.5rem;
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.3rem;
    letter-spacing: -0.03em; color: #1E1E1E;
}
.nav-bolt {
    width: 28px; height: 28px;
    background: #FFD700;
    clip-path: polygon(65% 0%, 35% 45%, 60% 45%, 35% 100%, 65% 55%, 40% 55%);
}
.nav-links { display: flex; gap: 2rem; }
.nav-links a {
    font-size: 0.88rem; font-weight: 500; color: #1E1E1E;
    text-decoration: none; opacity: 0.65;
    transition: opacity 0.2s;
}
.nav-links a:hover { opacity: 1; }
.nav-cta {
    background: #1E1E1E; color: #FFD700 !important;
    padding: 0.55rem 1.3rem; border-radius: 50px; font-size: 0.88rem;
    font-weight: 500; text-decoration: none; opacity: 1 !important;
    transition: background 0.2s, transform 0.15s;
}
.nav-cta:hover { background: #FFD700 !important; color: #1E1E1E !important; transform: scale(1.03); }

/* ===== HERO ===== */
.hero {
    min-height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center;
    padding: 8rem 5vw 5rem;
    position: relative; overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: -10%; left: 50%; transform: translateX(-50%);
    width: 700px; height: 700px;
    background: radial-gradient(circle, rgba(255,215,0,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 0.4rem;
    background: rgba(255,215,0,0.15); border: 1px solid rgba(255,215,0,0.4);
    color: #B8960C; font-size: 0.78rem; font-weight: 500; letter-spacing: 0.08em;
    text-transform: uppercase; padding: 0.35rem 1rem; border-radius: 50px;
    margin-bottom: 2rem;
}
.hero-badge-dot { width: 6px; height: 6px; background: #FFD700; border-radius: 50%; animation: pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(1.3)} }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 5vw, 4.5rem);
    font-weight: 800; line-height: 1.08;
    letter-spacing: -0.04em; color: #1E1E1E;
    max-width: 850px; margin-bottom: 1.5rem;
}
.hero-title span { color: #FFD700; }

.hero-sub {
    font-size: clamp(1rem, 1.6vw, 1.2rem);
    font-weight: 300; color: rgba(30,30,30,0.6);
    max-width: 520px; line-height: 1.7; margin-bottom: 2.8rem;
}

.cta-group { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.btn-primary {
    background: #FFD700; color: #1E1E1E;
    padding: 0.9rem 2.2rem; border-radius: 50px;
    font-weight: 600; font-size: 1rem;
    text-decoration: none; transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 24px rgba(255,215,0,0.35);
    cursor: pointer; border: none; font-family: 'DM Sans',sans-serif;
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(255,215,0,0.45); }
.btn-secondary {
    background: transparent; color: #1E1E1E;
    padding: 0.9rem 2.2rem; border-radius: 50px;
    font-weight: 500; font-size: 1rem;
    border: 1.5px solid rgba(30,30,30,0.2);
    text-decoration: none; transition: border-color 0.2s, background 0.2s;
    cursor: pointer; font-family: 'DM Sans',sans-serif;
}
.btn-secondary:hover { border-color: #1E1E1E; background: rgba(30,30,30,0.04); }

.hero-stats {
    display: flex; gap: 3rem; justify-content: center; flex-wrap: wrap;
    margin-top: 4rem; padding-top: 3rem;
    border-top: 1px solid rgba(30,30,30,0.08);
}
.stat-item { text-align: center; }
.stat-num {
    font-family: 'Syne', sans-serif; font-size: 2.2rem;
    font-weight: 800; color: #1E1E1E;
}
.stat-num span { color: #FFD700; }
.stat-label { font-size: 0.82rem; color: rgba(30,30,30,0.5); margin-top: 0.2rem; }

/* ===== SECTION WRAPPER ===== */
.section {
    padding: 6rem 5vw;
    max-width: 1200px; margin: 0 auto;
}
.section-label {
    font-size: 0.75rem; font-weight: 500; letter-spacing: 0.12em;
    text-transform: uppercase; color: #B8960C;
    margin-bottom: 0.8rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(1.8rem, 3vw, 2.8rem);
    font-weight: 800; letter-spacing: -0.03em;
    line-height: 1.15; margin-bottom: 1rem;
}
.section-sub {
    font-size: 1rem; color: rgba(30,30,30,0.55);
    max-width: 480px; line-height: 1.7;
}

/* ===== ROI SIMULATOR ===== */
.roi-wrapper {
    background: #1E1E1E;
    border-radius: 24px;
    padding: 3rem;
    color: #F7F5F0;
    position: relative; overflow: hidden;
}
.roi-wrapper::after {
    content: '';
    position: absolute; bottom: -60px; right: -60px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(255,215,0,0.15) 0%, transparent 70%);
}
.roi-slider-label {
    font-size: 0.82rem; letter-spacing: 0.06em; text-transform: uppercase;
    color: rgba(247,245,240,0.45); margin-bottom: 1rem;
}
.roi-result {
    background: rgba(255,215,0,0.1);
    border: 1px solid rgba(255,215,0,0.25);
    border-radius: 16px; padding: 1.5rem 2rem;
    margin-top: 2rem;
}
.roi-result-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;
}
.roi-metric-val {
    font-family: 'Syne', sans-serif;
    font-size: 2rem; font-weight: 800; color: #FFD700;
}
.roi-metric-lbl {
    font-size: 0.78rem; color: rgba(247,245,240,0.5);
    margin-top: 0.25rem;
}

/* ===== SERVICES CARDS ===== */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.5rem; margin-top: 3rem;
}
.service-card {
    background: #fff;
    border: 1px solid rgba(30,30,30,0.07);
    border-radius: 20px;
    padding: 2rem;
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
    position: relative; overflow: hidden;
}
.service-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255,215,0,0.4);
    box-shadow: 0 12px 40px rgba(255,215,0,0.12);
}
.service-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: #FFD700; transform: scaleX(0); transform-origin: left;
    transition: transform 0.3s;
}
.service-card:hover::before { transform: scaleX(1); }
.card-icon {
    width: 48px; height: 48px;
    background: rgba(255,215,0,0.12);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem; margin-bottom: 1.2rem;
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem; font-weight: 700;
    margin-bottom: 0.6rem;
}
.card-desc { font-size: 0.88rem; color: rgba(30,30,30,0.55); line-height: 1.6; }
.card-tag {
    display: inline-block; margin-top: 1rem;
    font-size: 0.72rem; font-weight: 500; letter-spacing: 0.04em;
    background: rgba(255,215,0,0.12); color: #B8960C;
    padding: 0.25rem 0.7rem; border-radius: 50px;
}

/* ===== DEMO IA ===== */
.demo-wrapper {
    background: #1E1E1E; border-radius: 24px;
    padding: 3rem; margin-top: 3rem; color: #F7F5F0;
}
.demo-header {
    display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;
}
.demo-dot {
    width: 10px; height: 10px; border-radius: 50%; background: #FFD700;
    animation: pulse 2s infinite;
}
.demo-title {
    font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 700;
}
.demo-subtitle { font-size: 0.82rem; color: rgba(247,245,240,0.45); }

.ai-response {
    background: rgba(255,215,0,0.06);
    border: 1px solid rgba(255,215,0,0.2);
    border-radius: 14px; padding: 1.5rem;
    font-size: 0.9rem; line-height: 1.7;
    color: rgba(247,245,240,0.85);
    white-space: pre-wrap; margin-top: 1.5rem;
}
.ai-response strong { color: #FFD700; }

/* ===== STREAMLIT WIDGET OVERRIDES ===== */
[data-testid="stTextArea"] textarea {
    background: rgba(247,245,240,0.06) !important;
    border: 1px solid rgba(247,245,240,0.15) !important;
    border-radius: 12px !important;
    color: #F7F5F0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: rgba(255,215,0,0.5) !important;
    box-shadow: 0 0 0 3px rgba(255,215,0,0.1) !important;
}
[data-testid="stTextArea"] label {
    color: rgba(247,245,240,0.5) !important;
    font-size: 0.78rem !important; letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
}

div[data-testid="stSlider"] {
    padding: 0 !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] {
    background: transparent !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
    background: #FFD700 !important;
    border: none !important;
    box-shadow: 0 0 0 4px rgba(255,215,0,0.25) !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child > div {
    background: rgba(247,245,240,0.15) !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child > div:nth-child(2) {
    background: #FFD700 !important;
}
div[data-testid="stSlider"] [aria-valuetext] {
    color: rgba(247,245,240,0.7) !important;
    font-size: 0.8rem !important;
}

div[data-testid="stButton"] > button {
    background: #FFD700 !important; color: #1E1E1E !important;
    border: none !important; border-radius: 50px !important;
    font-weight: 600 !important; font-size: 0.95rem !important;
    padding: 0.7rem 2rem !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
    box-shadow: 0 4px 20px rgba(255,215,0,0.3) !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(255,215,0,0.45) !important;
}

/* ===== PROCESS ===== */
.process-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem; margin-top: 3rem; position: relative;
}
.process-step { text-align: center; position: relative; }
.step-num {
    width: 52px; height: 52px; border-radius: 50%;
    background: #1E1E1E; color: #FFD700;
    font-family: 'Syne', sans-serif; font-size: 1.2rem; font-weight: 800;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 1rem;
}
.step-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1rem; margin-bottom: 0.4rem; }
.step-desc { font-size: 0.82rem; color: rgba(30,30,30,0.5); line-height: 1.6; }

/* ===== TESTIMONIALS ===== */
.testimonials-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem; margin-top: 3rem;
}
.testi-card {
    background: #fff; border: 1px solid rgba(30,30,30,0.07);
    border-radius: 20px; padding: 2rem;
}
.testi-stars { color: #FFD700; font-size: 0.9rem; margin-bottom: 1rem; }
.testi-text { font-size: 0.92rem; line-height: 1.7; color: rgba(30,30,30,0.7); margin-bottom: 1.2rem; font-style: italic; }
.testi-author { display: flex; align-items: center; gap: 0.75rem; }
.testi-avatar {
    width: 40px; height: 40px; border-radius: 50%;
    background: #1E1E1E; color: #FFD700;
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: 0.85rem;
    display: flex; align-items: center; justify-content: center;
}
.testi-name { font-weight: 600; font-size: 0.88rem; }
.testi-role { font-size: 0.75rem; color: rgba(30,30,30,0.45); }

/* ===== CTA BAND ===== */
.cta-band {
    background: #1E1E1E;
    padding: 5rem 5vw;
    text-align: center;
}
.cta-band h2 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(1.8rem, 3.5vw, 3rem);
    font-weight: 800; letter-spacing: -0.03em;
    color: #F7F5F0; margin-bottom: 1rem;
}
.cta-band h2 span { color: #FFD700; }
.cta-band p { color: rgba(247,245,240,0.45); font-size: 1rem; margin-bottom: 2.5rem; }

/* ===== FOOTER ===== */
.footer {
    padding: 3rem 5vw;
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 1.5rem;
    border-top: 1px solid rgba(30,30,30,0.08);
}
.footer-logo {
    font-family: 'Syne', sans-serif; font-weight: 800;
    font-size: 1.1rem; letter-spacing: -0.03em;
    display: flex; align-items: center; gap: 0.5rem;
}
.footer-tagline { font-size: 0.82rem; color: rgba(30,30,30,0.4); }
.footer-links { display: flex; gap: 2rem; }
.footer-links a { font-size: 0.82rem; color: rgba(30,30,30,0.5); text-decoration: none; }
.footer-links a:hover { color: #1E1E1E; }
.footer-badge {
    font-size: 0.75rem; background: rgba(255,215,0,0.12);
    color: #B8960C; padding: 0.3rem 0.8rem; border-radius: 50px;
    font-weight: 500;
}

/* ===== DIVIDER ===== */
.divider {
    height: 1px; background: rgba(30,30,30,0.07);
    max-width: 1200px; margin: 0 auto;
}

/* ===== SPACER ===== */
.spacer-lg { height: 6rem; }
.spacer-md { height: 3rem; }
</style>
""", unsafe_allow_html=True)

# ── NAVBAR ────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav">
    <div class="nav-logo">
        <div class="nav-bolt"></div>
        Floxia Service
    </div>
    <div class="nav-links">
        <a href="#services">Services</a>
        <a href="#simulateur">ROI</a>
        <a href="#demo">Démo IA</a>
        <a href="#contact" class="nav-cta">Commencer →</a>
    </div>
</nav>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="hero">
    <div class="hero-badge">
        <div class="hero-badge-dot"></div>
        IA pour artisans & PME
    </div>
    <h1 class="hero-title">
        Arrêtez de subir<br>votre paperasse.<br><span>Automatisez-la.</span>
    </h1>
    <p class="hero-sub">
        Floxia transforme vos tâches administratives répétitives en workflows automatisés.
        Devis, relances, rapports — tout, sans lever le petit doigt.
    </p>
    <div class="cta-group">
        <button class="btn-primary" onclick="document.getElementById('simulateur-section').scrollIntoView({behavior:'smooth'})">
            ⚡ Calculer mon gain de temps
        </button>
        <button class="btn-secondary" onclick="document.getElementById('demo-section').scrollIntoView({behavior:'smooth'})">
            Voir la démo IA
        </button>
    </div>
    <div class="hero-stats">
        <div class="stat-item">
            <div class="stat-num">16<span>h</span></div>
            <div class="stat-label">gagnées/mois en moyenne</div>
        </div>
        <div class="stat-item">
            <div class="stat-num"><span>−</span>80<span>%</span></div>
            <div class="stat-label">de temps administratif</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">3<span>min</span></div>
            <div class="stat-label">pour générer un devis</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── SERVICES ──────────────────────────────────────────────────────────────────
st.markdown("""
<div id="services" style="scroll-margin-top: 80px;">
<div class="section">
    <div class="section-label">L'écosystème Floxia</div>
    <h2 class="section-title">Tout ce dont vous avez besoin,<br>connecté ensemble.</h2>
    <p class="section-sub">Quatre briques intelligentes qui s'assemblent pour couvrir l'ensemble de votre flux administratif.</p>
    <div class="cards-grid">
        <div class="service-card">
            <div class="card-icon">💬</div>
            <div class="card-title">Devis WhatsApp</div>
            <div class="card-desc">Envoyez un message vocal, Floxia génère et envoie automatiquement votre devis PDF au client en moins de 3 minutes.</div>
            <span class="card-tag">⚡ Gain : 45 min/devis</span>
        </div>
        <div class="service-card">
            <div class="card-icon">🔔</div>
            <div class="card-title">Relance Automatique</div>
            <div class="card-desc">Plus jamais un devis oublié. Relances SMS et e-mail programmées intelligemment selon le profil du client.</div>
            <span class="card-tag">⚡ +30% de conversion</span>
        </div>
        <div class="service-card">
            <div class="card-icon">📸</div>
            <div class="card-title">Scan de Tickets IA</div>
            <div class="card-desc">Photographiez vos tickets de caisse chantier. L'IA extrait automatiquement les montants et les intègre à votre compta.</div>
            <span class="card-tag">⚡ Zéro ressaisie</span>
        </div>
        <div class="service-card">
            <div class="card-icon">🎙️</div>
            <div class="card-title">Rapports Vocaux</div>
            <div class="card-desc">Dictez votre rapport de fin de journée en 2 minutes. Floxia le structure, le met en page et l'envoie au client.</div>
            <span class="card-tag">⚡ Rapport en 2 min</span>
        </div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── ROI SIMULATOR ─────────────────────────────────────────────────────────────
st.markdown("""
<div id="simulateur-section" style="scroll-margin-top: 80px;">
<div class="section">
    <div class="section-label">Simulateur ROI</div>
    <h2 class="section-title">Calculez votre temps libéré.</h2>
    <p class="section-sub">Bougez le curseur pour voir ce que Floxia peut faire pour vous chaque mois.</p>
</div>
</div>
""", unsafe_allow_html=True)

col_l, col_r = st.columns([1, 1], gap="large")

with col_l:
    st.markdown("""
    <div class="roi-wrapper">
        <div class="roi-slider-label">Nombre de devis par mois</div>
    """, unsafe_allow_html=True)

    nb_devis = st.slider(
        label="",
        min_value=1,
        max_value=80,
        value=15,
        step=1,
        key="roi_slider",
        label_visibility="collapsed"
    )

    # Calculs
    temps_par_devis = 64          # minutes par devis sans Floxia
    temps_floxia = 3              # minutes avec Floxia
    temps_relances = nb_devis * 12  # 12 min/relance sans Floxia
    temps_relances_floxia = 0

    heures_gagnees = round(((temps_par_devis - temps_floxia) * nb_devis + temps_relances) / 60, 1)
    gain_euros = round(heures_gagnees * 55)   # taux horaire artisan ~55€
    roi_pourcent = round((gain_euros / 99) * 100)  # abonnement Floxia ~99€/mois

    st.markdown(f"""
        <div class="roi-result">
            <div style="font-size: 0.78rem; color: rgba(247,245,240,0.45); text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 1.2rem;">
                Résultats pour {nb_devis} devis/mois
            </div>
            <div class="roi-result-grid">
                <div>
                    <div class="roi-metric-val">{heures_gagnees}h</div>
                    <div class="roi-metric-lbl">temps libéré</div>
                </div>
                <div>
                    <div class="roi-metric-val">{gain_euros}€</div>
                    <div class="roi-metric-lbl">valeur récupérée</div>
                </div>
                <div>
                    <div class="roi-metric-val">{roi_pourcent}%</div>
                    <div class="roi-metric-lbl">ROI mensuel</div>
                </div>
            </div>
        </div>
        <div style="font-size: 0.75rem; color: rgba(247,245,240,0.25); margin-top: 1rem;">
            *Basé sur un taux horaire artisan de 55€/h et un abonnement Floxia à 99€/mois.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_r:
    st.markdown("""
    <div style="padding: 2rem 0;">
        <div class="section-label">Comment ça marche</div>
        <div class="process-grid" style="grid-template-columns: 1fr; gap: 1.5rem; margin-top: 1.5rem;">
            <div class="process-step" style="text-align: left; display: flex; gap: 1rem; align-items: flex-start;">
                <div class="step-num" style="min-width:52px;">1</div>
                <div>
                    <div class="step-title">Connectez vos outils</div>
                    <div class="step-desc">WhatsApp Business, Gmail, Google Drive — configuration en 15 minutes sans technique.</div>
                </div>
            </div>
            <div class="process-step" style="text-align: left; display: flex; gap: 1rem; align-items: flex-start;">
                <div class="step-num" style="min-width:52px;">2</div>
                <div>
                    <div class="step-title">Parlez ou photographiez</div>
                    <div class="step-desc">Message vocal, photo de ticket, note de chantier — Floxia comprend et traite.</div>
                </div>
            </div>
            <div class="process-step" style="text-align: left; display: flex; gap: 1rem; align-items: flex-start;">
                <div class="step-num" style="min-width:52px;">3</div>
                <div>
                    <div class="step-title">L'IA travaille pour vous</div>
                    <div class="step-desc">Devis généré, envoyé, relancé. Rapport structuré. Ticket comptabilisé. Automatiquement.</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider" style="margin-top: 3rem;"></div>', unsafe_allow_html=True)

# ── DEMO IA ───────────────────────────────────────────────────────────────────
st.markdown("""
<div id="demo-section" style="scroll-margin-top: 80px;">
<div class="section">
    <div class="section-label">Démo en direct</div>
    <h2 class="section-title">Testez l'IA Floxia<br>maintenant.</h2>
    <p class="section-sub">Dictez une note vocale ou décrivez un ticket de chantier. L'IA analyse et structure en temps réel.</p>
</div>
</div>
""", unsafe_allow_html=True)

demo_col_l, demo_col_r = st.columns([1, 1], gap="large")

with demo_col_l:
    st.markdown('<div class="demo-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="demo-header">
        <div class="demo-dot"></div>
        <div>
            <div class="demo-title">Analyse IA Floxia</div>
            <div class="demo-subtitle">Powered by Claude (Anthropic)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    note_input = st.text_area(
        "VOTRE NOTE OU TICKET",
        placeholder="Ex: Chantier Dupont – pose de 12m² de carrelage salle de bain, joint époxy gris clair, dépose ancienne faïence incluse. Matériaux : 85€ de carrelage, 22€ de joint, 15€ de colle...",
        height=160,
        key="demo_note",
        label_visibility="visible"
    )

    if st.button("⚡ Analyser avec l'IA Floxia", key="demo_btn"):
        if note_input.strip():
            with st.spinner(""):
                try:
                    client = anthropic.Anthropic()
                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=600,
                        messages=[{
                            "role": "user",
                            "content": f"""Tu es l'assistant IA de Floxia Service, spécialisé dans l'automatisation administrative pour les artisans.

Analyse cette note de chantier ou ce ticket et produis :
1. **Synthèse** : résumé en 1-2 phrases
2. **Éléments détectés** : liste structurée (main d'œuvre, matériaux, montants)
3. **Action recommandée** : devis, facture, rapport, ou autre
4. **Estimation rapide** : fourchette de prix HT si applicable

Note/ticket : {note_input}

Réponds de façon concise et professionnelle, en français."""
                        }]
                    )
                    ai_text = response.content[0].text
                    st.session_state["demo_result"] = ai_text
                except Exception as e:
                    st.session_state["demo_result"] = f"Erreur de connexion : {e}"
        else:
            st.warning("Veuillez entrer une note ou un ticket.")

    if "demo_result" in st.session_state and st.session_state["demo_result"]:
        result_html = st.session_state["demo_result"].replace(
            "**", "<strong>").replace("**", "</strong>")
        # Simple bold replacement
        import re
        result_formatted = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>',
                                   st.session_state["demo_result"])
        st.markdown(f'<div class="ai-response">{result_formatted}</div>',
                    unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

CARD_STYLE = (
    "background:#fff;"
    "border:1px solid rgba(30,30,30,0.08);"
    "border-radius:16px;"
    "padding:1.2rem 1.5rem;"
    "transition:border-color .25s;"
)
TAG_STYLE = (
    "font-size:0.72rem;"
    "text-transform:uppercase;"
    "letter-spacing:0.08em;"
    "color:#B8960C;"
    "margin-bottom:0.4rem;"
    "font-weight:600;"
)
TEXT_STYLE = (
    "font-size:0.85rem;"
    "color:rgba(30,30,30,0.65);"
    "line-height:1.6;"
    "font-style:italic;"
)

with demo_col_r:
    st.markdown(f"""
    <div style="padding:1.5rem 0;">
        <div style="font-size:0.75rem;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:#B8960C;margin-bottom:0.5rem;">
            Exemples à tester
        </div>
        <p style="font-size:0.88rem;color:rgba(30,30,30,0.5);line-height:1.6;margin-bottom:1.5rem;">
            Copiez-collez l'un de ces exemples dans le champ pour tester l'IA.
        </p>
        <div style="display:flex;flex-direction:column;gap:1rem;">
            <div style="{CARD_STYLE}">
                <div style="{TAG_STYLE}">🎙️ Note vocale</div>
                <div style="{TEXT_STYLE}">
                    "Chantier Martin, peinture salon 28m², 2 couches, sous-couche comprise.
                    J'ai utilisé 4 pots de 5L à 28€ chaque. Compter 6h de boulot."
                </div>
            </div>
            <div style="{CARD_STYLE}">
                <div style="{TAG_STYLE}">🧾 Ticket matériaux</div>
                <div style="{TEXT_STYLE}">
                    "Leroy Merlin – Vis 6x80 x200 = 4.90€, Chevilles diam8 x100 = 6.50€,
                    Placo 120x250 x3 = 47€, Bande placo = 8.20€. Total 66.60€."
                </div>
            </div>
            <div style="{CARD_STYLE}">
                <div style="{TAG_STYLE}">🏗️ Fin de chantier</div>
                <div style="{TEXT_STYLE}">
                    "Chantier Leblanc terminé aujourd'hui. Électricité cuisine OK,
                    tableau mis à jour, prises USB installées. Réserve : attente carreleur
                    pour finition plinthe."
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider" style="margin-top: 3rem;"></div>', unsafe_allow_html=True)

# ── TESTIMONIALS ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-label">Ils nous font confiance</div>
    <h2 class="section-title">Ce que disent nos artisans.</h2>
    <div class="testimonials-grid">
        <div class="testi-card">
            <div class="testi-stars">★★★★★</div>
            <p class="testi-text">"Avant Floxia, je passais mes soirées à taper des devis. Maintenant j'envoie un message et c'est fait. Mes clients reçoivent un PDF pro en 3 minutes."</p>
            <div class="testi-author">
                <div class="testi-avatar">TP</div>
                <div>
                    <div class="testi-name">Thomas P.</div>
                    <div class="testi-role">Plombier – Caen</div>
                </div>
            </div>
        </div>
        <div class="testi-card">
            <div class="testi-stars">★★★★★</div>
            <p class="testi-text">"Le scan de tickets IA m'a changé la vie. Plus de saisie manuelle, plus d'erreurs en compta. Je gagne facilement 8h par mois juste sur ça."</p>
            <div class="testi-author">
                <div class="testi-avatar">MR</div>
                <div>
                    <div class="testi-name">Marie R.</div>
                    <div class="testi-role">Électricienne – Lyon</div>
                </div>
            </div>
        </div>
        <div class="testi-card">
            <div class="testi-stars">★★★★★</div>
            <p class="testi-text">"Les relances automatiques ont boosté mon taux d'acceptation de devis de 20%. Je n'aurais jamais eu le temps de le faire moi-même."</p>
            <div class="testi-author">
                <div class="testi-avatar">KA</div>
                <div>
                    <div class="testi-name">Karim A.</div>
                    <div class="testi-role">Menuisier – Bordeaux</div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CTA BAND ─────────────────────────────────────────────────────────────────
st.markdown("""
<div id="contact" class="cta-band">
    <h2>Prêt à récupérer<br><span>votre temps ?</span></h2>
    <p>Démarrage en 15 minutes. Sans engagement. Premier mois offert.</p>
</div>
""", unsafe_allow_html=True)

cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])
with cta_col2:
    st.markdown('<div style="background: #1E1E1E; padding: 0 5vw 4rem; text-align: center;">', unsafe_allow_html=True)
    if st.button("⚡ Démarrer gratuitement — 1 mois offert", key="main_cta"):
        st.balloons()
        st.success("🎉 Merci ! L'équipe Floxia vous contacte dans les 24h.")
    st.markdown('</div>', unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="footer">
    <div>
        <div class="footer-logo">
            <div class="nav-bolt" style="width:22px;height:22px;"></div>
            Floxia Service
        </div>
        <div class="footer-tagline" style="margin-top: 0.4rem;">
            Floxia répond à tous vos besoins.
        </div>
    </div>
    <div class="footer-links">
        <a href="#">Mentions légales</a>
        <a href="#">Confidentialité</a>
        <a href="#">Contact</a>
    </div>
    <div class="footer-badge">⚡ Propulsé par l'IA</div>
</footer>
""", unsafe_allow_html=True)
