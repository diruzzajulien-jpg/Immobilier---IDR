import streamlit as st

st.set_page_config(page_title="Tableau de Bord Immo", layout="wide")

# ---- EN-TÊTE ----
st.title("🏢 Analyseur d'Annonces Immobilier")
st.write("Copiez-collez le texte de l'annonce ci-dessous. (Le remplissage automatique arrive bientôt !)")

annonce = st.text_area("📋 Collez l'annonce ici :", height=150)

if st.button("✨ Analyser l'annonce"):
    st.info("Le cerveau de l'IA sera bientôt branché ici ! En attendant, vous pouvez tester les cases ci-dessous.")

st.divider()

# ---- DISPOSITION COMME VOTRE EXCEL ----
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📘 INFORMATIONS DE BASES")
    prix = st.number_input("Prix proposé", value=260000, step=1000)
    nego = st.number_input("Négociation (Prix d'achat final)", value=234000, step=1000)
    apport = st.number_input("Apport (MdF)", value=50000, step=1000)
    
    notaire = nego * 0.077  # Environ 7,7%
    dossier_hypo = 5000
    total_acq = nego + notaire + dossier_hypo
    total_financer = total_acq - apport
    
    st.write(f"**Notaire (estimé 7,7%) :** {notaire:,.0f} €")
    st.write(f"**Dossier & Hypothèque :** {dossier_hypo:,.0f} €")
    st.write(f"**Total acquisition :** {total_acq:,.0f} €")
    st.write(f"**Total à financer :** {total_financer:,.0f} €")

with col2:
    st.markdown("### 📙 CHARGES & FINANCEMENT")
    tf = st.number_input("Taxe foncière", value=5700, step=100)
    assurances = st.number_input("Assurances (PNO + Prêt)", value=2640, step=100)
    autres_frais = st.number_input("Frais divers / Expert / Élec", value=3180, step=100)
    
    total_charges = tf + assurances + autres_frais
    st.write(f"**TOTAL CHARGES ANNUEL :** {total_charges:,.0f} €")
    
    st.markdown("### 🏦 PRÊT / RENTE")
    mensualite = st.number_input("Mensualité à régler (ou Rente)", value=1206, step=50)

with col3:
    st.markdown("### 📗 REVENUS & RÉSULTATS")
    loyers = st.number_input("Loyers perçus (Mensuel)", value=2271, step=50)
    revenus_annuels = loyers * 12
    st.write(f"**TOTAL REVENUS ANNUEL :** {revenus_annuels:,.0f} €")
    
    st.markdown("### 📊 INFORMATIONS RÉSULTATS")
    remboursements = mensualite * 12
    res_annuel = revenus_annuels - remboursements - total_charges
    res_mensuel = res_annuel / 12
    
    st.write(f"Revenus : {revenus_annuels:,.0f} €")
    st.write(f"Remboursements : - {remboursements:,.0f} €")
    st.write(f"Charges : - {total_charges:,.0f} €")
    st.write(f"**Résultat annuel : {res_annuel:,.0f} €**")
    
    if res_mensuel >= 0:
        st.success(f"**RÉSULTAT MENSUEL : + {res_mensuel:,.0f} €** 🟢")
    else:
        st.error(f"**RÉSULTAT MENSUEL : {res_mensuel:,.0f} €** 🔴")
