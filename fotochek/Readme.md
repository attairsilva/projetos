# 📸 Validador de Fotos (FotoChek)

Este é um aplicativo web desenvolvido em Python com **Streamlit** e **OpenCV**. O objetivo do sistema é automatizar a validação de fotos submetidas por colaboradores, garantindo que elas atendam a padrões rigorosos (como os exigidos em documentos oficiais ou crachás) antes de serem aceitas no sistema.

## 🚀 Funcionalidades

O sistema avalia a imagem carregada e verifica matematicamente as seguintes regras:
- **Proporção da Imagem:** Verifica se a foto está no padrão 3x4 (aspect ratio entre 0.67 e 0.83).
- **Nitidez (Foco):** Analisa a variância do Laplaciano para garantir que a foto não está borrada (índice mínimo de 60).
- **Fundo Branco:** Extrai amostras dos cantos da imagem para calcular o brilho médio (garantindo que é branco/claro).
- **Textura do Fundo:** Mede o desvio padrão das amostras de fundo para barrar fundos com texturas ou sombras fortes.

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/) - Para a interface gráfica da aplicação web.
- [OpenCV](https://opencv.org/) - Para o processamento e análise matemática da imagem.
- [NumPy](https://numpy.org/) - Para cálculos de matrizes e arrays de pixels.
- [Pillow (PIL)](https://python-pillow.org/) - Para manipulação e exibição de imagens.

## ⚙️ Como executar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   venv\Scripts\activate     # No Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install streamlit opencv-python numpy pillow
   ```

4. **Inicie a aplicação:**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador:**
   O aplicativo estará disponível no endereço `http://localhost:8501`.

## 📄 Estrutura do Projeto

- `app.py`: Arquivo principal contendo a lógica de validação e a interface do Streamlit.
- `README.md`: Documentação do projeto.