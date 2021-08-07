# Desafio 1


i_char = ">"

print("Olá, me chamo bot42");
user_name = input("Qual o seu nome:\n" + i_char)

age = input("Qual a sua idade:\n" + i_char)

id_discord = input("Qual o seu id do discord:\n" + i_char)

print(f"Seu nome é {user_name}, você tem {age} anos de idade" + 
      f" e seu id do discord é {id_discord}")

print("[bzzzzztt.... bzzzzztttt....]")
print("Agora, por gentileza, MORRA!")

# bonus 1: gravar os dados em arquivo no disco
livro_visitas = open("usuarios_eliminados.txt", 'a+')

# adicionando quebra de linha \n ao final para que não seja tudo
# escrito em uma única linha
livro_visitas.write(f"{user_name} {age} {id_discord}\n")

# bonus 2: exibar os dados gravados no arquivo na tela

# voltamos o ponteiro de leitura  que estava na última linha para o ínicio do arquivo
# fazemos isso pois queremos ler todos os usuários
livro_visitas.seek(0)
kill_list = livro_visitas.readlines() # lendo todas a linhas e guardando em lista

# imprimindo todos os usuários
for user in kill_list:
    # retirando a quebra de linha para adicionarmos a string abaixo ao final da linha
    user = user.replace('\n', ' ', 1)
    print(user + "status: eliminado")

# sempre "puxe a descarga" e "feche a tampa" após lidar com arquivos
livro_visitas.flush()
livro_visitas.close()

