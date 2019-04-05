__alunos__ = ["email_aluno_1", "email_aluno2"]
import auxiliares as aux


def calcula_media_palavras_livro(palavras):
    """
    (list) -> (dict)
    Recebe uma lista de palavras e devolve um Dicionário Python onde cada
    chave é uma das palavras passadas como paramêtro e o valor associado é a
    média de ocorrências da palavra nos livros da bíblia.
    """

    biblia = {}
    livros = 0
    for linha in aux.le_biblia():
        if aux.eh_novo_livro(linha):
            livros += 1
        for palavra in linha.split():
            if palavra not in biblia:
                biblia[palavra] = 1
            else:
                biblia[palavra] += 1
    medias = {}
    for palavra in palavras:
        if palavra in biblia:
            medias[palavra] = biblia[palavra]/livros
        else:
            medias[palavra] = 0
    return medias


print(calcula_media_palavras_livro(['angel']))
