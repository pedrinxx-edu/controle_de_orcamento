from difflib import get_close_matches
import csv

decisao = "sim"
totDespesas = []
listaNomeDespesas = []
despesasDetalhadas = []
opcoes_validas = [
    "1", "renda", "cadastrar renda", "um",
    "2", "despesa", "cadastrar despesa", "despesas", "consultar despesas", "dois",
    "3", "consultar saldo", "saldo", "tres", "três",
    "4", "quatro", "consultar valor de gastos", "gastos", "gasto", "consultar gasto",
    "5", "cinco", "remover", "remover despesa",
    "6", "seis", "exportar dados", "dados", "exportar", "exportar dados",
    "7", "sete", "sair", "exit"
]
renda = 0
qtdAltRenda = 0
repAviso = 0
controleTry = 0
contRepDespesa = 0
contRepRenda = 0

nome = input("Olá! Qual seu nome? ")
print(f"\nOlá {nome}, bem vindo(a)! Esse é um sistema teste de controle de orçamento")

while decisao in ("sim", "s", "ss"):
    continuar = "sim"
    if renda > 0 and repAviso > 0:
        print(f"\nPerfeito {nome} sua renda foi cadastrada!! Caso deseje, sua renda poderá ser alterada posteriormente.\n")
        repAviso = 0
    print("\n1 - Cadastrar renda \n2 - Cadastrar despesa \n3 - Consultar saldo \n4 - Consultar valor de gastos \n5 - Remover Despesa \n6 - Exportar dados \n7 - Sair")
    opcao = input("\nPara continuarmos poderia informar qual das opções acima deseja realizar? ").strip() .lower()

    if opcao not in opcoes_validas:
        parecido = get_close_matches(opcao, opcoes_validas, n=1, cutoff=0.6)
        if parecido:
            resposta = input(f"Você quis dizer {parecido[0]}? ")
            if resposta in ("sim", "s", "ss"):
                opcao = parecido[0]

    while continuar in ("sim", "ss", "s"):
        controleTry = 0
        if opcao in ("1", "renda", "cadastrar renda", "um"):
            if qtdAltRenda == 0:
                try:
                    renda = float(input("\nPerfeito! Qual o valor da sua renda? "))
                except ValueError:
                    renda = 0
                    print("\nRenda inválida! Por favor digite um número")
                    continuar = input("\nDeseja tentar novamente (sim/não)? ").strip() .lower()
                    if continuar in ("sim", "s", "ss"):
                        decisao = "sim"
                    else:
                        continuar = "não"
                        decisao = input("\nDeseja continuar usando o sistema (sim/não)? ").strip() .lower()
                        if decisao in ("sim", "s", "ss"):
                            continuar = "não"
                        else:
                            continuar = "não"
                            decisao = "não"
                            contRepRenda +=1
                    controleTry +=1
                qtdAltRenda += 1
                repAviso += 1
                saldo = renda
            else:
                try:
                    renda = float(input("\nPerfeito! Qual o valor da sua nova renda? "))
                except ValueError:
                    print("\nRenda inválida! Precisa ser um número")
                    continuar = input("\nDeseja tentar novamente (sim/não)? ").strip() .lower()
                    if continuar in ("sim", "s", "ss"):
                        continue
                    else:
                        continuar = "não"
                        decisao = input("\nDeseja continuar usando o sistema (sim/não)? ").strip() .lower()
                        if decisao in ("sim", "s", "ss"):
                            continuar = "não"
                        else:
                            continuar = "não"
                            decisao = "não"
                qtdAltRenda += 1
                repAviso += 1
                saldo = renda - sum(totDespesas)
            if renda > 0:
                decisao = input(f"\n{nome} o valor da renda em R$ {renda:.2f} está correto (sim/não)? ").strip() .lower()
                if decisao in ("sim", "ss", "s"):
                    continuar = "não"
                else:
                    print("\nRenda não cadastrada")
                    continuar = input("\nDeseja tentar cadastrar de novo (sim/não)? ").strip() .lower()
                    repAviso = 0
                    if continuar in ("sim", "s", "ss"):
                        continue
                    else:
                        decisao = input("\nDeseja continuar usando o sistema (sim/não)? ").strip() .lower()
                        if decisao in ("sim", "s", "ss"):
                            continuar = "não"
                        else:
                            continuar = "não"
                            decisao = "não"
            else:
                if controleTry == 0:
                    print("\nRenda inválida")
                    continuar = "não"
                else:
                    if contRepRenda == 0:
                        qtdAltRenda = 0
                        continuar = "sim"
                    else:
                        continuar = "não"
        
        elif opcao in ("2", "despesa", "cadastrar despesa", "despesas", "consultar despesas", "dois"):
            repDespesa = "sim"
            while repDespesa in ("sim", "s", "ss"):
                if renda > 0:
                    nomeDespesa = input("\nPerfeito! Qual o nome da despesa? ")
                    try:
                        despesa = float(input("\nE qual o valor da despesa? "))
                    except ValueError:
                        print("\nDespesa inválida! Precisa ser um número")
                        despesa = 0
                        repDespesa = input("\nDeseja tentar cadastrar de novo (sim/não)? ").strip() .lower()
                        if repDespesa in ("sim", "s", "ss"):
                            contRepDespesa += 1
                            continue
                        else:
                            print("\nPerfeito! Vamos continuar então.")
                            repDespesa = "não"
                            continuar = "não"
                        controleTry += 1
                    if  0 < despesa <= saldo:
                        confirmacaoDespesa = input(f"\n{nome} o valor da despesa em R$ {despesa:.2f} está correto (sim/não)? ").strip() .lower()
                        if confirmacaoDespesa in ("sim", "ss", "s"):
                            repDespesa = input(f"\nDespesa cadastrada {nome}! Deseja cadastrar mais despesas (sim/não)? ").strip() .lower()
                            listaNomeDespesas.append(nomeDespesa)
                            totDespesas.append(despesa)
                            despesasDetalhadas.append([nomeDespesa, despesa])
                            saldo = renda - sum(totDespesas)
                        else:
                            print("\nDespesa não cadastrada")
                            repDespesa = input("\nDeseja tentar cadastrar de novo (sim/não)? ").strip() .lower()
                        if repDespesa in ("sim", "s", "ss"):
                            continue
                        else: 
                            print("\nPerfeito! Vamos continuar então.")
                            repDespesa = "não"
                            continuar = "não"
                    else:
                        if controleTry == 0:
                            print("\nDespesa inválida")
                            repDespesa = "sim"
                        else:
                            if contRepDespesa == 0:
                                repDespesa = "nao"
                            else:
                                repDespesa = "sim"
                else:
                    repDespesa = "não"
                    print("\nVocê precisa cadastrar sua renda primeiro!")
                    continuar = "não"
        
        elif opcao in ("3", "consultar saldo", "saldo", "tres", "três"):
            if renda == 0:
                print("\nVocê precisa cadastrar sua renda antes de consultar o saldo!")
                continuar = "não"
            else:
                saldo = renda - sum(totDespesas)
                continuar = "não"
                print(f"\nPerfeito {nome}! Seu saldo atual é de R${saldo:.2f}")
        
        elif opcao in ("4", "quatro", "consultar valor de gastos", "gastos", "gasto", "consultar gasto"):
            if renda == 0:
                print("\nVocê precisa cadastrar sua renda antes de consultar os gastos!")
                continuar = "não"
            else:
                print(f"\nPerfeito {nome}! O valor total de seus gastos é R${sum(totDespesas):.2f}")
                continuar = "não"

        elif opcao in ("5", "cinco", "remover", "remover despesa"):
            if len(listaNomeDespesas) == 0:
                print("\nVocê ainda não tem despesas cadastradas!")
                continuar = "não"
            else:
                print(f"\nPerfeito {nome}! Aqui estão suas despesas:")
                contagem = 1
                for nomesDespesas in listaNomeDespesas:
                    print(f"{contagem} - {nomesDespesas}")
                    contagem += 1
                try:
                    remove = int(input("\nQual seria a opção a ser removida (Selecione o número respectivo)? ").strip())
                except ValueError:
                    remove = 0
                if 1 <= remove <= len(listaNomeDespesas):
                    despesasDetalhadas.pop(remove - 1)
                    listaNomeDespesas.pop(remove - 1)
                    totDespesas.pop(remove - 1)
                    saldo = renda - sum(totDespesas)
                    print("\nDespesa removida!")
                    continuar = "não"
                else:
                    print("\nNúmero inválido! Digite um número da lista.")
                    continuar = input("\nDeseja tentar de novo (sim/não)? ").strip() .lower()
                    if continuar not in ("sim", "s", "ss"):
                        continuar = "não"

        elif opcao in ("6", "seis", "exportar dados", "dados", "exportar", "exportar dados"):
            if renda == 0:
                print("\nVocê precisa cadastrar sua renda antes de exportar os dados!")
                continuar = "não"
            else:  
                saldo = renda - sum(totDespesas)
                dados = [
                    ["Nome", "Renda", "Despesas Totais", "Saldo Restante"],
                    [nome, str(renda).replace(".", ","), str(sum(totDespesas)).replace(".", ","), str(saldo).replace(".", ",")]
                ]

                csvDespesas = [
                    ["Despesas", "Valor"]
                ]

                with open(f"{nome}Despesas.csv", "w", newline="", encoding="utf-8") as arquivo:
                    escritor = csv.writer(arquivo, delimiter=";")
                    escritor.writerows(dados)
                    escritor.writerow([])
                    escritor.writerows(csvDespesas)
                    for nomeDespesa, despesa in despesasDetalhadas:
                        escritor.writerow([nomeDespesa, f"{despesa:.2f}".replace(".", ",")])
                    print(f"\nPerfeito {nome}! Seu arquivo CSV foi criado com sucesso.\n")
                continuar = "não"
        
        elif opcao in ("7", "sete", "sair", "exit"):
            continuar = "não"
            decisao = "não"
        
        else:
            print("\nOpção Inválida!")
            continuar = "não"
            decisao = input("\nDeseja continuar usando o sistema (sim/não)? ").strip() .lower()
            if decisao in ("sim", "s", "ss"):
                continuar = "não"
            else:
                continuar = "não"
                decisao = "não"
print(f"\n\nMuito obrigado por utilizar nosso sistema {nome}! Até a próxima.\n\n")