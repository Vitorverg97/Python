# O que é uma String?
# 'Sou uma String' || "Sou uma String"; Is the same thing

t= 'mundo'

# Função Type
type(t)    # Saída: str

# Função IN

'm' in t   # saída: TRUE

'M' in t   # saída: FALSE

# Função len()
# conta elementos

len(t)    # saída: 5

## Indexação de strings

c = 'Curso de Python'
c[0] ## Saída: 'C'

len(c)  ## Saída: 15

nova_string= c[0:5] ## nova_string=s[0:5] == nova_string=s[:5] is TRUE
print(nova_string) ## Saída: Curso

nova_string= c[1:5]
print(nova_string) ## Saída: urso

c [-1] # In negative index, it counted by the right to left. It's like selecting the word with a mouse from the right to the left.
## Output: 'n'
