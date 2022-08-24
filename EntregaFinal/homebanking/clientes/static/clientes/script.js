function mostrarResultados(informacion) {
  let dolares = [
    "Dolar Oficial",
    "Dolar Blue",
    "Dolar Contado con Liqui",
    "Dolar Bolsa",
    "Dolar turista",
  ];

  let diccionarioDeIds = {
    "Dolar Oficial": "dolaroficial",
    "Dolar Blue": "dolarblue",
    "Dolar Bolsa": "dolarMEP",
    "Dolar Contado con Liqui": "dolarcontadoconliqui",
    "Dolar turista": "dolarturista",
  };

  let cotizaciones = informacion
    .map((info) => info.casa)
    .filter((info) => dolares.includes(info.nombre));

  cotizaciones.forEach((dolar) => {
    let id = diccionarioDeIds[dolar.nombre];
    if (id) {
      let div = document.getElementById(id);
      div.innerHTML = `${dolar.compra} / ${dolar.venta}`;
    }
  });
}

function consultaCotizaciones() {
  let informacion = [];
  fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then((response) => response.json())
    .then(mostrarResultados);
}

consultaCotizaciones();
