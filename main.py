import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.svm import SVR

def getPrediction(prediction, tam):
	if(prediction <= tam):
		return "praia"
	elif(prediction <= 2*tam):
		return "floresta"
	elif(prediction <= 3*tam):
		return "urbana"
	elif(prediction <= 4*tam):
		return "oceano"
	elif(prediction <= 5*tam):
		return "deserto"
	elif(prediction <= 6*tam):
		return "polar"
	elif(prediction <= 7*tam):
		return "rural"

# Read all images
tam = 5
vetor_nome = []
vetor_teste_praias = []
vetor_teste_praias_resized = []
for i in range (tam):
	aux = str(i+1)
	vetor_teste_praias.append(cv2.imread('images/teste/praia' + aux + '.jpg'))
	vetor_teste_praias_resized.append(cv2.resize(vetor_teste_praias[i], (10,10)))
	vetor_nome.append("praia" + aux)
vetor_teste_praias_resized = np.array(vetor_teste_praias_resized)

vetor_teste_florestas = []
vetor_teste_florestas_resized = []
for i in range (tam):
	aux = str(i+1)
	vetor_teste_florestas.append(cv2.imread('images/teste/floresta' + aux + '.jpg'))
	vetor_teste_florestas_resized.append(cv2.resize(vetor_teste_florestas[i], (10,10)))
	vetor_nome.append("floresta" + aux)
vetor_teste_florestas_resized = np.array(vetor_teste_florestas_resized)

vetor_teste_cidades = []
vetor_teste_cidades_resized = []
for i in range (tam):
	aux = str(i+1)
	vetor_teste_cidades.append(cv2.imread('images/teste/urbana' + aux + '.jpg'))
	vetor_teste_cidades_resized.append(cv2.resize(vetor_teste_cidades[i], (10,10)))
	vetor_nome.append("urbana" + aux)
vetor_teste_cidades_resized = np.array(vetor_teste_cidades_resized)

vetor_teste_oceano = []
vetor_teste_oceano_resized = []
for i in range (tam):
	aux = str(i+1)
	vetor_teste_oceano.append(cv2.imread('images/teste/oceano' + aux + '.jpg'))
	vetor_teste_oceano_resized.append(cv2.resize(vetor_teste_oceano[i], (10,10)))
	vetor_nome.append("oceano" + aux)
vetor_teste_oceano_resized = np.array(vetor_teste_oceano_resized)

vetor_teste_deserto = []
vetor_teste_deserto_resized = []
for i in range (tam):
	aux = str(i+1)
	vetor_teste_deserto.append(cv2.imread('images/teste/deserto' + aux + '.jpg'))
	vetor_teste_deserto_resized.append(cv2.resize(vetor_teste_deserto[i], (10,10)))
	vetor_nome.append("deserto" + aux)
vetor_teste_deserto_resized = np.array(vetor_teste_deserto_resized)

vetor_teste_polar = []
vetor_teste_polar_resized = []
for i in range (tam):
	aux = str(i+1)
	vetor_teste_polar.append(cv2.imread('images/teste/polar' + aux + '.jpg'))
	vetor_teste_polar_resized.append(cv2.resize(vetor_teste_polar[i], (10,10)))
	vetor_nome.append("polar" + aux)
vetor_teste_polar_resized = np.array(vetor_teste_polar_resized)

vetor_teste_rural = []
vetor_teste_rural_resized = []
for i in range (tam):
	aux = str(i+1)
	vetor_teste_rural.append(cv2.imread('images/teste/rural' + aux + '.jpg'))
	vetor_teste_rural_resized.append(cv2.resize(vetor_teste_rural[i], (10,10)))
	vetor_nome.append("rural" + aux)
vetor_teste_rural_resized = np.array(vetor_teste_rural_resized)

# ------------------------------------------------------

tam = 5
vetor_treino_praias = []
vetor_treino_praias_resized = []
for i in range (0,tam):
	aux = str(i+6)
	vetor_treino_praias.append(cv2.imread('images/treino/praia' + aux + '.jpg'))
	vetor_treino_praias_resized.append(cv2.resize(vetor_treino_praias[i], (10,10)))

vetor_treino_florestas = []
vetor_treino_florestas_resized = []
for i in range (0,tam):
	aux = str(i+6)
	vetor_treino_florestas.append(cv2.imread('images/treino/floresta' + aux + '.jpg'))
	vetor_treino_florestas_resized.append(cv2.resize(vetor_treino_florestas[i], (10,10)))

vetor_treino_cidades = []
vetor_treino_cidades_resized = []
for i in range (0,tam):
	aux = str(i+6)
	vetor_treino_cidades.append(cv2.imread('images/treino/urbana' + aux + '.jpg'))
	vetor_treino_cidades_resized.append(cv2.resize(vetor_treino_cidades[i], (10,10)))

vetor_treino_oceano = []
vetor_treino_oceano_resized = []
for i in range (0,tam):
	aux = str(i+6)
	vetor_treino_oceano.append(cv2.imread('images/treino/oceano' + aux + '.jpg'))
	vetor_treino_oceano_resized.append(cv2.resize(vetor_treino_oceano[i], (10,10)))

vetor_treino_deserto = []
vetor_treino_deserto_resized = []
for i in range (0,tam):
	aux = str(i+6)
	vetor_treino_deserto.append(cv2.imread('images/treino/deserto' + aux + '.jpg'))
	vetor_treino_deserto_resized.append(cv2.resize(vetor_treino_deserto[i], (10,10)))

vetor_treino_polar = []
vetor_treino_polar_resized = []
for i in range (0,tam):
	aux = str(i+6)
	vetor_treino_polar.append(cv2.imread('images/treino/polar' + aux + '.jpg'))
	vetor_treino_polar_resized.append(cv2.resize(vetor_treino_polar[i], (10,10)))

vetor_treino_rural = []
vetor_treino_rural_resized = []
for i in range (0,tam):
	aux = str(i+6)
	vetor_treino_rural.append(cv2.imread('images/treino/rural' + aux + '.jpg'))
	vetor_treino_rural_resized.append(cv2.resize(vetor_treino_rural[i], (10,10)))

# Resize images to 10px x 10px

'''
# Concat all arrays to one

'''

X = np.concatenate((vetor_treino_praias_resized, vetor_treino_cidades_resized, vetor_treino_florestas_resized, 

							vetor_treino_oceano_resized, vetor_treino_deserto_resized,

	 						vetor_treino_polar_resized, vetor_treino_rural_resized), axis=0)

# Create index to arrays
y = []
for i in range(7*tam):
	y.append(i+1)
#y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Set y as a array
y = np.array(y)

# Reshape y
Y = y.reshape(-1)

# Reshape X with length of y
X = X.reshape(len(y), -1)

# Create the classifier 
classifier_linear = SVC(kernel='linear')

print(40 * '-')
print('Started train of SVC model')

# Train the classifier with images and indexes
classifier_linear.fit(X,Y)

print('Finished train')
print(40 * '-')

# ---------------------------------------------------------

vetor_teste = np.concatenate((vetor_teste_praias_resized, vetor_teste_cidades_resized, vetor_teste_florestas_resized, 

							vetor_teste_oceano_resized, vetor_teste_deserto_resized,

	 						vetor_teste_polar_resized, vetor_teste_rural_resized), axis=0)

for i in range(len(vetor_teste)):
	print(vetor_nome[i] + " é " + getPrediction(classifier_linear.predict(vetor_teste[i].reshape(1,-1)), tam))
