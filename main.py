import PySimpleGUIWeb as gui
import json as js
class pedido:
    def __init__(self):
        self.items = []
    def parte(self,alt,lar,con,quan):
        self.items.append({'alt':alt,'lar':lar,'con':con,'quan':quan})
    def ret(self,nome,tel,ender):
        doc = [F'Nome: {nome}\n Tel: {tel}\n Ender: {ender}','='*50]
        for c in range(len(self.items)):
            dt = self.items[c]
            doc.append(f'{c}) A {dt["alt"]} L {dt["lar"]} -> T {dt["con"]} Q {dt["quan"]}')
        return '\n'.join(doc)
class main():
    def __init__(self):
        layout = [
            [gui.Column([
                [gui.Text('Nome:')],
                [gui.Text('Tel:')],
                [gui.Text('ender:')]
            ]),gui.Column([
                    [gui.Input(key='nome')],
                    [gui.Input(key='tel')],
                    [gui.Input(key='ender')]
                ])],
            [gui.Button('enter')]
        ]
        win = gui.Window('Ambientt',layout)
        while True:
            eve,val = win.read()
            if eve == gui.WIN_CLOSED:
                break
main()