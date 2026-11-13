import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Validador de Fotos", page_icon="📸")
st.title("📸 Validador de Fotos para Sistema")
st.write("Faça o upload da foto do colaborador para verificar se ela atende às restrições do sistema.")

def avaliar_foto(img):
    altura, largura, _ = img.shape
    motivos_reprovacao = []

    # 1. VALIDAÇÃO DE PROPORÇÃO (3x4 -> 0.67 a 0.83)
    proporcao = largura / altura
    if not (0.67 <= proporcao <= 0.83):
        motivos_reprovacao.append(f"**Proporção fora do 3x4:** Calculado {proporcao:.2f} (Exigido: 0.67 a 0.83)")

    # 2. VALIDAÇÃO DE NITIDEZ (Desfoque)
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nitidez = cv2.Laplacian(cinza, cv2.CV_64F).var()
    if nitidez < 60:
        motivos_reprovacao.append(f"**Foto desfocada:** Índice de nitidez {nitidez:.0f} (Mínimo exigido: 60)")

    # 3. VALIDAÇÃO DE FUNDO BRANCO E TEXTURA
    # Analisando os cantos superiores
    canto_esq = cinza[0:50, 0:50]
    canto_dir = cinza[0:50, largura-50:largura]
    
    brilho_medio = (np.mean(canto_esq) + np.mean(canto_dir)) / 2
    variacao = (np.std(canto_esq) + np.std(canto_dir)) / 2

    if brilho_medio < 225:
        motivos_reprovacao.append(f"**Fundo não branco ou com sombra:** Brilho {brilho_medio:.0f} (Mínimo exigido: 225)")
    
    if variacao > 18:
        motivos_reprovacao.append(f"**Fundo com textura:** Variação {variacao:.0f} (Máximo permitido: 18)")

    return motivos_reprovacao

# Área de Upload
arquivo_enviado = st.file_uploader("Selecione a foto (JPG ou PNG)", type=["jpg", "jpeg", "png"])

if arquivo_enviado is not None:
    # Exibir a imagem na interface usando PIL
    imagem_pil = Image.open(arquivo_enviado)
    st.image(imagem_pil, caption="Foto Submetida", width=300)
    
    # Repor o ponteiro do ficheiro para o início
    arquivo_enviado.seek(0)
    
    # Converter a imagem do Streamlit para o formato do OpenCV
    file_bytes = np.asarray(bytearray(arquivo_enviado.read()), dtype=np.uint8)
    img_cv2 = cv2.imdecode(file_bytes, 1)
    
    st.markdown("---")
    st.subheader("Resultado da Análise:")
    
    with st.spinner("A analisar proporção, nitidez e fundo..."):
        erros = avaliar_foto(img_cv2)
        
        if len(erros) == 0:
            st.success("✅ **FOTO APROVADA!** A imagem atende a todos os requisitos matemáticos do sistema.")
        else:
            st.error("❌ **FOTO REPROVADA.** O sistema identificou as seguintes restrições:")
            for erro in erros:
                st.warning(erro)