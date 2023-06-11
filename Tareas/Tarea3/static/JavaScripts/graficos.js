const generateGraf = () => {


    
    $.ajax({
        url: "/get_info_grafic",
        method: "GET",
        success: function(response) {
            const colors = ['red', 'green', 'blue', 'black', 'pink']
    
            const donations = response[0];
            const orders = response[1];
    
            const keysDonations = Object.keys(donations);
            const keysorders = Object.keys(orders);
            
            var datosDonation = [];
            keysDonations.forEach(element => {
                datosDonation.push([element, donations[element]]);
            });

            console.log(datosDonation)

            var opciones = {
                chart: {
                  type: 'pie'
                },
                title: {
                  text: 'Gráfico tipo de donaciones'
                },
                series: [{
                  name: 'Cantidad',
                  data: datosDonation
                }]
              };
          
              // Crear el gráfico circular
              Highcharts.chart('graficoDonacion', opciones);
              
              var datosOrder = [];
              keysorders.forEach(element => {
                datosOrder.push([element, orders[element]]);
              });
  
              console.log(datosOrder)
  
              var opciones2 = {
                  chart: {
                    type: 'pie'
                  },
                  title: {
                    text: 'Grafico de tipos de pedidos'
                  },
                  series: [{
                    name: 'Cantidad',
                    data: datosOrder
                  }]
                };
            
                // Crear el gráfico circular
                Highcharts.chart('graficoPedido', opciones2);
        }
    })
};

document.addEventListener('DOMContentLoaded', generateGraf);
