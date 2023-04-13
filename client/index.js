document.getElementById("btn").addEventListener("click", () => {
  eel.search(document.getElementById("query").value)}
)

fetch("/searches.json")
.then(function(response){
  return response.json();
}).then(json => console.log(json))
.then(function(products){
   let placeholder = document.querySelector("#data-output");
   let out = "";
   for(let product of products){
      out += `
         <tr>
            <td>${product.title}</td>
            <td>${product.price}</td>
            <td>${product.link}</td>
            <td>${product.location}</td>
         </tr>
      `;
   }
 
   placeholder.innerHTML = out;
});


