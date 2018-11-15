import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.svm import SVR

# Read all images

'''
praia_g = cv2.imread('images/treino/praia/praia.jpg')
print(praia_g)
cidade_g = cv2.imread('images/treino/cidade/cidade.jpg')
floresta_g = cv2.imread('images/treino/floresta/floresta.jpg')
'''
test_praia_g = cv2.imread('images/teste/praia/praia.jpg')
test_cidade_g = cv2.imread('images/teste/cidade/cidade.jpg')
test_floresta_g = cv2.imread('images/teste/floresta/floresta.jpg')
test_floresta2_g = cv2.imread('images/teste/floresta/floresta2.jpg')
test_oceano_g = cv2.imread('images/teste/oceano/oceano1.jpg')
test_polar_g = cv2.imread('images/teste/polar/polar1.jpg')
test_rural_g = cv2.imread('images/teste/rural/rural1.jpg')
test_deserto_g = cv2.imread('images/teste/deserto/deserto1.jpg')


vetor_treino_praias = []
vetor_treino_praias_resized = []
for i in range (0,2):
	aux = str(i+1)
	vetor_treino_praias.append(cv2.imread('images/treino/praia' + aux + '.jpg'))
	vetor_treino_praias_resized.append(cv2.resize(vetor_treino_praias[i], (10,10)))

vetor_treino_florestas = []
vetor_treino_florestas_resized = []
for i in range (0,2):
	aux = str(i+1)
	vetor_treino_florestas.append(cv2.imread('images/treino/floresta' + aux + '.jpg'))
	vetor_treino_florestas_resized.append(cv2.resize(vetor_treino_florestas[i], (10,10)))

vetor_treino_cidades = []
vetor_treino_cidades_resized = []
for i in range (0,2):
	aux = str(i+1)
	vetor_treino_cidades.append(cv2.imread('images/treino/cidade' + aux + '.jpg'))
	vetor_treino_cidades_resized.append(cv2.resize(vetor_treino_cidades[i], (10,10)))

vetor_treino_oceano = []
vetor_treino_oceano_resized = []
for i in range (0,2):
	aux = str(i+1)
	vetor_treino_oceano.append(cv2.imread('images/treino/oceano' + aux + '.jpg'))
	vetor_treino_oceano_resized.append(cv2.resize(vetor_treino_oceano[i], (10,10)))

vetor_treino_deserto = []
vetor_treino_deserto_resized = []
for i in range (0,2):
	aux = str(i+1)
	vetor_treino_deserto.append(cv2.imread('images/treino/deserto' + aux + '.jpg'))
	vetor_treino_deserto_resized.append(cv2.resize(vetor_treino_deserto[i], (10,10)))

vetor_treino_polar = []
vetor_treino_polar_resized = []
for i in range (0,2):
	aux = str(i+1)
	vetor_treino_polar.append(cv2.imread('images/treino/polar' + aux + '.jpg'))
	vetor_treino_polar_resized.append(cv2.resize(vetor_treino_polar[i], (10,10)))

vetor_treino_rural = []
vetor_treino_rural_resized = []
for i in range (0,2):
	aux = str(i+1)
	vetor_treino_rural.append(cv2.imread('images/treino/rural' + aux + '.jpg'))
	vetor_treino_rural_resized.append(cv2.resize(vetor_treino_rural[i], (10,10)))


#cv2.imshow("vetor praia ", vetor_treino_praias[1])
#cv2.imshow("vetor floresta ", vetor_treino_florestas[1])
#cv2.imshow("vetor floresta ", vetor_treino_cidades[1])
#cv2.imshow("vetor floresta ", vetor_treino_deserto[1])
#cv2.imshow("vetor floresta ", vetor_treino_oceano[1])
#cv2.imshow("vetor floresta ", vetor_treino_polar[1])
#cv2.imshow("vetor floresta ", vetor_treino_rural[1])

# Resize images to 10px x 10px


'''
treino_praia = cv2.resize(praia_g, (10,10))
treino_cidade = cv2.resize(cidade_g, (10,10))
treino_floresta = cv2.resize(floresta_g, (10,10))
'''

test_praia = cv2.resize(test_praia_g, (10,10))	
test_floresta = cv2.resize(test_floresta_g, (10,10))
test_floresta2 = cv2.resize(test_floresta2_g, (10,10))
test_oceano = cv2.resize(test_oceano_g, (10,10))
test_polar = cv2.resize(test_polar_g, (10,10))
test_cidade = cv2.resize(test_cidade_g, (10,10))
test_rural = cv2.resize(test_rural_g, (10,10))
test_deserto = cv2.resize(test_deserto_g, (10,10))

'''
# Concat all arrays to one

'''

X = np.concatenate((vetor_treino_praias_resized, vetor_treino_cidades_resized, vetor_treino_florestas_resized, 

							vetor_treino_oceano_resized, vetor_treino_deserto_resized,

	 						vetor_treino_polar_resized, vetor_treino_rural_resized), axis=0)

# Create index to arrays
y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

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

# Predict the category of image 
prediction = classifier_linear.predict(test_rural.reshape(1,-1))

# Score of predict 
score = classifier_linear.score(X,Y)

# Show prediction
print('Result: {}'.format(prediction))

# Show prediction score
print('Score of precision: {:.1f}%'.format(score * 100))

# Set result as image of prediction
if prediction <=2 :
	print("é da classe praia")
elif prediction <=4:
	print("é da classe cidade")
elif prediction <= 6:
	print("é da classe floresta")
elif prediction <= 8:
	print("é da classe oceano")
elif prediction <= 10:
	print("é da classe deserto")
elif prediction <= 12:
	print("é da classe polar")
elif prediction <= 14:
	print("é da classe rural")

# Show image based on prediction
#cv2.imshow("Resultado do Algoritmo", result)
# Show the image tested
#cv2.imshow("Imagem passada no teste", test_floresta2_g)
# Wait for key
cv2.waitKey(0)

