Esta biblioteca manipula os pixels da imagem, ela trabalha com uma matriz tipo NumPy

Carregar biblioteca:
```
from matplotlib import image
from matplotlib import pyplot
```


Carregar pixels da imagem apartir da URL:
```
numpy = image.imread(url)
```
Exibir dados do NumPy:
```
texto = numpy.dtype
```
menor valor:
```
inteiro = numpy.min()
```
maior valor:
```
inteiro = numpy.max()
```

exibir em forma de imagem:
```
pyplot.imshow(numpy)
pyplot.show()
```

Converter objeto Image para NumPy:
```
from numpy import asarray:
numpy = asarray(imagem)
```

Converter NumPy para objeto Image
```
from PIL import Image:
imagem = Image.fromarray(numpy)
```
Mudar formato
```
numpy = pixels.astype('float32')
```