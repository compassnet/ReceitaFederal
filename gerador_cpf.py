#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import random

"""
Gerador de CPF - Programa que gera números válidos de CPF
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
    """Classe que representa o CPF (Cadastro de Pessoa Física)."""

    def __init__(self):
        """Inicializar os atributos abaixo, caso presentes."""

    def instrucoes_gerais(self):
        """Instruções gerais sobre o funcionamento do programa."""
        mensagem = (
                    "\nSeja bem vindo ao Gerador de CPF!"
                    "\nEste programa gera números de CPF válidos."
                    "\nOs números gerados não necessariamente existem."
                    "\nPara sair a qualquer momento, digite 's'."
                    )
        print(mensagem)


class PessoaFisica(ReceitaFederal):
    """Representar um CPF (Cadastro de Pessoa Física)."""
    
    def __init__(self):
        """Inicializar os atributos abaixo, caso presentes."""
        super().__init__()
        # Atributo self.sair para sair do programa.
        self.sair = None
        # Armazenar a região fiscal.
        self.regiao_fiscal = None
        # Armazenar os oito primeiros números aleatórios de um CPF.
        self.cpf_oito_numeros_aleatorios = None
        # Armazenar o primeiro dígito verificador de um CPF.
        self.cpf_primeiro_digito_verificador = None
        # Armazenar o segundo dígito verificador de um CPF.
        self.cpf_segundo_digito_verificador = None

    def gerar_oito_aleatorios(self):
        """Gerar os primeiros oito números aleatórios."""
        # Armazenar os oito primeiros números aleatórios do CPF.
        self.cpf_oito_numeros_aleatorios = []
        # Criar um contador começando do 0.
        contador = 0
        # Criar um loop com o while, para gerar oito números aleatórios.
        while contador < 8:
            # Gerar um número aleatório entre 0 e 9.
            numero_aleatorio = random.randint(0, 9)
            # Salvar cada número aleatório em oito_números_aleatorios.
            self.cpf_oito_numeros_aleatorios.append(numero_aleatorio)
            # Aumentar o contador em uma unidade.
            contador += 1
        return self.cpf_oito_numeros_aleatorios

    def gerar_regiao_fiscal(self):
        """Utilizar a região fiscal desejada pelo usuário."""
        # Perguntar para o usuário qual a região fiscal desejada.
        mensagem = (
                    "\nDigite a região fiscal desejada."
                    "\nSe desejar uma região fiscal aleatória, digite '0'."
                    "\n\n0ª Região: Região Fiscal aleatória;"
                    "\n1ª Região: DF, GO, MT, MS e TO;"
                    "\n2ª Região: AC, AM, AP, PA, RO e RR;"
                    "\n3ª Região: CE, MA e PI;"
                    "\n4ª Região: AL, PB, PE e RN;"
                    "\n5ª Região: BA e SE;"
                    "\n6ª Região: MG;"
                    "\n7ª Região: ES e RJ;"
                    "\n8ª Região: SP;"
                    "\n9ª Região: PR e SC;"
                    "\n10ª Região: RS."
                    "\n\nDigite o número da região fiscal desejada (0 a 10): "
                    )

        """
        Restringir self.regiao_fiscal a um número inteiro entre 0 e 10.
        Também é possível reescrever o código, não utilizando o try e
        usando strings ao invés de números inteiros como anteriormente
        em instrucoes_gerais().
        Para efeito de aprendizagem, resolvi deixar como abaixo.
        """
        while True:
            try:
                self.regiao_fiscal = input(mensagem)
                """
                Lista de compreensão para gerar os números sequenciais
                de 1 a 10 (números das regiões fiscais).
                """
                numero_valido = [numero for numero in range(1, 10)]
                """
                Verificar se região_fiscal e um número valido, caso
                contrário solicitar novamente.
                """
                if self.regiao_fiscal == '0':
                    """
                    A região fiscal 0 faz com que self.regiao_fiscal
                    assuma um valor aleatório entre 1 e 9. 0 é
                    reservado para a região fiscal 10 logo abaixo.
                    """
                    self.regiao_fiscal = random.randint(1, 9)
                    return self.regiao_fiscal
                    break
                if self.regiao_fiscal == '10':
                    # A região fiscal 10 assume o valor 0.
                    self.regiao_fiscal = 0
                    return self.regiao_fiscal
                elif self.regiao_fiscal in str(numero_valido):
                    print(f"\nVocê selecionou a {self.regiao_fiscal}ª Região "
                        "Fiscal.")
                    return self.regiao_fiscal
                    break
                elif self.regiao_fiscal == 's':
                    print("Saindo do programa...")
                    exit()
                else:
                    continue
            except ValueError:
                continue
        
    def gerar_primeiro_digito_verificador(self):
        """Gerar o primeiro dígito verificador."""
        while True:
            """
            Cálculo do primeiro dígito verificador. A regra utilizada
            pode ser encontrada aqui:
            https://www.somatematica.com.br/faq/cpf.php
            """
            digito_1 = self.cpf_oito_numeros_aleatorios[0] * 10
            digito_2 = self.cpf_oito_numeros_aleatorios[1] * 9
            digito_3 = self.cpf_oito_numeros_aleatorios[2] * 8
            digito_4 = self.cpf_oito_numeros_aleatorios[3] * 7
            digito_5 = self.cpf_oito_numeros_aleatorios[4] * 6
            digito_6 = self.cpf_oito_numeros_aleatorios[5] * 5
            digito_7 = self.cpf_oito_numeros_aleatorios[6] * 4
            digito_8 = self.cpf_oito_numeros_aleatorios[7] * 3
            digito_9 = int(self.regiao_fiscal) * 2
            soma = (digito_1 + digito_2 + digito_3 + digito_4 + digito_5
                    + digito_6 + digito_7 + digito_8 + digito_9)
            resto = soma % 11
            if resto == 0 or resto == 1:
                self.cpf_primeiro_digito_verificador = 0
            else:
                self.cpf_primeiro_digito_verificador = 11 - resto
            return self.cpf_primeiro_digito_verificador

    def gerar_segundo_digito_verificador(self):
        """Gerar o segundo dígito verificador."""
        while True:
            """
            Cálculo do segundo dígito verificador. A regra utilizada
            pode ser encontrada aqui:
            https://www.somatematica.com.br/faq/cpf.php
            """
            digito_1 = self.cpf_oito_numeros_aleatorios[0] * 11
            digito_2 = self.cpf_oito_numeros_aleatorios[1] * 10
            digito_3 = self.cpf_oito_numeros_aleatorios[2] * 9
            digito_4 = self.cpf_oito_numeros_aleatorios[3] * 8
            digito_5 = self.cpf_oito_numeros_aleatorios[4] * 7
            digito_6 = self.cpf_oito_numeros_aleatorios[5] * 6
            digito_7 = self.cpf_oito_numeros_aleatorios[6] * 5
            digito_8 = self.cpf_oito_numeros_aleatorios[7] * 4
            digito_9 = int(self.regiao_fiscal) * 3
            digito_10 = self.cpf_primeiro_digito_verificador * 2
            soma = (digito_1 + digito_2 + digito_3 + digito_4 + digito_5
                    + digito_6 + digito_7 + digito_8 + digito_9 + digito_10)
            resto = soma % 11
            if resto == 0 or resto == 1:
                self.cpf_segundo_digito_verificador = 0
            else:
                self.cpf_segundo_digito_verificador = 11 - resto
            return self.cpf_segundo_digito_verificador

    def gerar_cpf_formatado(self):
        """
        Gerar um CPF com duas formatações para
        facilitar o copiar e colar.
        """
        while True:
            # Gerar um CPF sem formatação.
            print("\nCPF gerado sem formatação:")
            print(self.cpf_oito_numeros_aleatorios[0], end = "")
            print(self.cpf_oito_numeros_aleatorios[1], end = "")
            print(self.cpf_oito_numeros_aleatorios[2], end = "")
            print(self.cpf_oito_numeros_aleatorios[3], end = "")
            print(self.cpf_oito_numeros_aleatorios[4], end = "")
            print(self.cpf_oito_numeros_aleatorios[5], end = "")
            print(self.cpf_oito_numeros_aleatorios[6], end = "")
            print(self.cpf_oito_numeros_aleatorios[7], end = "")
            print(self.regiao_fiscal, end = "")
            print(self.cpf_primeiro_digito_verificador, end = "")
            print(self.cpf_segundo_digito_verificador, end = "")
            print("\nCPF gerado com formatação:")
            # Gerar um CPF com formatação.
            print(self.cpf_oito_numeros_aleatorios[0], end = "")
            print(self.cpf_oito_numeros_aleatorios[1], end = "")
            print(self.cpf_oito_numeros_aleatorios[2], end = ".")
            print(self.cpf_oito_numeros_aleatorios[3], end = "")
            print(self.cpf_oito_numeros_aleatorios[4], end = "")
            print(self.cpf_oito_numeros_aleatorios[5], end = ".")
            print(self.cpf_oito_numeros_aleatorios[6], end = "")
            print(self.cpf_oito_numeros_aleatorios[7], end = "")
            print(self.regiao_fiscal, end = "-")
            print(self.cpf_primeiro_digito_verificador, end = "")
            print(self.cpf_segundo_digito_verificador, end = "\n")
            break


teste = PessoaFisica()
teste.instrucoes_gerais()
teste.gerar_oito_aleatorios()
teste.gerar_regiao_fiscal()
teste.gerar_primeiro_digito_verificador()
teste.gerar_segundo_digito_verificador()
teste.gerar_cpf_formatado()
