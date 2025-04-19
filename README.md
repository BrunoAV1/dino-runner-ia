# 🦖 Dino Runner IA — Aprendizado por Reforço em Pygame  

Projeto educacional que demonstra uma IA aprendendo, via **Q-Learning**, a jogar um clone do Dino do Chrome.  
A cada tentativa, a IA evolui sua capacidade de desviar dos obstáculos, aprimorando sua estratégia com base em erros anteriores.

---

## 📌 Tecnologias Utilizadas  

- **Python 3.10+** — Linguagem principal utilizada para a implementação da IA e da lógica do jogo.  
- **Pygame** — Framework para desenvolvimento de jogos 2D em Python.  
- **Q-Learning** — Algoritmo de aprendizado por reforço que permite a IA melhorar sua jogabilidade.  
- **Pickle** — Utilizado para salvar e carregar o conhecimento adquirido pela IA.

---

## 🎮 Como Funciona  

A IA analisa os seguintes fatores:  

✅ **Distância** até o primeiro e segundo obstáculos.  
✅ **Altura** dos obstáculos.  
✅ **Sua posição vertical** (se está pulando ou não).  

Com base nessas variáveis, a IA decide entre duas ações:  

- `0` → **não pular**  
- `1` → **pular**  

Ela recebe **recompensa positiva ao sobreviver** e **penalização ao colidir**, ajustando sua estratégia para melhorar a cada rodada.

---

## 🚀 Como Rodar o Projeto  

### 1️⃣ Clone o repositório  

```bash
git clone https://github.com/BrunoAV1/dino-runner-ia.git
cd dino-runner-ia
```

### 2️⃣ Crie um ambiente virtual  

```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# Linux/macOS
source venv/bin/activate
```

### 3️⃣ Instale as dependências  

```bash
pip install pygame
```

### 4️⃣ Execute o jogo  

```bash
python main.py
```

---

## 🎯 Controles  

| Tecla | Função |  
|-------|-----------------------------|  
| `T`   | Ativar/desativar modo turbo (300 FPS) |  
| `R`   | Resetar o cérebro da IA (Q-table) |  

---

## 📈 Dificuldade Progressiva  

O jogo começa fácil e aumenta gradativamente a dificuldade:  

| Pontuação | Intervalo entre obstáculos |  
|-----------|----------------------------|  
| 0 - 10    | 1200ms                      |  
| 10 - 20   | 1000ms                      |  
| 20 - 30   | 800ms                       |  
| 30 - 50   | 700ms                        |  
| 50 - 80   | 600ms                        |  
| 80+       | 500ms                        |  

Quanto maior a pontuação, menor o tempo de reação! 🚀  

---

## 💾 Salvamento da IA  

A IA **salva** seu aprendizado automaticamente para evoluir ao longo das execuções:  

- O arquivo `q_table.pkl` **armazena a experiência acumulada**.  
- A IA **fica mais eficiente a cada nova rodada**.  
- **Pressionar `R` durante o jogo apaga a memória** e reinicia do zero.

---

## 📁 Estrutura do Projeto  

```plaintext
dino-runner-ia/
├── ai/
│   └── agent.py         # IA baseada em Q-Learning
├── assets/              # Pasta para sprites e sons (opcional)
├── game.py              # Mecânica e lógica do jogo
├── main.py              # Arquivo principal de execução
├── q_table.pkl          # Memória da IA (salva automaticamente)
└── README.md            # Documentação do projeto
```

---

## 🧠 Conceitos Aplicados  

✔️ **Q-Learning** — Aprendizado por reforço sem supervisão direta.  
✔️ **Discretização** de variáveis contínuas para tomada de decisão.  
✔️ **Machine Learning** sem bibliotecas externas sofisticadas.  
✔️ **Jogo 2D** desenvolvido com **Pygame**.  
✔️ **Persistência de dados** para manter aprendizado ao longo do tempo.  

---

## 🤝 Contribuição  

🔹 Curtiu o projeto? Sinta-se à vontade para contribuir!  
Sugestões de melhorias:  

✅ **Criar novos desafios** para tornar o jogo mais desafiador.  
✅ **Adicionar power-ups** para variar a jogabilidade.  
✅ **Melhorar o visual** com sprites ou animações.  
✅ **Implementar novos sons** para feedback auditivo.  

📌 **Pull requests são muito bem-vindos!**  

---

## 👨‍💻 Autor  

**Bruno Vasconcellos**  

Este projeto foi desenvolvido com fins didáticos para aprofundar o aprendizado de IA em ambientes gamificados.
