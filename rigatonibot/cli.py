import click
from pathlib import Path
import requests

@click.command()
@click.argument('filename', type=click.Path(exists=True, readable=True), nargs=1)
def main(filename):
    path = Path(filename).as_posix()

    with open(path, 'r') as file:
        data = file.read()
        web_address = requests.post('http://paste.rs', data=data)

    print(web_address.text)

if __name__ == '__main__':
    main()


# Ta esse eh o unico arquivo que soh eu tenho por enquanto:
"""
Ideias:
1- fazer primeiro via cli, 
    python rigatoni.py <arquivo>.py --> nao precisa ser py, mas acho que comece assim
                                    --> a nao ser que converter pra txt sempre funcione
        a) devolve o link criado no paste
        b) abre direto no navegador o negocio criado

2- depois dar um jeito de fazer isso virar uma ferramenta sh
    rigatoni <arquivo>.py

3- depois (ou antes) ja fazer um bot de telegrao
    (eh bom pq dai a galera nao tem que instalar essa pomba no pc)

4- oferecer outras ferramentas de paste
    rigatoni <arquivo>  {paste, gist}
                (ei, nao precisa ser .py!)
"""