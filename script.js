fetch("inventory.json")
    .then((response) => response.json())
    .then((items) => {
        const list = document.querySelector("#inventory");
        items.forEach((item) => {
            const newItem = document.createElement("li");
            newItem.textContent= 
                '${item["Reagent Name"]} | Instrument: ${item.Instrument} | Side: ${item.Side} | Par: ${item.Par}'
            list.appendChild(newItem);
        });
    })
