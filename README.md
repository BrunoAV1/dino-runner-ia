# 🦖 Dino Runner IA — Aprendizado por Reforço em Pygame

Projeto educacional que simula uma IA aprendendo, via **Q-Learning**, a jogar um clone do Dino do Chrome.  
A cada tentativa, a IA evolui sua capacidade de desviar dos obstáculos, aprendendo com os próprios erros.

---

## 📌 Tecnologias Utilizadas

- Python 3.10+
- Pygame
- Algoritmo de Aprendizado por Reforço (Q-Learning)
- Pickle para persistência de dados

---

## 🎮 Como Funciona

A IA observa:

- Distância até o 1º e 2º obstáculo
- Altura dos obstáculos
- Sua posição vertical (se está pulando ou não)

E decide:

- `0` → não pular  
- `1` → pular

Ela recebe **recompensa positiva se sobrevive** e **penalização se colide**. Com isso, aprende sozinha a jogar melhor a cada rodada.

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/dino-runner-ia.git
cd dino-runner-ia
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install pygame
```

### 4. Execute o jogo

```bash
python main.py
```

---

## 🎯 Controles

| Tecla | Ação                                  |
|-------|----------------------------------------|
| `T`   | Alterna modo turbo (300 FPS)           |
| `R`   | Reseta o cérebro da IA (Q-table)       |

---

## 📈 Dificuldade Progressiva

O jogo começa fácil e vai ficando cada vez mais insano:

| Score        | Delay entre obstáculos |
|--------------|------------------------|
| 0 - 10       | 1200ms                 |
| 10 - 20      | 1000ms                 |
| 20 - 30      | 800ms                  |
| 30 - 50      | 700ms                  |
| 50 - 80      | 600ms                  |
| 80+          | 500ms                  |

Quanto mais pontos, menos tempo pra respirar.

---

## 💾 Salvamento da IA

- O arquivo `q_table.pkl` guarda o aprendizado da IA.
- A IA melhora a cada execução do jogo.
- Pressionar `R` durante o jogo apaga essa memória e recomeça do zero.

---

## 📁 Estrutura do Projeto

```
dino-runner-ia/
├── ai/
│   └── agent.py         # IA baseada em Q-Learning
├── assets/              # Pasta reservada para sprites/sons (opcional)
├── game.py              # Mecânica e lógica completa do jogo
├── main.py              # Arquivo de execução principal
├── q_table.pkl          # Memória da IA (salva automaticamente)
└── README.md            # Esse readme bonito aqui
```

---

## 🧠 Conceitos Aplicados

- Q-Learning (Reforço)
- Discretização de variáveis contínuas
- Machine Learning simples sem libs externas
- Jogo 2D com Pygame
- Persistência de dados com Pickle

---

## 🤝 Contribuição

Curtiu o projeto?  
Fica à vontade pra:
- Criar novos desafios
- Adicionar power-ups
- Melhorar o visual
- Subir sprites e sons

Pull requests são bem-vindos!

---

## 👨‍💻 Autor

**Bruno Vasconcellos**  
Projeto acadêmico com fins didáticos para estudo de IA em ambientes gamificados.
