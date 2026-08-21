import streamlit as st

st.set_page_config(page_title="Calculateur Immo", layout="centered")

st.title("📊 Calculateur d'Investissement")
st.write("Vérifiez instantanément si votre cash-flow est neutre ou positif.")

# Section 1 : Base
st.header("📘 1. Le Bien")
prix = st.number_input("Prix d'achat ou Bouquet proposé (€)", value=234000, step=1000)
apport = st.number_input("Votre Apport max (€)", value=50000, step=1000)

notaire = prix * 0.07
frais_annexes = 5000
total_financer = (prix + notaire + frais_annexes) - apport

st.info(f"Frais de notaire estimés (7%) : {notaire:,.0f} €")

# Section 2 : Les sous
st.header("📗 2. Revenus & Remboursement")
loyers = st.number_input("Loyers perçus (Mensuel en €)", value=2271, step=50)
mensualite = st.number_input("Remboursement crédit ou Rente (Mensuel en €)", value=1206, step=50)

# Section 3 : Charges
st.header("📙 3. Charges")
st.write("Modifiez ces cases si l'annonce donne d'autres chiffres :")
tf = st.number_input("Taxe Foncière annuelle (€)", value=5700, step=100)
autres_charges = st.number_input("Autres charges annuelles (Assurance, divers) (€)", value=5820, step=100)

charges_mensuelles = (tf + autres_charges) / 12

# Section 4 : Le verdict
st.header("🎯 4. Résultat du Cash-Flow")
cash_flow = loyers - mensualite - charges_mensuelles

if cash_flow >= 0:
    st.success(f"✅ EXCELLENT ! Le cash-flow est POSITIF de +{cash_flow:,.0f} € par mois.")
else:
    st.error(f"❌ ATTENTION ! Le cash-flow est NÉGATIF de {cash_flow:,.0f} € par mois. Négociation obligatoire !")
