from pyswip import Prolog

# Criando o objeto Prolog
prolog = Prolog()

# Definindo fatos sobre times de futebol
prolog.assertz("time(flamengo)")
prolog.assertz("time(palmeiras)")
prolog.assertz("time(corinthians)")
prolog.assertz("time(santos)")
prolog.assertz("joga_em(cristiano, flamengo)")
prolog.assertz("joga_em(neymar, santos)")
prolog.assertz("joga_em(messi, palmeiras)")

# Definindo regras
prolog.assertz("jogador(X) :- joga_em(X, _)")
prolog.assertz("joga_no_time(X, Y) :- joga_em(X, Y)")

# Consultando se o Neymar é jogador
result = list(prolog.query("jogador(neymar)"))
print(f"jogador(neymar)? {bool(result)}")

# Consultando quais times possuem jogadores
result = list(prolog.query("joga_no_time(X, _)"))
print(f"joga_no_time(X, _)? {result}")
