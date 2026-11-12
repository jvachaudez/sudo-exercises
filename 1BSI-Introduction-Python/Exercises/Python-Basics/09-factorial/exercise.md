# Calculer une factorielle

Écrivez `factorial(n)` qui retourne la factorielle de l’entier `n`.

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
0! = 1
```

Levez `ValueError` si `n` est négatif et utilisez une boucle.

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style ifelse fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style outputError fill:#d8ffd8,stroke:#78a078,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style forloop fill:#ffe0b0,stroke:#b99f79,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir n]@{ shape: in-out } --> ifelse{n < 0 ?}@{ shape: decision }
    ifelse -->|Oui| outputError[Lever ValueError]@{ shape: lean-r }
    ifelse -->|Non| variables[result prend 1]@{ shape: rect }
    variables --> forloop[Pour i de 1 à n, multiplier result par i]@{ shape: hex }
    forloop --> output[Retourner result]@{ shape: lean-r }
```
