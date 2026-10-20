//This script provides a way for us to access the json of the inventory items and display it as a table

//This portion retrieves the json file, and catches any errors with retrieval
fetch("inventory.json")
    .then((response) => response.json())
    .then((inventory) => { 
        createTable(inventory.reagents);
    })
    .catch(error => console.error('Error:', error))


//this section adds the createTable function referenced above. 
function createTable(inventory){
        const table = document.createElement('table');
        const tableHead = document.createElement('thead');
        const tableBody = document.createElement('tbody');

        //This section adds the head and body to the table.
        table.appendChild(tableHead);
        table.appendChild(tableBody);

        //This section defines what tableHead is
        let row = tableHead.insertRow();
        Object.keys(data[0]).forEach(key=>{
            let th = document.createElement('th');
            th.textContent = key.toUpperCase();
            row.appendChild(th);
        });

        //creating table body

        inventory.forEach((item) => {
            let row = tableBody.insertRow();
            Object.values(item).forEach(value => {
                let cell = row.insertCell();
                cell.textContent = value;
            });
        });

        //adding the table to the HTML
        document.getElementById('inventory').appendChild(table);
    }
