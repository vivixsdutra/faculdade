from app.database import SessionLocal, engine, Base
from app import models

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Gêneros
nomes = ['Ação','Aventura','Drama','Comédia','Terror','Ficção Científica','Animação','Thriller','Romance','Crime']
objs = []
for nome in nomes:
    g = models.Genero(nome=nome)
    db.add(g)
    objs.append(g)
db.commit()
for g in objs:
    db.refresh(g)

gen = {g.nome: g for g in objs}

# Filmes
filmes_data = [
    dict(
        titulo='Inception', tipo='filme', ano=2010,
        diretor='Christopher Nolan', duracao_min=148,
        poster_url='https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg',
        sinopse='Um ladrão especialista em invadir sonhos recebe a missão de plantar uma ideia na mente de um empresário.',
        generos=[gen['Ação'], gen['Ficção Científica'], gen['Thriller']]
    ),
    dict(
        titulo='Interstellar', tipo='filme', ano=2014,
        diretor='Christopher Nolan', duracao_min=169,
        poster_url='https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
        sinopse='Astronautas viajam por um buraco de minhoca em busca de um novo lar para a humanidade.',
        generos=[gen['Aventura'], gen['Drama'], gen['Ficção Científica']]
    ),
    dict(
        titulo='Breaking Bad', tipo='serie', ano=2008,
        diretor='Vince Gilligan', duracao_min=None,
        poster_url='https://image.tmdb.org/t/p/w500/ggFHVNu6YYI5L9pCfOacjizRGt.jpg',
        sinopse='Um professor de química se torna fabricante de metanfetamina após ser diagnosticado com câncer.',
        generos=[gen['Crime'], gen['Drama'], gen['Thriller']]
    ),
    dict(
        titulo='O Rei Leão', tipo='filme', ano=1994,
        diretor='Roger Allers', duracao_min=88,
        poster_url='https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg',
        sinopse='O jovem leão Simba precisa enfrentar seu passado para se tornar o rei que seu reino precisa.',
        generos=[gen['Animação'], gen['Aventura'], gen['Drama']]
    ),
    dict(
        titulo='Stranger Things', tipo='serie', ano=2016,
        diretor='Irmãos Duffer', duracao_min=None,
        poster_url='https://image.tmdb.org/t/p/w500/49WJfeN0moxb9IPfGn8AIqMGskD.jpg',
        sinopse='Um grupo de crianças descobre forças sobrenaturais e experimentos secretos em sua cidade.',
        generos=[gen['Terror'], gen['Ficção Científica'], gen['Drama']]
    ),
    dict(
        titulo='Pulp Fiction', tipo='filme', ano=1994,
        diretor='Quentin Tarantino', duracao_min=154,
        poster_url='https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
        sinopse='Histórias entrelaçadas de criminosos, um boxeador e assassinos em Los Angeles.',
        generos=[gen['Crime'], gen['Drama'], gen['Thriller']]
    ),
]

filmes = []
for f_data in filmes_data:
    gens = f_data.pop('generos')
    f = models.Filme(**f_data)
    f.generos = gens
    db.add(f)
    filmes.append(f)

db.commit()
for f in filmes:
    db.refresh(f)

# Avaliações
avaliacoes = [
    # Inception
    dict(filme=filmes[0], autor='Carlos', nota=9.5, comentario='Obra-prima do Nolan! Cada detalhe é perfeito.'),
    dict(filme=filmes[0], autor='Ana', nota=8.0, comentario='Muito complexo na primeira vez, mas incrível.'),
    dict(filme=filmes[0], autor='Pedro', nota=10.0, comentario='Melhor filme que já assisti na vida.'),
    # Interstellar
    dict(filme=filmes[1], autor='Julia', nota=9.0, comentario='A cena do buraco negro me deixou sem palavras.'),
    dict(filme=filmes[1], autor='Marcos', nota=8.5, comentario='Trilha sonora do Hans Zimmer é inesquecível.'),
    # Breaking Bad
    dict(filme=filmes[2], autor='Lucas', nota=10.0, comentario='A melhor série já feita. Ponto final.'),
    dict(filme=filmes[2], autor='Fernanda', nota=9.8, comentario='Walter White é o personagem mais bem escrito da TV.'),
    dict(filme=filmes[2], autor='Rafael', nota=9.5, comentario='Cada temporada melhor que a anterior.'),
    # O Rei Leão
    dict(filme=filmes[3], autor='Beatriz', nota=9.0, comentario='Clássico eterno! Cresci assistindo e ainda me emociona.'),
    dict(filme=filmes[3], autor='Thiago', nota=8.5, comentario='As músicas são inesquecíveis até hoje.'),
    # Stranger Things
    dict(filme=filmes[4], autor='Camila', nota=9.0, comentario='A primeira temporada é perfeita!'),
    dict(filme=filmes[4], autor='Diego', nota=8.0, comentario='Muito nostalgia dos anos 80, adorei.'),
    # Pulp Fiction
    dict(filme=filmes[5], autor='Rodrigo', nota=9.5, comentario='Tarantino no seu melhor. Diálogos geniais.'),
    dict(filme=filmes[5], autor='Isabela', nota=8.5, comentario='Estrutura narrativa única, muito criativo.'),
]

for a in avaliacoes:
    filme = a.pop('filme')
    av = models.Avaliacao(**a, filme_id=filme.id)
    db.add(av)

db.commit()
db.close()
print('Seed concluido! Filmes, generos e avaliacoes cadastrados.')
