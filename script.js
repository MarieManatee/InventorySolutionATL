fetch("inventory.json")
    .then((response) => response.json())
    .then((inventory) => {
        const list = document.querySelector("#inventory");
        inventory.forEach((item) => {
            const newItem = document.createElement("li");
            newItem.textContent = `${item.name}`
            list.appendChild(newItem);
        });
    })
