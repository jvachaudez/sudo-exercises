# Calculer la somme de 1 à n

Écrivez `sum_to_n(n)` qui retourne la somme des entiers de `1` à `n` inclus.

- Pour `n = 0`, retournez `0`.
- Pour un nombre négatif, levez `ValueError`.
- Utilisez une boucle, sans formule directe.

```python
sum_to_n(5) # 15
```

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
    ifelse -->|Non| variables[total prend 0]@{ shape: rect }
    variables --> forloop[Pour i de 1 à n, ajouter i]@{ shape: hex }
    forloop --> output[Retourner total]@{ shape: lean-r }
```
