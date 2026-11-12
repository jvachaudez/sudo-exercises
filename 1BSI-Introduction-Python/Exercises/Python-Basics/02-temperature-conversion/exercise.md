# Convertir une température

Écrivez `celsius_to_fahrenheit(celsius)` qui convertit une température Celsius en Fahrenheit.

Utilisez la formule :

$$F = C \times \frac{9}{5} + 32$$

```python
celsius_to_fahrenheit(0)   # 32
celsius_to_fahrenheit(100) # 212
```

```mermaid
flowchart TD
    style input fill:#d0e8ff,stroke:#7088a0,stroke-width:2px
    style variables fill:#ffffd8,stroke:#a0a078,stroke-width:2px
    style output fill:#d8ffd8,stroke:#78a078,stroke-width:2px

    input[Recevoir celsius]@{ shape: in-out }
    -->variables[Calculer celsius × 9 ÷ 5 + 32]@{ shape: rect }
    -->output[Retourner la température]@{ shape: lean-r }
```
