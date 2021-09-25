# Definicao da classe Pondo2D
class Ponto2D:

    # Inicializador da classe Ponto 2D
    def __init__( self, x=0.0, y=0.0 ):

        self.__x = x
        self.__y = y


    # get x
    @property
    def x( self ):
        return self.__x

    # get y
    @property
    def y( self ):
        return self.__y


    # set x
    @x.setter        
    def x( self, x ):
        self.__x = x

    # set y
    @y.setter        
    def y( self, y ):
        self.__y = y      

     
    # Retorna a representação em string do Ponto2D
    def __str__( self ):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"

# Fim da definicao da classe Pondo2D
    



# Definicao da classe Retangulo
class Retangulo:
    
    # Inicializador da classe Retangulo
    def __init__(self, esq_sup, dir_inf):
        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf


    # get esq_sup
    @property
    def esq_sup( self ):
        return self.__esq_sup

    # get dir_inf
    @property
    def dir_inf( self ):
        return self.__dir_inf    


    # set esq_sup
    @esq_sup.setter
    def esq_sup( self, esq_sup ):
        self.__esq_sup = esq_sup

    # set dir_inf
    @dir_inf.setter
    def dir_inf( self, dir_inf ):
        self.__dir_inf = dir_inf     


    # get width
    @property
    def width( self ):
        return self.dir_inf.x - self.esq_sup.x

    # get height
    @property
    def height( self ):
        return self.esq_sup.y - self.dir_inf.y        


    # Calcula a área desse retângulo
    def calcularArea( self ):
        return ( (self.__dir_inf.x - self.__esq_sup.x) *
                 (self.__esq_sup.y - self.__dir_inf.y) )


    # Determina se há interseção entre esse retângulo e o retângulo
    # passado como parâmetro. Se não tiver, retorna None. Se tiver,
    # retorna a área da interseção dos 2 retângulos.
    def calcularIntersecao( self, ret ):

        x1_esq = self.esq_sup.x
        x1_dir = self.dir_inf.x
        y1_inf = self.dir_inf.y
        y1_sup = self.esq_sup.y

        x2_esq = ret.esq_sup.x
        x2_dir = ret.dir_inf.x
        y2_inf = ret.dir_inf.y
        y2_sup = ret.esq_sup.y


        if( x2_esq >= x1_dir  or
            x1_esq >= x2_dir  or
            y2_inf >= y1_sup  or
            y1_inf >= y2_sup ):

            return None

        else:

            abscissas = [ x1_esq, x1_dir, x2_esq, x2_dir ]
            ordenadas = [ y1_inf, y1_sup, y2_inf, y2_sup ]
            abscissas.sort()
            ordenadas.sort()

            return ( abscissas[2]-abscissas[1] ) * ( ordenadas[2]-ordenadas[1] )
        
# Fim da definicao da classe Retangulo


