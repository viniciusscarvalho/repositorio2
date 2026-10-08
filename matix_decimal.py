import random

def criar_tabuleiro():
    """
    Cria o tabuleiro 5x5 com 24 moedas decimais e 1 curinga (R$).
    """
    # Lista com as 24 moedas conforme o documento
    moedas = [0.05]*6 + [0.10]*6 + [0.25]*6 + [0.50]*6
    random.shuffle(moedas)
    
    # Inserção do Curinga no meio (ou posição aleatória)
    tabuleiro = []
    idx = 0
    curinga_pos = (2, 2) # Posição central inicial
    
    for l in range(5):
        linha = []
        for c in range(5):
            if (l, c) == curinga_pos:
                linha.append("  R$  ")
            else:
                linha.append(moedas[idx])
                idx += 1
        tabuleiro.append(linha)
        
    return tabuleiro, curinga_pos

def exibir_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro formatado no terminal.
    """
    print("\n   " + " ".join([f"  C{c}  " for c in range(5)]))
    print("  " + "------" * 5)
    for l in range(5):
        linha_str = f"L{l} |"
        for c in range(5):
            val = tabuleiro[l][c]
            if val == "  R$  ":
                linha_str += f"{val}|"
            elif val == " --- ":
                linha_str += f"{val}|"
            else:
                linha_str += f" R${val:.2f}|"
        print(linha_str)
    print("  " + "------" * 5 + "\n")

def tem_jogada_valida(tabuleiro, referencia, orientacao):
    """
    Verifica se existem peças disponíveis na linha ou coluna de referência.
    """
    ref_l, ref_c = referencia
    if orientacao == "H": # Horizontal: busca na mesma linha
        for c in range(5):
            if tabuleiro[ref_l][c] not in ["  R$  ", " --- "]:
                return True
    else: # Vertical: busca na mesma coluna
        for l in range(5):
            if tabuleiro[l][ref_c] not in ["  R$  ", " --- "]:
                return True
    return False

def jogar_matix_decimal():
    print("==========================================")
    print("    BEM-VINDO AO MATIX (DECIMAIS)")
    print("==========================================")
    
    # 1. Cadastro dos Jogadores
    p1_nome = input("Nome do Jogador 1: ").strip()
    p1_idade = int(input(f"Idade do(a) {p1_nome}: "))
    
    p2_nome = input("Nome do Jogador 2: ").strip()
    p2_idade = int(input(f"Idade do(a) {p2_nome}: "))
    
    # Definir quem começa (mais velho)
    if p1_idade >= p2_idade:
        jogadores = [{'nome': p1_nome, 'pontos': 0.0}, {'nome': p2_nome, 'pontos': 0.0}]
    else:
        jogadores = [{'nome': p2_nome, 'pontos': 0.0}, {'nome': p1_nome, 'pontos': 0.0}]
        
    print(f"\n-> {jogadores[0]['nome']} começa jogando por ser mais velho(a)!")

    # 2. Definir as orientações fixas de ataque
    print(f"\n{jogadores[0]['nome']}, escolha sua orientação de ataque:")
    ori1 = input("Digite 'H' para Horizontal ou 'V' para Vertical: ").strip().upper()
    while ori1 not in ['H', 'V']:
        ori1 = input("Opção inválida. Digite 'H' ou 'V': ").strip().upper()
        
    jogadores[0]['orientacao'] = ori1
    jogadores[1]['orientacao'] = 'V' if ori1 == 'H' else 'H'
    
    print(f"-> {jogadores[0]['nome']} joga no eixo: {'HORIZONTAL (Linhas)' if ori1 == 'H' else 'VERTICAL (Colunas)'}")
    print(f"-> {jogadores[1]['nome']} joga no eixo: {'VERTICAL (Colunas)' if ori1 == 'H' else 'HORIZONTAL (Linhas)'}")
    
    # 3. Inicializar o tabuleiro
    tabuleiro, curinga_pos = criar_tabuleiro()
    pos_referencia = curinga_pos  # Primeira jogada refere-se ao curinga
    
    turno = 0
    
    # Loop Principal do Jogo
    while True:
        jogador_atual = jogadores[turno % 2]
        ori = jogador_atual['orientacao']
        ref_l, ref_c = pos_referencia
        
        exibir_tabuleiro(tabuleiro)
        
        # Verificar condição de término (Sem jogadas válidas no eixo obrigatório)
        if not tem_jogada_valida(tabuleiro, pos_referencia, ori):
            print(f"⚠️ Não há peças disponíveis no eixo exigido ({'Linha ' + str(ref_l) if ori == 'H' else 'Coluna ' + str(ref_c)}).")
            print("FIM DE JOGO!")
            break
            
        print(f"🎮 Vez de **{jogador_atual['nome']}** | Seu eixo de captura: {'HORIZONTAL' if ori == 'H' else 'VERTICAL'}")
        if turno == 0:
            print(f"Referência inicial: CURINGA em (Linha {ref_l}, Coluna {ref_c})")
        else:
            print(f"Referência obrigatória: Última peça capturada em (Linha {ref_l}, Coluna {ref_c})")

        # Entrada e Validação da Jogada
        while True:
            try:
                if ori == 'H':
                    l = ref_l
                    c = int(input(f"Escolha a COLUNA (0 a 4) na Linha {l}: "))
                else:
                    c = ref_c
                    l = int(input(f"Escolha a LINHA (0 a 4) na Coluna {c}: "))
                
                # Validações
                if not (0 <= l <= 4 and 0 <= c <= 4):
                    print("Posição fora do tabuleiro! Tente novamente.")
                    continue
                
                peca = tabuleiro[l][c]
                if peca in ["  R$  ", " --- "]:
                    print("Posição inválida/vazia! Escolha uma moeda disponível.")
                    continue
                
                # Jogada válida realizada
                jogador_atual['pontos'] += peca
                tabuleiro[l][c] = " --- "  # Removida do tabuleiro
                pos_referencia = (l, c)    # Atualiza a referência para o próximo jogador
                print(f"✅ {jogador_atual['nome']} capturou R$ {peca:.2f}!")
                break
                
            except ValueError:
                print("Por favor, insira um número válido (0 a 4).")

        turno += 1

    # 4. Encerramento e Placar Final
    print("\n==========================================")
    print("             RESULTADO FINAL              ")
    print("==========================================")
    print(f"{jogadores[0]['nome']}: R$ {jogadores[0]['pontos']:.2f}")
    print(f"{jogadores[1]['nome']}: R$ {jogadores[1]['pontos']:.2f}")
    print("------------------------------------------")
    
    if jogadores[0]['pontos'] > jogadores[1]['pontos']:
        print(f"🏆 Vencedor(a): {jogadores[0]['nome']}!")
    elif jogadores[1]['pontos'] > jogadores[0]['pontos']:
        print(f"🏆 Vencedor(a): {jogadores[1]['nome']}!")
    else:
        print("🤝 Empate!")

# Execução do jogo
if __name__ == "__main__":
    jogar_matix_decimal()