
import streamlit as st
import time

st.set_page_config(page_title="Jogos da Ancestralidade", page_icon=":leaves:", layout="centered")

st.title("🌿 Jogos da Ancestralidade")
st.subheader("Desafio dos Saberes Indígenas")
st.markdown("Responda às perguntas, acumule pontos e avance nos níveis até se tornar um Guardião da Ancestralidade!")

perguntas_nivel_1 = [
    {
        "pergunta": "Qual é o povo indígena que vive no Território Arariboia?",
        "opcoes": ["Guajajara", "Yanomami", "Pataxó", "Xavante"],
        "resposta": "Guajajara"
    },
    {
        "pergunta": "O que representa a pintura corporal na cultura indígena?",
        "opcoes": ["Enfeite", "Proteção espiritual", "Moda", "Aleatoriedade"],
        "resposta": "Proteção espiritual"
    }
]

perguntas_nivel_2 = [
    {
        "pergunta": "Qual desses é um jogo tradicional indígena?",
        "opcoes": ["Corrida de tora", "Futebol", "Basquete", "Vôlei"],
        "resposta": "Corrida de tora"
    },
    {
        "pergunta": "O que significa o timbó na pesca tradicional?",
        "opcoes": ["Veneno natural", "Rede de pesca", "Canoa", "Armadilha de pedra"],
        "resposta": "Veneno natural"
    }
]

if 'pontos' not in st.session_state:
    st.session_state.pontos = 0
if 'nivel' not in st.session_state:
    st.session_state.nivel = 1

def jogar(perguntas):
    for p in perguntas:
        st.subheader(p["pergunta"])
        resposta = st.radio("Escolha uma opção:", p["opcoes"], key=p["pergunta"])
        if st.button("Responder", key=p["pergunta"]+"_botao"):
            if resposta == p["resposta"]:
                st.session_state.pontos += 1
                st.success("Resposta certa! +1 ponto")
            else:
                st.session_state.pontos -= 1
                st.error("Resposta errada! -1 ponto")
            st.info(f"Pontos atuais: {st.session_state.pontos}")

st.markdown(f"### Pontuação Atual: {st.session_state.pontos}")

if st.session_state.nivel == 1:
    st.header("Nível 1")
    jogar(perguntas_nivel_1)
    if st.session_state.pontos >= 2:
        st.success("Parabéns! Você avançou para o Nível 2!")
        st.session_state.nivel = 2
elif st.session_state.nivel == 2:
    st.header("Nível 2")
    jogar(perguntas_nivel_2)
    if st.session_state.pontos >= 4:
        st.success("Você completou o jogo e é um Guardião da Ancestralidade! 🏆")
    else:
        st.warning("Você não alcançou o nível máximo. Tente novamente!")

if st.button("Reiniciar Jogo"):
    st.session_state.pontos = 0
    st.session_state.nivel = 1
    st.experimental_rerun()
