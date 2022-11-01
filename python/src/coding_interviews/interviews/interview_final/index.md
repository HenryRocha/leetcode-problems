## Problema

Problema número 290 - LeetCode

## Word Pattern

Dado um padrão `p` e uma string `s`, descubra de `s` segue o padrão `p`.

## Exemplo 1

Input: `pattern = "abba"`, `s = "dog cat cat dog"`

Output: `true`

## Exemplo 2

Input: `pattern = "abba"`, `s = "dog cat cat fish"`

Output: `false`

## Exemplo 3

Input: `pattern = "ab"`, `s = "dog dog dog"`

Output: `false`

## Dicas

1. Tente eliminar os casos em que _com certeza_ `s` não segue o padrão `p`.

2. Tente usar a quantidade palavras em `s` e o número de letras em `p` para determinar se é _possível_ que `s` siga o padrão `p`.
Tente pensar também no número de palavras únicas _vs._ letras únicas.

1. Sabendo que a string tem que seguir o padrão, como faria para ligar cada palavra a uma letra do padrão?

2. Tente passar de palavra em palavra e letra em letra para realizar o mapeamento palavra -> letra.

## Solução

Para solucionar o problema podemos começar retirando os casos em que sabemos que não é possível que a string `s` siga o padrão `p`.
Um desses casos é quando o número de palavras em `s` é diferente do número de letras em `p`.
Nesse caso, não é possível mapear cada palavra para uma letra no padrão.
Outro caso é quando o número de palavras únicas em `s` é diferente do número de letras únicas em `p`.
Como sabemos que cada letra pode representar apenas uma palavra, caso as quantidades sejam diferentes, podemos determinar que a string não segue o padrão.

Eliminando esses casos, sabemos que podemos tentar mapear cada palavra para uma letra.
Podemos ir passando, ao mesmo tempo, de palavra em palavra de `s` e de letra em letra em `p`.
Desse modo podemos ir mapeando cada palavra para uma letra. 
Caso a palavra já tenha sido mapeada, a letra atual tem que ser igual à letra para qual essa palavra foi mapeada, caso contrário sabemos que a string `s` não segue o padrão `p`.
Se a palavra ainda não foi mapeada, podemos apenas adicionar essa palavra no nosso dicionário, apontando para a letra atual.

Se passamos por todo esse processo, temos certeza que `s` segue o padrão `p`.

## Complexidade

A solução encontrada tem complexidade de tempo `O(n)` e complexidade de espaço `O(n)`.
