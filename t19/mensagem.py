from __future__ import annotations


class Objeto:
    def __init__(self) -> None:
        pass

    def mensagem(self, outro: Objeto) -> None:
        # Não está claro, no enunciado, a funcionalidade de mensagem,
        # entretanto, a nível de abstração, a implementação seria
        # colocada neste local com as operações a serem realizadas
        # em ambos objetos.
        #
        # Neste caso, a instancia de objeto que envia a mensagem
        # é aquela a partir da qual o método foi invocado,
        # e o receptor da mensagem é outra instância de Objeto,
        # passado por meio do parâmetro formal "outro",
        # presente na assinatura da função acima.
        pass
