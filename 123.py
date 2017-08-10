import matplotlib.pyplot as plt
import numpy as np

ArrayY  = [ 120, 232, 200, 54 ]

tamanho_da_classe = 0.6     # isto e a largura da classe.
localizacao_das_labels=0.3  # isto e o sition onde devem estar as labels depois
                            # do inicio de cada classe.

# np.arange(4) = array([0, 1, 2, 3]) porque queres fazer quatro barras.
plt.bar(np.arange(4),ArrayY,tamanho_da_classe)
# agora estou a dar um nome a cada posicao do np.arange(4) com o ArrayX.
plt.xticks(np.arange(4)+localizacao_das_labels,('2000','2001','2002','2003'))
# Como os limites automaticos podem dar um mau efeito estou a inseri-los
# manualmente dizendo que quero o minimo do np.arange(4) e o maximo mais o 
# tamanho da classe com intervalo de visualizacao.
plt.xlim(np.arange(4).min(),np.arange(4).max()+tamanho_da_classe)
# Depois de ter editado tudo posso lancar o grafico.
plt.show()
