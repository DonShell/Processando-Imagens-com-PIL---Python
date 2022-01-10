from PIL import Image, ImageFilter, ImageDraw
#converter  para exibir imagem
from numpy import asarray
from matplotlib import image, pyplot



url = "cidade1.jpeg"

imagem = Image.open(url)

#xy = (-1,-1)

#pixel = imagem.getpixel(xy)

#print(pixel[0],pixel[1],pixel[2])



def aplicarFiltroESalvar(img,filtro):
	imagemNova = img.filter(getattr(ImageFilter,filtro))
	imagemNova = imagemNova.resize((400,400))
	imagemNova.save("imagens-Com-Filtros/NovaImagem-"+filtro+".png",format="PNG")

def aplicarTodosOsFiltrosESalvar(img):
	filtros = ("BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SMOOTH", "SMOOTH_MORE", "SHARPEN")
	for i in range(len(filtros)):
		aplicarFiltroESalvar(img,filtros[i])

def RiscandoAImagem(img):
	desenho = ImageDraw.Draw(img)
	#.line((x,y)+(x,y),fill=( R , G , B ))
	desenho.line((0, 0) + img.size, fill=(255, 255, 255))
	return img


def ExibirObjetoImagem(img):
	dados = asarray(img)
	pyplot.imshow(dados)
	pyplot.show()


aplicarTodosOsFiltrosESalvar(imagem)

ExibirObjetoImagem(RiscandoAImagem(imagem))

