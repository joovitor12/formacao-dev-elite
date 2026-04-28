# Changelog — Aula 07

## Added
- Suporte a formatos de payload com `id` no root, envelope `record`, envelope `data` e lista `items` na ingestao (`ingest_service._extract_record`).
- Normalizacao do identificador externo com fallback `id`/`recordId` e sanitizacao de string (`mapper._normalize_external_id`).
- Helpers de mapeamento para desembrulhar payload aninhado no proprio mapper (`mapper._unwrap_record_shape` e `_pick_first_dict`).

## Changed
- `ingest_service.ingest_raw_json` passou a validar tipo de entrada (`raw` como `str`) e estrutura apos parse (`payload` como objeto JSON).
- `map_record_to_internal` deixou de assumir `record["id"]` diretamente e centralizou normalizacao e validacao antes de montar o contrato interno.
- Fluxo de ingestao e mapeamento preserva interface publica (`ingest_raw_json(raw: str) -> dict` e chaves `internal_id`/`display_name`).

## Verified
- **Coberto por testes**
- `test_current_behavior_characterization.py`: cenarios `ingest__id_no_root__sucesso`, `ingest__id_em_data__sucesso`, `ingest__record_recordId_camelCase__sucesso`, `ingest__items_lista__sucesso`.
- `test_current_behavior_characterization.py`: cenarios `mapper__id_no_root__sucesso`, `mapper__id_em_data__sucesso`, `mapper__recordId_camelCase__sucesso`, `mapper__items_lista__sucesso`.
- `test_api_id_characterization.py`: caracterizacao de contrato para `ingest_raw_json` com `id`, `record.id`, `record.recordId`, `data.id` e `items[0].id`, alem de mapeamento direto com `data.id`.
- `test_mapper_api_shapes.py`: provas rapidas de contrato para payload plano, envelope `record.recordId` e mapeamento direto de payload com `data`.

- **Risco residual (nao coberto explicitamente por testes)**
- JSON invalido e erro de parse (`json.loads`) nao possui cenario dedicado de assercao.
- Casos de tipo incorreto em runtime (`raw` nao string, payload nao objeto, `record` nao dict) sem testes especificos.
- Validacao de ID vazio/whitespace (`ValueError`) e ausencia simultanea de `id` e `recordId` (`KeyError`) sem testes negativos dedicados.
- `items` com elementos nao-dict ou lista vazia sao tratados pelo fluxo, mas sem suite de regressao explicita para esses formatos.
