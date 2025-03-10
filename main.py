from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
from mangum import Mangum

app = FastAPI()

def is_prime(n: int) -> bool:
    'Check if a number is prime.'
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_fun_fact(n: int) -> str:
    """Fetch a fun fact about the number from NumbersAPI."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}", timeout=5)
        return response.text if response.status_code == 200 else "No fact available."
    except requests.exceptions.RequestException:
        return "No fact available."

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="The number to classify")):
    """Classifies a number and returns mathematical properties in JSON format."""
    try:
        number = int(number)
    except ValueError:
        return JSONResponse(status_code=400, content={"number": "alphabet", "error": True})

    # Determine properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    # Create response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": get_fun_fact(number),
    }
    
    return JSONResponse(status_code=200, content=response)

# Run using: uvicorn filename:app --reload

handler = Mangum(app)
