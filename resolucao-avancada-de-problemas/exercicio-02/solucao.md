# Nota curta da solução

O gargalo estava na varredura repetida de `events`: para cada usuário distinto, o código percorria toda a lista novamente, gerando custo quadrático no pior caso.

A solução foi trocar para uma única passagem sobre `events`, acumulando os pontos em um `dict` por `user_id` (`totals[user_id] = totals.get(user_id, 0.0) + points`).

Com isso, o custo dominante passou a ser linear em relação ao número de eventos, preservando a assinatura e o significado da saída `(totals, operations)`.

Validação: `pytest -q` passou e o `example.py` mostrou `operacoes_contadas` igual ao número de eventos no cenário testado.
