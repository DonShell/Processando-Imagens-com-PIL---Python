Importar biblioteca:
```
from PIL import Image
```

Carregar imagem apartir de uma url:
```
imagem = Image.open(url)
```

Ver informações:
```
#formato
string = imagem.format

#modo
Ver modo
string = imagem.mode

#tamanho
string = imagem.size
```


Converter de Image para NumPy:
```
from numpy import asarray
numpy = asarray(imagem)
```
Realiza-se esta conversão para transformar a imagem em uma matriz de pixels e cores


Converter NumPy para objeto Image:
```
imagem = Image.fromarray(numpy)
```




Salvando arquivo:
```
imagem.save("NovaImagem.png",format="PNG")
```

Mudando o tamanho da imagem:
```
imagem.tumbinail((100,100))
```
mantem a dimenção para não distorcer ex:
```
imagem.size == (150,300)
imagem.tumbinail((100,100))
imagem.size == (50,100)
```

Distorcer para deixar do tamanho exato descrito:
```
imagem.resize((100,100))
```

Espelhar a imagem:
```
#horizontal
imagem.transpose(Image.FLIP_LEFT_RIGHT)

#vertical
imagem.transpose(Image.FLIP_TOP_BOTTOM)
```


Rotacionar:
```
#o valor é passado em graus
imagem.rotate(45)
```

Cortar imagem coordenadas 
```
#os valores passados são inteiros representando a coordenada em pixels
imagem.crop(direita,cima,esquerda,baixo)
```

Capturar pixel
```
#criar objeto x,y
xy = (-1,-1)

#captura o pixel
pixel = imagem.getpixel(xy)

#exibe os valores de cores do pixel
print(pixel[0],pixel[1],pixel[2])
```



Transformar em Preto e Branco:
```
imagemPretoEBranco = imagem.convert(mode="L")
```


Tipos de filtros:
```
BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, e SHARPEN.
```

Aplicando filtros a imagem
```
from PIL import ImageFilter
im = i.filter(ImageFilter.EMBOSS)
```


Desenhar na imagem
```
from PIL import ImageDraw

desenho = ImageDraw.Draw(imagem)

#.line( linha , cor )
#.line((local_partida,Local_fim), fill= (RGB) ou (escala de cinza))
#.line((x,y)+(x,y),fill=( 0~255 , 0~255 , 0~255 ) ou fill=(0~255))
desenho.line((0, 0) + img.size, fill=(255, 255, 255))
desenho.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
desenho.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))

#agora a variavel imagem possui desenhos em cima da imagem original

```
