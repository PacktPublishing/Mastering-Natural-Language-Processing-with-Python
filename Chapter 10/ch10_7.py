import nltk
correct = nltk.chunk.tagstr2tree(
	"[ the/DT little/JJ cat/NN ] sat/VBD on/IN [ the/DT mat/NN ]")
print(correct.flatten())
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)

grammar = r"NP: {<PRP|DT|POS|JJ|CD|N.*>+}"
chunk_parser = nltk.RegexpParser(grammar)
tagged_tok = [("the", "DT"), ("little", "JJ"), ("cat", "NN"),("sat", "VBD"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]
chunkscore = nltk.chunk.ChunkScore()
guessed = cp.parse(correct.flatten())
chunkscore.score(correct, guessed)
print(chunkscore)
