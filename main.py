import spacy

nlp_pt = spacy.load("pt_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

doc_pt = nlp_pt("""No dia 15 de maio de 2022, ocorreu uma partida de futebol 
eletrizante entre as equipes do Real Madrid e do Barcelona. 
O jogo foi disputado no Estádio Santiago Bernabéu, em Madrid, e contou com a 
presença de renomados jogadores como Lionel Messi, Sergio Ramos, Karim Benzema e 
Gerard Piqué. A partida foi marcada por lances emocionantes, belos gols e uma 
intensa rivalidade entre as equipes. No final, o Real Madrid saiu vitorioso, com um 
placar de 3 a 2, em um jogo que ficará marcado na história do futebol.""")

frase = nlp_pt("O cachorro latiu durante a noite.")

#_____________________________________________
#Entidades no texto |
entidades_text = list(doc_pt.ents)
print(f'Entidades do texto -> {entidades_text}')


#_____________________________________________
#Classe gramaticais |
etiquetas_class = [(token.orth_, token.pos_) for token in doc_pt]
print(f'Classe gramatical das palavras -> {etiquetas_class}')

"""
ADJ: adjective
ADP: adposition
ADV: adverb
AUX: auxiliary verb
CONJ: coordinating conjunction
DET: determiner
INTJ: interjection
NOUN: noun
NUM: numeral
PART: particle
PRON: pronoun
PROPN: proper noun
PUNCT: punctuation
SCONJ: subordinating conjunction
SYM: symbol
VERB: verb
X: other

"""
#_____________________________________________
#Detalhes das entidades |
entidades_detail = [(entidade, entidade.label_) for entidade in doc_pt.ents]
print(f'Detalhamento das entidades -> {etiquetas_class}')


#_____________________________________________
#Sujeito da frase |
sujeito = [suj for suj in frase if suj.dep_ == 'nsubj']
print(f'Sujeitos -> {sujeito}')


#_____________________________________________
#Lematização |
lemmas = [token.lemma_ for token in doc_pt if token.pos_ == 'VERB']
print(f'Lematização dos verbos -> {lemmas}')