$( document ).ready(function(){
  console.log('=======document is now ready!!!!!======');

 $( ".bizCategory" ).on( "click", function() {
    console.log('click event');
    // $(".item-container li").removeClass( "active" );
    $( this ).addClass( "active" );
  });

  function initialize() {
  var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
  var mapOptions = {
    zoom: 4,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Hello World!'
  });

   
  }

  var result=google.maps.event.addDomListener(window, 'load', initialize);


 }) //document-ready close

