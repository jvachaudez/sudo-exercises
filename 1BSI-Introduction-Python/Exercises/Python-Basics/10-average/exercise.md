# Calculer une moyenne

Écrivez `average(values)` qui retourne la moyenne arithmétique des nombres de la liste.

- N’utilisez pas `sum()`.
- Pour une liste vide, levez `ValueError`.
- Retournez le résultat sans l’afficher.

```python
average([10, 12, 14]) # 12
average([-2, 2])      # 0
```

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style ifelse fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style outputError fill:#d8ffd8,stroke:#78a078,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style forloop fill:#ffe0b0,stroke:#b99f79,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir values]@{ shape: in-out } --> ifelse{Liste vide ?}@{ shape: decision }
    ifelse -->|Oui| outputError[Lever ValueError]@{ shape: lean-r }
    ifelse -->|Non| variables[total prend 0]@{ shape: rect }
    variables --> forloop[Pour chaque valeur, l’ajouter à total]@{ shape: hex }
    forloop --> output[Retourner total ÷ longueur]@{ shape: lean-r }
```
