#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import random

"""
Gerador de CNPJ - Programa que gera n�meros v�lidos de CNPJ
Copyright (C) 2020 Compass 
Websites:
    https://8kun.top/slackware/
    https://github.com/compassnet
IRC Channels:
    #slackware@irc.rizon.net
    ##python@irc.rizon.net
    ##linux@irc.rizon.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""


class ReceitaFederal:
    """Classe que representa o CNPJ (Cadastro de Pessoa Jur�dica)."""

    def __init__(self):
        """Inicializar os atributos abaixo, caso presentes."""

    def instrucoes_gerais(self):
        """Instru��es gerais sobre o funcionamento do programa."""
        mensagem = (
                    "\nSeja bem vindo ao Gerador de CNPJ!"
                    "\nEste programa gera n�meros de CNPJ v�lidos."
                    "\nOs n�meros gerados s�o todos de uma matriz."
                    "\nOs n�meros gerados n�o necessariamente existem."
                    )
        print(mensagem)


class PessoaJuridica(ReceitaFederal):
    """Representar um CNPJ (Cadastro Nacional da Pessoa Jur�dica)."""
    
    def __init__(self):
        """Inicializar os atributos abaixo, caso presentes."""
        super().__init__()
        # Atributo self.sair para sair do programa.
        self.sair = None
        # Armazenar os oito primeiros n�meros aleat�rios de um CNPJ.
        self.cnpj_oito_numeros_aleatorios = None
        # Armazenar o primeiro d�gito verificador de um CNPJ.
        self.cnpj_primeiro_digito_verificador = None
        # Armazenar o segundo d�gito verificador de um CNPJ.
        self.cnpj_segundo_digito_verificador = None

    def gerar_oito_aleatorios(self):
        """Gerar os primeiros oito n�meros aleat�rios."""
        # Armazenar os oito primeiros n�meros aleat�rios do CNPJ.
        self.cnpj_oito_numeros_aleatorios = []
        # Criar um contador come�ando do 0.
        contador = 0
        # Criar um loop com o while, para gerar oito n�meros aleat�rios.
        while contador < 8:
            # Gerar um n�mero aleat�rio entre 0 e 9.
            numero_aleatorio = random.randint(0, 9)
            # Salvar cada n�mero aleat�rio em oito_n�meros_aleatorios.
            self.cnpj_oito_numeros_aleatorios.append(numero_aleatorio)
            # Aumentar o contador em uma unidade.
            contador += 1
        return self.cnpj_oito_numeros_aleatorios

    def gerar_primeiro_digito_verificador(self):
        """Gerar o primeiro d�gito verificador."""
        while True:
            """
            C�lculo do primeiro d�gito verificador. A regra utilizada
            pode ser encontrada aqui:
            https://www.geradorcnpj.com/algoritmo_do_cnpj.htm
            """
            digito_1 = self.cnpj_oito_numeros_aleatorios[0] * 5
            digito_2 = self.cnpj_oito_numeros_aleatorios[1] * 4
            digito_3 = self.cnpj_oito_numeros_aleatorios[2] * 3
            digito_4 = self.cnpj_oito_numeros_aleatorios[3] * 2
            digito_5 = self.cnpj_oito_numeros_aleatorios[4] * 9
            digito_6 = self.cnpj_oito_numeros_aleatorios[5] * 8
            digito_7 = self.cnpj_oito_numeros_aleatorios[6] * 7
            digito_8 = self.cnpj_oito_numeros_aleatorios[7] * 6
            digito_9 = 0 * 5
            digito_10 = 0 * 4
            digito_11 = 0 * 3
            digito_12 = 1 * 2
            soma = (digito_1 + digito_2 + digito_3 + digito_4 + digito_5
                    + digito_6 + digito_7 + digito_8 + digito_9 + digito_10
                    + digito_11 + digito_12)
            resto = soma % 11
            if resto < 2:
                self.cnpj_primeiro_digito_verificador = 0
            else:
                self.cnpj_primeiro_digito_verificador = 11 - resto
            return self.cnpj_primeiro_digito_verificador

    def gerar_segundo_digito_verificador(self):
        """Gerar o segundo d�gito verificador."""
        while True:
            """
            C�lculo do segundo d�gito verificador. A regra utilizada
            pode ser encontrada aqui:
            https://www.geradorcnpj.com/algoritmo_do_cnpj.htm
            """
            digito_1 = self.cnpj_oito_numeros_aleatorios[0] * 6
            digito_2 = self.cnpj_oito_numeros_aleatorios[1] * 5
            digito_3 = self.cnpj_oito_numeros_aleatorios[2] * 4
            digito_4 = self.cnpj_oito_numeros_aleatorios[3] * 3
            digito_5 = self.cnpj_oito_numeros_aleatorios[4] * 2
            digito_6 = self.cnpj_oito_numeros_aleatorios[5] * 9
            digito_7 = self.cnpj_oito_numeros_aleatorios[6] * 8
            digito_8 = self.cnpj_oito_numeros_aleatorios[7] * 7
            digito_9 = 0 * 6
            digito_10 = 0 * 5
            digito_11 = 0 * 4
            digito_12 = 1 * 3
            digito_13 = self.cnpj_primeiro_digito_verificador * 2
            soma = (digito_1 + digito_2 + digito_3 + digito_4 + digito_5
                    + digito_6 + digito_7 + digito_8 + digito_9 + digito_10
                    + digito_11 + digito_12 + digito_13)
            resto = soma % 11
            if resto < 2:
                self.cnpj_segundo_digito_verificador = 0
            else:
                self.cnpj_segundo_digito_verificador = 11 - resto
            return self.cnpj_segundo_digito_verificador

    def gerar_cnpj_formatado(self):
        """
        Gerar um CNPJ com duas formata��es
        para facilitar o copiar e colar.
        """
        while True:
            # Gerar um CNPJ sem formata��o.
            print("\nCNPJ gerado sem formata��o:")
            print(self.cnpj_oito_numeros_aleatorios[0], end = "")
            print(self.cnpj_oito_numeros_aleatorios[1], end = "")
            print(self.cnpj_oito_numeros_aleatorios[2], end = "")
            print(self.cnpj_oito_numeros_aleatorios[3], end = "")
            print(self.cnpj_oito_numeros_aleatorios[4], end = "")
            print(self.cnpj_oito_numeros_aleatorios[5], end = "")
            print(self.cnpj_oito_numeros_aleatorios[6], end = "")
            print(self.cnpj_oito_numeros_aleatorios[7], end = "")
            print(0, end = "")
            print(0, end = "")
            print(0, end = "")
            print(1, end = "")
            print(self.cnpj_primeiro_digito_verificador, end = "")
            print(self.cnpj_segundo_digito_verificador, end = "")
            print("\nCNPJ gerado com formata��o:")
            # Gerar um CNPJ com formata��o.
            print(self.cnpj_oito_numeros_aleatorios[0], end = "")
            print(self.cnpj_oito_numeros_aleatorios[1], end = ".")
            print(self.cnpj_oito_numeros_aleatorios[2], end = "")
            print(self.cnpj_oito_numeros_aleatorios[3], end = "")
            print(self.cnpj_oito_numeros_aleatorios[4], end = ".")
            print(self.cnpj_oito_numeros_aleatorios[5], end = "")
            print(self.cnpj_oito_numeros_aleatorios[6], end = "")
            print(self.cnpj_oito_numeros_aleatorios[7], end = "/")
            print(0, end = "")
            print(0, end = "")
            print(0, end = "")
            print(1, end = "-")
            print(self.cnpj_primeiro_digito_verificador, end = "")
            print(self.cnpj_segundo_digito_verificador, end = "\n")
            break

teste = PessoaJuridica()
teste.instrucoes_gerais()
teste.gerar_oito_aleatorios()
teste.gerar_primeiro_digito_verificador()
teste.gerar_segundo_digito_verificador()
teste.gerar_cnpj_formatado()
