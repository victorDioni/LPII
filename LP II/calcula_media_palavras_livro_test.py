import calcula_media_palavras_livro as cmpl


def test_jesus_the():
    dic = cmpl.calcula_media_palavras_livro(['the', 'Jesus'])
    assert abs(dic['Jesus'] - 10.909090909) < 0.0001
    assert abs(dic['the'] - 829.2878787878788) < 0.00001
