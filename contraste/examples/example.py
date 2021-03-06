#
# This file is part of Contraste.
# Copyright (C) 2021 INPE.
#
# Contraste is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

##Instalação do pacote gdal como pré-requisito do pacote 
from osgeo import gdal

##instalação do pacote
pip install contraste-1.0.tar.gz

##importar a função de contrastre raiz quadrada do pacote
#outras funções disponíveis: QUADRATICO,  MINMAX, LINEAR, NEGATIVO e EQUALIZACAO
from contraste.RaizQuadrada import RAIZQUADRADA

##Chamada da função
RAIZQUADRADA()
# A função listará os arquivos .tif do diretório raiz. Selecionar a imagem (Landsat 8) de acordo com a numeração.
# O contraste será aplicado na imagem selecionada

####importar a função de contrastre por classe
from contraste.PorClasse import PORCLASSE

##Chamada da função
PORCLASSE()
# A função listará os arquivos .tif do diretório raiz. Selecionar a imagem (Landsat 8) de acordo com a numeração e, posteriormente, a imagem classificada (Mapbiomas).
# Escolha se o contraste será otimizado (1) ou personalizado (2)
