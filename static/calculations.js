async function loadCalculations() {
    const response = await fetch("/calculations");
    const calculations = await response.json();

    const calculationsList = document.getElementById("calculations-list");
    calculationsList.innerHTML = "";

    calculations.forEach(calc => {
        const item = document.createElement("li");

        item.innerHTML = `
            ${calc.a} ${calc.type} ${calc.b} = ${calc.result}

            <button onclick="deleteCalculation(${calc.id})">
                Delete
            </button>

            <button onclick="editCalculation(
                ${calc.id},
                ${calc.a},
                ${calc.b},
                '${calc.type}'
            )">
                Edit
            </button>
        `;

        calculationsList.appendChild(item);
    });
}

document.getElementById("calc-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const a = document.getElementById("a").value;
    const b = document.getElementById("b").value;
    const type = document.getElementById("type").value;

    const response = await fetch("/calculations", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            a: parseFloat(a),
            b: parseFloat(b),
            type: type
        })
    });

    if (response.ok) {
        alert("Calculation created successfully");
        document.getElementById("calc-form").reset();
        loadCalculations();
    } else {
        alert("Error creating calculation");
    }
});

async function deleteCalculation(id) {
    const response = await fetch(`/calculations/${id}`, {
        method: "DELETE"
    });

    if (response.ok) {
        loadCalculations();
    }
}

async function editCalculation(id, oldA, oldB, oldType) {
    const newA = prompt("Enter new A value", oldA);
    const newB = prompt("Enter new B value", oldB);
    const newType = prompt(
        "Enter operation: Add, Sub, Multiply, Divide",
        oldType
    );

    const response = await fetch(`/calculations/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            a: parseFloat(newA),
            b: parseFloat(newB),
            type: newType
        })
    });

    if (response.ok) {
        loadCalculations();
    }
}

loadCalculations();