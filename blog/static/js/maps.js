function initialize() {
    //Para saber como funciona un mapa
    var mapa = {'zoom':15,'zoomcontrol':true};
    
    //OPCIONES DEL MAPA (https://developers.google.com/maps/documentation/javascript/reference?hl=es#MapOptions)
    var mapOptions = {
        zoom: mapa.zoom,
        center: new google.maps.LatLng(-31.3627,-64.2765),
        zoomControl:mapa.zoomcontrol,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    }
    //CREAMOS EL MAPA - LE PASAMOS DONDE LO CREAMOS (#map-canvas), Y LE PASAMOS OPCIONES
    var map = new google.maps.Map(document.getElementById('map-canvas'),
                                  mapOptions);
    
    
        
    //CREAMOS EL MARKER - 
    var image1 = '/static/images/pointer.png';
    var myLatLng1 = new google.maps.LatLng(-31.3627,-64.2765);
    var beachMarker = new google.maps.Marker({
        position: myLatLng1,
        map: map,
        icon: image1,
          animation:google.maps.Animation.BOUNCE
    });
    

    //CREAMOS EL INFOWINDOWS - LA VENTANITA QUE APARECE CUANDO HAGO CLICK EN EL MARKER
;
        var contentString ="<iframe width='560' height='315' src='https://www.youtube.com//embed//0Jb12-JIy9U' frameborder='2' allowfullscreen </iframe>";

    
    https://www.youtube.com/watch?v=OzkZWvAJUr0

    var infowindow = new google.maps.InfoWindow({
        content: contentString,
        maxWidth: 600
    });
    
    google.maps.event.addListener(beachMarker, 'click', function() {
        infowindow.open(map,beachMarker);
        map.setZoom(13);
  map.setCenter(marker.getPosition());
        
    });
    

}


google.maps.event.addDomListener(window, 'load', initialize);