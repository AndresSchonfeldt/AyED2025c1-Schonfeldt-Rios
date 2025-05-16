class Carta:
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self.visible = False

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, palo):
        self._palo = palo

    def _valor_numerico(self):
        valores = ['J', 'Q', 'K', 'A']
        if self.valor in valores:
            idx = valores.index(self.valor)
            return 11 + idx
        return int(self.valor)

    def __gt__(self, otra):
        return self._valor_numerico() > otra._valor_numerico()

    def __str__(self):
        if not self.visible:
            return "-X"
        else:
            return self.valor + self.palo

    def __repr__(self):
        return str(self)
