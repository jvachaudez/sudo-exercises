# Compter les voyelles

Écrivez `count_vowels(text)` qui retourne le nombre de voyelles présentes dans `text`.

Les voyelles utilisées sont `a`, `e`, `i`, `o`, `u` et `y`. Ignorez la différence entre majuscules et minuscules.

```python
count_vowels("bonjour") # 3
count_vowels("PYTHON")  # 2
```

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style forloop fill:#ffe0b0,stroke:#b99f79,stroke-width:2px
    style ifelse fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style variables2 fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir text]@{ shape: in-out } --> variables[count prend 0]@{ shape: rect }
    variables --> forloop[Pour chaque caractère]@{ shape: hex }
    forloop --> ifelse{Le caractère est une voyelle ?}@{ shape: decision }
    ifelse -->|Oui| variables2[Ajouter 1 à count]@{ shape: rect }
    ifelse -->|Non| forloop
    variables2 --> forloop
    forloop -->|Terminé| output[Retourner count]@{ shape: lean-r }
```
