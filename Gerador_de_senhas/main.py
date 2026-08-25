import random
class Senha:
    def gerar_senha():
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
        senha = ""
        
        for i in range(12):
            senha += random.choice(caracteres)
        
        return senha    
    
nova_senha = Senha.gerar_senha()
print(nova_senha)
       