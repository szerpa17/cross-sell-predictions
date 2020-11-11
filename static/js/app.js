// Initialize the page with a default plot
function init() {

    d3.json("/api/v1.0/testing_data").then((data) => {

        var id_list = data.map(function(customer) {
            return customer.id
        })
        
        console.log(id_list)

        // let dropdownMenu = d3.select("select");
        // data.id.forEach(ids => {
        //     dropdownMenu.append("option").text(ids);
        //     });
    
    });
}


// Load init()
init();
