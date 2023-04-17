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

$("#region").change(function () {
   if ($(this).val() == regions[0]) {
     $('#near').hide();
   } else {
     $("#near").show();
   }
 }).change()

document.getElementById("btn").addEventListener("click", () => {
   query = (document.getElementById("query").value)
   numOfPages = parseInt(document.getElementById("numOfPages").value)
   minPrice = parseInt(document.getElementById("minPrice").value)
   maxPrice = parseInt(document.getElementById("maxPrice").value)
   region = (document.getElementById("region").value)
   boolNear = (document.getElementById("nearby-regions").checked)
   eel.newSearch(query, numOfPages , region, minPrice, maxPrice, boolNear)
   loadData();
}
)

$(document).on('click', '.clickable-row', function() {
   window.open($(this).data("url"), "_blank", "noopener noreferrer"); 
});

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
               <tr class="clickable-row" data-url="${product.link}">
                  <td><img src="${product.imgSrc}" width="200" height="200"></img></td>
                  <td>${product.title}</td>
                  <td>${product.price}</td>
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