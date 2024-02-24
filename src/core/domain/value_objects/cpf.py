class Cpf:
    @staticmethod
    def validate(cpf: str) -> None:
        # cpf: str = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise ValueError(
                f"CPF {cpf} is invalid. Incorrect number of characters."
            )

        # Calcular o primeiro dígito verificador
        total = 0
        for i in range(9):
            total += int(cpf[i]) * (10 - i)
        resto = total % 11
        digito1 = 11 - resto if resto >= 2 else 0

        # Calcular o segundo dígito verificador
        total = 0
        for i in range(10):
            total += int(cpf[i]) * (11 - i)
        resto = total % 11
        digito2 = 11 - resto if resto >= 2 else 0

        # Verificar se os dígitos verificadores estão corretos
        if digito1 != int(cpf[9]) and digito2 != int(cpf[10]):
            raise ValueError(f"CPF {cpf} is invalid")
