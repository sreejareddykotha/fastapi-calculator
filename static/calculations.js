const form = document.getElementById("calc-form");
const calculationsList = document.getElementById("calculations-list");


async function loadCalculations() {

    const response = await fetch("/calculations");

    const calculations = await response.json();

    calculationsList.innerHTML = "";

    calculations.forEach(calc => {

        const li = document.createElement("li");

        li.innerHTML = `
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

        calculationsList.appendChild(li);
    });
}


form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const a = parseFloat(
        document.getElementById("a").value
    );

    const b = parseFloat(
        document.getElementById("b").value
    );

    const type = document.getElementById("type").value;

    const response = await fetch("/calculations", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            a: a,
            b: b,
            type: type
        })
    });

    if (response.ok) {

        alert("Calculation created successfully");

        loadCalculations();

        form.reset();

    } else {

        alert("Error creating calculation");
    }
});


async function deleteCalculation(id) {

    const response = await fetch(
        `/calculations/${id}`,
        {
            method: "DELETE"
        }
    );

    if (response.ok) {

        loadCalculations();
    }
}


async function editCalculation(
    id,
    oldA,
    oldB,
    oldType
) {

    const newA = prompt(
        "Enter new first number",
        oldA
    );

    const newB = prompt(
        "Enter new second number",
        oldB
    );

    const newType = prompt(
        "Enter new type",
        oldType
    );

    const response = await fetch(
        `/calculations/${id}`,
        {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                a: parseFloat(newA),
                b: parseFloat(newB),
                type: newType
            })
        }
    );

    if (response.ok) {

        loadCalculations();
    }
}


loadCalculations();