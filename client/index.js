regions = ["italia", "abruzzo", "basilicata", "calabria", "campania", "emilia-romagna", 
            "friuli venezia giulia", "lazio", "liguria", "lombardia", "marche", "molise",
            "piemonte", "puglia", "sardegna","sicilia", "toscana", "trentino alto adige",
            "umbria", "valle d'aosta", "veneto"]

var select = document.getElementById("region");
for(var i = 0; i < regions.length; i++) {
    var region = regions[i];
    var el = document.createElement("option");
    el.textContent = region;
    el.value = region;
    select.appendChild(el);
}

document.getElementById("btn").addEventListener("click", () => {
   query = (document.getElementById("query").value)
   numOfPages = parseInt(document.getElementById("numOfPages").value)
   minPrice = parseInt(document.getElementById("minPrice").value)
   maxPrice = parseInt(document.getElementById("maxPrice").value)
   region = (document.getElementById("region").value)
   eel.newSearch(query, numOfPages , region, minPrice, maxPrice)
   loadData();
}
)

function loadData(){
   if("searches.json"){
      fetch("searches.json")
      .then(function(response){
        return response.json();
      }).then(products => {
         console.log(products)
         let placeholder = document.getElementById("data-output");
         let out = "";
         for(let product of products){
            out += `
               <tr>
                  <td><img src="${product.imgSrc}" width="100" height="100"></img></td>
                  <td>${product.title}</td>
                  <td>${product.price}</td>
                  <td><a href=${product.link} target="_blank" rel="noopener noreferral">${product.link}</a></td>
                  <td>${product.location}</td>
               </tr>
            `;
         }
       
         placeholder.innerHTML = out;
      });
   }
   else{
      console.log("No database")
   }
}


loadData()



