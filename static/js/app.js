// Initialize the page with a default plot
function init() {

    d3.json("/api/v1.0/original_testing_data").then((data) => {
        console.log(data);
        
        // Populate dropdown menu with ids

        let id_values = data.map(callback(currentValue[, index[, array]]) {
            // return element for newArray, after executing something
          }[, thisArg]);


        let dropdownMenu = d3.select("select");
        data.id.forEach(ids => {
            dropdownMenu.append("option").text(ids);
            });
    
    });
}


// Load init()
init();
