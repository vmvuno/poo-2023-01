from __future__ import annotations


class Arquivo:
    def __init__(self) -> None:
        self._permissoes: list[Permissao] = []

    def adicionar_permissao(self, permissao: Permissao) -> None:
        self._permissoes.append(permissao)


class Usuario:
    def __init__(self) -> None:
        self._permissoes: list[Permissao] = []

    def adicionar_permissao(self, permissao: Permissao) -> None:
        self._permissoes.append(permissao)


class Permissao:
    def __init__(self,
                 arquivo: Arquivo,
                 usuario: Usuario,
                 leitura: bool,
                 escrita: bool,
                 execucao: bool) -> None:

        self.arquivo = arquivo
        self.usuario = usuario
        self.leitura = leitura
        self.escrita = escrita
        self.execucao = execucao

        arquivo.adicionar_permissao(self)
        usuario.adicionar_permissao(self)


class Disco:
    def __init__(self
                 # Parâmetros para inicialização dos arquivos
                 ) -> None:
        self.arquivos: list[Arquivo] = []

    # Numa implementação real, mais elaborada,
    # o construtor de disco receberia os parâmetros necessários
    # para inicializar os arquivos no disco,
    # caracterizando a relação de composição entre os dois.
    #
    # Uma vez que não foram fornecidas informações bastantes
    # para implementar a inicialização dos arquivos,
    # o método abaixo fornece a abstração necessária
    def adicionar_arquivo(self
                          # Parametros para inicialização dos arquivos
                          ) -> None:
        self.arquivos.append(
            Arquivo()  # Parâmetros de inicialização seriam repassados
                       # ao construtor da classe Arquivo.
                       # As instâncias de arquivos seriam inicializadas
                       # dentro da instância da classe Disco.
        )
