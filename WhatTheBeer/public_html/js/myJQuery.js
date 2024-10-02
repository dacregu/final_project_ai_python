formulario
quienes_somos

$(function() {

	//Controla que solo se puedan seleccionar 5 opciones en los "selectpicker" multiples
	$('.selectpicker').selectpicker({
     	maxOptions:5
  	});

	//Controla los links del header para mostrar las difernetes secciones de la pagina
	$(".open_div").click(function() {
		open = $(this).attr('href');
		$("html, body").animate({ scrollTop: 0 });
		if(open === "#formulario"){
			$("#formulario").show();
			$("#quienes_somos").hide();
			$("#tabla_recomendaciones").hide();
		}else{
			$("#formulario").hide();
			$("#quienes_somos").show();
			$("#tabla_recomendaciones").hide();
		}
	});

	//Controla que se muestren los inputs al ir seleccionando opciones en el desplegable "cervezas"
	$("#beers").change(function () {
	   count = $("#beers :selected").length;

	   for(i = 2; i <= 5; i++){
	   		if(i<=count){
	   			$("#div_punt_beer_"+i).show();
	   		}else{
	   			$("#div_punt_beer_"+i).hide();
	   		}
	   }
	});

	$("input[name=typeAbv]").click(function(){
		value = $(this).val();
		val_abv = parseFloat($("#punt_abv_1").val());
		val_abv2 = parseFloat($("#punt_abv_2").val());

		if(value == "entre"){
	   			$("#div_punt_abv_2").show();
				if(val_abv>val_abv2){
					$("#punt_abv_2").val(val_abv);
					$("#show_punt_abv_2").text(val_abv);
				}
		}else{
	   			$("#div_punt_abv_2").hide();
		}
	});

	$(".custom-range").change(function(){
		value = $(this).val();
		id = $(this).attr('id');
		console.log(id+" - "+value);
		$("#show_"+id).text(value);
	});

	$("#punt_abv_2, #punt_abv_1").change(function(){
		val_abv = parseFloat($("#punt_abv_1").val());
		val_abv2 = parseFloat($("#punt_abv_2").val());

		console.log(val_abv+" - "+val_abv2);
		
		if(val_abv>val_abv2){
			$("#punt_abv_2").val(val_abv);
			$("#show_punt_abv_2").text(val_abv);
		}

	});

	//Resetea el formulario web
	$("#restart").click(function(){
		$("#form")[0].reset();
	   	$('.selectpicker').selectpicker('refresh');
	   	$("#show_punt_beer_1").text("4");
	   	for(i = 2; i <= 5; i++){
	   		$("#div_punt_beer_"+i).hide();
	   		$("#show_punt_beer_"+i).text("4");
	   	}
	   	$("#div_punt_abv_2").hide();
	   	$("#show_punt_abv_2").text("8.6");
	   	$("#show_punt_abv_1").text("5");

	});

	$("#enviar").click(function(){
		
		typeAbvVAR = $("input[name='typeAbv']:checked").val();

		console.log(typeAbvVAR)

		beers = $("#beers").val();
		stringBeers = "";
		for(i=0;i<beers.length;i++){
			j = i+1;
			stringBeers += beers[i]+"|"+$("#punt_beer_"+j).val()+";";
		}
		stringBeers = stringBeers.slice(0, -1); 
		
		$("#formulario").hide();
		$("#quienes_somos").hide();
		$("#tabla_recomendaciones").hide();
		$("#cargando").show();

		urlVAR = "http://localhost:5000/recomendacion_beers?beers="+stringBeers+"&style="+$("#estilo").val()
			  +"&typeAbv="+typeAbvVAR+"&abv="+$("#punt_abv_2").val()+"-"+$("#punt_abv_1").val()

		$.ajax({
		    url: urlVAR,
		    type: "GET",
		    //data: dataVAR,
		    dataType: "json"
		    //contentType: 'application/json; charset=utf-8'
		})
	    .done( function (response) {
	    	resJSON = response.beers;
			$("#cargando").hide();
			$("#tabla_recomendaciones tbody tr").remove();
			$("#tabla_recomendaciones").show();
			var trsHTML = '';
			$.each(resJSON, function(i, item) {
	        	trsHTML += '<tr><td>' + item.beer + '</td><td>' + item.style + '</td><td>' + item.abv + '</td></tr>';
	        });
	        $('#insert_tabla_recomendaciones').append(trsHTML);

	    })
	    .fail( function(response){
	    	alert("Error al generar tabla ")
	    });
	});

		$.ajax({
		    url: "http://localhost:5000/getAll_beers",
		    type: "GET",
		    //data: dataVAR,
		    dataType: "json"
		    //contentType: 'application/json; charset=utf-8'
		})
	    .done( function (response) {
	    	resJSON = response.beers;
			var optionsHTML = '';
			$.each(resJSON, function(i, item) {
				optionsHTML += "<option value="+item.beer_id+">"+item.beer_name+"</option>";
	        });
	        $('#beers').append(optionsHTML);
	        console.log("Se añadieron cervezas: "+optionsHTML);
	        $('.selectpicker').selectpicker('refresh');
	    })
	    .fail( function(response){
	    	alert("Error al coger cervezas")
	    });

		$.ajax({
		    url: "http://localhost:5000/getAll_estilos",
		    type: "GET",
		    //data: dataVAR,
		    dataType: "json"
		    //contentType: 'application/json; charset=utf-8'
		})
	    .done( function (response) {
	    	resJSON = response.estilos;
			var optionsHTML = '';
			$.each(resJSON, function(i, item) {
				optionsHTML += "<option value=\""+item.estilo+"\">"+item.estilo+"</option>";
	        });
	        $('#estilo').append(optionsHTML);
	        console.log("Se añadieron estilos: "+optionsHTML);
	        $('.selectpicker').selectpicker('refresh');

	    })
	    .fail( function(response){
	    	alert("Error al coger estilos.")
	    });
});