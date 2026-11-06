# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars.

| Parameter   | Values                      | Notes                     |
|-------------|-----------------------------|---------------------------|
| `weight_kg` | any positive float          | parcel weight             |
| `zone`      | `"local"`, `"regional"`     | delivery zone             |
| `service`   | `"standard"`, `"express"`   | default: `"standard"`     |

Express shipping adds a **$7 surcharge** on top of the standard rate.

**Rate formula:** `base + 1.5 × weight_kg (+ $7 for express)`

| Zone       | Standard base | Express base |
|------------|--------------|--------------|
| `local`    | $5.00        | $12.00       |
| `regional` | $8.00        | $15.00       |

### CLI

The command-line entry point prints a quote for an order:

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```bash
python -m warehouse.cli 2 local                   # $8.00
python -m warehouse.cli 2 local --service express # $15.00
```
