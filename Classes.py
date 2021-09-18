# Definicao da classe Pondo2D
class Ponto2D:

    def __init__( self, x, y ):

        self.x = x
        self.y = y


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


    def __str__( self ):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

# Fim da definicao da classe Pondo2D
    






class Retangulo:
    #Adicione o seu codigo aqui
    pass


p1 = Ponto2D( 2.3, 4.3 )
print(p1)