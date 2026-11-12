# Trouver le maximum de trois nombres

Écrivez `maximum_of_three(a, b, c)` qui retourne le plus grand des trois nombres.

N’utilisez pas la fonction intégrée `max()` et gérez correctement les valeurs égales.

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style ifelse fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style ifelse2 fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style variablesB fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style variablesC fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir a, b et c]@{ shape: in-out } --> variables[maximum prend a]@{ shape: rect }
    variables --> ifelse{b > maximum ?}@{ shape: decision }
    ifelse -->|Oui| variablesB[maximum prend b]@{ shape: rect }
    ifelse -->|Non| ifelse2{c > maximum ?}@{ shape: decision }
    variablesB --> ifelse2
    ifelse2 -->|Oui| variablesC[maximum prend c]@{ shape: rect }
    ifelse2 -->|Non| output[Retourner maximum]@{ shape: lean-r }
    variablesC --> output
```
