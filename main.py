diferencas_git = {
    "fetch_vs_pull": {
        "git fetch": "Faz o download de todos os novos commits e referências do repositório remoto localmente, mas não altera os arquivos que você está editando. É uma ação segura para inspeção.",
        "git pull": "Baixa as novidades e imediatamente as aplica (via merge ou rebase) na branch em que você está trabalhando.",
        "regra_de_ouro": "git pull = git fetch + git merge."
    },
    "merge_vs_rebase": {
        "git merge": "Junta o histórico das duas branches criando um novo commit de merge. Preserva a linha do tempo exata de quando as coisas aconteceram.",
        "git rebase": "Move a base da sua branch e reaplica seus commits no topo da branch alvo. Cria um histórico linear e limpo, sem commits de merge adicionais.",
        "regra_de_ouro": "Use merge para preservar o histórico real; use rebase para manter a leitura do histórico limpa. Nunca faça rebase em commits já enviados (pushed) para branches públicas."
    },
    "reset_vs_revert": {
        "git reset": "Reescreve o histórico movendo o ponteiro da branch para um commit anterior, efetivamente apagando da linha do tempo os commits mais recentes.",
        "git revert": "Cria um novo commit cujo conteúdo é o exato inverso das alterações que você quer desfazer, mantendo todo o histórico intacto.",
        "regra_de_ouro": "Use reset para limpar bagunças no seu ambiente local; use revert para desfazer erros em branches compartilhadas (como a main)."
    }
}

conceitos_git = {
    "HEAD": {
        "definicao": "Ponteiro de referência que indica exatamente qual commit e branch você está visualizando e editando no momento.",
        "regra_de_ouro": "É o adesivo 'Você está aqui' no mapa do histórico do seu projeto."
    },
    "staging_area": {
        "definicao": "Zona intermediária (também chamada de Index) onde você prepara os arquivos modificados usando 'git add' antes de salvá-los definitivamente.",
        "regra_de_ouro": "É a 'caixa de embalagem'. Você escolhe o que entra nela e, quando faz sentido, sela a caixa com o 'git commit'."
    },
    "branch": {
        "definicao": "Uma linha independente e isolada de desenvolvimento, criada a partir de um ponto específico do histórico do código.",
        "regra_de_ouro": "É um 'universo paralelo' do projeto onde você pode mexer à vontade sem quebrar o código original da sua equipe."
    },
    "conflito_de_merge": {
        "definicao": "Situação em que o Git paralisa uma integração porque a mesma linha do mesmo arquivo foi alterada de maneiras diferentes em duas branches distintas.",
        "regra_de_ouro": "Não é um erro do sistema, mas o Git pedindo socorro humano: 'Qual destas duas edições na mesma linha eu devo manter?'."
    }
}

comandos_git_uso = {
    "git stash": {
        "quando_utilizar": "Quando tem alterações não guardadas, mas precisa de mudar de branch urgentemente sem fazer um commit de código incompleto. Guarda as alterações temporariamente.",
        "regra_de_ouro": "É uma 'gaveta mágica'. Varre a desarrumação da sua secretária para a gaveta, trabalha noutra coisa limpa e, no fim, volta a colocar tudo na secretária."
    },
    "git checkout": {
        "quando_utilizar": "Quando segue tutoriais mais antigos ou precisa de um comando 'faz-tudo' que serve tanto para mudar de branch como para restaurar ficheiros.",
        "regra_de_ouro": "É o 'canivete suíço' antigo do Git. É importante conhecê-lo, mas nas versões modernas recomenda-se o uso de ferramentas específicas (switch/restore) para evitar acidentes."
    },
    "git switch": {
        "quando_utilizar": "Quando quer apenas e de forma segura mudar de branch. Foi introduzido nas versões mais recentes para substituir o checkout nesta função específica.",
        "regra_de_ouro": "É o seu 'teletransporte' entre branches. Move o HEAD para outra linha temporal do projeto e faz apenas isso."
    },
    "git restore": {
        "quando_utilizar": "Quando quer desfazer alterações em ficheiros específicos que ainda não sofreram commit (seja para retirá-los da staging area ou reverter para o estado original).",
        "regra_de_ouro": "É o seu botão de 'Desfazer' (Ctrl+Z) para ficheiros. Restaura-os para o seu último estado seguro."
    }
}

def exibir_guia_git():
    print("=" * 60)
    print(" 📘 GLOSSÁRIO E GUIA PRÁTICO DO GIT ".center(60))
    print("=" * 60)

    # Exibindo Diferenças
    print("\n[ PARTE 1: DIFERENÇAS ENTRE COMANDOS ]")
    print("-" * 60)
    for chave, detalhes in diferencas_git.items():
        titulo = chave.replace("_", " ").upper()
        print(f"\n🔹 {titulo}")
        for k, v in detalhes.items():
            if k == "regra_de_ouro":
                print(f"   ⭐ Regra de Ouro: {v}")
            else:
                print(f"   • {k}: {v}")

    # Exibindo Conceitos
    print("\n\n[ PARTE 2: CONCEITOS FUNDAMENTAIS ]")
    print("-" * 60)
    for chave, detalhes in conceitos_git.items():
        titulo = chave.replace("_", " ").upper()
        print(f"\n🔹 {titulo}")
        print(f"   • Definição: {detalhes['definicao']}")
        print(f"   ⭐ Regra de Ouro: {detalhes['regra_de_ouro']}")

    # Exibindo Quando Utilizar
    print("\n\n[ PARTE 3: QUANDO UTILIZAR ]")
    print("-" * 60)
    for comando, detalhes in comandos_git_uso.items():
        print(f"\n🔹 {comando.upper()}")
        print(f"   • Quando usar: {detalhes['quando_utilizar']}")
        print(f"   ⭐ Regra de Ouro: {detalhes['regra_de_ouro']}")

    print("\n" + "=" * 60 + "\n")

# Executando o script
if __name__ == "__main__":
    exibir_guia_git()