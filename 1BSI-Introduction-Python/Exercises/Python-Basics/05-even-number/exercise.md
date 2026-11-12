# Déterminer si un nombre est pair

Écrivez `is_even(number)` qui retourne un booléen :

- `True` si `number` est pair ;
- `False` sinon.

Utilisez l’opérateur modulo `%`. Les nombres négatifs doivent également fonctionner.

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style ifelse fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style outputTrue fill:#d8ffd8,stroke:#78a078,stroke-width:2px
    style outputFalse fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir number]@{ shape: in-out } --> ifelse{number modulo 2 == 0 ?}@{ shape: decision }
    ifelse -->|Oui| outputTrue[Retourner True]@{ shape: lean-r }
    ifelse -->|Non| outputFalse[Retourner False]@{ shape: lean-r }
```
