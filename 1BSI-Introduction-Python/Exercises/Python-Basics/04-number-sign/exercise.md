# Déterminer le signe d’un nombre

Écrivez `number_sign(number)` qui retourne exactement :

- `"positif"` si le nombre est supérieur à zéro ;
- `"négatif"` s’il est inférieur à zéro ;
- `"nul"` s’il vaut zéro.

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style ifelse fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style ifelse2 fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style outputPositive fill:#d8ffd8,stroke:#78a078,stroke-width:2px
    style outputNegative fill:#d8ffd8,stroke:#78a078,stroke-width:2px
    style outputZero fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir number]@{ shape: in-out } --> ifelse{number > 0 ?}@{ shape: decision }
    ifelse -->|Oui| outputPositive[Retourner positif]@{ shape: lean-r }
    ifelse -->|Non| ifelse2{number < 0 ?}@{ shape: decision }
    ifelse2 -->|Oui| outputNegative[Retourner négatif]@{ shape: lean-r }
    ifelse2 -->|Non| outputZero[Retourner nul]@{ shape: lean-r }
```
