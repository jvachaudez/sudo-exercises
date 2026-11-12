# Calculer l’aire d’un rectangle

Écrivez `rectangle_area(length, width)` qui retourne l’aire du rectangle.

L’aire est égale à `length × width`. Aucune validation particulière des dimensions n’est demandée.

```python
rectangle_area(5, 3)   # 15
rectangle_area(2.5, 4) # 10
```

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir length et width]@{ shape: in-out }
    -->variables[Calculer length × width]@{ shape: rect }
    -->output[Retourner l’aire]@{ shape: lean-r }
```
