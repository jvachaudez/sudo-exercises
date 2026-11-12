# Doubler un nombre

Écrivez la fonction `double_number(number)` qui retourne le double du nombre reçu.

```python
double_number(5)    # 10
double_number(-2.5) # -5
```

La fonction doit retourner le résultat sans l’afficher.

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir number]@{ shape: in-out }
    -->variables[Calculer number × 2]@{ shape: rect }
    -->output[Retourner le résultat]@{ shape: lean-r }
```
