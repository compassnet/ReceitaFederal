#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import random

"""
Gerador de CPF/CNPJ - Programa que gera números válidos de CPF/CNPJ
Copyright (C) 2020 Compass 
Website:
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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

class CadastroReceitaFederal:
    """Classe que representa o CPF (Cadastro de Pessoa Física) e o CNPJ (Cadastro de Pessoa Jurídica)."""

    def __init__(self):
        """Inicializar os atributos abaixo, caso presentes."""
        # Atributo self.opcao para armazenar a escolha do usuário (CPF, CNPJ ou sair do programa).
        #self.opcao = None

    def instrucoes_gerais(self):
        """Instruções gerais sobre o funcionamento do programa."""
        mensagem = "\nSeja bem vindo ao Gerador de CPF!"
        mensagem = "\nSeja bem vindo ao Gerador de CPF/CNPJ!"
        mensagem += "\nEste programa possui dois módulos: CPF e CNPJ."
        mensagem += "\nPara gerar um CPF, digite '1'."
        mensagem += "\nPara gerar um CNPJ, digite '2'."
        mensagem += "\nPara sair, digite 's'."
        mensagem += "\nDigite a sua opção ('1', '2' ou 's'): "
        self.opcao = input(mensagem)
        return self.opcao

#    def opcoes_programa(self):
#        """Escolha do módulo ou sair do programa."""
#        # Lista contendo as opções válidas, inclusive o s maiúsculo caso o usuário o digite.
#        mensagens_validas = ['1', '2', 's', 'S']
#        # Loop mostrando o módulo escolhido. Opções inválidas não são aceitas.
#        while True:
#            if self.opcao in mensagens_validas:
#                if self.opcao == '1':
#                    print(f"Você escolheu o módulo CPF!")
#                    break
#                elif self.opcao == '2':
#                    print(f"Você escolheu o módulo CNPJ!")
#                    break
#                elif self.opcao == 's' or self.opcao == 'S':
#                    print("Saindo do programa!")
#                    break

class PessoaFisica(CadastroReceitaFederal):
    """Representar um CPF (Cadastro de Pessoa Física)."""
    
    def __init__(self):
        """Inicializar os atributos abaixo, caso presentes."""
        super().__init__()
        # Atributo self.opcao para armazenar a escolha do usuário (CPF, CNPJ ou sair do programa).
        self.opcao = None
        # Atributo self.regiao_fiscal para armazenar a região fiscal escolhida pelo usuário.
        self.regiao_fiscal = None
        # Atributo self.cpf_oito_numeros_aleatorios para armazenar os oito primeiros números aleatórios de um CPF.
        self.cpf_oito_numeros_aleatorios = None
        # Atributo self.cpf_primeiro_digito_verificador para armazenar o primeiro dígito verificador de um CPF.
        self.cpf_primeiro_digito_verificador = None
        # Atributo self.cpf_segundo_digito_verificador para armazenar o segundo dígito verificador de um CPF.
        self.cpf_segundo_digito_verificador = None

    def gerar_oito_aleatorios(self):
        """Gerar os primeiros oito números aleatórios."""
        # Criar uma lista vazia para armazenar os oito primeiros números aleatórios do CPF.
        self.cpf_oito_numeros_aleatorios = []
        # Criar um contador comecando do 0.
        contador = 0
        # Criar um loop com o while, para gerar oito números aleatórios.
        while contador < 8:
            # Gerar um número aleatório entre 0 e 9.
            numero_aleatorio = random.randint(0, 9)
            # Salvar cada número aleatório criado em oito_números_aleatorios.
            self.cpf_oito_numeros_aleatorios.append(numero_aleatorio)
            # Aumentar o contador em uma unidade.
            contador += 1
        return self.cpf_oito_numeros_aleatorios

    def gerar_regiao_fiscal(self):
        """Utilizar a região fiscal desejada pelo usuário."""
        # Perguntar para o usuário qual a região fiscal desejada.
        mensagem = "\nPara escolher um número de CPF regional, digite a região fiscal desejada."
        mensagem += "\nSe desejar uma região fiscal aleatória, digite '0'."
        mensagem += "\n\n0ª Região: Região Fiscal aleatória;"
        mensagem += "\n1ª Região: DF, GO, MT, MS e TO;"
        mensagem += "\n2ª Região: AC, AM, AP, PA, RO e RR;"
        mensagem += "\n3ª Região: CE, MA e PI;"
        mensagem += "\n4ª Região: AL, PB, PE e RN;"
        mensagem += "\n5ª Região: BA e SE;"
        mensagem += "\n6ª Região: MG;"
        mensagem += "\n7ª Região: ES e RJ;"
        mensagem += "\n8ª Região: SP;"
        mensagem += "\n9ª Região: PR e SC;"
        mensagem += "\n10ª Região: RS."
        mensagem += "\n\nDigite o número da região fiscal desejada (somente números de 0 a 10): "

        """
        Restringir self.regiao_fiscal a um número inteiro entre 0 e 10.
        Também é possível reescrever o código, não utilizando o try e usando strings ao invés de números inteiros como anteriormente em instrucoes_gerais().
        Para efeito de aprendizagem, resolvi deixar como abaixo.
        """
        while True:
            # Sair do programa caso o usuário digite 's' (ou 'S' por engano).
            #if self.opcao == '2' or self.opcao == 's' or self.opcao == 'S':
            #    break
            try:
                self.regiao_fiscal = int(input(mensagem))
                # Lista de compreensão para gerar os números sequenciais de 1 a 10 (números das regiões fiscais).
                numero_valido = [numero for numero in range(1, 10)]
                # Verificar se região_fiscal e um número valido, caso contrário solicitar novamente.
                if self.regiao_fiscal == 0:
                    # A região fiscal 0 faz com que self.regiao_fiscal assuma um valor aleatório entre 1 e 9. 0 é reservado para a região fiscal 10 logo abaixo.
                    self.regiao_fiscal = random.randint(1, 9)
                    return self.regiao_fiscal
                    break
                if self.regiao_fiscal == 10:
                    # A região fiscal 10 assume o valor 0.
                    self.regiao_fiscal = 0
                    return self.regiao_fiscal
                elif self.regiao_fiscal in numero_valido:
                    print(f"\nVocê selecionou a {self.regiao_fiscal}ª Região Fiscal.")
                    return self.regiao_fiscal
                    break
                else:
                    continue
            except ValueError:
                continue
        
    def gerar_primeiro_digito_verificador(self):
        """Gerar o primeiro dígito verificador."""
        while True:
            # Sair do programa caso o usuário digite 's' (ou 'S' por engano).
            #if self.opcao == '2' or self.opcao == 's' or self.opcao == 'S':
            #    break
            # Cálculo do primeiro dígito verificador. A regra utilizada pode ser encontrada aqui: https://www.somatematica.com.br/faq/cpf.php
            digito_1 = self.cpf_oito_numeros_aleatorios[0] * 10
            digito_2 = self.cpf_oito_numeros_aleatorios[1] * 9
            digito_3 = self.cpf_oito_numeros_aleatorios[2] * 8
            digito_4 = self.cpf_oito_numeros_aleatorios[3] * 7
            digito_5 = self.cpf_oito_numeros_aleatorios[4] * 6
            digito_6 = self.cpf_oito_numeros_aleatorios[5] * 5
            digito_7 = self.cpf_oito_numeros_aleatorios[6] * 4
            digito_8 = self.cpf_oito_numeros_aleatorios[7] * 3
            digito_9 = self.regiao_fiscal * 2
            soma = digito_1 + digito_2 + digito_3 + digito_4 + digito_5 + digito_6 + digito_7 + digito_8 + digito_9
            resto = soma % 11
            if resto == 0 or resto == 1:
                self.cpf_primeiro_digito_verificador = 0
            else:
                self.cpf_primeiro_digito_verificador = 11 - resto
            return self.cpf_primeiro_digito_verificador

    def gerar_segundo_digito_verificador(self):
        """Gerar o segundo dígito verificador."""
        while True:
            # Sair do programa caso o usuário digite 's' (ou 'S' por engano).
            #if self.opcao == '2' or self.opcao == 's' or self.opcao == 'S':
            #    break
            # Cálculo do segundo dígito verificador. A regra utilizada pode ser encontrada aqui: https://www.somatematica.com.br/faq/cpf.php
            digito_1 = self.cpf_oito_numeros_aleatorios[0] * 11
            digito_2 = self.cpf_oito_numeros_aleatorios[1] * 10
            digito_3 = self.cpf_oito_numeros_aleatorios[2] * 9
            digito_4 = self.cpf_oito_numeros_aleatorios[3] * 8
            digito_5 = self.cpf_oito_numeros_aleatorios[4] * 7
            digito_6 = self.cpf_oito_numeros_aleatorios[5] * 6
            digito_7 = self.cpf_oito_numeros_aleatorios[6] * 5
            digito_8 = self.cpf_oito_numeros_aleatorios[7] * 4
            digito_9 = self.regiao_fiscal * 3
            digito_10 = self.cpf_primeiro_digito_verificador * 2
            soma = digito_1 + digito_2 + digito_3 + digito_4 + digito_5 + digito_6 + digito_7 + digito_8 + digito_9 + digito_10
            resto = soma % 11
            if resto == 0 or resto == 1:
                self.cpf_segundo_digito_verificador = 0
            else:
                self.cpf_segundo_digito_verificador = 11 - resto
            return self.cpf_segundo_digito_verificador

    def gerar_cpf_formatado(self):
        """Gerar um CPF com duas formatações (para facilitar o copiar e colar)."""
        while True:
            # Sair do programa caso o usuário digite 's' (ou 'S' por engano).
            #if self.opcao == '2' or self.opcao == 's' or self.opcao == 'S':
            #    break
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

class PessoaJuridica(CadastroReceitaFederal):
    """Representar um CNPJ (Cadastro Nacional da Pessoa Jurídica)."""
    
    def __init__(self):
        """Inicializar os atributos abaixo, caso presentes."""
        super().__init__()
        # Atributo self.cnpj_oito_numeros_aleatorios para armazenar os oito primeiros números aleatórios de um CNPJ.
        self.cnpj_oito_numeros_aleatorios = None
        # Atributo self.cnpj_primeiro_digito_verificador para armazenar o primeiro dígito verificador de um CNPJ.
        self.cnpj_primeiro_digito_verificador = None
        # Atributo self.cnpj_segundo_digito_verificador para armazenar o segundo dígito verificador de um CNPJ.
        self.cnpj_segundo_digito_verificador = None

    def gerar_oito_aleatorios(self):
        """Gerar os primeiros oito números aleatórios."""
        # Criar uma lista vazia para armazenar os oito primeiros números aleatórios do CNPJ.
        self.cnpj_oito_numeros_aleatorios = []
        # Criar um contador comecando do 0.
        contador = 0
        # Criar um loop com o while, para gerar oito números aleatórios.
        while contador < 8:
            # Gerar um número aleatório entre 0 e 9.
            numero_aleatorio = random.randint(0, 9)
            # Salvar cada número aleatório criado em oito_números_aleatorios.
            self.cnpj_oito_numeros_aleatorios.append(numero_aleatorio)
            # Aumentar o contador em uma unidade.
            contador += 1
        return self.cnpj_oito_numeros_aleatorios

    def gerar_primeiro_digito_verificador(self):
        """Gerar o primeiro dígito verificador."""
        while True:
            # Sair do programa caso o usuário digite 's' (ou 'S' por engano).
            #if self.opcao == '1' or self.opcao == 's' or self.opcao == 'S':
            #    break
            #elif self.opcao == '2':
            #    continue
            # Cálculo do primeiro dígito verificador. A regra utilizada pode ser encontrada aqui: https://www.geradorcnpj.com/algoritmo_do_cnpj.htm
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
            soma = digito_1 + digito_2 + digito_3 + digito_4 + digito_5 + digito_6 + digito_7 + digito_8 + digito_9 + digito_10 + digito_11 + digito_12
            resto = soma % 11
            if resto < 2:
                self.cnpj_primeiro_digito_verificador = 0
            else:
                self.cnpj_primeiro_digito_verificador = 11 - resto
            return self.cnpj_primeiro_digito_verificador

    def gerar_segundo_digito_verificador(self):
        """Gerar o segundo dígito verificador."""
        while True:
            # Sair do programa caso o usuário digite 's' (ou 'S' por engano).
            #if self.opcao == '1' or self.opcao == 's' or self.opcao == 'S':
            #    break
            #elif self.opcao == '2':
            #    continue
            # Cálculo do segundo dígito verificador. A regra utilizada pode ser encontrada aqui: https://www.geradorcnpj.com/algoritmo_do_cnpj.htm
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
            soma = digito_1 + digito_2 + digito_3 + digito_4 + digito_5 + digito_6 + digito_7 + digito_8 + digito_9 + digito_10 + digito_11 + digito_12 + digito_13
            resto = soma % 11
            if resto < 2:
                self.cnpj_segundo_digito_verificador = 0
            else:
                self.cnpj_segundo_digito_verificador = 11 - resto
            return self.cnpj_segundo_digito_verificador

    def gerar_cnpj_formatado(self):
        """Gerar um CNPJ com duas formatações (para facilitar o copiar e colar)."""
        while True:
            # Sair do programa caso o usuário digite 's' (ou 'S' por engano).
            #if self.opcao == '1' or self.opcao == 's' or self.opcao == 'S':
            #    break
            #elif self.opcao == '2':
            #    continue
            # Gerar um CNPJ sem formatação.
            print("\nCNPJ gerado sem formatação:")
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
            print("\nCNPJ gerado com formatação:")
            # Gerar um CNPJ com formatação.
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

teste_cpf = PessoaFisica()
#teste_cnpj = PessoaJuridica()

teste_cpf.instrucoes_gerais()
while True:

    if teste_cpf.instrucoes_gerais() == '1':
        print(f"Você escolheu o módulo CPF!")
        teste_cpf.gerar_oito_aleatorios()
        teste_cpf.gerar_regiao_fiscal()
        teste_cpf.gerar_primeiro_digito_verificador()
        teste_cpf.gerar_segundo_digito_verificador()
        teste_cpf.gerar_cpf_formatado()
        break

    elif teste_cpf.instrucoes_gerais() == 's' or teste_cpf.instrucoes_gerais() == 'S':
        print("Saindo do programa!")
        break
"""
while True:
    teste_cnpj.instrucoes_gerais()

    if teste_cnpj.instrucoes_gerais() == '2':
        print(f"Você escolheu o módulo CNPJ!")
        teste_cnpj.gerar_oito_aleatorios()
        teste_cnpj.gerar_primeiro_digito_verificador()
        teste_cnpj.gerar_segundo_digito_verificador()
        teste_cnpj.gerar_cnpj_formatado()
        break

    elif teste_cnpj.instrucoes_gerais() == 's' or teste_cnpj.instrucoes_gerais() == 'S':
        print("Saindo do programa!")
        break
"""
