# Construire une table de multiplication

Écrivez `multiplication_table(number)` qui retourne une liste contenant les dix premiers multiples de `number`.

```python
multiplication_table(3)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

La fonction doit retourner la liste et ne doit pas l’afficher.

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style forloop fill:#ffe0b0,stroke:#b99f79,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir number]@{ shape: in-out }
    -->variables[Créer une liste vide]@{ shape: rect }
    -->forloop[Pour i de 1 à 10, ajouter number × i]@{ shape: hex }
    -->output[Retourner la liste]@{ shape: lean-r }
```
