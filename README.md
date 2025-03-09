# NumberClassification

# Number Classification API

This API classifies numbers and returns their mathematical properties and a fun fact.

## Usage

**Endpoint:** `GET /api/classify-number?number=<number>`

**Example:** `GET /api/classify-number?number=371`

**Response (200 OK):**

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

# Response (400 Bad Request):

{
    "number": "alphabet",
    "error": true
}