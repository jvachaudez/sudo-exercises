# Vérifier un palindrome

Un palindrome se lit de la même manière de gauche à droite et de droite à gauche.

Écrivez `is_palindrome(text)` qui retourne `True` ou `False` en ignorant la casse. Une chaîne vide est considérée comme un palindrome.

```python
is_palindrome("Radar")  # True
is_palindrome("Python") # False
```

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style ifelse fill:#ffd8d8,stroke:#ab8787,stroke-width:2px
    style outputTrue fill:#d8ffd8,stroke:#78a078,stroke-width:2px
    style outputFalse fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir text]@{ shape: in-out }
    -->variables[Convertir text en minuscules]@{ shape: rect }
    -->ifelse{text est égal à son inverse ?}@{ shape: decision }
    ifelse -->|Oui| outputTrue[Retourner True]@{ shape: lean-r }
    ifelse -->|Non| outputFalse[Retourner False]@{ shape: lean-r }
```
