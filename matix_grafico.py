import random
import tkinter as tk
from tkinter import messagebox

class MatixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MATIX DE NÚMEROS DECIMAIS")
        self.root.geometry("550x650")
        self.root.resizable(False, False)
        
        # Variáveis do jogo
        self.jogadores = []
        self.turno = 0
        self.pos_referencia = (2, 2)
        self.botoes = []
        
        self.iniciar_configuracao()

    def iniciar_configuracao(self):
        # Janela simples de diálogo/configuração inicial
        self.config_win = tk.Toplevel(self.root)
        self.config_win.title("Configuração das Duplas")
        self.config_win.geometry("300x250")
        
        tk.Label(self.config_win, text="Nome Jogador 1:").pack(pady=2)
        self.ent_p1 = tk.Entry(self.config_win)
        self.ent_p1.pack(pady=2)
        self.ent_p1.insert(0, "Jogador 1")
        
        tk.Label(self.config_win, text="Idade J1:").pack(pady=2)
        self.ent_i1 = tk.Entry(self.config_win)
        self.ent_i1.pack(pady=2)
        self.ent_i1.insert(0, "15")

        tk.Label(self.config_win, text="Nome Jogador 2:").pack(pady=2)
        self.ent_p2 = tk.Entry(self.config_win)
        self.ent_p2.pack(pady=2)
        self.ent_p2.insert(0, "Jogador 2")
        
        tk.Label(self.config_win, text="Idade J2:").pack(pady=2)
        self.ent_i2 = tk.Entry(self.config_win)
        self.ent_i2.pack(pady=2)
        self.ent_i2.insert(0, "14")
        
        tk.Button(self.config_win, text="Iniciar Jogo", command=self.confirmar_jogadores).pack(pady=10)

    def confirmar_jogadores(self):
        p1 = self.ent_p1.get()
        i1 = int(self.ent_i1.get())
        p2 = self.ent_p2.get()
        i2 = int(self.ent_i2.get())
        
        if i1 >= i2:
            self.jogadores = [{'nome': p1, 'pontos': 0.0, 'ori': 'H'},
                              {'nome': p2, 'pontos': 0.0, 'ori': 'V'}]
        else:
            self.jogadores = [{'nome': p2, 'pontos': 0.0, 'ori': 'H'},
                              {'nome': p1, 'pontos': 0.0, 'ori': 'V'}]
            
        self.config_win.destroy()
        self.montar_tabuleiro()

    def montar_tabuleiro(self):
        # 1. Gerar moedas
        moedas = [0.05]*6 + [0.10]*6 + [0.25]*6 + [0.50]*6
        random.shuffle(moedas)
        
        self.tabuleiro = []
        idx = 0
        for l in range(5):
            linha = []
            for c in range(5):
                if (l, c) == (2, 2):
                    linha.append("R$")
                else:
                    linha.append(moedas[idx])
                    idx += 1
            self.tabuleiro.append(linha)

        # 2. Área do Placar
        self.lbl_status = tk.Label(self.root, text="", font=("Arial", 11, "bold"))
        self.lbl_status.pack(pady=10)
        
        self.lbl_placar = tk.Label(self.root, text="", font=("Arial", 10))
        self.lbl_placar.pack(pady=5)

        # 3. Grid do Tabuleiro
        frame_grid = tk.Frame(self.root)
        frame_grid.pack(pady=10)
        
        for l in range(5):
            linha_botoes = []
            for c in range(5):
                val = self.tabuleiro[l][c]
                txt = "R$" if val == "R$" else f"R$ {val:.2f}"
                bg_cor = "#2ecc71" if val == "R$" else "#f1c40f"
                
                btn = tk.Button(frame_grid, text=txt, width=8, height=3, bg=bg_cor,
                                font=("Arial", 10, "bold"),
                                command=lambda r=l, col=c: self.executar_jogada(r, col))
                btn.grid(row=l, column=c, padx=3, pady=3)
                linha_botoes.append(btn)
            self.botoes.append(linha_botoes)

        self.atualizar_interface()

    def executar_jogada(self, l, c):
        j_atual = self.jogadores[self.turno % 2]
        ref_l, ref_c = self.pos_referencia
        ori = j_atual['ori']
        
        # Validação do eixo obrigatorio
        if ori == 'H' and l != ref_l:
            messagebox.showwarning("Jogada Inválida", f"Você deve escolher uma moeda na Linha {ref_l}!")
            return
        if ori == 'V' and c != ref_c:
            messagebox.showwarning("Jogada Inválida", f"Você deve escolher uma moeda na Coluna {ref_c}!")
            return
            
        peca = self.tabuleiro[l][c]
        if peca in ["R$", "---"]:
            messagebox.showwarning("Jogada Inválida", "Escolha uma moeda disponível!")
            return

        # Captura da moeda
        j_atual['pontos'] += peca
        self.tabuleiro[l][c] = "---"
        self.botoes[l][c].config(text="---", bg="#bdc3c7", state="disabled")
        self.pos_referencia = (l, c)
        
        self.turno += 1
        
        # Verificar Fim de Jogo
        if not self.tem_jogada_valida():
            self.lbl_status.config(text="⚠️ FIM DE JOGO! Não há jogadas válidas.")
            p1, p2 = self.jogadores[0], self.jogadores[1]
            msg = f"Placar Final:\n{p1['nome']}: R$ {p1['pontos']:.2f}\n{p2['nome']}: R$ {p2['pontos']:.2f}\n\n"
            if p1['pontos'] > p2['pontos']:
                msg += f"🏆 Vencedor: {p1['nome']}!"
            elif p2['pontos'] > p1['pontos']:
                msg += f"🏆 Vencedor: {p2['nome']}!"
            else:
                msg += "🤝 Empate!"
            messagebox.showinfo("Fim de Jogo", msg)
            return

        self.atualizar_interface()

    def tem_jogada_valida(self):
        j_proximo = self.jogadores[self.turno % 2]
        ref_l, ref_c = self.pos_referencia
        ori = j_proximo['ori']
        
        if ori == 'H':
            for c in range(5):
                if self.tabuleiro[ref_l][c] not in ["R$", "---"]:
                    return True
        else:
            for l in range(5):
                if self.tabuleiro[l][ref_c] not in ["R$", "---"]:
                    return True
        return False

    def atualizar_interface(self):
        j_atual = self.jogadores[self.turno % 2]
        p1, p2 = self.jogadores[0], self.jogadores[1]
        ref_l, ref_c = self.pos_referencia
        
        eixo_str = f"Linha {ref_l}" if j_atual['ori'] == 'H' else f"Coluna {ref_c}"
        self.lbl_status.config(text=f"Vez de: {j_atual['nome']} | Eixo Obrigatório: {eixo_str}")
        self.lbl_placar.config(text=f"{p1['nome']} (Horizontal): R$ {p1['pontos']:.2f}  |  {p2['nome']} (Vertical): R$ {p2['pontos']:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatixGUI(root)
    root.mainloop()