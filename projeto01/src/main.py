import json
from arvore_avl import AVLTree
from grafo import Grafo

ARQUIVO_CIDADES = "./cidades.json"


def carregar_cidades():
    """Carrega as cidades do arquivo JSON, se existir."""
    try:
        with open(ARQUIVO_CIDADES, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_cidades(cidades):
    """Salva as cidades no arquivo JSON."""
    with open(ARQUIVO_CIDADES, "w", encoding="utf-8") as f:
        json.dump(cidades, f, ensure_ascii=False, indent=4)

def mostrar_menu():
    print("\n🌎 MENU - Gerenciador de Cidades e Grafos")
    print("1. Cadastrar cidade")
    print("2. Remover cidade")
    print("3. Mostrar percursos da árvore (AVL)")
    print("4. Criar grafo local de uma cidade")
    print("5. Exibir complexidades teóricas")
    print("0. Sair")

def main():
    cidades = carregar_cidades()
    arvore = AVLTree()

    # Inserir cidades carregadas
    for cidade in cidades:
        arvore.insert(cidade)

    grafos = {}

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cidade = input("Nome da cidade: ").strip()
            if cidade in cidades:
                print("⚠️ Cidade já cadastrada.")
            else:
                cidades.append(cidade)
                arvore.insert(cidade)
                salvar_cidades(cidades)
                print("✅ Cidade cadastrada com sucesso. (O(log n))")

        elif opcao == "2":
            cidade = input("Nome da cidade a remover: ").strip()
            if cidade not in cidades:
                print("⚠️ Cidade não encontrada.")
            else:
                cidades.remove(cidade)
                arvore.remove(cidade)
                salvar_cidades(cidades)
                print("🗑️ Cidade removida. (O(log n))")

        elif opcao == "3":
            print("\nPercurso em ordem:", arvore.inorder())
            print("Percurso pré-ordem:", arvore.preorder())
            print("Percurso pós-ordem:", arvore.postorder())

        elif opcao == "4":
            cidade = input("Cidade para criar grafo: ").strip()
            if cidade not in cidades:
                print("⚠️ Cidade não cadastrada.")
                continue

            if cidade not in grafos:
                grafos[cidade] = Grafo()

            grafo = grafos[cidade]

            print(f"\n🌐 Gerenciando grafo local de {cidade}")
            print("1. Adicionar ligação")
            print("2. Mostrar conexões")
            print("3. Buscar caminho (BFS)")
            print("0. Voltar")

            sub = input("Escolha: ")
            if sub == "1":
                destino = input("Conectar com cidade: ")
                grafo.adicionar_aresta(cidade, destino)
                print("✅ Ligação adicionada. (O(1))")

            elif sub == "2":
                grafo.mostrar_grafo()

            elif sub == "3":
                alvo = input("Cidade de destino: ")
                grafo.busca_largura(cidade, alvo)

        elif opcao == "5":
            print("\n📘 Complexidades teóricas:")
            print("Inserção AVL: O(log n)")
            print("Remoção AVL: O(log n)")
            print("Busca AVL: O(log n)")
            print("Percursos: O(n)")
            print("Busca em largura (BFS): O(V + E)")

        elif opcao == "0":
            print("👋 Saindo... até logo!")
            break

        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
