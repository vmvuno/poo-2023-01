class Luz:
    _CODIGOS_VALIDOS = {
        'L1': 'MALS (Sistema de luzes de aproximação '
              'de intensidade média, sem flash)',

        'L2': 'MALSF (Sistema de luzes para aproximação '
              'de intensidade média com flash)',

        'L2A': 'MALSR (Sistema de luzes para aproximação de intensidade '
               'média com luzes indicadoras de alinhamento de pista',

        'L3': 'ALS (Sistema de luzes de aproximação sem flash)',
        'L4': 'ALSF-1 (ALS Categoria I, com flash)',
        'L5': 'ALSF-2 (ALS Categoria II, com flash)',

        'L6': 'VASIS (Sistema indicador de rampa de aproximação visual) de '
              '2 barras e rampa de 3°. Quando diferente de 3°, o ângulo de '
              'rampa aparecerá entre parênteses, após a indicação L6',

        'L7': 'VASIS de 3 barras (duas rampas de aproximação). Os ângulos da '
              '1ª e 2ª rampas aparecerão entre parênteses, '
              'após a indicação L7',

        'L8': 'AVASIS (VASIS de duas barras com n° reduzido de caixas). '
              'Quando diferente de 3°, o ângulo de rampa aparecerá '
              'entre parênteses, após a indicação L8',

        'L9': 'PAPI (Sistema indicador de rampa de aproximação de precisão), '
              'com rampa normal de 3°. Quando diferente de 3°, o ângulo '
              'de rampa aparecerá entre parênteses, após a indicação L9',

        'L9A': 'APAPI (Sistema indicador de rampa de aproximação '
               'de precisão simplificada)',

        'L10': 'REIL (Luzes indicadoras de cabeceira de pista)',
        'L11': 'Luzes de zona de contato',
        'L11A': 'Luzes de zona de contato de alta intensidade',
        'L12': 'Luzes de cabeceira '
               '(verde no início e vermelha no fim da pista)',

        'L12A': 'Luzes de cabeceira de alta intensidade '
                '(verde no início e vermelha no fim da pista)',

        'L13': 'Luzes intermitentes de direção de pista',
        'L14': 'Luzes ao longo das laterais da pista, de 60 em 60 metros',

        'L14A': 'Luzes ao longo das laterais da pista de alta intensidade, '
                'de 60 em 60 metros',

        'L15': 'Luzes (azuis) de pista de táxi, indicando sua trajetória',
        'L16': 'Refletores na cabeceira da pista, indicando sua localização',

        'L17': 'Placas refletoras instaladas ao lado das luzes laterais '
               'e de fim-de-pista, que refletem a luz dos faróis de pouso',

        'L18': 'Balizamento de emergência (lampiões colocados '
               'ao longo das laterais da pista de 60 em 60 metros)',

        'L19': 'Luzes de eixo-de-pista',
        'L19A': 'Luzes de eixo de pista de alta intensidade',
        'L20': 'Luzes de eixo-de-pista-de-táxi para saída à grande velocidade',

        'L20A': 'Luzes de eixo-de-pista-de-táxi para saída '
                'à grande velocidade, de alta intensidade',

        'L21': 'Farol rotativo de aeródromo',
        'L22': 'Farol de identificação de aeródromo',
        'L23': 'Luzes de obstáculo',
        'L24': 'Farol de perigo',
        'L25': 'Luzes de contorno de área de aeródromo',
        'L26': 'Indicador de direção de vento iluminado',
        'L27': 'Luzes de Barra de Parada',
        'L30': 'Luzes de limite de área de pouso de helipontos',
        'L31': 'Sinal luminoso de identificação de heliponto',
        'L32': 'Faróis de heliponto',
        'L33': 'Luzes indicadoras de direção de aproximação de heliponto',
        'L34': 'Luzes indicadoras de área de toque quadradas de heliponto',
        'L35': 'Luzes indicadoras do ângulo de direção do heliponto'
        }

    def __init__(self,
                 codigo: str) -> None:

        if codigo.upper() not in self._CODIGOS_VALIDOS:
            raise ValueError('Código de iluminação inválido')

        self.codigo = codigo
        self.descricao = self._CODIGOS_VALIDOS[codigo]
