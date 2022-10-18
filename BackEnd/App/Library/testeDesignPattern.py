def gerarPessoa(nome, sobrenome):
    pessoa = {}
    pessoa['nome'] = nome
    pessoa['sobrenome'] = sobrenome
    
    def nomeCompleto():
        return f"{pessoa['nome']} {pessoa['sobrenome']}"
    
    pessoa['nomeCompleto'] = nomeCompleto()
    
    return pessoa

pessoaA = gerarPessoa('Luiz', 'Felipe')
pessoaB = gerarPessoa('João', 'Pedro')

print(pessoaA['nome'])
print(pessoaB['nome'])
print(pessoaA['nomeCompleto'])
print(pessoaB['nomeCompleto'])

